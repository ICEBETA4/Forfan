import os
import time
import random
import sys
from datetime import datetime

def clear_screen():
    """Clear the terminal screen based on OS."""
    os.system('cls' if os.name == 'nt' else 'clear')

def type_text(text, delay=0.03):
    """Display text with typewriter effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def matrix_rain(duration=3):
    """Display Matrix-style digital rain."""
    width = os.get_terminal_size().columns
    chars = "01ハムイタヤ"  # Mix of binary and Japanese-looking characters
    
    green = "\033[32m"
    bright_green = "\033[92m"
    reset = "\033[0m"
    
    start_time = time.time()
    while time.time() - start_time < duration:
        line = ""
        for _ in range(width):
            if random.random() > 0.8:  # 80% chance of characters
                char = random.choice(chars)
                # Random chance of bright green for emphasis
                color = bright_green if random.random() > 0.7 else green
                line += f"{color}{char}{reset}"
            else:
                line += " "
        print(line)
        time.sleep(0.05)
        
    clear_screen()

def fake_hack_progress(task, duration=2):
    """Show a fake hacking progress bar."""
    print(f"\033[93m[*] {task}...\033[0m")
    for i in range(101):
        bar = "█" * (i // 2) + " " * (50 - (i // 2))
        sys.stdout.write(f"\r[{bar}] {i}%")
        sys.stdout.flush()
        time.sleep(duration/100)
    print("\n\033[92m[+] Complete!\033[0m")
    time.sleep(0.3)

def show_ip_addresses():
    """Display fake IP tracking information."""
    ips = [
        "192.168.1.1",
        "10.0.0.138",
        "172.16.254.1",
        "8.8.8.8",
        "104.18.21.226",
        "45.33.32.156"
    ]
    
    print("\033[94m[*] Scanning network...\033[0m")
    time.sleep(0.5)
    
    print("\033[94m[*] IPs detected:\033[0m")
    for ip in ips:
        print(f"\033[96m    → {ip}\033[0m")
        time.sleep(0.2)
    
    target_ip = random.choice(ips)
    print(f"\n\033[91m[!] Target acquired: {target_ip}\033[0m")
    time.sleep(1)

def show_haytham_logo():
    """Display Haytham hacker logo."""
    logo = """
\033[92m
    ██╗  ██╗ █████╗ ██╗   ██╗████████╗██╗  ██╗ █████╗ ███╗   ███╗
    ██║  ██║██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔══██╗████╗ ████║
    ███████║███████║ ╚████╔╝    ██║   ███████║███████║██╔████╔██║
    ██╔══██║██╔══██║  ╚██╔╝     ██║   ██╔══██║██╔══██║██║╚██╔╝██║
    ██║  ██║██║  ██║   ██║      ██║   ██║  ██║██║  ██║██║ ╚═╝ ██║
    ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝
                                                                 
    ██╗  ██╗ █████╗  ██████╗██╗  ██╗    ██╗   ██╗ ██████╗ ██╗   ██╗
    ██║  ██║██╔══██╗██╔════╝██║ ██╔╝    ╚██╗ ██╔╝██╔═══██╗██║   ██║
    ███████║███████║██║     █████╔╝      ╚████╔╝ ██║   ██║██║   ██║
    ██╔══██║██╔══██║██║     ██╔═██╗       ╚██╔╝  ██║   ██║██║   ██║
    ██║  ██║██║  ██║╚██████╗██║  ██╗       ██║   ╚██████╔╝╚██████╔╝
    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ 
\033[0m
"""
    print(logo)

def simulate_terminal_access():
    """Simulate gaining terminal access to a system."""
    prompts = [
        "root@target-system:~# ",
        "admin@secure-server:~$ ",
        "haytham@victim-pc:/$ ",
        "system@breached:~# "
    ]
    
    commands = [
        "cat /etc/passwd",
        "ls -la /home/",
        "whoami",
        "netstat -tuln",
        "ps aux",
        "sudo rm -rf /*",  # This is just for show, not a real command to execute!
        "download user_credentials.db",
        "./persistence.sh",
        "export LOOT=/tmp/extracted"
    ]
    
    prompt = random.choice(prompts)
    
    for _ in range(5):
        cmd = random.choice(commands)
        sys.stdout.write(f"\033[92m{prompt}\033[0m")
        type_text(cmd, 0.05)
        
        # Simulate command output
        if "cat" in cmd:
            print("root:x:0:0:root:/root:/bin/bash")
            print("user:x:1000:1000:user:/home/user:/bin/bash")
            print("admin:x:1001:1001:admin:/home/admin:/bin/bash")
        elif "ls" in cmd:
            print("drwxr-xr-x 2 root  root  4096 Mar 15 15:34 .")
            print("drwxr-xr-x 4 root  root  4096 Mar 15 15:34 ..")
            print("drwx------ 15 user  user  4096 Mar 22 09:12 user")
            print("drwx------ 10 admin admin 4096 Mar 23 11:45 admin")
        elif "whoami" in cmd:
            print("root")
        elif "download" in cmd:
            fake_hack_progress("Downloading sensitive data", 3)
        elif "rm" in cmd:
            print("\033[91mSystem wiped. No traces left.\033[0m")
        else:
            # Generic output
            print("Command executed successfully.")
            
        time.sleep(0.5)

def run_hacking_simulation():
    """Run the main hacking simulation sequence."""
    clear_screen()
    
    # Intro
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f"\033[37m[{current_time}] \033[91mInitiating hack sequence...\033[0m")
    time.sleep(1)
    
    # Matrix rain effect
    matrix_rain(3)
    
    # Show logo
    show_haytham_logo()
    time.sleep(2)
    
    # Fake hacking progress
    fake_hack_progress("Bypassing firewall")
    fake_hack_progress("Cracking password hashes", 3)
    fake_hack_progress("Gaining system access", 2)
    
    # Show fake IP tracking
    show_ip_addresses()
    
    # Terminal access simulation
    print("\n\033[93m[*] Terminal access granted\033[0m")
    time.sleep(0.5)
    simulate_terminal_access()
    
    # Final message
    print("\n\033[91m")
    type_text("YOUR SYSTEM HAS BEEN COMPROMISED", 0.07)
    type_text("ALL YOUR DATA BELONGS TO HAYTHAM NOW", 0.07)
    print("\033[0m")
    
    # Flashing effect for dramatic ending
    for _ in range(5):
        clear_screen()
        time.sleep(0.2)
        show_haytham_logo()
        print("\n\033[91m        *** SYSTEM COMPROMISED ***\033[0m")
        time.sleep(0.2)
    
    print("\n\033[92m[Press Enter to exit]\033[0m")
    input()
    
    # Clean up terminal
    clear_screen()
    print("\033[0m")

if __name__ == "__main__":
    try:
        run_hacking_simulation()
    except KeyboardInterrupt:
        # Ensure clean exit on Ctrl+C
        print("\n\033[0mProgram terminated.")
    except Exception as e:
        print(f"\n\033[91mError: {e}\033[0m")
    finally:
        # Reset terminal colors
        print("\033[0m")
        
