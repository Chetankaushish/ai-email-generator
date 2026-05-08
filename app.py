import streamlit as st
from email_generator import generate_email

st.set_page_config(page_title="AI Email Generator")

st.title("📧 AI Email Generator")

topic = st.text_area("Enter Email Topic")

tone = st.selectbox(
    "Select Tone",
    ["formal", "casual", "friendly"]
)

if st.button("Generate Email"):

    if topic:

        with st.spinner("Generating Email..."):

            result = generate_email(topic, tone)

            st.success("Email Generated!")

            st.text_area(
                "Generated Email",
                result,
                height=300
            )

    else:
        st.warning("Please enter topic")
        
