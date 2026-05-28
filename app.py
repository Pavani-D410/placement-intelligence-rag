import streamlit as st

from src.pipeline import run_pipeline


st.set_page_config(
    page_title="Placement Intelligence Assistant",
    layout="wide"
)


st.title(
    "Placement Intelligence Assistant"
)


if "messages" not in st.session_state:

    st.session_state.messages = []


for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )

        if (
            message["role"] == "assistant"
            and "sources" in message
        ):

            if message["sources"]:

                st.markdown("### Sources")

                for source in message["sources"]:

                    st.info(source)


prompt = st.chat_input(
    "Ask a placement-related question"
)


if prompt:

    st.session_state.messages.append({

        "role": "user",
        "content": prompt
    })


    with st.chat_message("user"):

        st.markdown(prompt)


    with st.chat_message("assistant"):

        with st.spinner(
            "Thinking..."
        ):

            result = run_pipeline(prompt)

            answer = result["answer"]

            sources = result["sources"]


        st.markdown(answer)


        if sources:

            st.markdown("### Sources")

            for source in sources:

                st.info(source)


    st.session_state.messages.append({

        "role": "assistant",
        "content": answer,
        "sources": sources
    })