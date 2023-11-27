#!/bin/bash

# Function to print a decorated message
print_welcome() {
  echo "**********************************************"
  echo "*                 Nmap Tool                  *"
  echo "*               Made by Akash Motkar         *"
  echo "**********************************************"
}

# Function to perform network scan with live host detection
scan_network() {
  read -p "Enter target IP or domain name: " target
  read -p "Do you want to scan with ports? (y/n): " with_ports

  if [ "$with_ports" == "y" ]; then
    nmap -p- "$target"
  else
    nmap "$target"
  fi
}

# Function to perform version and script scanning
scan_versions_scripts() {
  read -p "Enter target IP or domain name: " target
  nmap -sV -sC "$target"
}

# Function to determine the OS of the target machine
scan_os() {
  read -p "Enter target IP or domain name: " target
  nmap -O "$target"
}

# Function to list all open ports of the target
list_open_ports() {
  read -p "Enter target IP or domain name: " target
  nmap -p- "$target"
}

# Function to perform a specific port scan
specific_port_scan() {
  read -p "Enter target IP or domain name: " target
  read -p "Enter specific port to scan: " port
  nmap -p "$port" "$target"
}

# Function to perform an aggressive scan
aggressive_scan() {
  read -p "Enter target IP or domain name: " target
  nmap -A "$target"
}

# Function to perform a TCP/full open scan
tcp_full_open_scan() {
  read -p "Enter target IP or domain name: " target
  nmap -p 1-65535 -T4 -O --open "$target"
}

# Function to perform a stealth scan (TCP half-open)
stealth_scan() {
  read -p "Enter target IP or domain name: " target
  nmap -sS "$target"
}

# Function to perform scanning using NSE scripts
scan_nse_scripts() {
  read -p "Enter target IP or domain name: " target
  read -p "Enter NSE script to perform: " script
  nmap --script "$script" "$target"
}

# Main menu
print_welcome
echo "Select the task(s) you want to perform:"
echo "1) Scanning network live hosts"
echo "2) Scripts and versions running on the target machine"
echo "3) OS of the target machine"
echo "4) All open ports of the target"
echo "5) Specific port scan of the target"
echo "6) Aggressive scan"
echo "7) TCP/full open scan"
echo "8) Stealth scan/TCP half-open scan"
echo "9) Scanning using NSE scripts"

read -p "Enter your choice(s) separated by commas (e.g., 1,2,4): " choices

output_file="nmap_output.txt"

for choice in $(echo $choices | tr "," "\n")
do
  case $choice in
    1) scan_network ;;
    2) scan_versions_scripts ;;
    3) scan_os ;;
    4) list_open_ports ;;
    5) specific_port_scan ;;
    6) aggressive_scan ;;
    7) tcp_full_open_scan ;;
    8) stealth_scan ;;
    9) scan_nse_scripts ;;
    *) echo "Invalid choice: $choice";;
  esac
done | tee "$output_file"

echo "Thanks for using this tool! Output saved to $output_file"
