@echo off
REM This batch script installs requirements and runs the Streamlit dashboard for the Lime IoT ML Platform.

REM Install requirements
pip install -r requirements.txt

REM Launch Streamlit dashboard
streamlit run app.py