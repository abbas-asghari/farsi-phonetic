import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Access your API key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


# Set up your OpenAI API key. You can also use Streamlit's secrets for this.
OPENAI_API_KEY = "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"


st.title('Finglish ⇨ English Translator')

phonetic = st.text_input('Enter farsi phonetic (word or phrase) to translate to English')

if st.button('Translate ⇨ English'):

    client = OpenAI(
        api_key=OPENAI_API_KEY,
    )

    stream = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[{"role": "system", "content": "help me translate the Farsi phonetics to english. Only state the english meaning."}
            ,{"role": "user", "content": phonetic}],
        stream=True,
    )
    write_stream = ""
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            write_stream += chunk.choices[0].delta.content
    
    st.write(write_stream)

st.divider()

st.title('English ⇨ Finglish Translator')

english = st.text_input('Enter English (word or phrase) to translate to Finglish')

if st.button('Translate ⇨ Finglish'):
    # Make an API call to OpenAI's GPT-3
    # response = openai.Completion.create(
    #     engine="gpt-4-0125-preview", # Or any other available engine
    #     prompt=phonetic,
    #     temperature=0.7,
    #     max_tokens=150
    # )

    # # Display the generated text
    # st.text_area("Generated Text", response.choices[0].text, height=250)


    client = OpenAI(
        api_key=OPENAI_API_KEY,
    )

    stream = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[{"role": "system", "content": "help me translate this to Farsi in phonetics. Only state the phonetics."}
            ,{"role": "user", "content": english}],
        stream=True,
    )
    write_stream = ""
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            write_stream += chunk.choices[0].delta.content
    
    st.write(write_stream)