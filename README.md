# Adaptive SDN Flow Rule Timeout Manager

## 📌 Overview

This project implements an **Adaptive Software Defined Networking (SDN) Controller** using POX. The controller dynamically manages flow rules based on traffic intensity, optimizing network performance and flow table usage.

---

## 🎯 Problem Statement

Design and implement a **Flow Rule Timeout Manager** that:

* Uses timeout-based flow rule management
* Dynamically configures idle timeouts
* Removes expired flow rules
* Demonstrates flow rule life cycle
* Analyzes behavior under different traffic conditions
* Ensures consistency through regression testing

---

## 💡 Key Features

* Adaptive traffic classification (LOW / MEDIUM / HIGH)
* Dynamic idle timeout assignment
* Flow rules installed only for high traffic
* Automatic flow removal using OpenFlow timeouts
* Real-time traffic monitoring via logs

---

## 🧠 Concept Used

* Software Defined Networking (SDN)
* OpenFlow Protocol
* Control Plane vs Data Plane separation
* Traffic-aware flow management

---

## 🏗️ Project Structure

```
.
├── student1_adaptive_pox.py   # POX Controller
├── student1_topology.py       # Mininet Topology
└── README.md
```

---

## 🌐 Network Topology

* 2 Switches (s1, s2)
* 5 Hosts (h1–h5)
* Inter-switch backbone link

        h1     h2     h3
         |       |       |
         --------S1-------
                |
                | (High BW link)
                |
         --------S2-------
         |               |
        h4             h5

---

## ⚙️ How It Works

1. Switch sends unknown packets to controller (PacketIn)
2. Controller learns MAC and tracks traffic
3. Traffic classified into:

   * LOW
   * MEDIUM
   * HIGH
4. Flow rules installed only for HIGH traffic
5. Flow rules expire based on timeout

---

## 🔄 Flow Rule Lifecycle

1. Packet arrives → no rule
2. Controller processes traffic
3. High traffic → flow installed
4. Switch handles packets
5. Timeout → flow removed

---

## 🧪 How to Run

### Step 1: Start POX Controller

```
cd pox
python3 pox.py log.level --CRITICAL openflow.of_01 student1_adaptive_pox
```

### Step 2: Run Mininet Topology

```
sudo python3 student1_topology.py
```

### Step 3: Test Traffic

```
pingall
h1 ping -c 10 h5
```

---

## 📊 Traffic Classification

| Traffic Count | Level  | Timeout |
| ------------- | ------ | ------- |
| < 3           | LOW    | 30s     |
| ≥ 3           | MEDIUM | 15s     |
| ≥ 8           | HIGH   | 5s      |

---

## 🔍 Analysis

* Low traffic handled by controller
* High traffic optimized using flow rules
* Efficient use of flow table resources

---

## 🔁 Regression Testing

* Repeated `ping` tests ensure consistent behavior
* Traffic classification remains stable across runs

---

## 🚀 Conclusion

This project demonstrates an efficient and adaptive approach to flow rule management in SDN, improving scalability and performance by installing rules only when necessary.

---

## 👨‍💻 Authors

* Abhay TS


