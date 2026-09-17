import pandas as pd
from google import genai

# 🔑 1. Enter your API Key that you just copied from Geminin
client = genai.Client(api_key="Enter your Gemini secret key here")

# 📊 2. Retrieve dataf from P&L table in excel file
print("Readging from Excel...")
df = pd.read_excel('Board_Report_Data.xlsx')
financial_data = df.to_markdown(index=False)

# 🤖 3. The Executive Prompt
# Set a default currency for the terminal execution
currency = "USD"
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

print("Sending data to Gemini AI to analyse (wait a minite)...")

# 🚀 4. Combine and send to AI (new Syntax version)
final_prompt = f"{system_prompt}\n\nHere is the P&L Data:\n{financial_data}"

response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents=final_prompt
)

# 📈 5. Print the result
print("\n" + "="*50)
print("🎯 EXECUTIVE MD&A COMMENTARY GENERATED (By Gemini)")
print("="*50 + "\n")
print(response.text)