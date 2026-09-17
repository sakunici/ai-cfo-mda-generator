import streamlit as st
import pandas as pd
from google import genai

# --- 1. Setup Front-end page---
st.set_page_config(page_title="AI CFO | Automated MD&A", page_icon="📊", layout="wide")
st.title("🤖 AI CFO: Automated Board Commentary")
st.markdown("Financial Analysis & Automated MD&A Generator (Powered by Gemini 3.6 Flash)")

# --- 2. Sidebar for setting up ---
with st.sidebar:
    st.header("⚙️ Settings")
    api_key = st.text_input("🔑 API Key:", type="password")
    
    # Add a dropdown for the user to select the preferred currency
    currency = st.selectbox("💱 Select Currency:", ["THB", "USD", "EUR", "GBP", "SGD"])
    
    st.markdown("---")
    st.markdown("💡 **How to use:**\n1. Enter your API Key \n2. Select Currency \n3. Upload P&L file (Excel)\n4. Click Generate")

# --- 3. File upload area ---
uploaded_file = st.file_uploader("📂 Uppload your file here (Excel)", type=["xlsx"])

if uploaded_file is not None:
    # Display elegant tables on the web interface
    df = pd.read_excel(uploaded_file)
    df.columns = ['Line Item', 'Actual', 'Budget', 'Variance', 'Variance %']
    st.subheader("📊 Uploaded P&L Data:")
    st.dataframe(df, use_container_width=True)
    
    # --- 4. Run AI Button ---
    if st.button("🚀 Generate Executive MD&A Report", type="primary"):
        if not api_key:
            st.error("🚨 Please enter your API Key in the sidebar first!")
        else:
            with st.spinner("🧠 AI CFO is analyzing the data..."):
                try:
                    # Initialize Gemini Client
                    client = genai.Client(api_key=api_key)
                    financial_data = df.to_markdown(index=False)
                    
                    # Define the persona and instructions for the AI
                    system_prompt = f"""
                    You are an elite CFO of a dietary supplement clinic. 
                    Your task is to analyze the provided P&L Variance Report and write a concise, 3-paragraph Management Discussion & Analysis (MD&A) for the Board of Directors.
                    
                    Guidelines:
                    1. Executive Summary: Evaluate the overall financial performance, highlighting the main discrepancies between Actual and Budget for Revenue and Net Income.
                    2. Root Cause Analysis: Identify and analyze the top 3 root causes driving the most significant variances across all line items in the data.
                    3. Strategic Action: Suggest 1 forward-looking strategic action plan to optimize operations and profitability for the upcoming period.
                    
                    4. Formatting & Number Presentation: 
                       - DO NOT use the '$' symbol under any circumstances.
                       - Always append '{currency}' to all monetary values.
                       - Executive Formatting: Divide raw numbers by 1,000,000 and format them in millions with 'M' (e.g., write "9.50M {currency}" instead of 9,500,000). For numbers under 1 million, divide by 1,000 and use 'K' (e.g., "800K {currency}").
                       
                    5. Data Interpretation: The column containing the highest numerical values or labeled as 'YTD', 'Current', or 'Actuals' represents the Actual performance. The column labeled 'Bud', 'Plan', or 'Target' represents the Budget. Do not strictly rely on exact column headers.
                    
                    Maintain a highly professional, objective, and executive tone. Do not use generic filler words.
                    """
                    
                    final_prompt = f"{system_prompt}\n\nHere is the P&L Data:\n{financial_data}"
                    
                    # Execute the API call using the latest model
                    response = client.models.generate_content(
                        model='gemini-3.6-flash',
                        contents=final_prompt
                    )
                    
                    # Display the final output
                    st.success("✅ Analysis Complete!")
                    st.subheader("📑 Executive MD&A Commentary")
                    st.info(response.text)
                    
                except Exception as e:
                    st.error(f"Error encountered: {e}")