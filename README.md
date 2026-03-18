# 🤖 Smart Desktop Organizer

An automated Python background service that monitors your Downloads directory in real-time and intelligently categorizes incoming files into specific folders based on their extensions.

## ✨ Features
- **Real-Time Tracking:** Instantly detects newly downloaded files using the `watchdog` library.
- **Smart Categorization:** Automatically sorts files into `Images`, `Documents`, `Videos`, `Audio`, `Archives`, and `Executables`.
- **Desktop Notifications:** Alerts the user with a system notification using `plyer` upon a successful file transfer.
- **Cross-Platform:** Dynamically locates the Downloads folder, making it compatible with Windows, macOS, and Linux.

## 📸 Screenshots
<div align="center">
  <img src="image (1).png" alt="Files Organized" width="400">
  <img src="image (4).png" alt="Desktop Notification" width="400">
</div>

## 🛠️ Technologies Used
- **Python 3.x**
- `watchdog` (File system events monitoring)
- `plyer` (Cross-platform notifications)
- `shutil` & `os` (File operations)

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Ahmed-Saeed-Abdullah-Alshanwany/Smart-Desktop-Organizer.git](https://github.com/Ahmed-Saeed-Abdullah-Alshanwany/Smart-Desktop-Organizer.git)

   cd Smart-Desktop-Organizer

2. **Install the required dependencies:**
```bash
pip install watchdog plyer
```
3. **Run the script:**
```bash
python organizer.py
```
