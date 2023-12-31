import streamlit as st
from langchain.llms import OpenAI
from langchain import PromptTemplate

st.set_page_config(page_title="🦜🔗Blog Outline Generator APP")
st.title("🦜🔗Blog Outline Generator APP")


def generate_response(topic):
  llm = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")
  # Prompt
  template = '経験豊富なデータサイエンティストとして、またテクニカルライターとして、次のようなブログのアウトラインを作成してください。 {topic}.'
  prompt = PromptTemplate(input_variables=['topic'], template=template)
  prompt_query = prompt.format(topic=topic)
  # Run LLM model and print out response
  response = llm(prompt_query)
  return st.info(response)

with st.form('myform'):
  topic_text = st.text_input('Enter keyword:', '')
  submitted = st.form_submit_button('Submit')
  generate_response(topic_text)
