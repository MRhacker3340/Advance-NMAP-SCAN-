#!/usr/bin/env python3
"""
Example Usage Scripts for Advanced Nmap Scanner
Real-world scenarios for bug hunters and pentesters
"""

import os

def print_example(title, description, commands):
    """Print a formatted example"""
    print(f"\n{'='*80}")
    print(f"🎯 {title}")
    print(f"📝 {description}")
    print(f"{'='*80}")
    
    for i, cmd in enumerate(commands, 1):
        print(f"\n{i}. {cmd['desc']}")
        print(f"   💻 {cmd['cmd']}")

def main():
    print("""
 🔍 ADVANCED NMAP SCANNER - EXAMPLE USAGE SCENARIOS
 
 This guide shows real-world examples for different penetration testing
 and bug hunting scenarios using the Advanced Nmap Scanner.
 
 ⚠️  IMPORTANT: Only use these examples on networks you own or have 
     explicit permission to test!
    """)

    examples = [
        {
            "title": "WEB APPLICATION SECURITY TESTING",
            "description": "Comprehensive scanning for web application penetration testing",
            "commands": [
                {
                    "desc": "Initial quick scan to identify web services",
                    "cmd": "python3 advanced_nmap_scanner.py -t example.com --quick --save-results"
                },
                {
                    "desc": "Detailed scan of web ports with service detection",
                    "cmd": "python3 advanced_nmap_scanner.py -t example.com --ports 80,443,8080,8443,9090 --service-version"
                },
                {
                    "desc": "HTTP enumeration and vulnerability scanning",
                    "cmd": "python3 advanced_nmap_scanner.py -t example.com --nse-script 'http-*' --ports 80,443"
                },
                {
                    "desc": "SSL/TLS security assessment",
                    "cmd": "python3 advanced_nmap_scanner.py -t example.com --nse-script ssl-enum-ciphers --ports 443"
                }
            ]
        },
        {
            "title": "INTERNAL NETWORK PENETRATION TESTING",
            "description": "Complete internal network assessment workflow",
            "commands": [
                {
                    "desc": "Network discovery - find live hosts",
                    "cmd": "python3 advanced_nmap_scanner.py -t 192.168.1.0/24 --host-discovery --save-results"
                },
                {
                    "desc": "Quick scan of discovered hosts",
                    "cmd": "python3 advanced_nmap_scanner.py -t 192.168.1.1-254 --quick --save-results"
                },
                {
                    "desc": "Comprehensive scan of critical server",
                    "cmd": "python3 advanced_nmap_scanner.py -t 192.168.1.10 --aggressive --save-results"
                },
                {
                    "desc": "Stealth scan to avoid detection",
                    "cmd": "python3 advanced_nmap_scanner.py -t 192.168.1.0/24 --stealth --ports 22,135,139,445"
                }
            ]
        },
        {
            "title": "WINDOWS ACTIVE DIRECTORY ASSESSMENT",
            "description": "Scanning and enumeration for Windows AD environments",
            "commands": [
                {
                    "desc": "Identify Windows systems and services",
                    "cmd": "python3 advanced_nmap_scanner.py -t 192.168.1.0/24 --ports 135,139,445,3389 --service-version"
                },
                {
                    "desc": "SMB enumeration and vulnerability detection",
                    "cmd": "python3 advanced_nmap_scanner.py -t 192.168.1.100 --nse-script 'smb-*' --ports 445"
                },
                {
                    "desc": "Domain controller identification",
                    "cmd": "python3 advanced_nmap_scanner.py -t 192.168.1.100 --nse-script 'ldap-*' --ports 389,636"
                },
                {
                    "desc": "RDP security assessment",
                    "cmd": "python3 advanced_nmap_scanner.py -t 192.168.1.100 --nse-script rdp-enum-encryption --ports 3389"
                }
            ]
        },
        {
            "title": "LINUX SERVER ASSESSMENT",
            "description": "Security testing of Linux servers and services",
            "commands": [
                {
                    "desc": "Comprehensive server scan",
                    "cmd": "python3 advanced_nmap_scanner.py -t 192.168.1.50 --aggressive --save-results"
                },
                {
                    "desc": "SSH security assessment",
                    "cmd": "python3 advanced_nmap_scanner.py -t 192.168.1.50 --nse-script 'ssh-*' --ports 22"
                },
                {
                    "desc": "FTP service enumeration",
                    "cmd": "python3 advanced_nmap_scanner.py -t 192.168.1.50 --nse-script 'ftp-*' --ports 21"
                },
                {
                    "desc": "Database service detection",
                    "cmd": "python3 advanced_nmap_scanner.py -t 192.168.1.50 --ports 3306,5432,1433,27017 --service-version"
                }
            ]
        },
        {
            "title": "IoT AND EMBEDDED DEVICE TESTING",
            "description": "Security assessment of IoT devices and embedded systems",
            "commands": [
                {
                    "desc": "IoT device discovery",
                    "cmd": "python3 advanced_nmap_scanner.py -t 192.168.1.0/24 --ports 23,80,443,8080,9000 --service-version"
                },
                {
                    "desc": "Telnet service enumeration",
                    "cmd": "python3 advanced_nmap_scanner.py -t 192.168.1.200 --nse-script telnet-encryption --ports 23"
                },
                {
                    "desc": "Web interface vulnerability scan",
                    "cmd": "python3 advanced_nmap_scanner.py -t 192.168.1.200 --vulnerability --ports 80,443,8080"
                },
                {
                    "desc": "SNMP enumeration",
                    "cmd": "python3 advanced_nmap_scanner.py -t 192.168.1.200 --nse-script snmp-sysdescr --ports 161"
                }
            ]
        },
        {
            "title": "WIRELESS NETWORK ASSESSMENT",
            "description": "Testing wireless access points and related infrastructure",
            "commands": [
                {
                    "desc": "Access point web interface scan",
                    "cmd": "python3 advanced_nmap_scanner.py -t 192.168.0.1 --ports 80,443,8080 --service-version"
                },
                {
                    "desc": "Router service enumeration",
                    "cmd": "python3 advanced_nmap_scanner.py -t 192.168.0.1 --nse-script 'http-*' --ports 80,443"
                },
                {
                    "desc": "SNMP community string detection",
                    "cmd": "python3 advanced_nmap_scanner.py -t 192.168.0.1 --nse-script snmp-brute --ports 161"
                }
            ]
        },
        {
            "title": "STEALTH AND EVASION TECHNIQUES",
            "description": "Advanced techniques to avoid detection during scans",
            "commands": [
                {
                    "desc": "Ultra-stealth SYN scan with timing",
                    "cmd": "python3 advanced_nmap_scanner.py -t 192.168.1.1 --stealth --ports 1-1000"
                },
                {
                    "desc": "Fragmented packet scan (add -f to nmap)",
                    "cmd": "# Modify scanner to add: command.extend(['-f'])"
                },
                {
                    "desc": "Randomize scan order (add --randomize-hosts)",
                    "cmd": "# For network scans: command.extend(['--randomize-hosts'])"
                },
                {
                    "desc": "Source port spoofing (add --source-port 53)",
                    "cmd": "# Modify scanner to add: command.extend(['--source-port', '53'])"
                }
            ]
        },
        {
            "title": "AUTOMATION AND SCRIPTING",
            "description": "Automating scans for large-scale assessments",
            "commands": [
                {
                    "desc": "Batch scan multiple targets",
                    "cmd": "for ip in 192.168.1.{1..10}; do python3 advanced_nmap_scanner.py -t $ip --quick --save-results; done"
                },
                {
                    "desc": "Automated vulnerability assessment",
                    "cmd": "python3 vuln_scan.py 192.168.1.100"
                },
                {
                    "desc": "Quick comprehensive scan",
                    "cmd": "python3 quick_scan.py 192.168.1.100"
                },
                {
                    "desc": "Create scan report directory",
                    "cmd": "mkdir scan_results_$(date +%Y%m%d) && mv scan_*.txt scan_results_$(date +%Y%m%d)/"
                }
            ]
        }
    ]

    for example in examples:
        print_example(example["title"], example["description"], example["commands"])

    print(f"\n{'='*80}")
    print("🎓 LEARNING RESOURCES")
    print(f"{'='*80}")
    print("""
📚 Additional NSE Scripts to Explore:
   • vuln - General vulnerability detection
   • brute - Brute force authentication
   • discovery - Service and host discovery
   • safe - Safe scripts that won't crash services
   • intrusive - More aggressive scanning scripts

🔧 Custom NSE Script Examples:
   • http-sql-injection - SQL injection detection
   • ssl-heartbleed - Heartbleed vulnerability check
   • smb-vuln-ms17-010 - EternalBlue vulnerability
   • dns-brute - DNS subdomain brute forcing

⚡ Performance Tips:
   • Use -T4 timing for faster scans (default in our tool)
   • Limit port ranges for faster results
   • Use --max-parallelism for controlling scan speed
   • Save results to files for analysis

🛡️ Ethical Guidelines:
   • Always get written permission before scanning
   • Respect rate limits and system resources
   • Follow responsible disclosure for vulnerabilities
   • Document your findings properly
   • Never use for malicious purposes
    """)

if __name__ == "__main__":
    main()