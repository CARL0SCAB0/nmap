# nmap Network Scanner

This project is a network scanner based on Nmap implemented in Python. It uses the `python-nmap` library to perform network scans and display the results in the console.

## Requirements

- Python 3.12
- nmap
- Python libraries:
  - python-nmap

## Installation

**Clone the repository:**

   ```bash
   git clone <your_repository_URL>
   cd <project_directory_name>
   ```
**Install the dependencies:**

```bash
   pip install -r requirements.txt
   ```

##Usage

**Run the script:**
```bash
python nmap_scanner.py
   ```

**Follow the instructions in the console:**

The program will prompt you to enter the following details:

Hosts: The range of IPs or the individual IP to scan (e.g., 192.168.1.0/24 or 192.168.0.1).
Ports: The ports to scan (e.g., 22, 80, 443).
Nmap arguments: The Nmap arguments you want to use (e.g., -sS -O).
Run as superuser: Indicate if you want to run the command as a superuser (y/n).
If you choose to run as a superuser, you will be asked for the sudo password.

**Scan results:**
The program will display the scan results in the console, including the status of the hosts and ports.
