from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import languages
import threading
import pathlib
import speechTranslate as st
import textToSpeech as tts
import imageInterpreter as ii


# Translates input audio into English
def speechtranslate():
    try:
        targetLang = langVariable.get()
        translatedText = st.recordAudio(targetLang)
        textBox.insert(1.0, translatedText)
        translatebutton.config(text="Translate") 
    except:
         translatebutton.config(text="Translate") 

# Translates text into desired language
def texttranslate():
    
    input = textBox.get("1.0",END)
    lang = langVariable.get()
    result=st.translate(input,lang)
    textBox.delete('1.0', END)
    textBox.insert(1.0, result)

# Calls the speechtranslate while threading
def listen():
    textBox.delete('1.0', END)
    translatebutton.config(text="Listening...") 
    thread = threading.Thread(target=speechtranslate)
    thread.start()
# Changes text to speech
def speak():
   
    language = langVariable.get()
    text = textBox.get("1.0",END)
    if len(text) == 1:
        text = st.translate("No text available",language)
    print(type(text))
    tts.playAudio(language,text)

# Calls translate function upon language change
def change(event):
    input = textBox.get("1.0",END)
    lang = langVariable.get()
    result=st.translate(input,lang)
    textBox.delete('1.0', END)
    textBox.insert(1.0, result)

# upload image fuction
def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)
    result = ii.getTextFromImage(filename)
    lang = langVariable.get()
    result=st.translate(result,lang)
    textBox.delete('1.0', END)
    textBox.insert(1.0, result)
    

    
#path of current file 
path = pathlib.Path(__file__).parent.absolute()

#App icon image 
filename= str(path) + '/images/image.png'

#Window components
window = Tk()
window.iconphoto(False, PhotoImage(file=filename))
window.title("Speech Translate")
window.geometry('400x500')
window.configure(background = "#161d25")
window.resizable(False, False)

#Body Frame
frame = Frame(window,bg = "#161d25",width=400,height=500)
frame.grid(row=0,column=0,sticky="NW")
frame.grid_propagate(0)
frame.update()

OPTIONS = languages.getLanguages()

#Language Button

langVariable = StringVar(frame)
langVariable.set("english") # default value


languageOption = OptionMenu(frame, langVariable, *OPTIONS, command = change)
languageOption.place(x=200, y=20, anchor="center")

languageOption.config(bg = "#161d25",font=("Courier", 15),height = 10, width = 15)


#TextBox

textBox = Text(frame)
textBox.place(x=200, y=150, anchor="center")
textBox.config(font=("Courier", 15),height = 12,width = 40)



#Speech Translate Button
iconFile = str(path) + '/images/icon.png'
photo = PhotoImage(file = iconFile)
speechbutton = Button(frame, text="Speech Translate", image = photo , command=listen)
speechbutton.place(x=200, y=290, anchor="center")
speechbutton.config(fg = "#161d25",font=("Courier", 15),height = 50, width = 50)

#Text Translate Button
translatebutton = Button(frame, text="Translate", command=texttranslate)
translatebutton.place(x=120, y=350, anchor="center")
translatebutton.config(fg = "#161d25",font=("Courier", 15),height = 2, width = 16)

#Play Audio Button
Audiobutton = Button(frame, text="Play Audio", command=speak)
Audiobutton.place(x=280, y=350, anchor="center")
Audiobutton.config(fg = "#161d25",font=("Courier", 15),height = 2, width = 16)

#Upload Image Button
imageButton = Button(frame, text="Image Upload", command=UploadAction)
imageButton.place(x=200, y=420, anchor="center")
imageButton.config(fg = "#161d25",font=("Courier", 15),height = 2, width = 16)


window.mainloop()