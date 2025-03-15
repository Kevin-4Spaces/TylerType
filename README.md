### **📌 TylerType **
A simple Python app that runs in the background and counts the number of key presses. It displays a small window with the total count and supports minimizing to the system tray.

---

## **🔧 Features**
✔️ Runs in the background and listens for key presses  
✔️ Displays a counter in a small window  
✔️ Works on **Windows** and **macOS**  
✔️ Minimizes to the system tray (optional)  

---

## **🚀 Installation & Setup**
### **1️⃣ Install Dependencies**
Make sure you have Python installed, then install the required packages:

```sh
pip install -r requirements.txt
```

---

### **2️⃣ Run the App**
To start the Key Counter:

```sh
python key_counter.py
```

---

## **🖥️ Creating a Standalone Executable**
You can package the app into a standalone executable.

### **Windows (.exe)**
```sh
pyinstaller --onefile --windowed key_counter.py
```
- The `.exe` will be in the `dist/` folder.

### **macOS (.app)**
```sh
pyinstaller --onefile --windowed --name "TylerType" key_counter.py
```
- The app bundle will be in `dist/TylerType.app`.

---

## **📂 File Structure**
```
/KeyCounter
│── key_counter.py       # Main application script
│── requirements.txt     # Dependencies
│── README.md            # Project documentation
└── dist/                # Executable output (after running PyInstaller)
```

---

## **🔧 Troubleshooting**
- **macOS: Tkinter Warning**  
  If you see `DEPRECATION WARNING: The system version of Tk is deprecated`, install the latest Tk:

  ```sh
  brew install tcl-tk
  ```

- **PyInstaller Not Found?**  
  Ensure it's installed:

  ```sh
  pip install pyinstaller
  ```

- **App Crashes on macOS?**  
  Run with:

  ```sh
  python -m key_counter.py
  ```

---

## **📝 License**
This project is open-source. Feel free to modify and improve it! 🚀
