import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS

# Page Title
st.title("🌍 AI Language Translation Tool")

# Supported Languages
languages = {
    "English": "en",
    "Hindi": "hi",
    "Bengali": "bn",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja"
}

# User Input
text = st.text_area("Enter Text")

# Source Language
source = st.selectbox(
    "Source Language",
    languages.keys()
)

# Target Language
target = st.selectbox(
    "Target Language",
    languages.keys()
)

# Translate Button
if st.button("Translate"):

    if text.strip() == "":
        st.warning("Please enter some text.")

    else:

        # Translation
        translated_text = GoogleTranslator(
            source=languages[source],
            target=languages[target]
        ).translate(text)

        # Show Result
        st.write("### Translated Text")
        st.success(translated_text)

        # Copy Feature
        st.code(translated_text)

        # Text To Speech
        tts = gTTS(
            text=translated_text,
            lang=languages[target]
        )

        tts.save("translated_audio.mp3")

        audio_file = open(
            "translated_audio.mp3",
            "rb"
        )

        st.audio(audio_file.read())