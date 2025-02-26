from datetime import datetime
from scanner import scan_wifi
from analyzer import detect_weak_networks, detect_evil_twins
from colorama import Fore, Style

def main():
    print(f"\n🔍 Scan Time: {datetime.now()}\n")

    networks = scan_wifi()
    if not networks:
        print(Fore.RED + "No networks detected. Are you connected to Wi-Fi?" + Style.RESET_ALL)
        return

    # Detect weak networks
    weak_networks = detect_weak_networks(networks)
    if weak_networks:
        print(Fore.RED + "⚠️ Insecure Networks Found:" + Style.RESET_ALL)
        for network in weak_networks:
            print(Fore.RED + f"  - {network}" + Style.RESET_ALL)
    else:
        print(Fore.GREEN + "✅ No insecure networks detected." + Style.RESET_ALL)

    # Detect Evil Twin attacks
    evil_twins = detect_evil_twins(networks)
    if evil_twins:
        print(Fore.YELLOW + "\n🚨 Possible Evil Twin Attack Detected! 🚨" + Style.RESET_ALL)
        for ssid in evil_twins:
            print(Fore.YELLOW + f"⚠️ Multiple networks with SSID: {ssid}" + Style.RESET_ALL)
    else:
        print(Fore.GREEN + "\n✅ No Evil Twin networks detected." + Style.RESET_ALL)

if __name__ == "__main__":
    main()