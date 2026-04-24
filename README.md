# Packet Logger using SDN Controller (OS-Ken + Mininet)

## Overview

This project demonstrates a Software Defined Networking (SDN) application where a controller dynamically monitors and logs network packets. The controller is built using OS-Ken (Ryu-based framework) and interacts with a Mininet topology.

The system performs:

* Dynamic MAC learning (like a switch)
* Packet forwarding
* Real-time logging of IPv4 traffic
* Flow rule installation to reduce controller load

---

## Concept

Traditional networks rely on hardware devices for control decisions. 
In SDN:

* Control plane is separated from data plane
* Controller manages the entire network logically
* Switches act as simple forwarding devices

This project uses that idea to:

* Capture packets at the controller
* Log IP-level communication
* Learn and optimize forwarding paths

---

##  Project Structure

```
.
├── packet_logger.py   # SDN Controller logic
├── topo.py            # Custom Mininet topology
└── README.md          # Project documentation
```

---

##  Requirements

* Python 3.x
* Mininet
* OS-Ken (Ryu-based controller)

Install OS-Ken:

```bash
pip install os-ken
```

---

## Network Topology

* 1 Switch (`s1`)
* 3 Hosts (`h1`, `h2`, `h3`)
* All hosts connected to a single switch
* Switch is cconnected to a controller

```
h1 ----\
         \
h2 ------ s1 ----controller 
         /
h3 ----/
```

---

## How to Run

### Step 1: Start the Controller
               ryu-manager packet_logger.py


---

### Step 2: Start Mininet with Custom Topology
               sudo mn --custom topo.py --topo packetlog --controller=remote


---

### Step 3: Test Connectivity

               Inside Mininet:
                      mininet> h1 ping h2


---

##  Actual Flow

### 1. Switch Connection

* When switch connects, controller installs a **default rule**
* All packets are sent to controller initially

---

### 2. Packet Handling

* Each incoming packet triggers `packet_in_handler`
* Controller extracts:

  * Source MAC
  * Destination MAC
  * IP addresses (if available)

---

### 3. MAC Learning

* Controller stores:
     MAC → Port mapping
  
* Works like a learning switch

---

### 4. Forwarding Decision

* If destination MAC is known → forward directly
* Else → flood to all ports

---

### 5. Logging

For IPv4 packets:


Packet: <source_ip> → <destination_ip>


---

### 6. Flow Rule Installation

* Once path is known, controller installs flow rule
* Future packets bypass controller → faster forwarding

---

##  Key Features

* Dynamic MAC learning
* Real-time packet logging
* Reduced controller overhead using flow rules
* Simple and scalable topology
* Works with OpenFlow 1.3

---

##  Sample Output

Controller logs:

Packet: 10.0.0.1 → 10.0.0.2

Packet: 10.0.0.2 → 10.0.0.1


Mininet output:

3 packets transmitted, 3 received, 0% packet loss


---

## Observations

* First packet is slower due to controller involvement
* Subsequent packets are faster due to flow rules
* Flooding occurs only when destination is unknown
* Network becomes efficient over time

---


---

## Conclusion

This project shows how SDN enables centralized control and visibility in a network. By using a controller-based approach, we can monitor traffic, learn network behavior, and optimize packet forwarding dynamically. It highlights the flexibility and power of SDN compared to traditional networking.

---
