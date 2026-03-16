import streamlit as st
import pandas as pd
import plotly.express as px
from fpdf import FPDF
from datetime import date

# ----------------------
# PAGE CONFIG
# ----------------------
st.set_page_config(page_title="PW127F Engine Monitoring", layout="wide")

# ----------------------
# HEADER
# ----------------------
col1, col2 = st.columns([1,5])
with col1:
    st.image("pw.png", width=120)
with col2:
    st.title("PW127F ENGINE HEALTH MONITORING")
    st.subheader("Fleet & Advanced Analytics")
    st.write("Created by Y.A. PRASETYA PUTRA")

st.divider()

# ----------------------
# AIRCRAFT INFO
# ----------------------
c1,c2,c3,c4 = st.columns(4)
tanggal = c1.date_input("Date", date.today())
aircraft = c2.text_input("Aircraft Reg")
engine = c3.text_input("Engine Number")
route = c4.text_input("Route")
st.divider()

# ----------------------
# CYCLE INPUT
# ----------------------
cycle = st.number_input("Number of Cycles", 1, 10, 3)
data = []

for i in range(cycle):
    st.subheader(f"CYCLE {i+1}")
    col1, col2, col3 = st.columns(3)

    # ---------- Engine Start ----------
    with col1:
        st.markdown("### Engine Start")
        itt_start = st.number_input("ITT Start °C", 0.0, 1200.0, key=f"itt_start{i}")

    # ---------- Ground Idle ----------
    with col2:
        st.markdown("### Ground Idle")
        tq_g = st.number_input("Torque %", 0.0, 100.0, key=f"tqg{i}")
        np_g = st.number_input("NP %", 0.0, 110.0, key=f"npg{i}")
        itt_g = st.number_input("ITT °C", 0.0, 900.0, key=f"ittg{i}")
        nh_g = st.number_input("NH %", 0.0, 100.0, key=f"nhg{i}")
        oilp_g = st.number_input("Oil Pressure", 0.0, 100.0, key=f"oilpg{i}")
        oilt_g = st.number_input("Oil Temp °C", 0.0, 120.0, key=f"oiltg{i}")

    # ---------- Flight Power ----------
    with col3:
        st.markdown("### Flight Power")
        tq_f = st.number_input("Torque Flight %",0.0,120.0,key=f"tqf{i}")
        np_f = st.number_input("NP Flight %",0.0,110.0,key=f"npf{i}")
        itt_f = st.number_input("ITT Flight °C",0.0,900.0,key=f"ittf{i}")
        nh_f = st.number_input("NH Flight %",0.0,110.0,key=f"nhf{i}")
        nl_f = st.number_input("NL %",0.0,110.0,key=f"nlf{i}")
        oilp_f = st.number_input("Oil Pressure Flight",0.0,100.0,key=f"oilpf{i}")
        oilt_f = st.number_input("Oil Temp Flight",0.0,120.0,key=f"oiltf{i}")
        ff = st.number_input("Fuel Flow kg/hr",0.0,2000.0,key=f"ff{i}")

    # ---------- STATUS LOGIC ----------
    alerts = []
    causes = []
    actions = []
    status = "NORMAL"
    
    # Engine Start
    if itt_start >= 950:
        status = "MAINTENANCE REQUIRED"
        alerts.append("ITT START OVERLIMIT")
        causes.append("Hot start / excess fuel")
        actions.append("Inspect fuel nozzle and starter")
    elif itt_start >= 900:
        status = "ENGINE DEGRADED"
        alerts.append("HIGH ITT START")
        causes.append("Compressor fouling")
        actions.append("Perform compressor wash")

    # Ground Idle
    if tq_g >= 6:
        status = "MAINTENANCE REQUIRED"
        alerts.append("GROUND IDLE TORQUE HIGH")
        causes.append("Propeller drag")
        actions.append("Inspect propeller governor")
    if np_g >= 71:
        status = "MAINTENANCE REQUIRED"
        alerts.append("NP HIGH AT GROUND IDLE")
        causes.append("Propeller governor malfunction")
        actions.append("Inspect propeller control")
    if itt_g >= 280:
        status = "MAINTENANCE REQUIRED"
        alerts.append("ITT HIGH AT GROUND IDLE")
        causes.append("Compressor efficiency loss")
        actions.append("Engine performance inspection")
    if nh_g >= 80:
        status = "ENGINE DEGRADED"
        alerts.append("NH HIGH AT GROUND IDLE")
        causes.append("Compressor fouling")
        actions.append("Perform compressor wash")
    if oilp_g < 40 or oilp_g > 60:
        status = "MAINTENANCE REQUIRED"
        alerts.append("OIL PRESSURE ABNORMAL")
        causes.append("Lubrication system issue")
        actions.append("Inspect oil pump")
    if oilt_g >= 80:
        status = "ENGINE DEGRADED"
        alerts.append("OIL TEMP HIGH")
        causes.append("Oil cooler efficiency reduced")
        actions.append("Inspect oil cooler")

    # Flight Power
    if tq_f >= 90:
        status = "MAINTENANCE REQUIRED"
        alerts.append("TORQUE OVERLIMIT")
        causes.append("Engine overload")
        actions.append("Inspect propeller blade")
    if np_f >= 100:
        status = "MAINTENANCE REQUIRED"
        alerts.append("NP OVERLIMIT")
        causes.append("Propeller governor failure")
        actions.append("Check propeller control")
    if itt_f >= 740:
        status = "MAINTENANCE REQUIRED"
        alerts.append("ITT FLIGHT OVERLIMIT")
        causes.append("Hot section deterioration")
        actions.append("Hot section inspection")
    elif itt_f >= 720:
        status = "ENGINE DEGRADED"
        alerts.append("HIGH ITT FLIGHT")
        causes.append("Compressor fouling")
        actions.append("Perform compressor wash")
    if nh_f >= 100.1:
        status = "MAINTENANCE REQUIRED"
        alerts.append("NH OVERLIMIT")
        causes.append("Compressor performance degradation")
        actions.append("Borescope inspection")
    elif nh_f >= 99:
        status = "ENGINE DEGRADED"
        alerts.append("NH HIGH")
        causes.append("Early compressor deterioration")
        actions.append("Monitor performance")
    if nl_f >= 100.2:
        status = "MAINTENANCE REQUIRED"
        alerts.append("NL OVERLIMIT")
        causes.append("Power turbine overspeed")
        actions.append("Inspect power turbine")
    if oilp_f < 40 or oilp_f > 65:
        status = "MAINTENANCE REQUIRED"
        alerts.append("FLIGHT OIL PRESSURE ABNORMAL")
        causes.append("Lubrication system issue")
        actions.append("Inspect oil system")
    if oilt_f >= 80:
        status = "ENGINE DEGRADED"
        alerts.append("FLIGHT OIL TEMP HIGH")
        causes.append("Oil cooling issue")
        actions.append("Inspect oil cooler")
    if ff >= 580:
        status = "ENGINE DEGRADED"
        alerts.append("FUEL FLOW HIGH")
        causes.append("Engine efficiency loss")
        actions.append("Engine performance check")

    # ---------- DISPLAY ALERTS ----------
    st.markdown("### ENGINE DIAGNOSTIC")
    for a in alerts: st.error(a)

    st.markdown("### POSSIBLE CAUSE")
    for c in causes: st.write("-", c)

    st.markdown("### MAINTENANCE RECOMMENDATION")
    for r in actions: st.warning(r)

    # ---------- SAVE DATA ----------
    data.append({
        "Cycle": i+1,
        "Aircraft": aircraft,
        "Engine": engine,
        "ITT Start": itt_start,
        "ITT Flight": itt_f,
        "NH Flight": nh_f,
        "Torque Flight": tq_f,
        "Fuel Flow": ff,
        "Status": status
    })

