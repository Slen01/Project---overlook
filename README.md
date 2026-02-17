# Project Overlook: Remote Security Orchestrator (C2)

**Project Overlook** is a project featuring a custom Command and Control (C2) architecture. It allows for remote system monitoring and active threat response via a web-based dashboard.

## 🚀 Key Features
* **Live Process Monitor:** Real-time data exfiltration of running processes from the target agent.
* **Automated Threat Detection:** Visual highlighting of suspicious processes (e.g., cmd.exe, powershell.exe).
* **Remote Termination (Kill Switch):** Ability to remotely terminate any process on the target machine with a single click from the web UI.
* **Heartbeat Mechanism:** Distributed system architecture where the agent polls the server for instructions every 5 seconds.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Backend:** Flask (Web Server)
* **Agent Library:** `psutil` (System-level forensics & control)
* **Communication:** REST API (JSON payloads)
* **Frontend:** HTML5, CSS3 (Bootstrap), JavaScript

## 📦 Installation & Setup
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Slen01/Project---overlook.git](https://github.com/Slen01/Project---overlook.git)
   cd Project---overlook
