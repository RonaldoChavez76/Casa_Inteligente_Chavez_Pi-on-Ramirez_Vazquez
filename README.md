# 🏠 Sistema de Seguridad y Automatización para el Hogar

Este proyecto implementa un sistema inteligente de seguridad doméstica que integra sensores, actuadores y una interfaz de monitoreo, tanto en pantalla como en dispositivos móviles, para ofrecer protección en tiempo real y respuesta automatizada ante eventos sospechosos.

---

## 📦 Componentes del Sistema

### 🔍 Sensores

| Sensor                                 | Función                                                                                      | Precio estimado | Enlace de compra                                                                                                                   |
|----------------------------------------|-----------------------------------------------------------------------------------------------|-----------------|------------------------------------------------------------------------------------------------------------------------------------|
| Sensor de movimiento (PIR)             | Detecta la presencia de personas en zonas estratégicas.                                       | $70 MXN         | [Ver en MercadoLibre](https://articulo.mercadolibre.com.mx/MLM-623275379-sensor-de-movimiento-pir-hc-sr501-robotica-arduino-pic-avr-_JM) |
| Sensor magnético de puertas/ventanas   | Detecta la apertura o cierre, ideal para monitorear entradas.                                 | $100 MXN        | [Ver en MercadoLibre](https://articulo.mercadolibre.com.mx/MLM-791887986-2-piezas-sensor-magnetico-para-ventana-switch-puerta-arduino-_JM) |
| Sensor de luminosidad (GY-302)         | Mide la luz ambiental para activar el sistema según la iluminación del entorno.               | $60 MXN         | [Ver en MercadoLibre](https://articulo.mercadolibre.com.mx/MLM-640937024-modulo-sensor-de-intensidad-luminosa-luz-gy-302-bh1750-_JM)        |

---

### ⚙️ Actuadores

| Actuador                               | Función                                                                                       | Precio estimado | Enlace de compra                                                                                                                  |
|----------------------------------------|------------------------------------------------------------------------------------------------|-----------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Cerradura electromagnética             | Asegura puertas automáticamente al detectar intrusos.                                          | $250 MXN        | -                                                                                                                                |
| Alarma sonora (Buzzer)                 | Emite sonido al detectar movimientos o aperturas sospechosas.                                 | $35 MXN         | [Ver en MercadoLibre](https://articulo.mercadolibre.com.mx/MLM-593451492-modulo-zumbador-buzzer-5v-arduino-rasp-pic-_JM)         |
| Módulo LED RGB de 7 colores (KY-016)   | Iluminación de alerta visual o simulación de presencia.                                       | $5 MXN          | [Ver en MercadoLibre](https://articulo.mercadolibre.com.mx/MLM-2068584115-sensor-led-rgb-modulo-ky-016-compatible-con-arduino-_JM) |
| Pantalla táctil                        | Interfaz gráfica para visualizar eventos y controlar el sistema.                              | $400 MXN        | -                                                                                                                                |

---

## ⚙️ Funcionamiento del Sistema

- Monitoreo continuo de **movimiento**, **apertura de puertas/ventanas**, y **nivel de luminosidad**.
- Ante cualquier evento inusual:
  - Se activa la **cerradura electromagnética**.
  - Suena una **alarma sonora (buzzer)**.
  - Se encienden **luces LED RGB** de advertencia.
- Todos los eventos se **registran en una base de datos** (PostgreSQL).
- Interfaz táctil y aplicación móvil muestran:
  - Estado en tiempo real.
  - Historial de eventos.
  - Notificaciones mediante protocolo **MQTT** o servicios de notificación.

---

## 📡 Tecnologías y Protocolo

| Elemento                   | Descripción                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| Microcontrolador          | ESP32 (conectividad Wi-Fi integrada).                                       |
| Comunicación remota       | MQTT para enviar/recibir eventos entre sensores y plataforma móvil.         |
| Base de datos             | PostgreSQL para almacenar eventos de seguridad.                             |
| Monitoreo visual          | Pantalla táctil + Aplicación móvil (conectadas vía Wi-Fi).                  |
| Interfaz en Node.js       | Backend para manejar datos, notificaciones y conexión con base de datos.    |

---

## 🧱 Materiales Sugeridos para Ensamblaje

| Material     | Uso                                                                 |
|--------------|----------------------------------------------------------------------|
| Plástico o metal | Estructura externa del sistema para protección física y montaje.    |
| Madera       | Acabado estético y robusto para el hogar.                           |

---

## 📱 Características del Monitoreo

- Plataforma disponible en:
  - **Pantalla física** (interfaz local)
  - **Dispositivo móvil** (interfaz web o app)
- Permite:
  - Activar/desactivar elementos del sistema.
  - Ver estado actual de sensores y actuadores.
  - Recibir alertas inmediatas.

---

## 📝 Notas

- Este sistema puede expandirse fácilmente con más sensores (gas, humo, cámaras).
- Ideal para proyectos de domótica y seguridad doméstica con enfoque IoT.
