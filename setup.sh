#!/bin/bash

# Advanced Nmap Scanner Setup Script
# This script installs dependencies and sets up the scanner

echo "🚀 Setting up Advanced Nmap Scanner..."
echo "========================================"

# Check if running as root for some commands
if [[ $EUID -eq 0 ]]; then
   echo "⚠️  Running as root - be careful!"
fi

# Update package list
echo "📦 Updating package list..."
if command -v apt-get &> /dev/null; then
    sudo apt-get update
elif command -v yum &> /dev/null; then
    sudo yum update
elif command -v brew &> /dev/null; then
    brew update
fi

# Install nmap if not present
if ! command -v nmap &> /dev/null; then
    echo "📡 Installing nmap..."
    if command -v apt-get &> /dev/null; then
        sudo apt-get install -y nmap
    elif command -v yum &> /dev/null; then
        sudo yum install -y nmap
    elif command -v brew &> /dev/null; then
        brew install nmap
    else
        echo "❌ Could not install nmap automatically. Please install manually."
        exit 1
    fi
else
    echo "✅ nmap is already installed"
fi

# Install Python 3 if not present
if ! command -v python3 &> /dev/null; then
    echo "🐍 Installing Python 3..."
    if command -v apt-get &> /dev/null; then
        sudo apt-get install -y python3 python3-pip
    elif command -v yum &> /dev/null; then
        sudo yum install -y python3 python3-pip
    elif command -v brew &> /dev/null; then
        brew install python3
    else
        echo "❌ Could not install Python 3 automatically. Please install manually."
        exit 1
    fi
else
    echo "✅ Python 3 is already installed"
fi

# Make the script executable
chmod +x advanced_nmap_scanner.py

# Create a symbolic link for easy access (optional)
echo "🔗 Creating symbolic link..."
if [ -w /usr/local/bin ]; then
    sudo ln -sf "$(pwd)/advanced_nmap_scanner.py" /usr/local/bin/advanced-nmap-scanner
    echo "✅ You can now run the scanner with: advanced-nmap-scanner"
else
    echo "⚠️  Could not create symbolic link. Run with: python3 advanced_nmap_scanner.py"
fi

echo ""
echo "🎉 Setup complete!"
echo "Usage examples:"
echo "  python3 advanced_nmap_scanner.py -t 192.168.1.1 --quick"
echo "  python3 advanced_nmap_scanner.py -t example.com --aggressive"
echo "  python3 advanced_nmap_scanner.py --help"
echo ""
echo "Happy scanning! 🔍"