#!/bin/bash
echo "🚀 Installing GoTermix54 on Termux..."

# Update & install deps
pkg update -y
pkg install python git -y

# Clone and install
git clone https://github.com/KenyanRedwoods01/gotermix54.git
cd gotermix54
pip install -e .

# Add to path if not already
echo 'export PATH="$PATH:$HOME/gotermix54"' >> ~/.bashrc
source ~/.bashrc

echo "✅ GoTermix54 installed! Run 'gotermix54 --help'"
echo "🔑 Don't forget to set your Mistral API key in ~/.gotermix54/config.json"
