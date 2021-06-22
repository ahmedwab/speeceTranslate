
from gtts import gTTS
import os
import languages as lang
  
  


  
# Changes text to speech
def playAudio(speechLanguage, speechText):
    try:
        language = lang.get_key(speechLanguage)
        myobj = gTTS(text=speechText, lang=language, slow=False)
        myobj.save("translatedAudio.mp3")
        os.system("mpg321 translatedAudio.mp3")
        os.remove("translatedAudio.mp3")
    except:
        myobj = gTTS(text="Language is currently not supported", lang='en', slow=False)
        myobj.save("translatedAudio.mp3")
        os.system("mpg321 translatedAudio.mp3")
        os.remove("translatedAudio.mp3")



