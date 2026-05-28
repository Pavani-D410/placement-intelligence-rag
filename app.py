import streamlit as st

from src.pipeline import run_pipeline


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

    result = run_pipeline(query)

    st.subheader("Answer")

    st.write(result["answer"])

    st.subheader("Sources")

    for source in result["sources"]:

        st.write(source)