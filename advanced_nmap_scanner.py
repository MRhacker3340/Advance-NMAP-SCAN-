#!/usr/bin/env python3
"""
Advanced Nmap Scanner Tool
A comprehensive network scanning tool for bug hunters and pentesters
"""

import subprocess
import sys
import argparse
import json
import time
import os
from datetime import datetime
import ipaddress
import re

class AdvancedNmapScanner:
    def __init__(self):
        self.banner = """
 █████╗ ██████╗ ██╗   ██╗ █████╗ ███╗   ██╗ ██████╗███████╗██████╗ 
██╔══██╗██╔══██╗██║   ██║██╔══██╗████╗  ██║██╔════╝██╔════╝██╔══██╗
███████║██║  ██║██║   ██║███████║██╔██╗ ██║██║     █████╗  ██║  ██║
██╔══██║██║  ██║╚██╗ ██╔╝██╔══██║██║╚██╗██║██║     ██╔══╝  ██║  ██║
██║  ██║██████╔╝ ╚████╔╝ ██║  ██║██║ ╚████║╚██████╗███████╗██████╔╝
╚═╝  ╚═╝╚═════╝   ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝╚═════╝ 
    
    ███╗   ██╗███╗   ███╗ █████╗ ██████╗     ███████╗ ██████╗ █████╗ ███╗   ██╗
    ████╗  ██║████╗ ████║██╔══██╗██╔══██╗    ██╔════╝██╔════╝██╔══██╗████╗  ██║
    ██╔██╗ ██║██╔████╔██║███████║██████╔╝    ███████╗██║     ███████║██╔██╗ ██║
    ██║╚██╗██║██║╚██╔╝██║██╔══██║██╔═══╝     ╚════██║██║     ██╔══██║██║╚██╗██║
    ██║ ╚████║██║ ╚═╝ ██║██║  ██║██║         ███████║╚██████╗██║  ██║██║ ╚████║
    ╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝         ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                                                 
    Advanced Network Mapper for Bug Hunters & Pentesters v1.0
    Created for reconnaissance and network analysis
        """
        self.check_nmap_installation()
        
    def check_nmap_installation(self):
        """Check if nmap is installed on the system"""
        try:
            subprocess.run(['nmap', '--version'], capture_output=True, check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("❌ Error: nmap is not installed or not found in PATH")
            print("Please install nmap: sudo apt install nmap (Ubuntu/Debian) or brew install nmap (macOS)")
            sys.exit(1)
    
    def print_banner(self):
        """Print the tool banner"""
        print(self.banner)
        print("🔍 Starting Advanced Network Scanning...")
        print("-" * 80)
    
    def validate_target(self, target):
        """Validate target IP/hostname/network"""
        try:
            # Check if it's a valid IP address or network
            ipaddress.ip_address(target)
            return True
        except ValueError:
            try:
                # Check if it's a valid network
                ipaddress.ip_network(target, strict=False)
                return True
            except ValueError:
                # Check for hostname - more strict validation
                if re.match(r'^[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)*$', target):
                    return True
                # Check for IP ranges like 192.168.1.1-254
                if re.match(r'^(\d{1,3}\.){3}\d{1,3}-\d{1,3}$', target):
                    return True
                return False
    
    def run_nmap_command(self, command, description=""):
        """Execute nmap command and return results"""
        print(f"🔄 {description}")
        print(f"💻 Command: {' '.join(command)}")
        print("-" * 40)
        
        try:
            start_time = time.time()
            result = subprocess.run(command, capture_output=True, text=True, timeout=300)
            end_time = time.time()
            
            if result.returncode == 0:
                print(f"✅ Scan completed in {end_time - start_time:.2f} seconds")
                print("\n📊 Results:")
                print(result.stdout)
                return result.stdout
            else:
                print(f"❌ Error running command: {result.stderr}")
                return None
                
        except subprocess.TimeoutExpired:
            print("⏰ Command timed out after 5 minutes")
            return None
        except Exception as e:
            print(f"❌ Exception occurred: {str(e)}")
            return None
    
    def host_discovery(self, target):
        """Perform host discovery scan"""
        command = ['nmap', '-sn', target]
        return self.run_nmap_command(command, f"Host Discovery Scan on {target}")
    
    def quick_scan(self, target):
        """Perform quick scan of top 1000 ports"""
        command = ['nmap', '-T4', '-F', target]
        return self.run_nmap_command(command, f"Quick Scan (Top 1000 ports) on {target}")
    
    def full_port_scan(self, target):
        """Scan all 65535 ports"""
        command = ['nmap', '-p-', '-T4', target]
        return self.run_nmap_command(command, f"Full Port Scan (all 65535 ports) on {target}")
    
    def specific_port_scan(self, target, ports):
        """Scan specific ports"""
        command = ['nmap', '-p', ports, '-T4', target]
        return self.run_nmap_command(command, f"Specific Port Scan ({ports}) on {target}")
    
    def service_version_scan(self, target, ports=None):
        """Perform service version detection"""
        command = ['nmap', '-sV', '-T4']
        if ports:
            command.extend(['-p', ports])
        command.append(target)
        return self.run_nmap_command(command, f"Service Version Detection on {target}")
    
    def os_detection_scan(self, target):
        """Perform OS detection"""
        command = ['nmap', '-O', '-T4', target]
        return self.run_nmap_command(command, f"OS Detection Scan on {target}")
    
    def aggressive_scan(self, target):
        """Perform aggressive scan (OS detection, version detection, script scanning, and traceroute)"""
        command = ['nmap', '-A', '-T4', target]
        return self.run_nmap_command(command, f"Aggressive Scan on {target}")
    
    def stealth_scan(self, target, ports=None):
        """Perform stealth/SYN scan"""
        command = ['nmap', '-sS', '-T4']
        if ports:
            command.extend(['-p', ports])
        command.append(target)
        return self.run_nmap_command(command, f"Stealth (SYN) Scan on {target}")
    
    def tcp_connect_scan(self, target, ports=None):
        """Perform TCP connect scan"""
        command = ['nmap', '-sT', '-T4']
        if ports:
            command.extend(['-p', ports])
        command.append(target)
        return self.run_nmap_command(command, f"TCP Connect Scan on {target}")
    
    def udp_scan(self, target, ports=None):
        """Perform UDP scan"""
        command = ['nmap', '-sU', '-T4']
        if ports:
            command.extend(['-p', ports])
        else:
            command.extend(['-F'])  # Top ports only for UDP due to slowness
        command.append(target)
        return self.run_nmap_command(command, f"UDP Scan on {target}")
    
    def nse_script_scan(self, target, script_name, ports=None):
        """Run NSE scripts"""
        command = ['nmap', '--script', script_name, '-T4']
        if ports:
            command.extend(['-p', ports])
        command.append(target)
        return self.run_nmap_command(command, f"NSE Script Scan ({script_name}) on {target}")
    
    def vulnerability_scan(self, target):
        """Perform vulnerability scanning using NSE scripts"""
        command = ['nmap', '--script', 'vuln', '-T4', target]
        return self.run_nmap_command(command, f"Vulnerability Scan on {target}")
    
    def save_results(self, results, target, scan_type):
        """Save scan results to file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"scan_{scan_type}_{target.replace('/', '_')}_{timestamp}.txt"
        
        try:
            with open(filename, 'w') as f:
                f.write(f"Scan Type: {scan_type}\n")
                f.write(f"Target: {target}\n")
                f.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("-" * 80 + "\n")
                f.write(results)
            print(f"💾 Results saved to: {filename}")
        except Exception as e:
            print(f"❌ Error saving results: {str(e)}")

def main():
    parser = argparse.ArgumentParser(
        description="Advanced Nmap Scanner for Bug Hunters and Pentesters",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 advanced_nmap_scanner.py -t 192.168.1.1 --quick
  python3 advanced_nmap_scanner.py -t 192.168.1.0/24 --host-discovery
  python3 advanced_nmap_scanner.py -t example.com --aggressive
  python3 advanced_nmap_scanner.py -t 192.168.1.1 --ports 22,80,443 --service-version
  python3 advanced_nmap_scanner.py -t 192.168.1.1 --stealth --ports 1-1000
  python3 advanced_nmap_scanner.py -t 192.168.1.1 --nse-script http-enum
        """
    )
    
    # Required arguments
    parser.add_argument('-t', '--target', required=True,
                        help='Target IP address, hostname, or network (e.g., 192.168.1.1, example.com, 192.168.1.0/24)')
    
    # Scan types
    scan_group = parser.add_argument_group('Scan Types')
    scan_group.add_argument('--host-discovery', action='store_true',
                          help='Perform host discovery scan (ping sweep)')
    scan_group.add_argument('--quick', action='store_true',
                          help='Quick scan of top 1000 ports')
    scan_group.add_argument('--full-ports', action='store_true',
                          help='Scan all 65535 ports')
    scan_group.add_argument('--stealth', action='store_true',
                          help='Stealth/SYN scan')
    scan_group.add_argument('--tcp-connect', action='store_true',
                          help='TCP connect scan')
    scan_group.add_argument('--udp', action='store_true',
                          help='UDP scan')
    scan_group.add_argument('--aggressive', action='store_true',
                          help='Aggressive scan (OS detection, version detection, script scanning)')
    scan_group.add_argument('--os-detection', action='store_true',
                          help='OS detection scan')
    scan_group.add_argument('--service-version', action='store_true',
                          help='Service version detection')
    scan_group.add_argument('--vulnerability', action='store_true',
                          help='Vulnerability scan using NSE scripts')
    
    # Options
    options_group = parser.add_argument_group('Options')
    options_group.add_argument('--ports', 
                             help='Specific ports to scan (e.g., 22,80,443 or 1-1000)')
    options_group.add_argument('--nse-script',
                             help='NSE script to run (e.g., http-enum, smb-enum-shares)')
    options_group.add_argument('--save-results', action='store_true',
                             help='Save results to file')
    options_group.add_argument('--no-banner', action='store_true',
                             help='Suppress banner output')
    
    args = parser.parse_args()
    
    # Create scanner instance
    scanner = AdvancedNmapScanner()
    
    # Print banner unless suppressed
    if not args.no_banner:
        scanner.print_banner()
    
    # Validate target
    if not scanner.validate_target(args.target):
        print(f"❌ Invalid target: {args.target}")
        sys.exit(1)
    
    results = []
    
    # Execute scans based on arguments
    if args.host_discovery:
        result = scanner.host_discovery(args.target)
        if result and args.save_results:
            scanner.save_results(result, args.target, "host_discovery")
        results.append(("Host Discovery", result))
    
    if args.quick:
        result = scanner.quick_scan(args.target)
        if result and args.save_results:
            scanner.save_results(result, args.target, "quick_scan")
        results.append(("Quick Scan", result))
    
    if args.full_ports:
        result = scanner.full_port_scan(args.target)
        if result and args.save_results:
            scanner.save_results(result, args.target, "full_port_scan")
        results.append(("Full Port Scan", result))
    
    if args.stealth:
        result = scanner.stealth_scan(args.target, args.ports)
        if result and args.save_results:
            scanner.save_results(result, args.target, "stealth_scan")
        results.append(("Stealth Scan", result))
    
    if args.tcp_connect:
        result = scanner.tcp_connect_scan(args.target, args.ports)
        if result and args.save_results:
            scanner.save_results(result, args.target, "tcp_connect_scan")
        results.append(("TCP Connect Scan", result))
    
    if args.udp:
        result = scanner.udp_scan(args.target, args.ports)
        if result and args.save_results:
            scanner.save_results(result, args.target, "udp_scan")
        results.append(("UDP Scan", result))
    
    if args.aggressive:
        result = scanner.aggressive_scan(args.target)
        if result and args.save_results:
            scanner.save_results(result, args.target, "aggressive_scan")
        results.append(("Aggressive Scan", result))
    
    if args.os_detection:
        result = scanner.os_detection_scan(args.target)
        if result and args.save_results:
            scanner.save_results(result, args.target, "os_detection")
        results.append(("OS Detection", result))
    
    if args.service_version:
        result = scanner.service_version_scan(args.target, args.ports)
        if result and args.save_results:
            scanner.save_results(result, args.target, "service_version")
        results.append(("Service Version", result))
    
    if args.vulnerability:
        result = scanner.vulnerability_scan(args.target)
        if result and args.save_results:
            scanner.save_results(result, args.target, "vulnerability_scan")
        results.append(("Vulnerability Scan", result))
    
    if args.nse_script:
        result = scanner.nse_script_scan(args.target, args.nse_script, args.ports)
        if result and args.save_results:
            scanner.save_results(result, args.target, f"nse_{args.nse_script}")
        results.append((f"NSE Script ({args.nse_script})", result))
    
    if args.ports and not any([args.stealth, args.tcp_connect, args.udp, args.service_version, args.nse_script]):
        result = scanner.specific_port_scan(args.target, args.ports)
        if result and args.save_results:
            scanner.save_results(result, args.target, "specific_ports")
        results.append(("Specific Port Scan", result))
    
    # If no specific scan type is chosen, perform a quick scan
    if not any([args.host_discovery, args.quick, args.full_ports, args.stealth, 
                args.tcp_connect, args.udp, args.aggressive, args.os_detection, 
                args.service_version, args.vulnerability, args.nse_script, args.ports]):
        print("No scan type specified. Running quick scan...")
        result = scanner.quick_scan(args.target)
        if result and args.save_results:
            scanner.save_results(result, args.target, "quick_scan")
        results.append(("Quick Scan", result))
    
    # Summary
    print("\n" + "=" * 80)
    print("📋 SCAN SUMMARY")
    print("=" * 80)
    for scan_type, result in results:
        status = "✅ Success" if result else "❌ Failed"
        print(f"{scan_type}: {status}")
    
    print(f"\n🎯 Target: {args.target}")
    print(f"⏰ Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️ Scan interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {str(e)}")
        sys.exit(1)