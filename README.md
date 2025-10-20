# SmartPigCare

SmartPigCare is a web-based application built for the AI Foundry Hackathon at UIUC (2025), where it won the award for Best Presentation. This demo platform showcases how AI-driven tools can monitor and analyze swine health and feeding patterns using sample data and machine learning models.

## Overview

This project demonstrates a complete pig farm health management system with interactive dashboards, predictive analytics, and automated health monitoring. The application processes sample sensor data, pig images, and feeding logs to provide insights into animal welfare and farm operations.

The demo uses a combination of technologies including:
- **Flask** for the web application framework
- **Machine Learning Models** for body condition scoring and feeding behavior analysis
- **Sample Sensor Data** (CSV/JSON) to simulate real-time farm monitoring
- **Interactive Visualizations** to display health metrics and trends

## Features

### 1. Pig Health Dashboard

The dashboard provides a comprehensive view of individual pig profiles and farm-wide metrics:

- **Individual Pig Profiles**: Each pig has a profile displaying weight, age, Body Condition Score (BCS), feeding activity levels, and historical trends
- **Health Metrics Visualization**: Interactive graphs and charts generated from sample sensor logs showing feeding patterns, weight changes, and activity levels over time
- **Sample Data Structure**: The demo uses structured JSON data containing pig IDs, timestamps, sensor readings, and health indicators
- **Real-time Updates**: The interface simulates real-time monitoring by processing timestamped sample data

### 2. AI Predictions

The application demonstrates two core AI capabilities:

**Feeding Behavior Detection:**
- Analyzes feeding sensor logs to identify patterns such as underfeeding, feeding stalls, or abnormal feeding times
- Uses time-series analysis on sample feeding data (timestamp, pig ID, feed intake amounts)
- Detects anomalies by comparing individual feeding patterns against baseline behaviors
- Generates alerts when feeding activity falls outside expected parameters

**Body Condition Scoring (BCS):**
- Accepts pig image uploads and returns health score predictions (e.g., healthy, underweight, overweight)
- Machine learning model trained on sample pig images with labeled body condition scores
- Processes JPEG/PNG image formats and outputs confidence scores for each condition category
- Demo includes a set of pre-classified sample images for testing the prediction interface

### 3. Health Data & Alerts

**Sample Data Structure:**
- Example pig images stored in `/data` directory with associated metadata
- Feeding sensor logs in CSV/JSON format containing fields: timestamp, pig_id, feed_intake, duration
- Sample environmental data (temperature, humidity) demonstrating climate monitoring integration
- Pre-configured pig profiles with sample health histories

**Automated Alert System:**
- Triggers notifications when feeding activity drops below threshold levels
- Alerts when body condition scores fall outside healthy ranges (BCS 2.5-3.5)
- Monitors sample climate data and flags conditions that may pose health risks
- Dashboard displays active alerts with severity indicators and timestamps

## What You Need to Run the Demo

**Requirements:**
- **Python 3.8+**
- **Git**
- **VS Code (recommended)**
- All other dependencies listed in `requirements.txt`

**Installation and Setup:**

```bash
git clone https://github.com/abigailtay/smartpigcare.git
cd smartpigcare
python -m venv venv   # Create virtual environment
source venv/bin/activate  # Activate (use `venv\Scripts\activate` on Windows)
pip install -r requirements.txt
python app.py         # Start Flask server
```

Then visit [http://localhost:5000](http://localhost:5000) in your browser to view the dashboard.

## Demo Data and Technology

The application includes comprehensive sample data to demonstrate all features:

- **Combined Data File**: `/data/combined_data.json` contains all sample pig profiles, sensor readings, and health records
- **Image Dataset**: Sample pig images in `/data/images` for testing the BCS prediction model
- **Training Scripts**: `/scripts/train_feeding.py` and `/scripts/train_bcs.py` demonstrate the model training pipeline used for the demo
- **Dashboard Templates**: Frontend interface built with HTML/CSS/JavaScript in `/templates/index.html`
- **Model Architecture**: The demo uses scikit-learn for feeding behavior analysis and a CNN-based model for image classification
