from collections import Counter
from colorama import Fore, Style

def detect_weak_networks(networks):
    """Identifies open networks or those using weak encryption (WEP/WPA1)."""
    weak_networks = []
    for network in networks:
        security = network.split()[-1]  # Last column is SECURITY
        if "WEP" in security or "WPA1" in security or "NONE" in security:
            weak_networks.append(network)

    return weak_networks

def detect_evil_twins(networks):
    """Detects multiple networks with the same SSID (Evil Twin Attack)."""
    ssids = [network.split()[0] for network in networks if network.strip()]
    duplicate_ssids = [ssid for ssid, count in Counter(ssids).items() if count > 1]

    return duplicate_ssids
