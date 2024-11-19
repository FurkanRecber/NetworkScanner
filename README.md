# Network Scanner Script
This Python script allows you to perform a network scan using ARP (Address Resolution Protocol) requests to detect devices connected to a network. It is a basic tool for network discovery and utilizes the Scapy library for sending and receiving packets.

## Features
- Sends ARP requests to the specified IP address or subnet.
- Detects active devices on the network.
- Summarizes the responses.

## Requirements
- Python (3.x is recommended) should be installed.
- The Scapy library must be installed. To install it, use:
```bash
pip install scapy
```
## Cloning from GitHub
To clone this project from GitHub:
- If Git is not installed, download it from the [Git website.](https://git-scm.com/)
- Run the following command in your terminal:
```bash
git clone https://github.com/FurkanRecber/NetworkScanner.git
```
- Navigate to the project directory:
```bash
cd NetworkScanner
```

## Usage
#### Step 1: Running the Script
You can run the script from the command line as follows:
```bash
python network_scanner.py -i <hedef_IP_adresi veya alt_ağ>
```

Example:
```bash
python network_scanner.py -i 192.168.1.1/24
```

#### Step 2: Output
After running the script:
- The devices detected on the scanned network will be listed.
- A summary of responding devices will be displayed.

## Example Use Cases
- Discovering devices on a local network.
- Identifying the IP and MAC addresses of connected devices.

## Notes
- Administrator privileges are required to run the script:
  - **Linux:** Use `sudo` to execute the script.
  - **Windows:** Run the script as an administrator.
- Only scan networks you are authorized to access. Unauthorized scanning may lead to legal or ethical issues.
