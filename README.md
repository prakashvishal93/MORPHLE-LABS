# Flask htop Viewer

This is a simple Flask application that displays system process information using the `top` command. It also shows the server's current IST time and the system user running the app.

## Live URL
Access the application at:

[**htop Viewer**](https://cautious-space-acorn-jw57v4v776wcj79q-5000.app.github.dev/htop)

## Features
- Displays system process information using the `top` command.
- Shows the current **IST (Indian Standard Time)**.
- Fetches the system's logged-in user.

## Installation & Setup

### Prerequisites
- Python 3.x
- Flask

### Steps
1. **Clone the repository**
   ```sh
   git clone <repository-url>
   cd <repository-name>
   ```
2. **Create a virtual environment (Optional but recommended)**
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```
3. **Install dependencies**
   ```sh
   pip install flask
   ```
4. **Run the application**
   ```sh
   python3 app.py
   ```
5. **Access the app**
   Open your browser and go to:
   ```
   http://127.0.0.1:5000/htop
   ```

## How It Works
- The app runs a Flask server with an endpoint `/htop`.
- It retrieves system process info using `top -b -n 1` (Linux) or `top -l 1` (macOS).
- Displays results in a structured format via a web page.

## Example Output
```
Name: Vishal Prakash
User: codespace
Server Time (IST): 2025-03-07 15:45:43.981512

TOP output:
<system process info>
```

## Deployment
You can deploy this app on **GitHub Codespaces**, AWS, or any cloud service supporting Flask.

---
### Author
**Vishal Prakash**