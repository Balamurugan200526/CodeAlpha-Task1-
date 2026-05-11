# 🌐 Basic Network Sniffer — CodeAlpha Internship Task 1

!\[Python](https://img.shields.io/badge/Python-3.x-blue)
!\[Scapy](https://img.shields.io/badge/Library-Scapy-green)
!\[Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey)
!\[Status](https://img.shields.io/badge/Status-Completed-brightgreen)
!\[Internship](https://img.shields.io/badge/Company-CodeAlpha-orange)

A Python-based **Network Packet Sniffer** built using the `Scapy` library. This tool captures real-time network traffic and displays useful information such as source/destination IP addresses, protocols (TCP/UDP/ICMP), port numbers, and packet payloads.

\---

## 📋 Table of Contents

* [About the Project](#about-the-project)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [How to Run](#how-to-run)
* [Sample Output](#sample-output)
* [Output Explained](#output-explained)
* [What I Learned](#what-i-learned)

\---

## 📖 About the Project

This project is **Task 1** of the CodeAlpha Cybersecurity Internship. The goal was to build a network sniffer that captures and analyzes live network packets to understand how data flows across a network at the protocol level.

Network sniffers are used by cybersecurity professionals for:

* Monitoring network traffic for suspicious activity
* Debugging network issues
* Understanding protocol behavior
* Learning how data is structured at the packet level

\---

## ✨ Features

* Captures live network packets in real time
* Identifies and displays **TCP**, **UDP**, and **ICMP** protocols
* Shows **source IP** and **destination IP** for every packet
* Displays **port numbers** (source and destination)
* Extracts and prints **packet payloads**
* Works on both **Windows** and **Linux**
* Saves captured output to a log file

\---

## 🛠 Technologies Used

|Tool|Purpose|
|-|-|
|Python 3|Core programming language|
|Scapy|Packet capturing and analysis|
|Npcap (Windows)|Packet capture driver for Windows|
|libpcap (Linux)|Packet capture library for Linux|

\---

## ⚙️ Prerequisites

* Python 3.x installed
* pip (Python package manager)
* **Windows:** Npcap installed ([Download here](https://npcap.com/#download)) — install with "WinPcap API-compatible mode" checked
* **Linux:** Run with `sudo` privileges

\---

## 📦 Installation

**Step 1 — Clone the repository**

```bash
git clone https://github.com/yourusername/CodeAlpha\_BasicNetworkSniffer.git
cd CodeAlpha\_BasicNetworkSniffer
```

**Step 2 — Install Scapy**

```bash
pip install scapy
```

**Step 3 — (Windows only) Install Npcap**

Download and install from: https://npcap.com/#download

During installation, make sure to check:

```
✅ Install Npcap in WinPcap API-compatible mode
```

\---

## ▶️ How to Run

**On Windows (run CMD as Administrator):**

```bash
python sniffer.py
```

**On Linux/Kali:**

```bash
sudo python3 sniffer.py
```

**To save output to a file:**

```bash
python sniffer.py > output.txt
```

Press `Ctrl + C` to stop the sniffer at any time.

\---

## 📊 Sample Output

```
Starting Network Sniffer... Press Ctrl+C to stop

\[UDP] 192.168.29.249 → 192.168.29.255 | Port: 5775
  Payload: b'beacon:RFLSBJLA4142112:0:false:0:0:SV=1401'

\[UDP] 192.168.29.24 → 192.168.29.255 | Port: 15600
  Payload: b'SEARCH BSDP/0.1\\nDEVICE=0\\nSERVICE=1\\n'

\[TCP] 192.168.29.36 → 146.75.122.172 | Port: 80
  Payload: b'GET /filestreaming...'

\[TCP] 146.75.122.172 → 192.168.29.36 | Port: 54090
  Payload: b'\\x00P\\xd3J\\xa0\\x1f\\xde\\x11...'
```

\---

## 🔍 Output Explained

|Output|Meaning|
|-|-|
|`\[UDP]` / `\[TCP]`|Network protocol used by the packet|
|`192.168.29.x`|Local device IP address on the network|
|`146.75.122.172`|Remote server IP on the internet|
|`→ 192.168.29.255`|Broadcast — sent to all devices on network|
|`Port: 80`|HTTP web traffic port|
|`GET /filestreaming`|HTTP request payload — device downloading a file|
|`beacon:RFLSBJLA...`|A device announcing itself on the local network|

### Protocols captured:

* **UDP** — Fast, connectionless protocol. Used for broadcasts and device discovery.
* **TCP** — Reliable, connection-based protocol. Used for web browsing and file transfer.
* **Port 80** — Standard HTTP web traffic port.
* **Broadcast (255)** — Packets sent to every device on the local network.

\---

## 📚 What I Learned

* How network packets are structured at the IP, TCP, and UDP layers
* The difference between TCP (reliable) and UDP (fast/connectionless) protocols
* How devices communicate on a local network using broadcasts
* How HTTP requests look at the packet level (`GET /filestreaming`)
* How to use Python and Scapy to capture and parse live network traffic
* The importance of network monitoring in cybersecurity

\---

## ⚠️ Disclaimer

This tool is built for **educational purposes only** as part of the CodeAlpha Cybersecurity Internship. Only use this tool on networks you own or have explicit permission to monitor. Unauthorized packet sniffing is illegal and unethical.

\---

## 👤 Author

* **Name:** Balamurugan S
* **Internship:** CodeAlpha Cybersecurity Internship
* **LinkedIn:** https://www.linkedin.com/in/balamurugan-s-468387337?utm\_source=share\_via\&utm\_content=profile\&utm\_medium=member\_android
* **GitHub:** 

\---

> ⭐ If you found this helpful, give the repo a star!

