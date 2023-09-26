import nltk
import speech_recognition as sr


class speechText:
    nltk.download("punkt")
    nltk.download("stopwords")
    nltk.download("wordnet")

    def recognize_speech(self):
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            print("Please speak the scenario requirement for generating feature file ...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=10)

        try:
            # Recognize speech using Google Web Speech API
            spoken_text = recognizer.recognize_google(audio)
            print(spoken_text)
            return spoken_text

        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")

        except sr.RequestError as e:
            print(f"Could not request results; {e}")
