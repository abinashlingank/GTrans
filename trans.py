from googletrans import Translator

def translate_to_english(text,tarlan):
    translator = Translator()
    translation = translator.translate(text, src=tarlan, dest='en')
    return translation.text

# Example usage
def translate_to_tamil(text,tarlan):
    translator=Translator()
    translation=translator.translate(text,src=tarlan,dest='ta')
    return translation.text