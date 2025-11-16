Week 1 — Reflection

This week marked the true beginning of building my cybersecurity foundation. I didn’t just set up virtual machines—I built the environment where all future skills, investigations, and detections will happen. This lab immediately made the concepts I studied feel real and practical.

What I Accomplished

Fully set up Kali Linux and Windows 10 VMs

Fixed installation and storage controller issues in VirtualBox

Configured a blended NAT + Host-Only network layout

Validated connectivity (ICMP + DNS)

Performed Kali updates and cleanup

Organized documentation and screenshots

Connected the lab experience to the major concepts I studied today

This created a strong technical foundation to build on.

What I Experienced (Hands-On Insight)
Building the Lab Felt Like Building a Real SOC Environment

Setting up NAT + Host-Only networking helped me see how internal and external traffic are separated in real organizations.
Kali acting as a “security operations workstation” and Windows acting as the “endpoint” gave me my first practical sense of attacker vs defender environments.

Troubleshooting Taught Me More Than the Install Itself

Discovering why a network interface was down

Adjusting VirtualBox storage controllers

Understanding why DNS didn’t resolve at first
These problems helped me understand the system deeper than a smooth installation ever could.

Connectivity Testing Was the Moment It Clicked

Seeing:
ping 8.8.8.8
and
ping google.com
work told me the environment was stable—and that I knew how to diagnose issues properly.

What I Learned About Myself as a Beginner Analyst

I troubleshoot better than I expected once I calm down

I now understand why analysts focus so much on network basics

Documentation matters—screenshots, notes, and structure saved me time

I learn fastest when I combine theory with immediate hands-on practice

Concepts make sense to me once I see them in a live environment

This gave me confidence moving forward.

How Theory Connected to the Lab (Without Repeating It)

I realized today that:

Attack chains make more sense when you see real network interfaces, real logs, and real communication paths

Indicators (IOC/IOA) become easier to visualize when you know where traffic flows

The NIST IR structure matches how you would actually solve problems when something breaks

MITRE’s early tactics (Discovery, Execution) show up naturally even in simple commands

SIEM/EDR concepts map directly to the behaviors I will simulate in this environment

The lab turned abstract ideas into practical building blocks.

(Note: the detailed explanations of these concepts remain in the Theory file.)

What Was Challenging

VirtualBox storage errors

NICs being down after installation

DNS not resolving at first

Reading large VirtualBox logs

Keeping the environment clean and organized

These challenges made me realize why analysts need patience and good troubleshooting habits.

What Improved

Comfort navigating VirtualBox

Better understanding of VM networking

Stronger Linux troubleshooting skills

Better instinct for validating systems (connectivity, updates, status checks)

Cleaner documentation structure

I’m learning to think more like someone responsible for keeping systems healthy.

What I Want to Improve

Faster diagnostic workflow

More snapshot usage to avoid repeated reinstallations

Better understanding of Windows Event Logs

More practice capturing and interpreting logs

Expanding lab use into small investigations next week

Summary

Week 1 gave me exactly what I needed:
a working, stable, secure environment and the confidence that I can build things, troubleshoot, and understand the underlying systems.

This week was the shift from curiosity to capability—a step forward in the Grey → Blue transition.
