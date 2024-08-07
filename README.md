# Speech Translation and Synthesis

This project provides speech recognition, language detection, translation, and speech synthesis. It uses various libraries and models to convert spoken language into text, detect the language, translate it into another language, and finally convert the translated text back into speech.

## Features

- **Speech Recognition**: Converts spoken language into text using Google's speech recognition API.
- **Language Detection**: Automatically detects whether the input language is English or Persian.
- **Translation**: Translates the recognized text between English and Persian using [Facebook's mBART model](https://huggingface.co/facebook/mbart-large-50-many-to-many-mmt).
```python
model_name = 'facebook/mbart-large-50-many-to-many-mmt'
tokenizer = AutoTokenizer.from_pretrained(model_name) # or MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
model = AutoModelForCausalLM.from_pretrained(model_name)
```
- **Speech Synthesis**: Converts the translated text back into speech using Google's Text-to-Speech API.

## Requirements

To run code.py, you need to install the following Python libraries:

- `os`
- `gtts`
- `pyaudio`
- `speech_recognition`
- `transformers`

You can install the required libraries using pip:

```python
!pip install os gtts pyaudio speechrecognition transformers
```

## Code Overview

Here's a brief overview of the main functions:

- `detect_language(text)`: Detects the language of the input text.
- `speech_to_text()`: Listens to the microphone and converts spoken language into text.
- `translate_text(text, src_lang, dest_lang)`: Translates the input text from the source language to the destination language.
- `text_to_speech(text, lang)`: Converts the input text into speech in the specified language.

## Notes

- Ensure that your microphone is properly set up and functioning.
- An internet connection is required for speech recognition and translation.
- The script currently supports English and Persian languages.

## License

This project is licensed under the MIT License.

## Acknowledgements

- [Google Text-to-Speech](https://pypi.org/project/gTTS/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [Transformers by Hugging Face](https://huggingface.co/transformers/)
