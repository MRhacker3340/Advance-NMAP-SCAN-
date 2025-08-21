# Advanced Nmap Scanner 🔍

A comprehensive and user-friendly Nmap scanning tool designed specifically for bug hunters, penetration testers, and security professionals. This tool provides an intuitive interface to perform various types of network reconnaissance and vulnerability assessment.

## 🛠 Features

- **Network Host Discovery** - Live host detection and ping sweeps
- **Port Scanning** - Quick scans, full port scans, and specific port targeting
- **Service Detection** - Version detection and service enumeration
- **OS Detection** - Operating system fingerprinting
- **Stealth Scanning** - TCP SYN scans to avoid detection
- **Aggressive Scanning** - Comprehensive reconnaissance with scripts
- **Vulnerability Scanning** - NSE script-based vulnerability detection
- **NSE Script Execution** - Custom Nmap script execution
- **Multiple Scan Types** - TCP Connect, UDP, and stealth scans
- **Result Export** - Save scan results to files with timestamps
- **Beautiful Output** - Formatted and color-coded terminal output

## 📋 Requirements

- Python 3.6 or higher
- Nmap 7.0 or higher
- Linux, macOS, or Windows with WSL

## 🚀 Quick Setup

### Automatic Installation (Recommended)
```bash
git clone https://github.com/MRhacker3340/Advance-NMAP-SCAN-.git
cd Advance-NMAP-SCAN-
chmod +x setup.sh
./setup.sh
```

### Manual Installation
```bash
# Install Nmap
sudo apt install nmap          # Ubuntu/Debian
sudo yum install nmap          # CentOS/RHEL
brew install nmap              # macOS

# Clone repository
git clone https://github.com/MRhacker3340/Advance-NMAP-SCAN-.git
cd Advance-NMAP-SCAN-
chmod +x advanced_nmap_scanner.py
```

## 📖 Usage

### Basic Syntax
```bash
python3 advanced_nmap_scanner.py -t <target> [options]
```

### Quick Start Examples

#### Basic Scans
```bash
# Quick scan of top 1000 ports
python3 advanced_nmap_scanner.py -t 192.168.1.1 --quick

# Host discovery (ping sweep)
python3 advanced_nmap_scanner.py -t 192.168.1.0/24 --host-discovery

# Scan specific ports
python3 advanced_nmap_scanner.py -t example.com --ports 22,80,443,8080
```

#### Advanced Scans
```bash
# Aggressive scan (OS detection + service detection + scripts)
python3 advanced_nmap_scanner.py -t 192.168.1.1 --aggressive

# Stealth scan
python3 advanced_nmap_scanner.py -t 192.168.1.1 --stealth --ports 1-1000

# Service version detection
python3 advanced_nmap_scanner.py -t 192.168.1.1 --service-version

# OS detection
python3 advanced_nmap_scanner.py -t 192.168.1.1 --os-detection
```

#### Vulnerability Assessment
```bash
# Vulnerability scan using NSE scripts
python3 advanced_nmap_scanner.py -t 192.168.1.1 --vulnerability

# Custom NSE script execution
python3 advanced_nmap_scanner.py -t 192.168.1.1 --nse-script http-enum

# Web application enumeration
python3 advanced_nmap_scanner.py -t example.com --nse-script "http-*"
```

#### Save Results
```bash
# Save scan results to timestamped files
python3 advanced_nmap_scanner.py -t 192.168.1.1 --aggressive --save-results
```

### Utility Scripts

#### Quick Comprehensive Scan
```bash
# Runs host discovery + quick scan + service detection
python3 quick_scan.py 192.168.1.1
```

#### Focused Vulnerability Scan
```bash
# Dedicated vulnerability assessment
python3 vuln_scan.py 192.168.1.1
```

## 🎯 Scan Types Explained

| Scan Type | Purpose | Use Case |
|-----------|---------|----------|
| `--host-discovery` | Discover live hosts | Network mapping, initial reconnaissance |
| `--quick` | Scan top 1000 ports | Fast initial assessment |
| `--full-ports` | Scan all 65535 ports | Comprehensive port discovery |
| `--stealth` | SYN scan (half-open) | Avoid detection, stealthy reconnaissance |
| `--tcp-connect` | Full TCP connection | Firewall evasion, reliable results |
| `--udp` | UDP port scan | Discover UDP services |
| `--aggressive` | OS + Service + Scripts | Complete system profiling |
| `--vulnerability` | NSE vulnerability scripts | Security assessment |

## 🔧 Command Line Options

### Required Arguments
- `-t, --target` - Target IP, hostname, or network (e.g., 192.168.1.1, example.com, 192.168.1.0/24)

### Scan Types
- `--host-discovery` - Perform host discovery scan (ping sweep)
- `--quick` - Quick scan of top 1000 ports  
- `--full-ports` - Scan all 65535 ports
- `--stealth` - Stealth/SYN scan
- `--tcp-connect` - TCP connect scan
- `--udp` - UDP scan
- `--aggressive` - Aggressive scan (OS detection, version detection, script scanning)
- `--os-detection` - OS detection scan
- `--service-version` - Service version detection
- `--vulnerability` - Vulnerability scan using NSE scripts

### Options
- `--ports` - Specific ports to scan (e.g., 22,80,443 or 1-1000)
- `--nse-script` - NSE script to run (e.g., http-enum, smb-enum-shares)
- `--save-results` - Save results to timestamped files
- `--no-banner` - Suppress banner output

## 🌟 Advanced Usage Examples

### Network Reconnaissance
```bash
# Complete network discovery and enumeration
python3 advanced_nmap_scanner.py -t 192.168.1.0/24 --host-discovery --save-results
python3 advanced_nmap_scanner.py -t 192.168.1.1-254 --quick --save-results

# Deep port analysis
python3 advanced_nmap_scanner.py -t 192.168.1.1 --full-ports --save-results
```

### Web Application Testing
```bash
# Web server enumeration
python3 advanced_nmap_scanner.py -t example.com --ports 80,443,8080,8443 --service-version
python3 advanced_nmap_scanner.py -t example.com --nse-script "http-*"

# SSL/TLS analysis
python3 advanced_nmap_scanner.py -t example.com --nse-script ssl-enum-ciphers
```

### System Profiling
```bash
# Complete system fingerprinting
python3 advanced_nmap_scanner.py -t 192.168.1.1 --aggressive --save-results

# SMB enumeration
python3 advanced_nmap_scanner.py -t 192.168.1.1 --nse-script "smb-*"
```

## 📁 Output Files

When using `--save-results`, files are saved with descriptive names:
- `scan_quick_scan_192.168.1.1_20231215_143022.txt`
- `scan_aggressive_example.com_20231215_143045.txt`
- `scan_vulnerability_192.168.1.1_20231215_143112.txt`

## ⚠️ Legal and Ethical Usage

**IMPORTANT**: This tool is for educational and authorized testing purposes only.

- ✅ Use only on networks you own or have explicit permission to test
- ✅ Respect rate limits and avoid overwhelming target systems  
- ✅ Follow responsible disclosure for any vulnerabilities found
- ❌ Do not use for unauthorized network scanning or malicious purposes
- ❌ Do not use against third-party systems without permission

## 🛡️ Security Considerations

- Some scans require root/administrator privileges
- Aggressive scans may trigger security alerts
- Always verify target scope before scanning
- Use stealth options in sensitive environments

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for:
- New scanning features
- Performance improvements
- Bug fixes
- Documentation updates

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Created for the cybersecurity community to aid in legitimate security testing and network analysis.

---

**Happy Scanning! 🔍✨** 
