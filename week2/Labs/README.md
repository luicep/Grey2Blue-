Week 2 – Sysinternals & Wireshark Analysis Lab

Hands-on analysis using Sysinternals tools (Process Explorer, Autoruns, TCPView, ProcMon) and Wireshark.

🏗️ Lab Overview

This lab builds your core SOC skills by teaching you how to:

Identify malicious or suspicious activity using Sysinternals tools

Understand process behavior, signatures, parent/child chains

Detect persistence mechanisms

Inspect network connections

Capture and interpret OS-level events

Analyze HTTP traffic with Wireshark

Build a structured, screenshot-documented workflow for your SOC portfolio

📚 Tools Used

Process Explorer

Autoruns

TCPView

Process Monitor (ProcMon)

Wireshark

(All Sysinternals tools downloaded via Sysinternals Suite)

------------------------------------------
🧪 1. PROCESS EXPLORER ANALYSIS
------------------------------------------
✔️ Objective

Understand what processes are running, verify signatures, check parent/child relationships, and identify suspicious binaries.

🔧 Steps Performed
1. Launch Process Explorer

Right-click → Run as Administrator

Let it populate the full process tree.

2. Sort by CPU

View which processes are active and behaving unusually.

Screenshot: procexp-top-cpu.png

3. Inspect a suspicious or interesting process

Right-click any process → Properties
Check:

Company Name

Verified Signer

Image Path

Command Line

Parent Process

Threads / DLLs

Screenshot: procexp-process-properties.png

🔥 Red Flags to Look For

Unsigned binaries
Means Windows cannot confirm who created the file.

Odd parent relationships
Example:
cmd.exe → powershell.exe → random.exe
(Unusual chain often indicates execution via LOLBins)

Non-standard paths
Especially in:

C:\Users\<user>\AppData\Local\
C:\Users\<user>\AppData\Roaming\
C:\ProgramData\
Temp folders


Strange filenames
Examples: svchosst.exe, chrome_update1.exe, etc.

------------------------------------------
🧪 2. AUTORUNS – PERSISTENCE ANALYSIS
------------------------------------------
✔️ Objective

Identify processes configured to run automatically at system startup.

🔧 Steps Performed
1. Launch Autoruns

Run as Admin.

Screenshot: autoruns-open.png

2. Apply filters

Go to Options → Hide Microsoft Entries
This removes noise from built-in Windows components.

Screenshot: autoruns-hide-ms.png

3. Navigate to Logon tab

Tab used to detect common persistence mechanisms.

Screenshot: autoruns-logon-tab.png

🔥 Red Flags

Startup items running from AppData

Unsigned startup binaries

Entries pointing to deleted files (“File not found”)

Suspicious scheduled tasks

Unexpected browser helpers/toolbars

------------------------------------------
🧪 3. TCPVIEW – NETWORK CONNECTIONS
------------------------------------------
✔️ Objective

Identify live network connections and detect suspicious remote endpoints.

🔧 Steps Performed
1. Launch TCPView

Screenshot: tcpview-main.png

2. Sort by “Process”

Makes relationships easy to see.

Screenshot: tcpview-sorted-by-process.png

3. Click a process → view remote IP

Look for established connections.

Screenshot: tcpview-remote-ip.png

4. Compare “Expected vs Suspicious”

Screenshot examples:

tcpview-expected.png

tcpview-suspicious-or-interesting.png

🔥 Red Flags

Remote IP addresses in foreign countries

Repeated connections to unknown servers

LISTENING ports on unusual processes

High-frequency connections (beaconing)

Unknown service processes opening sockets

------------------------------------------
🧪 4. PROCESS MONITOR (PROCMON) – OS ACTIVITY
------------------------------------------
✔️ Objective

Capture system-level events (registry, file writes, process activity).

🔧 Steps Performed
1. Start ProcMon

Default view = very noisy.

Screenshot: procmon-initial-capture.png

2. Stop capture

Click the magnifying glass 🔍.

Screenshot: procmon-capture-stopped.png

3. Clear display

Screenshot: procmon-clear-display.png

4. Create filters

Example:

Process Name is msedge.exe → Include
Process Name is chrome.exe → Include
Process Name is firefox.exe → Include
Result is SUCCESS → Include
Process Name is Procmon.exe → Exclude


Screenshot: procmon-filtered.png
Screenshot: procmon-filtered-view.png

5. Inspect individual events

Right-click → Properties
Check:

File writes

Reg edits

Threads

Network activity

Screenshot: procmon-file-event-details.png

🔥 Red Flags

Unexpected registry modifications

File writes in sensitive locations

Processes modifying startup keys

Scripts executed repeatedly

DLL injection activity

------------------------------------------
🧪 5. WIRESHARK – NETWORK PACKET ANALYSIS
------------------------------------------
✔️ Objective

Capture and inspect HTTP/HTTPS traffic.

🔧 Steps Performed
1. Launch Wireshark

Screenshot: wireshark-installed.png

2. Start capture on main network interface

Screenshot: wireshark-capture-start.png

3. Apply HTTP filters
http
tcp.port==80
tcp.port==443

4. Capture HTTP GET/POST traffic

Screenshots:

wireshark-http-get.png

wireshark-http-301redirect.png

wireshark-http-favicon.png

🔥 Red Flags

Repeated HTTP POSTs to unknown servers

Unencrypted credentials

Suspicious user-agents

Beaconing patterns

Downloads of scripts or binaries

🏁 END OF LAB

Upload all screenshots into:

Week2/Screenshots/
