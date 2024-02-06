Automated CTF Tool

This Python-based tool is designed to streamline the initial stages of Capture The Flag (CTF) competitions by automating network scanning and web directory brute-forcing. The tool integrates Nmap for network scanning and FFUF for web directory brute-forcing, providing a comprehensive solution for reconnaissance in CTF challenges.

Features

Automated Network Scanning: Utilizes Nmap to scan target networks and identify open ports, services, and potential vulnerabilities.
Web Directory Bruteforcing: Utilizes FFUF to perform directory and file brute-forcing on web servers, uncovering hidden paths and resources.
Customizable Options: Offers flexible configuration options to adapt to various CTF scenarios and target environments.
Convenient Output Formats: Generates easy-to-read reports summarizing scan results for efficient analysis.

Requirements
Python 3.x
Nmap
FFUF

Installation
Clone the repository:

git clone https://github.com/parthyadav51/automated-nmap-and-ffuf-for-ctf-or-more

Install Python dependencies:
pip install -r requirements.txt

Ensure Nmap and FFUF are installed and accessible in your system's PATH.

Usage
Navigate to the project directory:
cd automated-ctf-tool

Run the tool with appropriate options:
python ctf_tool.py -t <target> -o <output_directory>
Replace <target> with the target IP address or hostname, and <output_directory> with the directory where you want the scan results to be saved.

Additional options can be explored using the -h or --help flag.

Example
python main.py -t 192.168.1.100 -o scans/
Contributing
Contributions are welcome! If you find any bugs or have suggestions for improvements, please feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Disclaimer
This tool is intended for educational and ethical purposes only. Use it responsibly and only on systems you are authorized to scan. The developers of this tool are not responsible for any misuse or damage caused by its usage.
