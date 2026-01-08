import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI


# shell: streamlit run main1.py

template = """

You are a job search assistant that helps users find the perfect job. \
You will be given information about the desired vacancies, experience and skills of the user: {user_input}. \

Your goal is to find job search websites on the Internet and find \
vacancies that match the user's desires, experience and skills. Then \
you need to list the vacancies with links to them in order from most \
suitable to least suitable.

YOUR RESPONSE:
"""
prompt = PromptTemplate(template=template, input_variables=["user_input"])

def load_LLM():
    try:
        llm = OpenAI(temperature=.5)
        return llm
    except KeyError:
        st.error("OpenAI API key not found in secrets. Please add it to your secrets.toml file.")
        return None

llm = load_LLM()

st.set_page_config(page_title="JobPilot", page_icon=":robot:")
st.header("Welcome to JobPilot - Job search assistant platform!")

col1, col2 = st.columns(2)

with col1:
    st.markdown("Job hunting often involves constantly browsing different websites to find the right vacancies, \
                and keeping track of your search history and communication with \
                different companies requires additional effort.  \n\n JobPilot now brings everything together\
                in one place and does it for you: all you need to do is enter your desired job vacancies and\
                your information about your experience and skills. \n\n  You receive personalised advice from\
                an AI assistant on any job search question, as well launch an in-depth investigation into\
                companies that interest you with a single click.")

with col2:
    st.image(image='TweetScreenshot.png', width=500, caption='https://twitter.com/DannyRichman/status/1598254671591723008')

st.markdown("### Please enter your desired vacancy, your experience and skills")

def get_text():
    input_text = st.text_input(label="",  placeholder="Desired vacancy, your experience and skills...", key="input_information")
    return(input_text)

input_information = get_text()

if input_information and llm is not None:
    llm_response = llm.invoke(prompt.format(user_input=input_information))
    st.write(llm_response)

