# BlindType
This is an attempt to build a text editor which assists and helps blind people type. At it's core, this program opens a text editor and logs everything typed on it. Depending on the presets, it can be made to say every letter typed out loud, or every word, or every sentence.

This project is still buggy in the sense that the text to speech module (pyttsx3) has an input delay during the part where it says the requested text out loud. It also does not allow it to be a part of another thread, due to which this project is at a roadblock right now.
