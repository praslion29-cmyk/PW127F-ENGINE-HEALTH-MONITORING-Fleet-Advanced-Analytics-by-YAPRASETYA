# PW127F Engine Health Monitoring  
Fleet & Advanced Analytics Dashboard

Created by **Y.A. PRASETYA PUTRA**

---

## Overview

This application is a **professional engine health monitoring dashboard** developed for the **PW127F turboprop engine** installed on the **ATR 72-600 aircraft (Wings Air fleet)**.

The tool simulates a **Skywise-style monitoring system** used by airline reliability engineers to monitor engine performance trends, detect anomalies, and provide maintenance insights.

The system allows engineers to monitor **multiple flight cycles** and analyze engine performance using **trend analysis, health scoring, and maintenance recommendations**.

---

## Main Features

### Engine Monitoring
The system monitors three operating conditions:

#### 1. Engine Start
Parameter monitored:

- ITT Start Temperature  
Limit:
- Maximum 950°C

---

#### 2. Ground Idle  
(Condition Lever: AUTO, Power Lever: Ground Idle)

Parameters monitored:

- Torque (TQ) < 6 %
- NP (Propeller Rotation) < 71 %
- ITT < 280 °C
- NH < 80 %
- Oil Pressure 40 – 60 psi
- Oil Temperature < 80 °C

---

#### 3. Flight Power  
(Condition Lever: AUTO, Power Lever: Notch)

Parameters monitored:

- Torque (TQ) < 90 %
- NP < 100 %
- ITT < 740 °C
- NH < 100.1 %
- NL < 100.2 %
- Oil Pressure 40 – 65 psi
- Oil Temperature < 80 °C
- Fuel Flow monitoring

---

## Traffic Light Monitoring System

The dashboard uses a **traffic light system**:

🟢 **Green** → Normal condition  
🟡 **Yellow** → Approaching limit  
🔴 **Red** → Over limit (maintenance attention required)

---

## Advanced Analytics

The system includes:

- ITT Trend Monitoring
- NH Trend Monitoring
- Fuel Flow Trend
- Torque Trend
- ITT vs Fuel Flow correlation
- Engine Health Score calculation

This allows engineers to detect:

- Compressor efficiency degradation
- Hot section deterioration
- Abnormal fuel consumption
- Engine performance drift

---

## Maintenance Insight

The application automatically generates maintenance recommendations based on trend analysis such as:

- Compressor wash recommendation
- Hot section inspection
- Lubrication system check
- Performance degradation detection

---

## Fleet Monitoring

The dashboard allows monitoring of:

- Aircraft Registration
- Engine Number
- Flight Route
- Multiple flight cycles

This simulates a **fleet monitoring environment used by airline reliability departments**.

---

## PDF Report

The system can generate a **maintenance report in PDF format** including:

- Aircraft information
- Engine parameters
- Cycle performance summary
- Health score

This feature allows engineers to **store maintenance records for analysis and documentation**.

---

## Installation

Make sure Python is installed.

Install required libraries:

```bash
python -m pip install -r requirements.txt