# 🤖 AI-Powered Knowledge Engine for Smart Support and Ticket Resolution

### 🏫 Developed under Infosys Springboard Internship 6.0

This project leverages **Natural Language Processing (NLP)**, **Machine Learning**, **Knowledge Graphs**, and a **stack-based notification system for low coverage areas** to build an intelligent, reliable, and context-aware support engine.

---

## 🚀 Overview

The **AI-Powered Knowledge Engine** automates customer support and ticket management by:
- Classifying and prioritizing support tickets.
- Suggesting context-based resolutions.
- Automating ticket workflows using machine learning.
- Handling notifications in low connectivity regions through a stack-based message queuing system.

---

## 🧩 Key Features

- 🧠 **AI Question Answering** – Understands user queries and provides contextual answers.  
- 📊 **Ticket Classification & Validation** – Categorizes tickets and evaluates model performance.  
- 📈 **Interactive Dashboard** – Displays metrics like Accuracy, Precision, Recall, and F1-score.  
- 🔄 **Google Sheets Integration** – Dynamically reads and updates records using Google Sheets API.  
- 🧱 **Stack-Based Notification System** – Stores and pushes alerts when connectivity is restored.  
- 🧰 **Secure & Scalable Design** – Environment variables and credentials kept isolated and secure.

---

## 🛠️ Tech Stack

| Component | Technology |
|------------|-------------|
| Frontend / UI | Streamlit |
| Backend | Python 3.10+ |
| Data Handling | Pandas, NumPy |
| Machine Learning | Scikit-learn, NLTK |
| Async Execution | AsyncIO, Nest-AsyncIO |
| External Integration | Google Sheets API |
| Notifications | Stack-based offline alert system |

---

## ⚙️ Setup and Installation Guide

Follow these steps to set up and run the project locally 👇

---

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/BalajiSunkara-123/AI-Powered-Knowledge-Engine-for-Smart-Support-and-Ticket-Resolution.git
cd AI-Powered-Knowledge-Engine-for-Smart-Support-and-Ticket-Resolution

### 2️⃣ Create a Virtual Environment
Create and activate a virtual environment to keep dependencies isolated.

```bash
# For Windows
python -m venv env
env\Scripts\activate

# For macOS/Linux
python3 -m venv env
source env/bin/activate
3️⃣ Install Required Packages
pip install -r requirements.txt

4️⃣ Setup Google Sheets API Credentials

Go to Google Cloud Console
.

Create/select a project.

Enable APIs:

Google Sheets API

Google Drive API

Create a Service Account → Add Key → Create JSON Key

Rename the file to credentials.json

Place it in the project root.

Add it to .gitignore:

credentials.json

5️⃣ Create .env File

Add environment variables in .env at the root:

GOOGLE_SHEETS_CREDENTIALS="credentials.json"
SPREADSHEET_ID="your_google_sheet_id_here"


Find SPREADSHEET_ID in your Google Sheet URL:

https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit#gid=0

6️⃣ Run Streamlit App
streamlit run app.py


Visit http://localhost:8501 in your browser to use the app.