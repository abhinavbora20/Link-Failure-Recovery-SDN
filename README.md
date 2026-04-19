## Phase 1: Setup and Baseline Verification

### Objective
To verify that Mininet and POX controller are correctly installed and can communicate.

### Steps
1. Started POX controller using forwarding.l2_learning
2. Ran Mininet with default topology
3. Verified connectivity using pingall

### Output
- All hosts successfully communicated
- 0% packet loss observed

### Screenshots
- POX running
- Mininet startup
- Ping results

## Phase 2: Custom Topology Design

### Objective
To design a custom network topology with redundancy for handling link failures.

### Topology Design
h1 — s1 — s2 — s3 — h2
        \__________/

### Explanation
- s1–s2–s3 forms the main path
- s1–s3 provides an alternate path
- This ensures connectivity even if one link fails

### Results
- All nodes connected successfully
- 0% packet loss observed

### Screenshots
- Custom topology
- Node list
- Ping results
- Network links

## Phase 3: Custom Controller Implementation

### Objective
To implement a custom SDN controller using POX.

### Features
- Handles PacketIn events
- Implements flooding-based forwarding
- Detects link status changes

### Implementation Details
- PacketIn events are processed and packets are forwarded using FLOOD
- PortStatus events detect link up/down

### Results
- Successful communication between hosts
- Controller logs show packet handling

### Screenshots
- Controller startup
- Mininet connection
- Ping results
- Packet processing logs

## Phase 4: Link Failure Detection & Validation

### Objective
To detect link failures and validate network behavior.

### Test Scenarios

#### Scenario 1: Normal Operation
- All links active
- Ping successful
- 0% packet loss

#### Scenario 2: Link Failure
- Link between s1 and s2 is brought down
- Controller detects failure
- Traffic rerouted via alternate path

### Observations
- Controller successfully detects link failure
- Network remains operational due to redundancy

### Screenshots
- Normal ping results
- Topology view
- Link failure detection logs
- Ping after failure

## Phase 5: Performance Observation & Analysis

### Metrics Measured

#### 1. Latency (Ping)
- Measured using ICMP ping
- Observed RTT values

#### 2. Throughput (Iperf)
- Measured bandwidth between hosts
- Stable performance observed

#### 3. Flow Table
- Observed OpenFlow rules
- Verified packet forwarding behavior

### Before Failure
- Low latency
- Lower throughput (~38 Kbits/sec)
- Traffic handled using flooding (less efficient)

### After Failure
- Slight variation in latency
- Higher throughput (~82 Mbits/sec)
- Traffic rerouted through a more efficient alternate path
- Network remained fully functional

### Key Insight
The increase in throughput after failure indicates that the alternate path provided a more efficient route, reducing overhead caused by flooding and improving performance.

### Observations
- The network remains functional even after link failure due to redundancy
- Latency shows minimal impact
- Throughput improved after failure due to better path utilization
- Flooding ensures connectivity but is not optimal for performance

### ConclusionThe system successfully maintains performance even after link failure due to redundancy.
The SDN-based network successfully maintains connectivity during link failure.
Performance analysis shows that topology and routing behavior significantly impact throughput and latency.


### Screenshots
- Ping results
- Iperf results
- Flow table
- After failure metrics

