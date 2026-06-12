Endpoint Security Incident Response and Automated Remediation

Networking Assignment 2

Student: Gokul Shiva Kumar
Student ID: 20097813

---

 Project Overview

This project was developed to demonstrate endpoint monitoring, threat detection, incident response, and automated remediation within a controlled laboratory environment. The solution uses Wazuh SIEM to collect and analyse security events from Windows and Linux systems. Additional telemetry was collected using Sysmon, PowerShell logging, and Linux auditd.

The project also includes a Docker-based AI security component using Ollama and Llama 3.2 to classify security alerts. Automated remediation actions were implemented using predefined and allow-listed scripts to ensure actions remained safe, auditable, and reversible.

---
 Project Objectives

The objectives of this project were:

* Build a secure endpoint monitoring environment.
* Configure Windows and Linux telemetry collection.
* Forward security logs to Wazuh SIEM.
* Create and validate security detections.
* Implement AI-based alert classification.
* Develop automated remediation actions.
* Demonstrate detection, response, and recovery processes.
* Maintain a safe and isolated lab environment.

---
 System Architecture

```text
                    +----------------------+
                    |   Windows 11 Host    |
                    |----------------------|
                    | Sysmon               |
                    | PowerShell Logging   |
                    | Wazuh Agent          |
                    +----------+-----------+
                               |
                               |
                               v
                    +----------------------+
                    | Ubuntu Wazuh Server  |
                    |----------------------|
                    | Wazuh Manager        |
                    | Wazuh Dashboard      |
                    | auditd               |
                    +----------+-----------+
                               |
                               |
                               v
                    +----------------------+
                    | Docker AI Platform   |
                    |----------------------|
                    | Ollama              |
                    | Llama 3.2           |
                    | AI Classifier       |
                    | Remediation Scripts |
                    +----------------------+
```

---

Technologies Used

| Technology         | Purpose                        |
| ------------------ | ------------------------------ |
| Wazuh              | SIEM and security monitoring   |
| Wazuh Agent        | Endpoint log collection        |
| Windows 11         | Endpoint system                |
| Ubuntu Server      | Wazuh Manager host             |
| Sysmon             | Detailed Windows telemetry     |
| PowerShell Logging | PowerShell activity monitoring |
| auditd             | Linux audit logging            |
| Docker             | Container platform             |
| Ollama             | Local LLM runtime              |
| Llama 3.2          | AI alert classification        |
| Python             | Automation scripting           |

---

Lab Environment

Windows Endpoint

* Windows 11
* Wazuh Agent installed
* Sysmon configured
* PowerShell Operational Logging enabled
* Windows Firewall testing performed

Linux Server

* Ubuntu Server
* Wazuh Manager
* Wazuh Dashboard
* auditd enabled
* Docker installed

---

Security Monitoring Configuration

Windows Monitoring

The Windows endpoint was configured with Sysmon and PowerShell logging to provide detailed visibility into process execution, user activity, command execution, and security events. The Wazuh agent forwarded these logs to the Wazuh Manager for analysis.

Linux Monitoring

The Linux server used auditd to monitor security-related activities including file creation, authentication events, and administrative actions. These events were collected and visualised through Wazuh.

---

Detection Use Cases

The following detections were successfully generated and observed:

User Account Creation

A test user account was created and Wazuh generated an alert indicating account creation activity.

 User Account Deletion or Disablement

User account disablement activities were detected and logged within Wazuh.

User Group Changes

Changes to user group membership were successfully detected and reported.

Account Discovery Activity

Commands such as net user triggered account discovery alerts.

PowerShell Activity Monitoring

PowerShell Operational logs were collected and analysed to identify administrative activity.

Sysmon Monitoring

Sysmon generated detailed process and registry monitoring events which were forwarded to Wazuh.

Firewall Configuration Changes

Firewall disablement and re-enablement activities were performed and verified during testing.

---

AI Alert Classification

An AI alert classification component was developed using Ollama and the Llama 3.2 language model.

The AI classifier receives a security alert and determines whether the activity appears suspicious. The classification process helps provide additional context for analysts and supports decision-making during incident response.

Example classification:

```text
Alert: User account created on Windows host

Classification: SUSPICIOUS
```

The AI component does not have direct command execution privileges and cannot independently perform remediation actions.

---

Automated Remediation

Two predefined remediation actions were implemented.

Process Termination

A suspicious process can be terminated using an allow-listed script.

Example action:

```text
taskkill /F /IM notepad.exe
```

Verification confirmed that the process was successfully terminated.

User Account Disablement

A predefined remediation script can disable a suspicious user account.

Example action:

```text
net user testuser123 /active:no
```

Verification confirmed that the account status changed from active to disabled.

---

Docker Deployment

The AI security stack was deployed using Docker Compose.

Docker components included:

* Ollama container
* Llama 3.2 model
* Python automation scripts

Container status was verified during testing and remained operational throughout the project.

---

Security Controls

The project included several security controls:

* Isolated lab environment
* No live malware usage
* Predefined remediation actions only
* Allow-listed command execution
* Manual verification of remediation actions
* Full logging and auditing of actions performed

These controls reduced the risk of unintended system impact.

---

Evidence Collected

The following evidence was collected during testing:

* Wazuh agent registration
* Endpoint connectivity validation
* Sysmon event generation
* PowerShell logging events
* Linux auditd monitoring
* User account creation alerts
* User account disablement alerts
* Group membership modification alerts
* Account discovery alerts
* Threat hunting dashboard screenshots
* AI classification output
* Process termination verification
* Docker container status verification
* Firewall disablement evidence
* Firewall re-enablement evidence

---

Repository Contents

```text
architecture.txt
docker-compose.yml
ai_classifier.py
remediation.py
README.md
Screenshots/
```

---

Project Results

The project successfully demonstrated endpoint security monitoring, security event collection, threat detection, AI-assisted alert classification, and automated remediation.

Windows and Linux security events were successfully collected and analysed within Wazuh. Detection rules generated alerts for user management activities, discovery commands, PowerShell execution, and Sysmon events. The AI component classified suspicious alerts, while remediation scripts demonstrated safe and auditable containment actions.

The implementation satisfied the project objectives while maintaining safe operational controls and supporting incident response activities.

---

Author
Gokul S

Endpoint Security Incident Response and Automated Remediation Assessment
