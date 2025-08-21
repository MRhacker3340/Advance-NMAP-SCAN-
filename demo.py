#!/usr/bin/env python3
"""
Advanced Nmap Scanner Demo
Demonstrates all features of the scanner
"""

import subprocess
import sys
import os
import time

def print_section(title):
    """Print a section header"""
    print("\n" + "="*80)
    print(f"🎯 {title}")
    print("="*80)

def run_demo_command(description, command, pause=True):
    """Run a demo command with description"""
    print(f"\n🔍 {description}")
    print(f"💻 Command: {' '.join(command)}")
    print("-" * 60)
    
    try:
        result = subprocess.run(command, text=True, timeout=60)
        if pause:
            input("\n⏸️  Press Enter to continue to next demo...")
    except subprocess.TimeoutExpired:
        print("⏰ Demo command timed out")
    except KeyboardInterrupt:
        print("\n⚠️  Demo interrupted by user")
        sys.exit(1)

def main():
    print("""
 █████╗ ██████╗ ██╗   ██╗ █████╗ ███╗   ██╗ ██████╗███████╗██████╗     ██████╗ ███████╗███╗   ███╗ ██████╗ 
██╔══██╗██╔══██╗██║   ██║██╔══██╗████╗  ██║██╔════╝██╔════╝██╔══██╗    ██╔══██╗██╔════╝████╗ ████║██╔═══██╗
███████║██║  ██║██║   ██║███████║██╔██╗ ██║██║     █████╗  ██║  ██║    ██║  ██║█████╗  ██╔████╔██║██║   ██║
██╔══██║██║  ██║╚██╗ ██╔╝██╔══██║██║╚██╗██║██║     ██╔══╝  ██║  ██║    ██║  ██║██╔══╝  ██║╚██╔╝██║██║   ██║
██║  ██║██████╔╝ ╚████╔╝ ██║  ██║██║ ╚████║╚██████╗███████╗██████╔╝    ██████╔╝███████╗██║ ╚═╝ ██║╚██████╔╝
╚═╝  ╚═╝╚═════╝   ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝╚═════╝     ╚═════╝ ╚══════╝╚═╝     ╚═╝ ╚═════╝ 
                                                                                                              
    🚀 Welcome to the Advanced Nmap Scanner Demo!
    This demonstration will showcase all the key features of the scanner.
    
    Target: 127.0.0.1 (localhost - safe for demonstration)
    
    Note: Some scans may take a few seconds to complete.
    """)
    
    input("Press Enter to start the demo...")
    
    scanner_path = os.path.join(os.path.dirname(__file__), 'advanced_nmap_scanner.py')
    
    if not os.path.exists(scanner_path):
        print(f"❌ Scanner not found at: {scanner_path}")
        sys.exit(1)
    
    # Demo 1: Help and Banner
    print_section("1. HELP SYSTEM & BANNER")
    run_demo_command(
        "Display help information",
        ['python3', scanner_path, '--help']
    )
    
    # Demo 2: Host Discovery
    print_section("2. HOST DISCOVERY")
    run_demo_command(
        "Discover if host is alive (ping sweep)",
        ['python3', scanner_path, '-t', '127.0.0.1', '--host-discovery']
    )
    
    # Demo 3: Quick Scan
    print_section("3. QUICK PORT SCAN")
    run_demo_command(
        "Quick scan of top 1000 ports",
        ['python3', scanner_path, '-t', '127.0.0.1', '--quick']
    )
    
    # Demo 4: Specific Ports
    print_section("4. SPECIFIC PORT SCANNING")
    run_demo_command(
        "Scan specific ports (SSH, HTTP, HTTPS)",
        ['python3', scanner_path, '-t', '127.0.0.1', '--ports', '22,80,443']
    )
    
    # Demo 5: Stealth Scan
    print_section("5. STEALTH SCANNING")
    run_demo_command(
        "Stealth SYN scan (half-open connections)",
        ['python3', scanner_path, '-t', '127.0.0.1', '--stealth', '--ports', '22,80,443']
    )
    
    # Demo 6: Service Version Detection
    print_section("6. SERVICE VERSION DETECTION")
    run_demo_command(
        "Detect service versions on open ports",
        ['python3', scanner_path, '-t', '127.0.0.1', '--service-version', '--ports', '22,80']
    )
    
    # Demo 7: TCP Connect Scan
    print_section("7. TCP CONNECT SCAN")
    run_demo_command(
        "Full TCP connection scan",
        ['python3', scanner_path, '-t', '127.0.0.1', '--tcp-connect', '--ports', '22,80,443']
    )
    
    # Demo 8: NSE Scripts
    print_section("8. NSE SCRIPT EXECUTION")
    run_demo_command(
        "Run SSH host key detection script",
        ['python3', scanner_path, '-t', '127.0.0.1', '--nse-script', 'ssh-hostkey', '--ports', '22']
    )
    
    # Demo 9: Save Results
    print_section("9. SAVE RESULTS TO FILE")
    run_demo_command(
        "Save scan results to timestamped file",
        ['python3', scanner_path, '-t', '127.0.0.1', '--quick', '--save-results']
    )
    
    # Demo 10: Utility Scripts
    print_section("10. UTILITY SCRIPTS")
    
    quick_scan_path = os.path.join(os.path.dirname(__file__), 'quick_scan.py')
    if os.path.exists(quick_scan_path):
        run_demo_command(
            "Run comprehensive quick scan utility",
            ['python3', quick_scan_path, '127.0.0.1'],
            pause=False
        )
    
    # Summary
    print_section("DEMO COMPLETE!")
    print("""
🎉 Congratulations! You've seen all the major features of the Advanced Nmap Scanner:

✅ Host Discovery - Find live hosts on networks
✅ Port Scanning - Quick scans, full scans, specific ports
✅ Service Detection - Identify services and versions
✅ Stealth Scanning - Avoid detection with SYN scans
✅ NSE Scripts - Extensible script engine
✅ Result Export - Save findings to files
✅ Multiple Scan Types - TCP, UDP, aggressive modes
✅ User-Friendly Interface - Clear output and options

🔍 NEXT STEPS:
• Try scanning your own network: python3 advanced_nmap_scanner.py -t 192.168.1.0/24 --host-discovery
• Explore NSE scripts: python3 advanced_nmap_scanner.py -t target --nse-script http-enum
• Use for penetration testing: python3 advanced_nmap_scanner.py -t target --aggressive
• Check the README.md for more examples and documentation

⚠️  REMEMBER: Only scan networks you own or have permission to test!

Happy hunting! 🎯
    """)
    
    # Show created files
    print("\n📁 Files created during demo:")
    try:
        result = subprocess.run(['ls', '-la', '*.txt'], capture_output=True, text=True, cwd=os.path.dirname(__file__))
        if result.returncode == 0:
            print(result.stdout)
        else:
            print("No scan result files found.")
    except:
        print("Could not list files.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️ Demo interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Demo error: {str(e)}")
        sys.exit(1)