# 🚀 AI Code Migration Tool

An intelligent code translation application built with **Streamlit** and powered by the **Claude 3.5 Opus** model. This tool automates the process of migrating Python logic into structured, compilable Java code.

## 📌 Project Overview
As developers frequently switch between languages, manual migration is time-consuming. This project leverages Large Language Models (LLMs) to handle syntax translation, boilerplate generation (Classes/Main methods), and logical mapping between Python and Java.

## ✨ Features
* **Automated Translation:** Converts Python scripts into production-ready Java code.
* **Smart Boilerplate:** Automatically wraps converted logic in a `public class ConvertedCode` and `main` method.
* **Instant Preview:** View converted code with full syntax highlighting directly in the browser.
* **One-Click Download:** Export your result as a `.java` file immediately.
* **Secure API Integration:** Supports dynamic API key input via the sidebar for privacy.

## 🛠️ Tech Stack
* **Frontend:** [Streamlit](https://streamlit.io/)
* **AI Model:** [Anthropic Claude 3.5 Opus](https://www.anthropic.com/claude)
* **Backend:** Python
* **Deployment:** Localhost (via Streamlit)

## 🚀 Getting Started

### Prerequisites
Ensure you have Python installed on your system. You will also need an **Anthropic API Key**.

### Installation
1. **Clone the repository:**
   git clone:
   ```bash
   https://github.com/T786-eng/Py2Java-AI-Migrator--LLM-Powered-Python-to-Java-Converter.git
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application:**
    ```bash
    streamlit run app.py
    ```

### How to Use
1. **Enter your Anthropic API Key** in the sidebar.
2. **Paste your Python code** into the text area.
3. **Click "Convert to Java"**.
4. **Preview the generated code** and click **"Download Java File"** to save it.

---

### 📁 Project Structure
* **app.py**: The main Streamlit interface and application logic.
* **converter.py**: Logic for communicating with the Claude API and post-processing the output.
* **requirements.txt**: List of necessary Python libraries including streamlit and anthropic.

