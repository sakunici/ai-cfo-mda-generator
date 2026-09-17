# 🤖 AI CFO: Automated Board Commentary Engine

An automated financial analysis web application that leverages **Google Gemini 3.6 Flash** to transform standard P&L variance reports into executive-grade Management Discussion & Analysis (MD&A) commentary. Built for CFOs and FP&A professionals to streamline board reporting.

## 🌟 Key Features
<img width="1295" height="575" alt="01_Step How to use" src="https://github.com/user-attachments/assets/de5ab370-f209-4888-b368-e84ff53ec169" />
<img width="1892" height="725" alt="02_Step Upload data" src="https://github.com/user-attachments/assets/caf8f22d-70fa-4228-84c3-23decc20572c" />
<img width="1477" height="581" alt="03_Step Result" src="https://github.com/user-attachments/assets/8d983ff9-3fc9-4219-ab84-525df8aa96f2" />


* **Executive-Grade Insights:** Automatically generates a concise, 3-paragraph root-cause analysis focusing on revenue divergence, cost overruns, and strategic action plans.
* **Universal Data Handling:** Dynamically standardizes messy or inconsistent Excel column headers without breaking the pipeline.
* **Dynamic Currency & Formatting:** Features a UI dropdown to select currencies (THB, USD, EUR, GBP, SGD). The LLM is strictly instructed to format large numbers using executive standards (e.g., `9.50M USD` or `800K EUR`) and explicitly avoids LaTeX rendering errors.
* **Situation-Agnostic AI:** Powered by advanced prompt engineering to evaluate any financial period (month, quarter, year) and any performance scenario (profit growth or margin compression) without hardcoded biases.
* **Clean Web Interface:** Built on Streamlit for a seamless, interactive user experience with secure API key management.

## 🛠️ Technology Stack

* **Language:** Python 3.13
* **Frontend:** Streamlit
* **AI/LLM:** Google GenAI SDK (`gemini-3.6-flash`)
* **Data Processing:** Pandas, Openpyxl

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/automated-board-commentary.git](https://github.com/your-username/automated-board-commentary.git)
   cd automated-board-commentary


