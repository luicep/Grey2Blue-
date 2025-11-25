Week 2 introduced the deeper internal mechanics of endpoint visibility (Sysinternals) and network visibility (Wireshark).
Together, these tools reveal how the OS behaves under normal conditions vs. attack conditions.

Memory: “See the system from the inside out.”
Techniques:

Validate processes

Detect persistence

Map network behavior

Monitor registry & file activity
Scenario: Analyst receives alert about suspicious CPU spikes → uses Process Explorer and ProcMon to confirm behavior.

🧱 2. CIA Triad (Applied to Tools)
Confidentiality — Keep data secret

Memory: Only Who Should See
Tools: Wireshark (detects unencrypted traffic), Process Explorer (detects data-stealing processes)
Scenario: Plain HTTP GET request shows full URL and user-agent.

Integrity — Keep data untampered

Memory: Untampered
Tools: ProcMon (detect reg/table changes), Process Explorer (detect unsigned DLLs)
Scenario: Malware modifies a registry Run key → ProcMon flags RegSetValue.

Availability — Keep systems usable

Memory: System Up
Tools: TCPView (detects DoS-like socket exhaustion), ProcMon (detects crashes/failures)
Scenario: Unknown EXE opens dozens of sockets → reduces availability.

🧠 3. SOC Tools Theory (Integrated & Expanded)
Process Explorer — Process Intelligence

Memory: Task Manager on Steroids
Techniques:

Signature verification

Parent/child mapping

Path validation

Investigation of DLLs, threads
Scenario: Fake svchost.exe running from AppData instead of System32.

Red Flags

Unsigned or “Unable to Verify”

Wrong directory (Temp/AppData/Downloads)

Weird names (chrome_update1.exe)

Suspicious parent (cmd → powershell → exe)

Autoruns — Persistence Detection

Memory: Startup Map
Techniques:

Inspect Logon keys

Check tasks, services, browser helpers

Identify missing or deleted file paths
Scenario: EXE configured to auto-run from HKCU\Run without a signature.

Red Flags

Unsigned startup items

File not found

Startup entries in AppData

Random browser extensions

TCPView — Live Network Behavior

Memory: Network Pulse Check
Techniques:

Map process → remote IP

Identify C2 behavior (beaconing)

Spot unknown connections
Scenario: Unknown EXE repeatedly connects to rare overseas IPs on port 443.

Red Flags

Repeated timed connections

LISTENING ports on non-system processes

Processes making connections without a UI

No reverse DNS for remote IPs

ProcMon — Deep System Activity

Memory: The Truth of What the System Is Doing
Techniques:

RegSetValue = persistence

CreateFile = dropping files

WriteFile = modifying sensitive areas

DLL Load = hijacking/injection
Scenario: Malware writes a DLL to AppData\Roaming then loads it via explorer.exe.

Red Flags

Registry modifications in Run/RunOnce

File writes into user-writable directories

Repeated writes/queries in abnormal volumes

DLL loads from unexpected locations

Wireshark — Packet-Level Visibility

Memory: Network X-Ray
Techniques:

Inspect HTTP headers

Track DNS queries

Identify TLS SNI values

Spot data exfiltration
Scenario: Plain HTTP POST to unknown server carrying base64-encoded strings.

Red Flags

Repeated DNS lookups to strange domains

Odd user-agents

HTTP POST loops

Traffic patterns with exact intervals (indicative of beaconing)

🧬 4. Attack Surface & Threat Concepts (From NOTES)
Threat

Memory: Danger
Techniques: Threat intel, monitoring
Scenario: Ransomware group targeting healthcare organizations.

Vulnerability

Memory: Weak Spot
Techniques: Patch management, config hardening
Scenario: Unpatched browser plugin allows code execution.

Risk

Memory: What Could Go Wrong
Techniques: Assessment, mitigation
Scenario: Unmonitored port exposes internal service.

Attack Vectors

Memory: Doors Attackers Use
Techniques: Phishing, exploits, infected USBs
Scenario: Malware enters via malicious PDF → Process Explorer reveals abnormal spawn chain.

⚙️ 5. IR Framework (NIST-Aligned)
1. Preparation

Memory: Be Ready
Tools: Sysinternals set up, logging, EDR
Scenario: SOC team configures ProcMon filters beforehand.

2. Detection & Analysis

Memory: Find & Verify
Tools: Process Explorer, TCPView, Wireshark
Scenario: SIEM alert → manual triage with Sysinternals.

3. Containment, Eradication, Recovery

Memory: Stop → Remove → Restore
Tools: ProcMon to confirm malicious events
Scenario: Kill process → remove persistence → clean registry → restore system.

4. Post-Incident

Memory: Learn & Improve
Techniques: Lessons learned, detection tuning
Scenario: New rule created for unusual parent-child chains.

🛡️ 6. Log & Event Theory (From NOTES)
Firewall Logs

Memory: Door Logs
Techniques: Blocked traffic, allowed outbound
Scenario: Outbound spike → cross-check with TCPView.

Network Logs

Memory: Inside Footprints
Techniques: DHCP, switch, internal movement
Scenario: Unknown MAC appears → process inspected with Process Explorer.

Server/System Logs

Memory: System Diary
Techniques: Failed logins, service failures
Scenario: Multiple failed logins → check ProcMon for brute force patterns.

SIEM

Memory: Log HQ
Techniques: Correlation, dashboards, alerts
Scenario: Impossible travel alert triggered by login anomalies.

🛡️ 7. Red Flags (Unified)

Memory: “Does this belong here?”

Processes

Unsigned

Wrong path

Odd parent

Suspicious filenames

Persistence

Unexpected Run keys

Scheduled tasks for unknown binaries

Network

Repeated identical connections

Foreign or rare IP blocks

Unknown processes establishing sockets

System Activity

Registry key creation in autorun paths

DLL loads from user folders

File writes in AppData

Network Traffic

HTTP POST loops

Strange user-agents

DNS queries to never-seen domains

🧩 8. How Everything Connects (Holistic SOC View)

Memory: “Sysinternals = Host, Wireshark = Network.”

Process Explorer → What is running?

Autoruns → What runs automatically?

TCPView → Who is it talking to?

ProcMon → What is it modifying?

Wireshark → What did it send?

Scenario (complete triage chain):
Alert → Process Explorer (identify process) → TCPView (IP check) → Autoruns (persistence check) → ProcMon (behavior) → Wireshark (traffic inspection).

🧵 9. Essential Memory Shortcuts

Unsigned + Strange Path = High Suspicion

AppData + .exe = Malware Chance

Repeated 443 outbound = C2

RegSetValue in Run key = Persistence

File writes before execution = Dropper

DNS → HTTP → POST = Exfiltration Pattern
