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

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from templates import TEMPLATES
from dotenv import load_dotenv
import os

load_dotenv()

def generate_email(topic, tone):

    template = TEMPLATES[tone]

    prompt = PromptTemplate(
        input_variables=["topic"],
        template=template
    )

    llm = ChatOpenAI(
        model= "model="deepseek/deepseek-r1:free"",

        base_url="https://openrouter.ai/api/v1",

        api_key=os.getenv("OPENROUTER_API_KEY"),

        temperature=0.7
    )

    chain = prompt | llm

    response = chain.invoke({
        "topic": topic
    })

    return response.content

TEMPLATES = {

    "formal": """
Write a professional formal email.

Topic: {topic}

Include:
- Subject
- Greeting
- Body
- Closing
""",

    "casual": """
Write a casual email.

Topic: {topic}
""",

    "friendly": """
Write a friendly email.

Topic: {topic}
"""
}
