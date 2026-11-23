# 🛡️ Phishing URL Detection System

A Machine Learning based cybersecurity application that analyzes URLs and predicts whether they are **Legitimate, Suspicious, or Phishing**.

The system extracts security-related characteristics from a URL and uses a **Random Forest Classifier** to identify potentially malicious websites.

## 🎯 Project Objective

Phishing attacks often attempt to trick users into visiting malicious websites that imitate legitimate services.

The objective of this project is to build an automated phishing detection system capable of analyzing characteristics of a URL and its domain to help identify potentially malicious websites.

## ✨ Features

- 🔍 URL-based phishing detection
- 🤖 Machine Learning classification using Random Forest
- 🔐 HTTPS/SSL certificate analysis
- 🌐 Domain information analysis
- 🔗 URL structure and pattern analysis
- 📊 Multiple security features used for prediction
- 🖥️ Simple desktop GUI built with Tkinter
- ⚡ Real-time URL analysis

## 🧠 How It Works

The application follows the following pipeline:

User enters URL
       ↓
URL Validation
       ↓
Security Feature Extraction
       ↓
Random Forest Classifier
       ↓
Prediction
       ↓
Legitimate / Suspicious / Phishing

## 🔎 Features Analyzed

Some of the security characteristics analyzed by the system include:

| Feature | Purpose |
|---|---|
| IP Address in URL | Detects URLs using IP addresses instead of normal domain names |
| URL Length | Checks for unusually long URLs |
| URL Shortening | Detects URL shortening services |
| `@` Symbol | Detects potentially misleading URL structures |
| Double Slash Redirect | Checks suspicious URL redirection patterns |
| Prefix/Suffix | Detects hyphens in domain names |
| Subdomains | Analyzes the number of subdomains |
| SSL Certificate | Checks HTTPS/SSL availability |
| Domain Registration | Examines domain registration information |
| Favicon | Checks website favicon information |
| Port | Examines network port accessibility |
| HTTPS Token | Detects misleading HTTPS text inside domain names |
| Request URL | Examines resources requested by the website |
| Anchor URLs | Analyzes links present on the webpage |

## 🛠️ Tech Stack

**Language**
- Python

**Machine Learning**
- Scikit-learn
- Random Forest Classifier
- Pandas
- SciPy

**Web & Security Analysis**
- Requests
- BeautifulSoup
- WHOIS
- SSL
- Socket
- urllib

**User Interface**
- Tkinter

---

## 📁 Project Structure

```text
phishing-url-detection/
│
├── phisher.py
├── Training Dataset.arff
├── Phishing Websites Features.docx
├── requirements.txt
├── screenshots/
│   └── application.png
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Prince-Mann94/Phishing_Detection.git
cd Phishing_Detection
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python phisher.py
```

---

## 🖥️ Usage

1. Launch the application.
2. Enter a complete URL such as:

```text
https://example.com
```

3. Click **Check URL**.
4. The application extracts relevant security features.
5. The machine-learning model analyzes the extracted features.
6. The URL is classified as:

```text
🟢 Legitimate
🟡 Suspicious
🔴 Phishing
```

---

## 🤖 Machine Learning Model

The project uses a **Random Forest Classifier** for phishing website classification.

Random Forest combines multiple decision trees and uses their collective predictions to produce the final classification. This makes it suitable for classification problems involving multiple URL and website security features.

---

## 🔮 Future Improvements

Planned improvements include:

- Gmail phishing-link scanning
- Improved feature extraction
- Model evaluation and performance metrics
- Browser extension integration
- REST API for URL scanning
- Web-based user interface
- Real-time threat intelligence integration
- Model persistence instead of retraining during application startup

---

## ⚠️ Disclaimer

This project was developed for **educational and cybersecurity research purposes**.

The predictions should not be treated as a replacement for professional security tools. A URL classified as legitimate may still be malicious, and phishing detection techniques can produce false positives or false negatives.

---

## 👨‍💻 Author

**Prince Mann**

GitHub: [Prince-Mann94](https://github.com/Prince-Mann94)

---## ⭐ Support

If you find this project useful, consider giving the repository a ⭐.
