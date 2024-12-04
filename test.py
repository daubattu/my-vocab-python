from googletrans import Translator
import eng_to_ipa as ipa

translator = Translator()
    
translated = translator.translate("This file contains metadata about your extension, including its name, version, permissions, and the background scripts it will use.", src='en', dest='vi')

print(translated.text)
print(ipa.convert('name'))
print(ipa.convert('jump'))
print(ipa.convert('mother'))