import os
from gtts import gTTS
import speech_recognition as sr
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = 'facebook/mbart-large-50-many-to-many-mmt'
tokenizer = AutoTokenizer.from_pretrained(model_name) # or MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
model = AutoModelForCausalLM.from_pretrained(model_name)

def detect_language(text):
    if any('\u0600' <= char <= '\u06FF' for char in text):
        return 'fa'
    return 'en'

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak:")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("You said: " + text)
            return text
        except sr.UnknownValueError:
            print("Ohh sorry, I did't understand what you said.")
        except sr.RequestError:
            print("500")

def translate_text(text, src_lang, dest_lang):
    tokenizer.src_lang = src_lang
    inputs = tokenizer(text, return_tensors='pt')
    translated_tokens = model.generate(**inputs, forced_bos_token_id=tokenizer.lang_code_to_id[dest_lang])
    translated_text = tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]
    print(f"Translated: {translated_text}")
    return translated_text

def text_to_speech(text, lang):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save("output.mp3")
    os.system("output.mp3")
    os.remove("output.mp3")

def main():
    user_input = speech_to_text()
    if user_input:
        src_lang = detect_language(user_input)
        dest_lang = 'en_XX' if src_lang == 'fa' else 'fa_IR'
        translated_text = translate_text(user_input, src_lang, dest_lang)
        text_to_speech(translated_text, lang='en' if dest_lang == 'en_XX' else 'fa')

main()

