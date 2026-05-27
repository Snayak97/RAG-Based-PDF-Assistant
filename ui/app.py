import streamlit as st
import requests

API_URL = "http://127.0.0.1:8002"

st.set_page_config(
    page_title="ChatPDF",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Chat with PDF")

st.markdown("---")


# Upload section
uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    with st.spinner("Uploading PDF..."):

        response = requests.post(
            f"{API_URL}/upload-pdf",
            files={
                "file": (
                    uploaded_file.name,
                    uploaded_file,
                    "application/pdf"
                )
            }
        )

    st.success("✅ PDF Uploaded Successfully")


st.markdown("---")


# Question section
question = st.text_input(
    "Ask Question"
)

if st.button("Ask AI"):

    with st.spinner("Thinking..."):

        response = requests.post(
            f"{API_URL}/ask",
            json={
                "question": question
            }
        )

        data = response.json()

    # Answer
    st.subheader("🤖 Answer")

    st.write(data["answer"])

    st.markdown("---")

    # Context
    with st.expander("📚 Retrieved Context"):

        for i, chunk in enumerate(data["context"]):

            st.markdown(f"### Chunk {i+1}")

            st.write(chunk)

            st.markdown("---")