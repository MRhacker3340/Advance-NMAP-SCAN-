#!/usr/bin/env python3
"""
Vulnerability Scanner
Focused vulnerability scanning using NSE scripts
"""

import subprocess
import sys
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 vuln_scan.py <target>")
        print("Examples:")
        print("  python3 vuln_scan.py 192.168.1.1")
        print("  python3 vuln_scan.py example.com")
        sys.exit(1)
    
    target = sys.argv[1]
    scanner_path = os.path.join(os.path.dirname(__file__), 'advanced_nmap_scanner.py')
    
    print(f"🔍 Running vulnerability scan on {target}...")
    print("This will check for common vulnerabilities using NSE scripts")
    print("-" * 60)
    
    # Run vulnerability scan
    subprocess.run([
        'python3', scanner_path, 
        '-t', target, 
        '--vulnerability', 
        '--save-results',
        '--no-banner'
    ])
    
    print("\n" + "="*60)
    print("💡 Additional NSE scripts you can run:")
    print("  --nse-script http-enum")
    print("  --nse-script smb-enum-shares")
    print("  --nse-script ftp-anon")
    print("  --nse-script ssh-hostkey")

if __name__ == "__main__":
    main()