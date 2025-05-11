# Explainable Fraud Alert System

## Overview
The Explainable Fraud Alert System uses machine learning algorithms to detect fraudulent transactions in real-time, providing clear and understandable explanations for flagged transactions. This system integrates Isolation Forest model with a Large Language Model (LLM) for generating human-readable explanations. The solution aims to enhance customer trust, improve fraud detection accuracy, and meet regulatory compliance by offering transparent fraud alerts.

## Contents

### 1. Abstract
A brief overview of the project, the algorithms used, and the problem solved.

### 2. The Code
A Python-based implementation that combines Isolation Forest model to detect anomalies and fraudulent transactions. It also includes an LLM-based explanation engine to provide clarity on why a transaction was flagged.

### 3. Output
The output of the system, showcasing detected fraudulent transactions and the corresponding explanations for each flagged transaction.

### 4. Presentation (PPT)
A PowerPoint presentation summarizing the problem, methodology, and business impact of the project.

## Getting Started

### ✅ Prerequisites

- **Operating System:** Linux, macOS, or Windows  
- **Python Version:** 3.8 or higher  
- **Dependencies:** Listed in `requirements.txt`  
- **Tools Recommended:** VSCode, Jupyter Notebook, PyCharm  

### 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/manish02007/Naan-Mudhalvan---NLP.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Naan-Mudhalvan---NLP
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### 📊 Dataset and Features

#### Dataset
Publicly available credit card transaction dataset.
https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud?resource=download

#### Features
- `V1–V28`: Anonymized principal components  
- `Amount`: Scaled transaction amount

#### Target Label
- `Class = 0`: Legitimate  
- `Class = 1`: Fraudulent

### 📈 Results

- **Accuracy:** ~99% overall  
- **Precision (Fraud):** ~29%  
- **Recall (Fraud):** ~28%  
- **True Positives (Fraud Detected):** 139  
- **Use Case:** Real-time alerting and early fraud flagging

## Acknowledgments

- The dataset used in this project is from the Kaggle Credit Card Fraud Detection dataset.
- The scikit-learn and other libraries were used for building the machine learning models.
