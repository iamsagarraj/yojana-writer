import streamlit as st
import openai

st.set_page_config(page_title="🧠 Yojana Writer", layout="centered")
st.title("📰 योजना लेखक (हिंदी में)")

openai.api_key = st.secrets["OPENAI_API_KEY"]

title = st.text_input("📌 योजना का शीर्षक दर्ज करें:")

if st.button("✍️ लेख तैयार करें"):
    if title.strip() == "":
        st.warning("कृपया शीर्षक दर्ज करें।")
    else:
        with st.spinner("लेख तैयार किया जा रहा है..."):
            try:
                prompt = f"हिंदी में {title} विषय पर एक विस्तृत योजना लेख 1500 शब्दों में लिखें।"
                response = openai.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7,
                    max_tokens=2000
                )
                article = response.choices[0].message.content
                st.success("✅ लेख तैयार हो गया!")
                st.text_area("📝 लेख:", article, height=400)

            except Exception as e:
                st.error(f"❌ कुछ त्रुटि हुई:\n\n{e}")
