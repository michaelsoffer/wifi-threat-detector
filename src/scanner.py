import subprocess
import platform

def scan_wifi():
    os_name = platform.system().lower()
    if os_name == "windows":
        return scan_wifi_windows()
    elif os_name == "linux":
        return scan_wifi_linux()
    else:
        raise Exception(f"Unsupported OS: {os_name}")

def scan_wifi_windows():
    try:
        result = subprocess.run(["netsh", "wlan", "show", "networks", "mode=Bssid"], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        print(f"Error scanning Wi-Fi: {e}")
        return None

def scan_wifi_linux():
    try:
        result = subprocess.run(["nmcli", "-t", "-f", "SSID,SECURITY", "dev", "wifi"], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        print(f"Error scanning Wi-Fi: {e}")
        return None
