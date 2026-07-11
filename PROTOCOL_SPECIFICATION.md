# AFO Protocol Specification: Operation & Execution Standards

This document outlines the formal protocols for agent-to-agent and system-to-environment communication within an AFO environment. 

## 1. The RAR Cycle (Recursive Architectural Refinement)
All autonomous loops are governed by a four stage cycle of state validation:

| Stage | Action ID | Objective | System Requirement |
| :--- | :--- | :--- | :--- |
| **AUDIT** | `AFO-A01` | Quantify current $\Delta S$ and $\Delta H$. | Observability Probe (OP) must return scalar. |
| **INJECT** | `AFO-I02` | Modulate arch-weights to minimize error vectors. | Gradient of semantic drift calculated via $D_{KL}$. |
| **VERIFY** | `AFO-V03` | Validate execution against state transition model. | Structural consistency check passed. |
| **REBASE** | `AFO-R04` | Re-orient context/memory for the next step in trajectory. | Zero residual drift residue ($\epsilon pprox 0$).

## 2. Interface & Interaction Protocols (IIP)

### 1. Archetype Weighting Signal (AWS)
A control signal passed through the orchestration layer that adjusts the attention mechanism's focus on specific semantic properties based on role identity.

### 2. Observability Probes (OP-S)
Low-latency measurement tools used by Meso and Micro roles to report real-time divergence metrics back to the Macro Orchestrator without polluting the primary task context.