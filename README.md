# 📡 Packet Logger in Software-Defined Networking (SDN)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Mininet](https://img.shields.io/badge/Mininet-Network%20Emulator-green)
![SDN](https://img.shields.io/badge/SDN-OpenFlow%201.3-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 📌 Overview
This project implements a **Packet Logger in a Software-Defined Networking (SDN) environment** using **Mininet** and the **OS-Ken controller**.

It demonstrates how a centralized controller can:
- Monitor network traffic  
- Log packet details in real time  
- Dynamically manage packet forwarding using a **learning switch mechanism**

---

## 🎯 Objectives
- Simulate an SDN environment  
- Implement a learning switch using OpenFlow  
- Log packet-level information (IP addresses)  
- Analyze network performance under normal and lossy conditions  

---

## 🛠️ Tech Stack
- Python  
- Mininet  
- OS-Ken Controller (Ryu-based)  
- OpenFlow v1.3  
- Linux / WSL  

---

## 📂 Project Structure

PACKET_LOGGER_SDN/
│── topo.py # Custom topology (3 hosts, 1 switch)
│── packet_logger.py # SDN controller (logging + forwarding)
│── README.md


---

## 🌐 Network Topology

h1 -----

h2 ------ s1 (Switch)
/
h3 -----/


---

## ⚙️ Setup Instructions

### 1️⃣ Install Dependencies
```bash
sudo apt update
sudo apt install mininet python3-pip -y
pip install os-ken
2️⃣ Start Controller
ryu-manager packet_logger.py
3️⃣ Run Custom Topology
sudo mn --custom topo.py --topo packetlog --controller remote
🧪 Testing
🔹 Test Connectivity
mininet> pingall
🔹 Ping Between Hosts
mininet> h1 ping h2
🔹 Simulate Packet Loss (20%)
sudo mn --topo single,3 --controller remote --link tc,loss=20
📊 Sample Outputs
📌 Packet Logs (Controller)
Packet: 10.0.0.1 → 10.0.0.2
Packet: 10.0.0.2 → 10.0.0.1
📌 Ping Results
7 packets transmitted, 3 received, 57% packet loss
rtt min/avg/max/mdev = 0.156/0.310/0.613/0.214 ms
⚡ Features
Real-time packet logging
MAC learning (learning switch)
Dynamic flow rule installation
Flooding for unknown destinations
Packet loss simulation & analysis
