Week 1 — Theory Notes

Foundational cybersecurity concepts that support the environment and skills built during this week.

1. Core Security Foundations
CIA Triad (Confidentiality, Integrity, Availability)

The fundamental model for protecting information.

Confidentiality: Keep data private (encryption).

Integrity: Keep data accurate (hashing, backups).

Availability: Keep systems accessible (redundancy).
Example: A hospital outage breaks Availability.

IOC — Indicator of Compromise

Evidence that a system was compromised.
Memory: AFTER
Examples:

Malicious hash

C2 IP

Registry key change

IOA — Indicator of Attack

Evidence an attack is happening right now.
Memory: DURING
Examples:

Brute force attempts

Suspicious PowerShell

Network scanning

Threat Actors

Memory: Attacker
Types:

Cybercriminal

APT (nation-state tier)

Insider threats

Attack Vectors

Memory: Door
How attackers get in:

Phishing

Exploits

Stolen credentials

2. Detection Concepts
False Positive vs True Positive

False Positive: Alert is wrong (safe activity looks bad).

True Positive: Real attack detected (Mimikatz dumping LSASS).

SIEM (Security Information & Event Management)

Centralized logs + correlation + alerting.
Example: Impossible travel alert.

EDR (Endpoint Detection & Response)

Monitors processes, behaviors, and allows isolation.
Example: Malicious PowerShell blocked.

3. Incident Response (NIST 800-61)

The standard IR lifecycle.

1) Preparation

Training, logging, playbooks.

2) Detection & Analysis

Identify and confirm malicious activity.

3) Containment → Eradication → Recovery (CER)

Stop the attack → clean system → restore environment.

4) Post-Incident Activity

Lessons learned and rule improvements.

Memory: PREP → DETECT → CER → IMPROVE

4. MITRE ATT&CK — Ultra Compact View

12 Tactics in order:

Initial Access (IN) — Phishing, exploits
Execution (RUN) — PowerShell, macros
Persistence (STAY) — Tasks, startup keys
Privilege Escalation (LEVEL UP) — UAC bypass
Defense Evasion (HIDE) — Disable AV
Credential Access (STEAL CREDS) — LSASS dump
Discovery (LOOK) — whoami, port scans
Lateral Movement (MOVE) — RDP, SMB
Collection (GRAB DATA) — staging files
Command & Control (CALL HOME) — beaconing
Exfiltration (SEND OUT) — HTTPS upload
Impact (BREAK STUFF) — ransomware

Memory:
IN → RUN → STAY → LEVEL UP → HIDE → STEAL CREDS → LOOK → MOVE → GRAB DATA → CALL HOME → SEND OUT → BREAK STUFF

5. Key Defensive Knowledge Learned
IR Team Structure

Roles include:

Triage analyst

Forensic responder

Incident commander

Playbooks

Step-by-step procedures for consistent incident handling.
Examples:

Phishing playbook

Malware containment playbook

TTPs (Tactics, Techniques, Procedures)

How attackers operate — their patterns and habits.
Used heavily in threat intelligence and detection engineering.

6. How These Concepts Connect to the Lab

The theory explains why the lab matters:

Understanding attack vectors helps explain Windows vs Kali roles

Knowing IOA/IOC helps identify signals during future scans

MITRE’s Discovery, Execution, and C2 relate directly to lab traffic

The IR lifecycle guides how to respond during later exercises

SIEM + EDR concepts connect to how logs and alerts will be created in your lab

This theory sets the foundation for every future investigation in your SOC environment.
