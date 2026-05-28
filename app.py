import streamlit as st


st.set_page_config(
    page_title="Placement Intelligence Assistant"
)

st.title(
    "Placement Intelligence Assistant"
)

query = st.text_input(
    "Ask a placement-related question"
)


if query:

    st.write(
        f"Processing query: {query}"
    )

    st.success(
        "RAG pipeline connected successfully."
    )