from googletrans import Translator

def translate_text(input_text, target_language):
    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(input_text, dest=target_language)
    return translation.text


input_text = input("Enter the text to translate: ")
target_language = input("Enter the target language code (e.g., fr for French): ")

translated_text = translate_text(input_text, target_language)
print(f"Translation: {translated_text}")
