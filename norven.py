#!/usr/bin/env python3
import os
import sys
import time
import threading
import subprocess
from datetime import datetime

# Farben für die GUI
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Norven:
    def __init__(self):
        self.clear()
        self.logo()
        self.menu()

    def clear(self):
        os.system('clear' if os.name == 'posix' else 'cls')

    def logo(self):
        logo = """
███╗   ██╗ ██████╗ ██████╗ ██╗   ██╗███████╗███╗   ██╗
████╗  ██║██╔═══██╗██╔══██╗██║   ██║██╔════╝████╗  ██║
██╔██╗ ██║██║   ██║██████╔╝██║   ██║█████╗  ██╔██╗ ██║
██║╚██╗██║██║   ██║��█╔══██╗╚██╗ ██╔╝██╔══╝  ██║╚██╗██║
██║ ╚████║╚██████╔╝██║  ██║ ╚████╔╝ ███████╗██║ ╚████║
╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝
        """
        print(Colors.HEADER + Colors.BOLD + logo + Colors.ENDC)

    def print_banner(self, text):
        print(Colors.OKCYAN + f"[+] {text}" + Colors.ENDC)

    def print_success(self, text):
        print(Colors.OKGREEN + f"[✔] {text}" + Colors.ENDC)

    def print_error(self, text):
        print(Colors.FAIL + f"[✖] {text}" + Colors.ENDC)

    def print_warning(self, text):
        print(Colors.WARNING + f"[!] {text}" + Colors.ENDC)

    def run_command(self, cmd):
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=60)
            print(result.stdout)
            if result.stderr:
                print(result.stderr)
        except subprocess.TimeoutExpired:
            self.print_error("Befehl dauerte zu lange.")
        except Exception as e:
            self.print_error(f"Fehler beim Ausführen: {e}")

    def menu(self):
        while True:
            self.clear()
            self.logo()
            print(Colors.OKBLUE + "=== NORDEN OSINT & HACKING SUITE ===" + Colors.ENDC)
            print(Colors.OKCYAN + "1. OSINT - Social Reconnaisance" + Colors.ENDC)
            print(Colors.OKCYAN + "2. Social Engineering (Phishing)" + Colors.ENDC)
            print(Colors.OKCYAN + "3. Brute Force (SSH/FTP)" + Colors.ENDC)
            print(Colors.OKCYAN + "4. Datenbank Hacking (SQLi)" + Colors.ENDC)
            print(Colors.OKCYAN + "5. Port Scan & Nmap" + Colors.ENDC)
            print(Colors.OKCYAN + "6. System Info & Ping" + Colors.ENDC)
            print(Colors.OKCYAN + "0. Exit" + Colors.ENDC)
            
            choice = input(Colors.WARNING + "\n> " + Colors.ENDC)
            
            if choice == '1':
                self.osint_menu()
            elif choice == '2':
                self.phishing_menu()
            elif choice == '3':
                self.bruteforce_menu()
            elif choice == '4':
                self.database_menu()
            elif choice == '5':
                self
