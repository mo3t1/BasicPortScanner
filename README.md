Usage Example (Single IP)
Run the script:

python3 port_scanner.py

When prompted:

Enter the IP address to scan: 192.168.1.1
Enter start port: 20
Enter end port: 100

What happens:

It will scan ports 20 to 100 on the IP 192.168.1.1.

Then it prints which ports are open.

Example Output

Scanning 192.168.1.1 from port 20 to 100...

Open ports:
Port 22 is open
Port 80 is open

Notes:

Single IP only — It scans only the one IP you enter.

One range — It needs a start and end port.

You can Ctrl+C anytime to stop scanning.

Validations are there: Wrong IP formats or port mistakes are caught immediately.
