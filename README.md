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
- **Hosts:** El rango de IPs o la IP individual a escanear (por ejemplo, 192.168.1.0/24 o 192.168.0.1).
- **Puertos:** Los puertos a escanear (por ejemplo, 22, 80, 443).
- **Argumentos de Nmap:** Los argumentos de Nmap que desea utilizar (por ejemplo, -sS -O).
- **Ejecutar como superusuario:** Indique si desea ejecutar el comando como superusuario (s/n).


**Scan results:**
The program will display the scan results in the console, including the status of the hosts and ports.
