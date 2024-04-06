import pyttsx3
txt_sp=pyttsx3.init()
#text=input('enter the txt...\n')
#txt_sp.say(text)
#txt_sp.runAndWait()


import pyttsx3
txt_sp=pyttsx3.init()
voices=txt_sp.getProperty('voices')
for i in voices:
    print('ID:',i.id)
text=input('enter the txt...\n')
txt_sp.say(text)
txt_sp.runAndWait()
