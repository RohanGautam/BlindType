import os
from tkinter import Tk, PhotoImage, Menu, Frame, Text, Scrollbar, IntVar,StringVar, BooleanVar, Button, END, Label, INSERT
import tkinter.filedialog
import tkinter.messagebox

import tkinter.font as tkFont

#to make shit clearer
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)



# for speech:
import threading
import pyttsx3
engine = pyttsx3.init('sapi5')
engine.setProperty('rate',200)
#function to interrupt
#def onWord(name, location, length):
#   print ('word', name, location, length)
#   if on_content_changed('onWord'):
#      engine.stop()
#engine = pyttsx.init()
#engine.connect('started-word', onWord)




#creating files, assigning its path and other variables
f=open('dummy.txt','w+')
f.close()
file_name='dummy.txt'
filepath='dummy.txt'
file_name2=file_name
PROGRAM_NAME = "BlindType"

root = Tk()
root.state('zoomed')
root.title(PROGRAM_NAME)

def say(thing):    
    engine.say(thing)
    engine.runAndWait()


threads=[]
def on_content_changed(event=None,src=''):
#    if src=='onWord':return True
    key=repr(event.char)
    print('Change',key)
    if key='\x08':key='Back'
    # threadobj=threading.Thread(target=say,args=[key])
    # threads.append(threadobj)
    # threadobj.start()

    

def exit_editor(event=None):
    save()
    root.destroy()


def write_to_file(file_name):
    try:
        content = content_text.get(1.0, 'end')
        with open(file_name, 'w') as the_file:
            the_file.write(content)
    except IOError:
        tkinter.messagebox.showwarning("Save", "Could not save the file.")


def save_as(event=None):
    input_file_name = tkinter.filedialog.asksaveasfilename(defaultextension=".txt",
                                                           filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if input_file_name:
#        global file_name
        file_name = input_file_name
        write_to_file(file_name)
        root.title('{} - {}'.format(os.path.basename(file_name), PROGRAM_NAME))
    return "break"


def save(event=None):
    global file_name
    if not file_name:
        save_as()
    else:
        write_to_file(file_name)
    return "break"




customFont = tkFont.Font(family="Consolas", size=12)

line_number_bar = Text(root, width=4, padx=3, takefocus=0,  border=0,
                       background='khaki', state='disabled',  wrap='none')

content_text = Text(root, wrap='word', undo=1,insertbackground='white',font=customFont)
content_text.pack(expand='yes', fill='both')
scroll_bar = Scrollbar(content_text)
content_text.configure(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=content_text.yview)
scroll_bar.pack(side='right', fill='y')
content_text.config(background='#000000', fg='#FFFFFF')

content_text.bind('<Control-S>', save)
content_text.bind('<Control-s>', save)

#The keys we want to associate with change
#http://www.tcl.tk/man/tcl8.4/TkCmd/keysyms.htm

s=list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
L=['space', 'exclam', 'quotedbl', 'numbersign', 'dollar', 'percent', 'ampersand', 'quoteright', 'parenleft', 'parenright', 'asterisk', 'plus', 'comma', 'minus', 'period', 'slash', '0', 'colon', 'semicolon', 'less', 'equal', 'greater', 'question', 'at', 'bracketleft', 'backslash', 'bracketright', 'asciicircum', 'underscore', 'quoteleft','BackSpace','Return']+s
for i in L:
    content_text.bind('<Key-{}>'.format(i), on_content_changed)

with open(filepath) as _file:
    content_text.insert(1.0, _file.read())

content_text.focus_set()

root.protocol('WM_DELETE_WINDOW', exit_editor)
root.mainloop()
