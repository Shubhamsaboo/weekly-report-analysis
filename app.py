import streamlit as st
import openai

# Set up the OpenAI API key and credentials
openai.api_key = st.secrets("API_KEY")

st.title("Weekly Report Analysis 🗂️")
st.image("logo.png")

st.subheader("Report Summary 📚")
# Create a text input field for the user to enter text
text = st.text_area("Weekly Report goes here 👇", height=150)

# Create a button that the user can click to generate a summary
if st.button("Summarize"):
    # Use the GPT-3 model to generate a summary of the text
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Summarize the weekly reports from all the employees into one concise and easy-to-read report to be sent to David Bennett. Make sure to summarize the report in 3-4 bullet points: \n {text}",
        max_tokens=250,
        temperature=0.6,
        best_of=2,
    )

    # Display the summary
    st.write(response["choices"][0]["text"], font_size=18, font_weight="bold")

st.subheader("Question Answering Bot 🤖")

question_text = st.text_input("Ask a question about the weekly report 👇")

if st.button("Ask a question"):
    # Use the GPT-3 model to create a Q&A bot
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Answer the following questions in brief and to the point by taking the context from the given text. Try to answer the questions in a listicle format and make the Q/A bot responses personalized for David Bennett who recevies the weekly report from each of his reportee: \n {text} \n Q: {question_text} \n A:",
        max_tokens=250,
        temperature=0.7,
    )

    # Display the Answers 
    st.write(response["choices"][0]["text"], font_size=18, font_weight="bold")

# Add a custom font to the page
st.markdown(
    """
    <style>
        body {
            font-family: "Lato", sans-serif;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Add a footer with a link to the company website
st.markdown(
    """
    ---
    © Powered by [Tenstorrent](https://tenstorrent.com)
    """
)
