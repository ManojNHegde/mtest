import streamlit as st
import speech_recognition as sr

def main():
    st.title("Speech to Text App")

    if st.button("Start Listening"):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            st.write("Listening...")
            audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            st.write("You said: ", text)
        except sr.UnknownValueError:
            st.write("Could not understand audio")
        except sr.RequestError as e:
            st.write(f"Could not request results; {e}")

if __name__ == "__main__":
    main()
