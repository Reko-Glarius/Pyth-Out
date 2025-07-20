
# 🥊 Pyth-Out

Controla el juego **"Super Punch-Out!!" (SNES)** usando los movimientos de tu cuerpo con visión por computadora y una cámara web.

Este proyecto usa **MediaPipe** para detectar tu pose corporal y simula entradas de teclado para jugar en el emulador **RetroArch**.

---

## 🎮 ¿Qué hace?

Convierte gestos reales en comandos del juego:

- ✋ Levantar los brazos → Defender (↑)
- 🤜 Gancho derecho → Golpe (A)
- 🤛 Gancho izquierdo → Golpe (Z)
- 💥 Golpe al hígado → Especial (X)
- ↔️ Mover el cuerpo → Esquivar (← y →)

---

## 🧰 Requisitos

- Python 3.9+ (recomendado)
- Una cámara web
- RetroArch con el juego "Super Punch-Out!!" cargado
- Teclado mapeado en RetroArch (teclas: A, Z, X, ←, →, ↑)

---

## 📦 Instalación (modo desarrollador)

1. Crea un entorno virtual:
   ```bash
   python -m venv venv
   ```

2. Activa el entorno:

   - En Windows:
     ```bash
     .\venv\Scripts\activate
     ```

3. Instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Ejecuta el script:
   ```bash
   python main.py
   ```

---

## 💾 Crear un ejecutable `.exe`

Con el entorno virtual activo:

```bash
pyinstaller --noconsole --onefile --add-data "venv\Lib\site-packages\mediapipe;mediapipe" main.py
```

El ejecutable estará en la carpeta `dist/`.

---

## 🚀 Uso

1. Abre **RetroArch** y carga "Super Punch-Out!!".
2. Ejecuta el programa (`python main.py` o `main.exe`).
3. Asegúrate de tener buena iluminación y que la cámara te vea bien (Ideal estas a una distancia de 2mt o más, para ver parte superior del cuerpo).
4. ¡Juega usando tu cuerpo!

Presiona `ESC` para cerrar el programa.

---

## 📸 Basado en

- [MediaPipe Pose](https://google.github.io/mediapipe/)
- [OpenCV](https://opencv.org/)
- [pyautogui](https://pyautogui.readthedocs.io/en/latest/)
- [pydirectinput](https://github.com/learncodebygaming/pydirectinput)

---

## 🧠 Autor

**Ricardo Aliste** – Proyecto personal para experimentar con control corporal en videojuegos clásicos.
