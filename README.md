# 🏠 Sistema de Seguridad y Automatización para el Hogar

Este proyecto implementa un sistema inteligente de seguridad doméstica que integra sensores, actuadores y una interfaz de monitoreo en una pantalla de Raspberry Pi, para ofrecer protección en tiempo real y respuesta automatizada ante eventos sospechosos.

---

## 📦 Componentes del Sistema

### 🔍 Sensores

| Sensor                                 | Función                                                                                      | Precio estimado | Enlace de compra                                                                                                                   |
|----------------------------------------|-----------------------------------------------------------------------------------------------|-----------------|------------------------------------------------------------------------------------------------------------------------------------|
| Sensor de movimiento (PIR)             | Detecta la presencia de personas en zonas estratégicas.                                       | $70 MXN         | ![image](https://github.com/user-attachments/assets/96e3feb2-3243-4aeb-b737-dc8b5042c66d)
 |
| Sensor magnético de puertas/ventanas   | Detecta la apertura o cierre, ideal para monitorear entradas.                                 | $100 MXN        | ![image](https://github.com/user-attachments/assets/0e3a6ee9-f653-42e4-9ba6-29b930e8a6c4)
 |
| Sensor de lectura NFC        | Garantiza el acceso y controla quien puede entrar y quien no              | $30 MXN         | ![image](https://github.com/user-attachments/assets/da28a110-a10e-45f0-b60f-63177d238a76)
     |

---

### ⚙️ Actuadores

| Actuador                               | Función                                                                                       | Precio estimado | Enlace de compra                                                                                                                  |
|----------------------------------------|------------------------------------------------------------------------------------------------|-----------------|-----------------------------------------------------------------------------------------------------------------------------------|                                                                                                                             |
| Alarma sonora (Buzzer)                 | Emite sonido al detectar movimientos o aperturas sospechosas.                                 | $35 MXN         | ![image](https://github.com/user-attachments/assets/b55f9377-e232-47cd-a03b-d1223a9a00ff)
      |
| Cinta LED WS2812B | Iluminación de alerta visual o simulación de presencia.                                                            | $40 MXN          | ![image](https://github.com/user-attachments/assets/12be199b-f9e9-43c0-98df-ca089a4a1a65)
 |
| Pantalla táctil                        | Interfaz gráfica para visualizar eventos y controlar el sistema.                              | $487 MXN        | - 
 ![image](https://github.com/user-attachments/assets/dc6bc78a-3607-4741-81ba-d8af06dbe695)    |

---

## ⚙️ Funcionamiento del Sistema

- Monitoreo continuo de **movimiento**, **apertura de puertas/ventanas**.
- Ante cualquier evento inusual:
  - Se abre la puerta
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
| Monitoreo visual          | Pantalla táctil (conectada vía Wi-Fi).                                      |

---

## 🧱 Materiales de Ensamblaje

| Material     | Uso                                                                 |
|--------------|----------------------------------------------------------------------|
| Plástico o metal | Creacio de ventana   |
| Madera       | Creacion completa de la casa y estructura para almacenar cables y componentes |

---

## 📝 Firma de ingeniera en procesos industriales: Ana Maria Fabiola Ramirez Vazquez | Egresada de: Universidad Tecnologica del Norte de Guanajuato

---
## 📱 Características del Monitoreo

- Plataforma disponible en:
  - **Pantalla física** (interfaz local)
    ![IMG_20250422_113644](https://github.com/user-attachments/assets/c09f5314-27ce-4f51-bfc1-8ae99ecf730c)
- Permite:
  - Ver estado actual de sensores y actuadores.
    ![image](https://github.com/user-attachments/assets/1a775980-b5be-46fa-b1d3-ea330c0931f7)
  - Recibir alertas inmediatas.
    ![image](https://github.com/user-attachments/assets/408aaf36-4658-4ca2-82ff-d68a762f1aed)

## 📔 Diagrama de conexion

![WhatsApp Image 2025-04-23 at 14 19 58_8eb88e7a](https://github.com/user-attachments/assets/0d5c6544-a294-4e7d-9292-73d284c03e36)


## 🚨 Evidencia de trabajo

### 💻 Fotos

![IMG_20250422_003142](https://github.com/user-attachments/assets/60588bbd-1964-4f74-87e3-704d7539c41b)
![IMG_20250423_132339](https://github.com/user-attachments/assets/0f9ef68c-a74e-461a-802f-3dc76fa77041)
![IMG_20250423_132343](https://github.com/user-attachments/assets/c18cdd0f-0adb-44e8-9349-658fd467fd22)
![IMG-20250422-WA0015](https://github.com/user-attachments/assets/d403049e-640c-44da-9cee-6866587c5472)
![IMG-20250421-WA0006](https://github.com/user-attachments/assets/d5a63d54-dc34-4639-bff5-9a34285e6c40)
![IMG-20250422-WA0010](https://github.com/user-attachments/assets/5dd4e44d-a665-4936-a0c3-b71ed006813c)
![WhatsApp Image 2025-04-23 at 14 00 54_85dd6915](https://github.com/user-attachments/assets/8995f6a2-4ba5-45ff-af03-f13e4ef5d656)

### 🎥 Video de funcionamiento
https://youtube.com/shorts/aCrdjMsCMPE
---

### 💻 Codigos

[Ver codigo de flujo de node-red](flows.json)
[Ver codigo principal del proyecto](elcodigoquejala.py)

## 📝 Notas
- Este sistema puede expandirse fácilmente con más sensores (gas, humo, cámaras).
