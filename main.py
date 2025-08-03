import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
import os
from chains import Chain
from portfolio import Portfolio
from utils import clean_text,remove_think_sections
from dotenv import load_dotenv

load_dotenv()


def create_streamlit_app(llm, portfolio, clean_text):
    st.title("📧 Cold Mail Generator")
    url_input = st.text_input("Enter a URL:")
    company_name = st.text_input("Enter your company name : ")
    position = st.text_input("Enter your position : ")
    name = st.text_input("Enter you name : ")
    company_description = st.text_input("Enter your company description (2 to 3 sentences) : ")

    submit_button = st.button("Submit")

    if submit_button: 
        if not url_input or not company_name or not position:
            return st.error("Please fill in all the required fields.")
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)
            for job in jobs:
                  skills = job.get('skills',[])
                  if not isinstance(skills,list):
                        skills = [skills]
                  skills = [str(s) for s in skills if s is not None]
                  links_metadata = portfolio.query_links(skills)
                  link_list = ", ".join(m.get("links", "") for m in links_metadata if m.get("links"))  
                  email = llm.write_mail(company_name, position, name, company_description, job, link_list)
                  email = remove_think_sections(email)  # Clean before display

                  st.code(email, language='markdown')
                
        except Exception as e:
            st.error(f"An Error Occurred: {e}")


# for job in jobs:
#     skills = job.get('skills', [])
#     if not isinstance(skills, list):
#         skills = [skills]
#     # make sure all skill items are strings
#     skills = [str(s) for s in skills if s is not None]
#     links_metadata = portfolio.query_links(skills)
#     # convert metadata to a readable comma-separated list of links
#     link_list = ", ".join(m.get("links", "") for m in links_metadata if m.get("links"))
#     email = llm.write_mail(company_name, position, name, company_description, job, link_list)
#     st.code(email, language='markdown')



# for job in jobs:
#                 skills = job.get('skills', [])
#                 links = portfolio.query_links(skills)
#                 email = llm.write_mail(company_name, position,name, company_description, job, links)
#                 st.code(email, language='markdown')



if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    create_streamlit_app(chain, portfolio, clean_text)

