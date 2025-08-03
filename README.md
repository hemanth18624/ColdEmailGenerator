# 📧 Cold Email Generator

A **smart and AI-powered cold email generation tool** that helps companies craft personalized outreach emails to their clients, based on job postings scraped from their websites.  

This tool integrates **DeepSeek R1 Distill LLaMA 70B** for high-quality content generation, combined with **ChromaDB** for efficient semantic retrieval of portfolio website links to be included in the email.  

Designed with a clean **Streamlit UI**, powered by **LangChain** for LLM orchestration, and accelerated with **Groq** for faster inference — making cold email creation seamless, personalized, and efficient.  

---

## 🚀 Features

- **AI-Powered Email Generation** – Automatically creates cold emails tailored to specific job postings.
- **Portfolio Showcase Integration** – Dynamically fetches and embeds portfolio website links from a **ChromaDB** vector database.
- **Semantic Search & Retrieval** – Efficiently finds the most relevant portfolio items to showcase for each email.
- **Interactive UI** – Built with **Streamlit** for an easy-to-use and responsive interface.
- **Faster LLM Execution** – Powered by **Groq** for low-latency and high-performance text generation.
- **Modular & Scalable** – Built using **LangChain** for flexible LLM workflow design.

---

## 🛠 Tech Stack

| Component | Technology |
|-----------|------------|
| **LLM Model** | DeepSeek-R1-Distill-LLaMA-70B |
| **Vector Database** | ChromaDB |
| **UI Framework** | Streamlit |
| **LLM Orchestration** | LangChain |
| **Performance Acceleration** | Groq |
| **Backend Language** | Python |

---

## 📂 Project Structure

```plaintext
Cold-Email-Generator/
│
├── app.py                 # Main Streamlit application
├── chains/                # LangChain pipeline scripts
├── portfolio/             # Portfolio data handling
├── utils/                 # Helper functions
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
