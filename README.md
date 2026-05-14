# 🔐 Flask Port Scanner & WHOIS Lookup Tool

A cybersecurity-focused web application built using Python and Flask that performs port scanning and WHOIS domain lookup. This project helps users understand network services, open ports, and basic reconnaissance techniques used in cybersecurity.

---

# 📌 Project Overview

This project is a simple web-based Port Scanner developed using Python Flask. It allows users to:

* Scan open ports of a target IP address or domain
* Perform WHOIS lookup for domains
* Understand basic network reconnaissance
* Learn how socket programming works in cybersecurity

The project demonstrates:

* Flask web development
* Socket programming
* Port scanning concepts
* WHOIS information gathering
* Basic cybersecurity principles

---

# 🚀 Features

✅ Scan target IP addresses or domains
✅ Detect open ports
✅ WHOIS domain lookup
✅ Flask web interface
✅ Beginner-friendly cybersecurity project
✅ Real-time scanning results
✅ Lightweight and easy to run

---

# 🛠️ Technologies Used

| Technology   | Purpose                   |
| ------------ | ------------------------- |
| Python       | Backend programming       |
| Flask        | Web framework             |
| Socket       | Port scanning             |
| Python-WHOIS | Domain information lookup |
| HTML/CSS     | Frontend UI               |

---

# 📂 Detailed Project Structure

```text
PortScanner/
│
├── app.py                    # Main Flask application
├── requirements.txt          # Required Python packages
├── README.md                 # Project documentation
│
├── templates/                # HTML templates folder
│   └── index.html            # Main frontend page
│
├── static/                   # Static files folder
│   ├── style.css             # CSS styling
│   ├── script.js             # JavaScript functionality (optional)
│   └── images/               # Images and assets
│
├── scans/                    # Saved scan reports (optional)
│   └── reports.txt
│
└── screenshots/              # Project screenshots for GitHub
    └── homepage.png
```

---

# 📁 File Explanation

| File/Folder        | Description                      |
| ------------------ | -------------------------------- |
| `app.py`           | Main backend Flask application   |
| `requirements.txt` | Stores required Python libraries |
| `templates/`       | Contains HTML frontend pages     |
| `static/`          | Stores CSS, JS, and images       |
| `style.css`        | Frontend design and styling      |
| `script.js`        | Client-side functionality        |
| `scans/`           | Stores generated scan results    |
| `screenshots/`     | Images used in GitHub README     |
| `README.md`        | Full project documentation       |

---

# ⚙️ Requirements

Before running the project, install the following:

## 🔹 Software Requirements

* Python 3.10 or higher
* VS Code (Recommended)
* Internet connection

## 🔹 Python Libraries

Install required packages using:

```bash
python -m pip install -r requirements.txt
```

If `requirements.txt` is missing, install manually:

```bash
python -m pip install flask
python -m pip install python-whois
```

---

# 📦 requirements.txt

Create a file named `requirements.txt` and add:

```text
Flask
python-whois
```

---

# 🔧 Installation Process

## Step 1 — Download the Project

Clone the repository:

```bash
git clone https://github.com/your-username/PortScanner.git
```

Or download ZIP and extract it.

---

## Step 2 — Open Project Folder

```bash
cd PortScanner
```

---

## Step 3 — Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

## Step 4 — Run the Application

```bash
python app.py
```

---

# ▶️ Running the Project

After running the command:

```bash
python app.py
```

You will see:

```text
* Running on http://127.0.0.1:5000
```

Open browser and visit:

```text
http://127.0.0.1:5000
```

---

# 🌐 How the Project Works

## Step 1 — User Inputs Target

The user enters:

* IP Address
  OR
* Domain Name

Example:

```text
google.com
127.0.0.1
scanme.nmap.org
```

---

## Step 2 — Flask Receives Request

The Flask backend receives the target from the web interface.

---

## Step 3 — Socket Port Scanning

Python uses socket programming to connect to ports.

Example:

```python
socket.connect((target, port))
```

If connection succeeds:

```text
Port is OPEN
```

Otherwise:

```text
Port is CLOSED
```

---

## Step 4 — WHOIS Lookup

The project retrieves domain information using:

```python
import whois
```

This provides:

* Domain registrar
* Creation date
* Expiration date
* Name servers

---

## Step 5 — Results Displayed

The results are shown on the webpage.

---

# 🔍 Example Ports

| Port | Service |
| ---- | ------- |
| 21   | FTP     |
| 22   | SSH     |
| 25   | SMTP    |
| 53   | DNS     |
| 80   | HTTP    |
| 443  | HTTPS   |

---

# 📸 Sample Output

```text
Open Ports:

22 → SSH
80 → HTTP
443 → HTTPS
```

---

# 🧠 Cybersecurity Concepts Used

This project demonstrates:

* Network Reconnaissance
* Port Enumeration
* Socket Programming
* Information Gathering
* Web Application Development
* Domain Intelligence

---

# ⚠️ Important Notes

* Use this project only for educational purposes.
* Scan only systems you own or have permission to test.
* Unauthorized scanning may violate laws or network policies.

---

# 🐞 Common Errors & Fixes

## Error: No module named 'whois'

Fix:

```bash
python -m pip install python-whois
```

---

## Error: Flask not found

Fix:

```bash
python -m pip install flask
```

---

## Error: Port already in use

Change Flask port:

```python
app.run(port=5001)
```

---

# 🔥 Future Improvements

Possible upgrades:

* Multi-threaded scanning
* Banner grabbing
* Service detection
* Dark mode UI
* Export reports
* Real-time scan progress
* IP geolocation
* Admin dashboard

---

# 📚 Learning Outcomes

By building this project, you learn:

* Flask web development
* Python networking
* Cybersecurity basics
* Socket programming
* Web application architecture
* Domain analysis

---

# 👨‍💻 Author

**Keerti Nalatawad**
Cybersecurity & MERN Stack Developer

---

# 📜 License

This project is for educational and learning purposes.

---

# ⭐ GitHub Upload Instructions

## Step 1 — Initialize Git

```bash
git init
```

---

## Step 2 — Add Files

```bash
git add .
```

---

## Step 3 — Commit

```bash
git commit -m "Initial commit"
```

---

## Step 4 — Connect GitHub Repository

```bash
git remote add origin https://github.com/your-username/PortScanner.git
```

---

## Step 5 — Push to GitHub

```bash
git branch -M main
git push -u origin main
```

