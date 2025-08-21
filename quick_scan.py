#!/usr/bin/env python3
"""
Quick Network Scanner
A simplified wrapper for common scanning tasks
"""

import subprocess
import sys
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 quick_scan.py <target>")
        print("Examples:")
        print("  python3 quick_scan.py 192.168.1.1")
        print("  python3 quick_scan.py example.com")
        print("  python3 quick_scan.py 192.168.1.0/24")
        sys.exit(1)
    
    target = sys.argv[1]
    scanner_path = os.path.join(os.path.dirname(__file__), 'advanced_nmap_scanner.py')
    
    print(f"🚀 Running comprehensive scan on {target}...")
    print("This will perform: Host Discovery → Quick Scan → Service Detection")
    print("-" * 60)
    
    # Run host discovery
    subprocess.run([
        'python3', scanner_path, 
        '-t', target, 
        '--host-discovery', 
        '--no-banner'
    ])
    
    print("\n" + "="*60)
    
    # Run quick scan
    subprocess.run([
        'python3', scanner_path, 
        '-t', target, 
        '--quick', 
        '--no-banner'
    ])
    
    print("\n" + "="*60)
    
    # Run service version detection
    subprocess.run([
        'python3', scanner_path, 
        '-t', target, 
        '--service-version', 
        '--no-banner'
    ])

if __name__ == "__main__":
    main()