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
        model="openai/gpt-3.5-turbo",

        base_url="https://openrouter.ai/api/v1",

        api_key=os.getenv("OPENROUTER_API_KEY"),

        temperature=0.7
    )

    chain = prompt | llm

    response = chain.invoke({
        "topic": topic
    })

    return response.content