st.divider()

# ---------- DATAFRAME ----------
df = pd.DataFrame(data)
st.header("Fleet Engine Health Table")
st.dataframe(df)

# ---------- TREND ANALYTICS ----------
st.header("Engine Trend Monitoring")

fig1 = px.line(df, x="Cycle", y="ITT Flight", markers=True, title="ITT Flight Trend")
st.plotly_chart(fig1, use_container_width=True)

fig2 = px.line(df, x="Cycle", y="NH Flight", markers=True, title="NH Trend")
st.plotly_chart(fig2, use_container_width=True)

fig3 = px.line(df, x="Cycle", y="Fuel Flow", markers=True, title="Fuel Flow Trend")
st.plotly_chart(fig3, use_container_width=True)

fig4 = px.scatter(df, x="Fuel Flow", y="ITT Flight", size="Torque Flight", title="ITT vs Fuel Flow")
st.plotly_chart(fig4, use_container_width=True)

st.divider()

# ---------- PDF REPORT ----------
if st.button("GENERATE PDF REPORT"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "PW127F ENGINE HEALTH REPORT", 0, 1, "C")

    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 8, f"Aircraft: {aircraft}", 0, 1)
    pdf.cell(0, 8, f"Engine: {engine}", 0, 1)
    pdf.cell(0, 8, f"Route: {route}", 0, 1)
    pdf.cell(0, 8, f"Date: {tanggal}", 0, 1)
    pdf.ln(5)

    for idx, row in df.iterrows():
        pdf.cell(0, 8, f"CYCLE {row['Cycle']}", 0, 1)
        pdf.cell(0, 8, f"ITT FLIGHT : {row['ITT Flight']} °C", 0, 1)
        pdf.cell(0, 8, f"NH FLIGHT  : {row['NH Flight']} %", 0, 1)
        pdf.cell(0, 8, f"FUEL FLOW  : {row['Fuel Flow']} kg/hr", 0, 1)
        pdf.cell(0, 8, f"STATUS     : {row['Status']}", 0, 1)
        pdf.ln(3)

    pdf.output("PW127F_ENGINE_REPORT.pdf")

    with open("PW127F_ENGINE_REPORT.pdf", "rb") as file:
        st.download_button(
            label="DOWNLOAD PDF REPORT",
            data=file,
            file_name="PW127F_ENGINE_REPORT.pdf",
            mime="application/pdf"
        )