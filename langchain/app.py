import streamlit as st

from transformers import pipeline
from components.text_splitter import create_recursive_text_splitter
from models.langchain_models.summarization_langchain import *


def main():
    st.title("Langchain Test Page")
    st.subheader('Summarize Text')

    # 텍스트 요약
    text_to_summarize = st.text_area("요약할 텍스트를 입력하세요.", height=250)
    if st.button("Summarize"):
        if not text_to_summarize.strip():
            st.warning("Please enter some text to summarize.")
        else:
            try:
                with st.spinner("Please wait..."):
                    # Split the source text
                    text_splitter = create_recursive_text_splitter()
                    texts = text_splitter.split_text(text_to_summarize)

                    summary = summarize_text(text_to_summarize)
                    st.success(summary)
            except Exception as e:
                st.exception(f"An error occurred: {e}")

    # HTML 파일에서 쿼리 날리기

if __name__ == "__main__":
    main()

# streamlit run app.py --server.port 8888