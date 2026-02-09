import requests
import psutil
import platform
import time

SERVER_URL = "http://127.0.0.1:5000/api/report"

def get_report():
    procs = []
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            procs.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return {"machine_name": platform.node(), "processes": procs[:50]}

def run():
    print(f"[*] Agent active on {platform.node()}")
    while True:
        try:
            r = requests.post(SERVER_URL, json=get_report())
            cmd = r.json()
            if cmd.get("action") == "kill":
                pid = cmd.get("pid")
                psutil.Process(pid).terminate()
                print(f"[!] Terminated PID: {pid}")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(5)

if __name__ == "__main__":
    run()