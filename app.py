import streamlit as st
import os
from converter import convert_python_to_java

st.set_page_config(page_title="LLM Code Migrator", page_icon="🚀")

st.title("🚀 AI Code Migration Tool")
st.write("Convert Python code into Java using Claude AI")

# API Key input in sidebar
with st.sidebar:
    api_key = st.text_input("Anthropic API Key", type="password", placeholder="sk-ant-...")
    if api_key:
        os.environ["ANTHROPIC_API_KEY"] = api_key
        st.success("API key set!")
    else:
        st.warning("Enter your Anthropic API key to use the converter")

python_code = st.text_area("Enter Python Code", height=300, placeholder="print('Hello World!')")

if st.button("Convert to Java"):
    if not os.environ.get("ANTHROPIC_API_KEY"):
        st.error("Please enter your Anthropic API key in the sidebar first.")
    elif python_code.strip() == "":
        st.warning("Please enter some Python code")
    else:
        with st.spinner("Converting using Claude AI..."):
            try:
                java_code = convert_python_to_java(python_code)
                st.subheader("Generated Java Code")
                st.code(java_code, language="java")
                st.download_button(
                    label="Download Java File",
                    data=java_code,
                    file_name="ConvertedCode.java",
                )
            except Exception as e:
                st.error(f"Conversion failed: {e}")