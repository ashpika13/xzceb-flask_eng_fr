from deep_translator import MyMemoryTranslator

def englishtofrench(english_text):
    """Convert english text to french"""
    french_text = MyMemoryTranslator(source='en-US', target='fr-FR').translate(english_text)
    print(french_text)
    return french_text

def frenchtoenglish(french_text):
    """Convert french text to english text"""
    english_text = MyMemoryTranslator(source='fr-FR', target='en-US').translate(french_text)
    print(english_text)
    return english_text
