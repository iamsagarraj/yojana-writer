import streamlit as st
import requests

DEESEEK_API_KEY = st.secrets["DEEPSEEK_API_KEY"]

def generate_content(prompt):
    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {DEESEEK_API_KEY}"
    }
    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "तू एक अनुभवी योजना लेखक आहेस. वापरकर्त्याला हवी ती योजना लिहून दे."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=data)
    result = response.json()
    return result["choices"][0]["message"]["content"]
