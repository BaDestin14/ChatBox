
import streamlit as st
import speech_recognition as sr

st.title("Voice-Enabled Chatbot")

user_text_input = st.text_input("Type your message here:")

voice_input_button = st.button("Speak")

response_placeholder = st.empty()

def speech_to_text():
    """Converts speech input from the microphone to text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...") # Visual feedback
        try:
            audio = r.listen(source)
            st.write("Processing...") # Visual feedback
            text = r.recognize_google(audio)
            st.write(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            st.write("Could not understand audio")
            return None
        except sr.RequestError as e:
            st.write(f"Could not request results from Google Speech Recognition service; {e}")
            return None

def get_chatbot_response(input_text):
    """
    Generates a chatbot response based on text input.

    Args:
        input_text: The user's input as a string.

    Returns:
        A string containing the chatbot's response.
    """
    if input_text:
        # Simple rule-based chatbot logic
        if "hello" in input_text.lower():
            return "Hi there!"
        elif "how are you" in input_text.lower():
            return "I'm a bot, so I don't have feelings, but I'm ready to help!"
        elif "bye" in input_text.lower():
            return "Goodbye!"
        elif "what is this" in input_text.lower():
             return "This is a simple chatbot example."
        else:
            return "I'm not sure how to respond to that."
    else:
        return "No input received."


# Handle user input
if user_text_input:
    response = get_chatbot_response(user_text_input)
    with response_placeholder.container():
        st.write("Chatbot:")
        st.write(response)

if voice_input_button:
    transcribed_text = speech_to_text()
    if transcribed_text:
        response = get_chatbot_response(transcribed_text)
        with response_placeholder.container():
            st.write("Chatbot:")
            st.write(response)
    else:
        with response_placeholder.container():
            st.write("Chatbot:")
            st.write("Sorry, I couldn't process your voice input.")
