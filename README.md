# 🏠 Sistema de Seguridad y Automatización para el Hogar

Este proyecto implementa un sistema inteligente de seguridad doméstica que integra sensores, actuadores y una interfaz de monitoreo en una pantalla de Raspberry Pi, para ofrecer protección en tiempo real y respuesta automatizada ante eventos sospechosos.

---

## 📦 Componentes del Sistema

### 🔍 Sensores

| Sensor                             | Función                                                                 | Precio estimado | Imagen                                                                                             |
|------------------------------------|-------------------------------------------------------------------------|-----------------|----------------------------------------------------------------------------------------------------|
| Sensor de movimiento (PIR)         | Detecta la presencia de personas en zonas estratégicas.                 | $70 MXN         | <img src="https://github.com/user-attachments/assets/96e3feb2-3243-4aeb-b737-dc8b5042c66d" width="150"/> |
| Sensor magnético de puertas/ventanas | Detecta la apertura o cierre, ideal para entradas.                    | $100 MXN        | <img src="https://github.com/user-attachments/assets/0e3a6ee9-f653-42e4-9ba6-29b930e8a6c4" width="150"/> |
| Sensor de lectura NFC              | Controla el acceso al hogar.                                            | $30 MXN         | <img src="https://github.com/user-attachments/assets/da28a110-a10e-45f0-b60f-63177d238a76" width="150"/> |

---

### ⚙️ Actuadores

| Actuador                           | Función                                                                 | Precio estimado | Imagen                                                                                             |
|------------------------------------|-------------------------------------------------------------------------|-----------------|----------------------------------------------------------------------------------------------------|
| Alarma sonora (Buzzer)             | Emite sonido ante movimientos o aperturas sospechosas.                 | $35 MXN         | <img src="https://github.com/user-attachments/assets/b55f9377-e232-47cd-a03b-d1223a9a00ff" width="150"/> |
| Cinta LED WS2812B                  | Iluminación de alerta visual o simulación de presencia.                | $40 MXN         | <img src="https://github.com/user-attachments/assets/12be199b-f9e9-43c0-98df-ca089a4a1a65" width="150"/> |
| Pantalla táctil                    | Interfaz gráfica para monitoreo y control del sistema.                 | $487 MXN        | <img src="https://github.com/user-attachments/assets/dc6bc78a-3607-4741-81ba-d8af06dbe695" width="150"/> |

---

## ⚙️ Funcionamiento del Sistema

- Monitoreo continuo de **movimiento** y **apertura de puertas/ventanas**.
- Ante eventos inusuales:
  - Se abre la puerta.
  - Suena una **alarma sonora**.
  - Se encienden **luces LED RGB** de advertencia.
- Los eventos se **registran en una base de datos PostgreSQL**.
- Interfaz táctil y aplicación móvil muestran:
  - Estado en tiempo real.
  - Historial de eventos.
  - Notificaciones mediante protocolo **MQTT** o servicios de alerta.

---

## 📡 Tecnologías y Protocolo

| Elemento             | Descripción                                                               |
|----------------------|---------------------------------------------------------------------------|
| Microcontrolador     | ESP32 con conectividad Wi-Fi integrada.                                   |
| Comunicación remota  | MQTT para envío/recepción de eventos.                                     |
| Base de datos        | PostgreSQL para registrar eventos.                                        |
| Monitoreo visual     | Pantalla táctil conectada vía Wi-Fi.                                      |

---

## 🧱 Materiales de Ensamblaje

| Material            | Uso                                                                              |
|---------------------|----------------------------------------------------------------------------------|
| Plástico o metal    | Creación de ventana.                                                             |
| Madera              | Estructura para la casa y organización de cables y componentes.                 |

---

## 👩‍🎓 Firma de ingeniería

**Ana Maria Fabiola Ramirez Vazquez**  
*Ingeniera en Procesos Industriales - Universidad Tecnológica del Norte de Guanajuato*

---

## 📱 Características del Monitoreo

- Plataforma disponible en:
  - **Pantalla física (interfaz local)**  
    <img src="https://github.com/user-attachments/assets/c09f5314-27ce-4f51-bfc1-8ae99ecf730c" width="200"/>
- Permite:
  - Ver estado actual de sensores y actuadores.  
    <img src="https://github.com/user-attachments/assets/1a775980-b5be-46fa-b1d3-ea330c0931f7" width="200"/>
  - Recibir alertas inmediatas.  
    <img src="https://github.com/user-attachments/assets/408aaf36-4658-4ca2-82ff-d68a762f1aed" width="200"/>

---

## 📔 Diagrama de conexión

<img src="https://github.com/user-attachments/assets/0d5c6544-a294-4e7d-9292-73d284c03e36" width="400"/>

---

## 🚨 Evidencia de Trabajo

### 💻 Fotos

<p float="left">
  <img src="https://github.com/user-attachments/assets/60588bbd-1964-4f74-87e3-704d7539c41b" width="200"/>
  <img src="https://github.com/user-attachments/assets/0f9ef68c-a74e-461a-802f-3dc76fa77041" width="200"/>
  <img src="https://github.com/user-attachments/assets/c18cdd0f-0adb-44e8-9349-658fd467fd22" width="200"/>
  <img src="https://github.com/user-attachments/assets/d403049e-640c-44da-9cee-6866587c5472" width="200"/>
  <img src="https://github.com/user-attachments/assets/d5a63d54-dc34-4639-bff5-9a34285e6c40" width="200"/>
  <img src="https://github.com/user-attachments/assets/5dd4e44d-a665-4936-a0c3-b71ed006813c" width="200"/>
  <img src="https://github.com/user-attachments/assets/8995f6a2-4ba5-45ff-af03-f13e4ef5d656" width="200"/>
</p>

### 🎥 Video de funcionamiento

[![Ver video](https://img.youtube.com/vi/aCrdjMsCMPE/0.jpg)](https://youtube.com/shorts/aCrdjMsCMPE)

---

## 💻 Códigos

- [Ver código de flujo de Node-RED](flows.json)
- [Ver código principal del proyecto](elcodigoquejala.py)

---

## 📝 Notas

Este sistema puede expandirse fácilmente con más sensores (gas, humo, cámaras).  
