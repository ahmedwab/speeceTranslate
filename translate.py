from tkinter import *
from tkinter import ttk
import languages
import threading
import speechTranslate as st



def speechtranslate():
    targetLang = langVariable.get()
    translatedText = st.recordAudio(targetLang)
    textBox.insert(1.0, translatedText)
    speechbutton.config(text="Translate") 
def texttranslate():
    
    input = textBox.get("1.0",END)
    lang = langVariable.get()
    result=st.translate(input,lang)
    textBox.delete('1.0', END)
    textBox.insert(1.0, result)


def listen():
    textBox.delete('1.0', END)
    speechbutton.config(text="Listening...") 
    thread = threading.Thread(target=speechtranslate)
    thread.start()
def change(event):
    input = textBox.get("1.0",END)
    lang = langVariable.get()
    result=st.translate(input,lang)
    textBox.delete('1.0', END)
    textBox.insert(1.0, result)
    
    

window = Tk()
window.title("Speech Translate")
window.geometry('400x300')
window.configure(background = "#161d25")
window.resizable(False, False)

#Body Frame
frame = Frame(window,bg = "#161d25",width=400,height=400)
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
speechbutton = Button(frame, text="Speech Translate", command=listen)
speechbutton.place(x=120, y=275, anchor="center")
speechbutton.config(fg = "#161d25",font=("Courier", 15),height = 2, width = 20)

#Text Translate Button
button = Button(frame, text="Translate", command=texttranslate)
button.place(x=290, y=275, anchor="center")
button.config(fg = "#161d25",font=("Courier", 15),height = 2, width = 16)

window.mainloop()