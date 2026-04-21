## Project Title

**Link Failure Detection and Recovery using SDN (POX Controller)**

---

## Problem Statement

To detect link failures in a network and dynamically update routing to maintain connectivity using Software Defined Networking (SDN).

---

## Phase 1: Setup and Baseline Verification

### Objective

To verify that Mininet and POX controller are correctly installed and functioning.

### Steps

1. Started POX controller using `forwarding.l2_learning`
2. Ran Mininet with default topology
3. Verified connectivity using `pingall`

### Output

* All hosts successfully communicated
* 0% packet loss observed

### Screenshots

* POX running
<img width="1470" height="956" alt="deafault pox Controller running" src="https://github.com/user-attachments/assets/be7474e0-e144-4fc8-90d0-ae353fd6d588" />

* Mininet startup
* Ping results
<img width="1470" height="956" alt="default mininet and pingall success" src="https://github.com/user-attachments/assets/eddc08f1-81ea-4251-a638-61b582f05d1c" />


---

## Phase 2: Custom Topology Design

### Objective

To design a custom topology with redundancy for link failure recovery.

### Topology Design

```
h1 — s1 — s2 — s3 — h2
        \__________/
```

### Explanation

* s1–s2–s3 is the primary path
* s1–s3 provides an alternate path
* Ensures connectivity even if one link fails

### Results

* All nodes connected successfully
* 0% packet loss observed

### Screenshots

* Custom topology
* Node list
* Ping results
<img width="1470" height="956" alt="custom topology(links and host), node check, pingall" src="https://github.com/user-attachments/assets/27a053f0-cd68-457d-a065-b95979d6bb3b" />

* Network links
<img width="1320" height="304" alt="link visualisation(design)" src="https://github.com/user-attachments/assets/31f9b685-a2ee-4b75-8740-2376747d8eab" />


---

## Phase 3: Custom Controller Implementation

### Objective

To implement a custom SDN controller using POX.

### Features

* Handles PacketIn events
* Implements flooding-based forwarding
* Detects link status changes

### Implementation Details

* Packets are forwarded using FLOOD action
* No permanent flow rules are installed
* PortStatus events detect link up/down

### Results

* Successful communication between hosts
* Controller logs show packet handling and switch connections

### Screenshots

* Controller startup
<img width="1470" height="956" alt="custom controller started   switch connected" src="https://github.com/user-attachments/assets/0e42d5c2-236b-49d5-a2ad-5c5baefd370d" />

* Mininet connection
* Ping results
<img width="1470" height="956" alt="mininet started, connected to controler + pingall" src="https://github.com/user-attachments/assets/25b5ec37-2525-4087-a371-603a6a438aad" />

* Packet processing logs
  <img width="1470" height="956" alt="packet handling" src="https://github.com/user-attachments/assets/89cb141b-8659-44b0-9b0d-6fdf87c482e2" />


---

## Phase 4: Link Failure Detection & Validation

### Objective

To detect link failures and validate network behavior.

### Test Scenarios

#### Scenario 1: Normal Operation

* All links active
* Ping successful
* 0% packet loss

#### Scenario 2: Link Failure

* Link between s1 and s2 is brought down
* Controller detects failure
* Traffic continues via alternate path (s1–s3)

### Observations

* Controller successfully detects link failure
* Network remains operational due to redundancy

### Screenshots

* Normal ping results
* Topology view
* Ping after failure
<img width="1470" height="956" alt="Normal vs link Failure( restore)" src="https://github.com/user-attachments/assets/88b7a189-20ba-4104-82b9-43b0d9e62bb3" />

* Link failure detection logs
<img width="1470" height="956" alt="link faiilure" src="https://github.com/user-attachments/assets/6c62d6ef-6868-44d3-a090-1d63b260d90a" />


---

## Phase 5: Performance Observation & Analysis

### Metrics Measured

#### 1. Latency (Ping)

* Measured using ICMP ping
* RTT values observed before and after failure

#### 2. Throughput (Iperf)

* Measured bandwidth between hosts using TCP

#### 3. Flow Table

* Observed using:

```
dpctl dump-flows
```

* Flow tables remain mostly empty due to flooding-based forwarding

---

### Before Failure

* Low latency
* Lower throughput (~38 Kbits/sec)
* Traffic handled using flooding (less efficient)

### After Failure

* Slight variation in latency
* Higher throughput (~82 Mbits/sec)
* Traffic rerouted through a more efficient alternate path
* Network remained fully functional

---

### Key Insight

The increase in throughput after failure indicates that the alternate path provided a more efficient route, reducing overhead caused by flooding and improving performance.

---

### Observations

* Network remains functional even after link failure
* Latency shows minimal impact
* Throughput improved after failure due to better path utilization
* Flooding ensures connectivity but is not optimal for performance

---

### Conclusion

The SDN-based network successfully maintains connectivity during link failure.
Performance analysis shows that topology and routing behavior significantly impact throughput and latency.

---

## Expected Output

* All hosts should communicate successfully (0% packet loss)
* Controller should detect link failures
* Network should remain operational after failure

---

## Validation

* Tested network behavior before and after link failure
* Verified connectivity and performance in both scenarios

---

## Proof of Execution

* Flow table output using `dpctl dump-flows`
- Flow table entries observed before failure correspond to control-plane traffic (LLDP)
- After failure, no persistent flow rules are installed as flooding is used
<img width="1099" height="370" alt="flow_before_failure" src="https://github.com/user-attachments/assets/4ccb9e57-97c2-46c0-b694-04a6ddf1ba0b" />

* Ping results before and after failure
<img width="1470" height="956" alt="ping_latency" src="https://github.com/user-attachments/assets/4b872e0f-11e9-4ded-8610-4ce57262fa34" />
<img width="1126" height="247" alt="ping after failure" src="https://github.com/user-attachments/assets/fbbe43f1-5e68-4d82-a037-d94d020f4e1c" />

* Iperf results before and after failure
<img width="1103" height="249" alt="Through(iperf) bandwidth before" src="https://github.com/user-attachments/assets/e200a90e-98cb-4c95-9e02-ef7e3cfcc7d8" />
<img width="1087" height="384" alt="bandwidth after failure" src="https://github.com/user-attachments/assets/80b5c24c-f11b-443d-9bed-30e48839e86f" />


* Controller logs showing before link failure detection
<img width="1470" height="956" alt="Controller running + switches connected" src="https://github.com/user-attachments/assets/5a2c1619-ecd5-4e75-a9d9-c767bc014481" />


---

## References

* https://noxrepo.github.io/pox-doc/html/
* http://mininet.org/documentation/
* OpenFlow Switch Specification
