from googletrans import Translator

words = input("Type a word you want to translate: ")

wordsArray = words.split(',')

translator = Translator()
translations = translator.translate(wordsArray, dest='en')

for translation in translations:
    print(translation.origin, '->', translation.text)
    
    
    
    