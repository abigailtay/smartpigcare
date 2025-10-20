# SmartPigCare

SmartPigCare is a web-based application built for the AI Foundry Hackathon at UIUC (2025), where it won the award for Best Presentation. The site demonstrates how AI-driven tools can help monitor and manage swine health and feeding using sample data.

## Overview

This project is a demo platform that showcases core features for pig farm health management. It offers:
- Interactive dashboards to visualize pig profiles and health metrics
- Prediction tools for feeding behavior and body condition
- Alerts for potential health or feeding issues

> **Note:** The default setup uses dummy images and sensor data for demonstration purposes. You can customize it for your farm with real data (see below).

## Features

### 1. Pig Health Dashboard
- **Displays pig profiles** with weight, age, BCS (Body Condition Score), feeding activity, and more.
- **Metrics and graphs** are generated from sample sensor logs and images.

### 2. AI Predictions
- **Feeding Behavior Detection:**
  - Models analyze feeding sensor logs to spot underfeeding, feeding stalls, or abnormal feeding times.
- **Body Condition Scoring (BCS):**
  - Upload pig images to see health score predictions (e.g., healthy, underweight, overweight).
  - Uses a machine learning model trained on sample images.

### 3. Health Data & Alerts
- **Dummy Data:**
  - Includes example pig images, sensor logs (CSV/JSON), and sample profiles.
- **Automatic Alerts:**
  - Get notified if feeding drops, body condition falls outside healthy ranges, or dummy climate data triggers risks.

## What You Need to Run the Demo

- **Python 3.8+**
- **Git**
- **VS Code (recommended)**
- All other dependencies in `requirements.txt`

To run locally:
```bash
git clone https://github.com/abigailtay/smartpigcare.git
cd smartpigcare
python -m venv venv   # Create virtual environment
source venv/bin/activate  # Activate (use `venv\Scripts\activate` on Windows)
pip install -r requirements.txt
python app.py         # Start Flask server
```
Then visit [http://localhost:5000](http://localhost:5000) in your browser to view the dashboard.

## How to Adapt for a Real Farm

If you want to use SmartPigCare with your own farm data:
- **Images:** Add JPEG/PNG images of your pigs to `/data` (label by pig ID for best results)
- **Feeding Logs:** Upload feeding activity logs (CSV/JSON: timestamp, pig ID, feed intake)
- **Sensors (Optional):** Only images and feed logs are needed for the basic demo. For advanced features use environmental sensors (temperature, humidity) and RFID for pig identification.
- **Retrain Models:** Use `/scripts/train_feeding.py` and `/scripts/train_bcs.py` with your data for improved accuracy.

## Customization
- Change sample data in `/data/combined_data.json`
- Edit dashboard templates in `/templates/index.html`
- Adjust alert thresholds in code, or contact the team for advanced features

## Future Work
- Expand prediction models (disease detection, weight estimation)
- Cloud hosting for multi-farm support
- Mobile-responsive dashboard
- Integration with more sensor hardware

For questions or feedback, please open an issue or contact the repository maintainer.
