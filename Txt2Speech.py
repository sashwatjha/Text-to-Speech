#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pyttsx
from pyttsx.drivers import sapi5

print("\n\t███████╗     ██╗\n\t██╔════╝     ██║\n\t███████╗     ██║\n\t╚════██║██   ██║\n\t███████║╚█████╔╝\n\t╚══════╝ ╚════╝\n")

engine = pyttsx.init()

voice = engine.getProperty('voices')

# In[4]:


def voiceType():
    o = input("\n\tPress 0 for Male Voice.\n\tPress 1 for Female Voice.\n\tPress 2 to Exit.\nEnter: ")
    if ((o == '0')or(o == '1')or(o == '2')):
        return o
    else:
        print("Wrong Input")
        return voiceType()
        
def speak(str):
    engine.say(str)


# In[8]:
type = 1
while (type == 1 or type == 0):

    type = int(voiceType())
    if type==2 :
        break
    engine.setProperty('voice',voice[type].id)
    engine.setProperty('rate', 140)
    say = input("Write Something: ")
    speak(say)
    engine.runAndWait()




