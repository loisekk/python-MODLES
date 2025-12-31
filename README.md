# 🧠 Python Projects Portfolio

This repository contains **two beginner-to-intermediate Python projects** focused on **Machine Learning fundamentals** and **Cybersecurity concepts**. Both projects are designed to be **resume-ready**, **GitHub-presentable**, and easy to understand for learners.

---

## 📂 Repository Structure

```text
python-projects/
│
├── ml-linear-regression/
│   ├── linear_regression.py
│   └── README.md
│
├── password-manager/
│   ├── password_manager.py
│   ├── salt.key            # Auto-generated
│   ├── password.txt        # Encrypted storage
│   └── README.md
│
└── README.md               # Main portfolio README
```

---

# 📊 Project 1: Student Score Prediction (Machine Learning)

A **Linear Regression** project that predicts student scores based on the number of hours studied. This project demonstrates the **complete ML workflow**: data preparation, model training, evaluation, and visualization.

### 🔧 Technologies Used

* Python
* NumPy
* Pandas
* scikit-learn
* Matplotlib

### 🧠 What This Project Demonstrates

* Feature vs target selection
* Train–test split
* Model training using Linear Regression
* Model evaluation using Mean Squared Error (MSE)
* Data visualization

### 📌 ML Logic Explained

* **Linear Regression** finds the best-fit straight line:

```
y = mx + c
```

* `Hours_studied` → Independent variable (X)
* `score` → Dependent variable (y)
* The model learns how study hours affect scores

### ▶ How to Run

```bash
cd ml-linear-regression
python linear_regression.py
```

---

# 🔐 Project 2: Password Manager (Cybersecurity)

A **command-line password manager** that securely stores and retrieves passwords using **Fernet symmetric encryption**. This project focuses on **security fundamentals**, encryption, and safe password handling.

### 🔧 Technologies Used

* Python
* cryptography (Fernet)
* PBKDF2 key derivation
* OS file handling

### 🔑 Key Security Concepts

* Master password protection
* Password-based key derivation (PBKDF2)
* Symmetric encryption (AES via Fernet)
* Secure password storage

### 🧠 How Security Works (Simplified)

```
Master Password
      ↓
PBKDF2 Key Derivation
      ↓
Fernet Encryption Key
      ↓
Encrypted Password Storage
```

### ▶ How to Run

```bash
cd password-manager
python password_manager.py
```

---

## 💼 Resume Highlights

* Built a **machine learning regression model** using real-world workflow
* Implemented **secure password storage** using industry-standard encryption
* Demonstrated strong understanding of **Python, security, and ML basics**
* Clean project structure with documentation

---

## 👨‍💻 Author

**Yash Brahmankar**
Aspiring Python Developer | ML & Security Enthusiast

---

## 📜 License

This repository is intended for **creating something**.
