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
