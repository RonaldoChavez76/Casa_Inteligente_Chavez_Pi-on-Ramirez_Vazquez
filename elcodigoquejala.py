from machine import Pin, PWM
import neopixel, time, network, ujson
from mfrc522 import MFRC522
from umqtt.simple import MQTTClient

# ————— CONFIGURACIÓN —————
WIFI_SSID    = 'Ronaldo SIUUU'
WIFI_PASS    = '11111111'
MQTT_BROKER   = 'broker.emqx.io'
MQTT_PORT     = 1883
MQTT_USER     = ''
MQTT_PASS     = ''

TOPIC_DOOR2 = 'iot/sensor/door'
TOPIC_NFC   = 'iot/sensor/nfc'

# ————— PINES —————
door2  = Pin(12, Pin.IN, Pin.PULL_UP)
buzzer = PWM(Pin(4), duty=0)
np1    = neopixel.NeoPixel(Pin(15), 8)
np2    = neopixel.NeoPixel(Pin(2), 8)
rdr    = MFRC522(sck=18, mosi=23, miso=19, rst=22, cs=5)
pir    = Pin(14, Pin.IN)  # PIR en pin 14

# ————— ESTADO —————
last_d2 = None
alarm_active = False
alarm_start = 0
door_opened_by_nfc = False
puerta_fue_abierta = False
pir_habilitado = True  # Control del sensor PIR

# ————— FUNCIONES AUXILIARES —————
def wifi_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASS)
    print("Conectando a Wi‑Fi...", end='')
    while not wlan.isconnected():
        time.sleep(0.5)
        print('.', end='')
    print(" ¡OK!", wlan.ifconfig())

def mqtt_connect():
    try:
        client = MQTTClient('esp32_'+str(time.ticks_ms()), MQTT_BROKER,
                            user=MQTT_USER, password=MQTT_PASS,
                            port=MQTT_PORT)
        client.connect()
        print("Conectado a MQTT en", MQTT_BROKER)
        return client
    except Exception as e:
        print("Error conectando a MQTT:", e)
        return None

def set_all(strip, color):
    for i in range(len(strip)):
        strip[i] = color
    strip.write()

def leds_off():
    set_all(np1, (0,0,0))
    set_all(np2, (0,0,0))

def siren_leds():
    set_all(np1, (255, 0, 0))
    set_all(np2, (255, 0, 0))

def safe_leds():
    set_all(np1, (0,255,0))
    set_all(np2, (0,255,0))

def start_buzzer():
    buzzer.freq(1000)
    buzzer.duty(512)

def stop_buzzer():
    buzzer.duty(0)

def stop_alarm():
    stop_buzzer()
    leds_off()

def leer_rfid():
    (stat, tag_type) = rdr.request(rdr.REQIDL)
    if stat == rdr.OK:
        (stat, raw_uid) = rdr.anticoll()
        if stat == rdr.OK:
            return raw_uid
    return None

# ————— INICIO —————
wifi_connect()
mqtt = mqtt_connect()

# ————— BUCLE PRINCIPAL —————
while True:
    now = time.ticks_ms()

    # — Sensor de puerta 2 —
    d2 = 'cerrada' if door2.value() == 0 else 'abierta'
    if d2 != last_d2:
        mqtt.publish(TOPIC_DOOR2, d2)
        print("Puerta2:", d2)
        last_d2 = d2

    # — Control del PIR —
    if pir_habilitado:
        if pir.value() == 1:
            print("Movimiento detectado")
            set_all(np1, (0, 0, 255))
            set_all(np2, (0, 0, 255))
        else:
            leds_off()

    # — Alarma si puerta 2 está abierta sin validación NFC —
    if door2.value() == 1:  # Puerta abierta
        pir_habilitado = False  # Desactiva PIR
        if door_opened_by_nfc:
            puerta_fue_abierta = True
            if alarm_active:
                print("Puerta abierta con validación NFC, desactivando alarma.")
                stop_alarm()
                alarm_active = False
            print("Puerta abierta con validación NFC, acceso permitido.")
        else:
            if not alarm_active:
                print("¡Puerta abierta sin validación NFC! Activando alarma.")
                alarm_active = True
                alarm_start = now
                start_buzzer()
                siren_leds()

    # — Si la puerta se cierra —
    if door2.value() == 0:
        if alarm_active:
            print("Puerta cerrada. Desactivando alarma.")
            stop_alarm()
            alarm_active = False
        if door_opened_by_nfc and puerta_fue_abierta:
            print("Puerta cerrada después del acceso con NFC. Reiniciando estado.")
            stop_alarm()
            door_opened_by_nfc = False
            puerta_fue_abierta = False
        pir_habilitado = True  # Reactiva el PIR

    # — RFID —
    uid = leer_rfid()
    if uid:
        print("UID leído:", [hex(i) for i in uid])
        if tuple(uid) == (0xa5, 0xb7, 0xfd, 0xc2, 0x2d):  # Llavero válido
            if not door_opened_by_nfc:
                print("Llavero válido detectado. Acceso permitido.")
                safe_leds()
                
                # Crear el mensaje para enviar el tag_id y reading_time
                #data = {
                #    'tag_id': ''.join([hex(i) for i in uid]), 
                 #   'reading_time': time.time()  # Tiempo en formato UNIX
                #}
                # Aquí se envía el UID como una cadena literal con los números pegados
                uid_str = "a5b7fdc22d"  # Cadena literal con los números pegados
                mqtt.publish(TOPIC_NFC, uid_str)  # Enviar el UID como cadena al tópico
                #mqtt.publish(TOPIC_NFC, ujson.dumps(data))
                #mqtt.publish(TOPIC_NFC, "llavero_valido")
                door_opened_by_nfc = True
                pir_habilitado = False  # Desactiva PIR al usar llavero válido
        else:
            print("Llavero no válido.")
            mqtt.publish(TOPIC_NFC, "llavero_no_valido")

         

    time.sleep(0.1)
