
# Python Port Scanner

A beginner-friendly TCP port scanner built using Python.

## Features

- Accepts a target IP address from the user.
- Allows custom port ranges.
- Detects open TCP ports.
- Stores discovered open ports.
- Displays a final scan summary.
- Uses socket timeouts.

## Technologies Used

- Python
- Socket library
- TCP networking

## How to Run

1. Make sure Python is installed.
2. Clone or download this repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python port-scanner.py
```

5. Enter the target IP address.
6. Enter the starting and ending ports.

## Example

```text
Enter target IP address: 127.0.0.1
Enter starting port: 7999
Enter ending port: 8001

Scanning 127.0.0.1 ...

Port 8000 is OPEN

Scan complete!
Open ports: [8000]
Total open ports: 1
```

## Disclaimer

Use this tool only on systems you own or have explicit permission to scan.

## Author

A beginner cybersecurity project created while learning Python and networking.
