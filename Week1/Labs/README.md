Week 1 Lab — Virtual Lab Setup (Kali + Windows)

This lab establishes the full working environment for all future security practice. I built two virtual machines, configured safe networking, applied updates, validated connectivity, and organized the environment for repeatable defensive work.

Purpose of the Lab

The goal was to create a stable, isolated security lab where I can safely perform testing, packet capture, log analysis, and defensive simulations without affecting my main system.

This included:

Building Kali Linux and Windows 10 VMs

Fixing installation issues

Setting up clean networking

Updating systems

Verifying the environment is fully functional

Virtual Machine Setup

Kali Linux

VM Name: KALIAB

CPU: 2 cores

RAM: 4 GB

Disk: 30–50GB dynamic

Storage controller: SATA (required to fix initial disk detection issues)

Installed directly from Kali ISO

Completed standard desktop install

Windows 10

VM Name: Windows 10 LAB

CPU: 2 cores

RAM: 4–8 GB

Disk: 50GB dynamic

Installed Windows 10/11 ISO

Verified the system boots correctly and shows proper hardware info in VirtualBox

Both VMs were configured for reliability and responsiveness so they can handle security tools later.

Network Configuration

The lab uses a two-network design, commonly used in security environments.

Adapter 1 — NAT

Provides internet access

Used for updates, package installs, downloads

Safely isolated (VM is not directly exposed to the host network)

Adapter 2 — Host-Only

Internal private network between Kali ↔ Windows

No internet exposure

Perfect for controlled testing, packet capture, and simulating events

Network Validation Steps

Listed current interfaces using: ip a

Noticed a disabled interface and brought it online with: sudo ip link set eth0 up

Confirmed both adapters were recognized and active

This ensures the lab is predictable and safe.

Updating and Cleaning Kali

Completed the initial maintenance process to get Kali fully up-to-date:

Refreshed package lists using: sudo apt update

Applied all updates using: sudo apt upgrade -y

Cleaned unused packages using: sudo apt autoremove -y

Why this matters:

Ensures tool compatibility

Reduces install errors later

Improves system stability

Aligns the system with expected behavior for tutorials and security tools

Connectivity Verification

ICMP Reachability Test

Pinged 8.8.8.8 (Google DNS)

Received successful replies

Confirmed outbound internet is working

DNS Resolution Test

Pinged google.com

DNS resolved correctly

Indicates NAT interface + DNS config are functioning

Combined Results

Internet: working

DNS: working

Host-Only communication: active

Both machines reachable within lab network

This verification step ensures the environment is ready for real exercises.

Screenshot Organization

All screenshots from this lab are stored in: Week1/Screenshots/

This includes:

Kali installation steps

Windows VM setup

Network settings

Interface outputs

Ping test results

Update and upgrade confirmations

Screenshots can be referenced inside notes later to show each step visually.

Key Lessons Learned

A clean VM environment prevents future issues

NAT + Host-Only is the ideal structure for safe cybersecurity labs

VirtualBox storage settings can break installs (SATA is required)

Linux interfaces may come up disabled after installation

Verifying DNS is as important as verifying internet

Updating Kali immediately avoids future tool problems

Why This Lab Matters for Future Work

This lab is the foundation for:

Packet capture and Wireshark analysis

Windows Event Log investigations

Privilege escalation practice

Detection engineering

Malware behavior simulation

Threat hunting patterns

A properly built environment shortens troubleshooting time and lets future labs focus on security, not setup.
