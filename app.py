import streamlit as st
import speech_recognition as sr

def main():
    st.title("Speech-to-Text App")
    st.write("Click the button and start speaking. The app will display what it hears.")

    r = sr.Recognizer()

    if st.button("Start Listening"):
        with st.spinner("Listening..."):
            try:
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)

                # Use Google Web Speech API for recognition
                text = r.recognize_google(audio)
                st.success("You said:")
                st.write(text)

            except sr.UnknownValueError:
                st.error("Sorry, I could not understand the audio.")
            except sr.RequestError as e:
                st.error(f"Could not request results from Google Speech Recognition service; {e}")
            except Exception as e:
                st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()