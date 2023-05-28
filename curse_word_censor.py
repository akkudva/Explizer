import whisper
import os
import string
import contractions
import tkinter as tk


model = whisper.load_model("small.en")

foldername = r"D:\nlp project"

c_words=[]
with open(r"D:\nlp project\curse_words.txt") as f:
       words = f.readlines()

       for word in words:
              c_words.append(word.rstrip())


def audio_input(audio_path):
       result = model.transcribe(audio_path)
       return result["text"]



def audio_file(f_path):
       text = audio_input(f_path)
              
       filename=input("Enter the txt file name:- ")+".txt"
              
       filepath = os.path.join(foldername, filename)
              
       text = clean_audio(text)
              
       with open(filepath, 'w') as r:
              r.write(text)


def recording():
       import audio_recorder as arc
       f_path = arc.op_fn_mp3
       text = audio_input(f_path)

       text = clean_audio(text)

       filename=input("Enter the txt file name:- ")+".txt"
              
       filepath = os.path.join(foldername, filename)

              
       with open(filepath, 'w') as r:
              r.write(text)



def clean_audio(text):
       text = text.translate(str.maketrans("","",string.punctuation))
       text = contractions.fix(text)
       text=text.lower()
       text_list=text.split()
       for i in range(len(text_list)):
             if text_list[i] in c_words:
                     text_list[i] = "*"*len(text_list[i])
       return " ".join(text_list)              

       
while(True):
       ch=int(input("1.Audio file\t 2.microphone input\n"))
        
       if ch==1:
              x=input("Enter file path:- ")
              audio_file(x)

       if ch==2:
              recording()

       if ch==0:
           break          
       
              

          

