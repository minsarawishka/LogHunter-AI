import streamlit as pd
import streamlit as st
import pandas as pd
import plotly.express as px
from log_parser import parse_log_file, detect_brute_force
from ai_analyzer import analyze_logs_with_ai

st.set_page_config(page_title="LogHunter AI", page_icon="🛡️", layout="wide")

st.markdown("<h1 style='text-align: center; color: #00FFCC;'>🛡️ LogHunter AI: Threat Investigator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888888;'>Upload server logs, detect brute-force attacks, and get automated AI insights instantly.</p>", unsafe_allow_html=True)
st.markdown("---")

uploaded_file = st.file_uploader("Upload your server log file (.log or .txt)", type=["log", "txt"])

if uploaded_file is not None:
    with open("temp_uploaded.log", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    with st.spinner("Parsing log file..."):
        df = parse_log_file("temp_uploaded.log")
        
    if not df.empty:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Log Entries", len(df))
        with col2:
            failed_count = len(df[df['status'].str.strip() == 'Failed Password'])
            st.metric("Total Failed Logins", failed_count, delta_color="inverse")
        with col3:
            success_count = len(df[df['status'].str.strip() == 'Successful Login'])
            st.metric("Successful Logins", success_count)
            
        st.subheader("🚨 Brute-Force Attack Detection")
        threshold = st.slider("Select Failed Password Threshold for Alert", min_value=2, max_value=10, value=3)
        
        alerts_df = detect_brute_force(df, threshold)
        
        if not alerts_df.empty:
            st.error(f"Critical Alert: Detected suspicious activity from {alerts_df['ip'].nunique()} unique IP addresses!")
            st.dataframe(alerts_df, use_container_width=True)
            
            st.markdown("### 📊 Attack Visualization")
            fig = px.bar(
                alerts_df, 
                x='ip', 
                color='user', 
                title='Failed Login Attempts per IP (Targeted Users)',
                labels={'ip': 'Attacker IP', 'count': 'Number of Attempts'}
            )
            st.plotly_chart(fig, use_container_width=True)
            
            st.markdown("---")
            st.markdown("### 🤖 AI Threat Analysis & Remediation")
            
            if st.button("Generate AI Insights"):
                with st.spinner("AI is analyzing the threat environment..."):
                    ai_report = analyze_logs_with_ai(alerts_df)
                    st.info(ai_report)
        else:
            st.success("No brute-force attacks detected based on the selected threshold.")
            
        st.markdown("---")
        st.subheader("📁 Raw Log Data Preview")
        st.dataframe(df, use_container_width=True)
        
    else:
        st.error("Could not parse any valid data from the uploaded file. Please check the log format.")