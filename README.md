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
* Mininet startup
* Ping results

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
* Network links

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
* Mininet connection
* Ping results
* Packet processing logs

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
* Link failure detection logs
* Ping after failure

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
* Ping results before and after failure
* Iperf results before and after failure
* Controller logs showing link failure detection

---

## References

* https://noxrepo.github.io/pox-doc/html/
* http://mininet.org/documentation/
* OpenFlow Switch Specification
