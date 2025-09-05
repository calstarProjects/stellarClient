from apiKey import key
import google.generativeai as genAI
import tkinter
import time
import string
import json
import os

allOldChats = []
with open('chatHistory.txt', 'r', encoding='utf-8') as f:
    try:
        allOldChats = json.load(f)
    except:
        pass

genAI.configure(api_key=key)
model = genAI.GenerativeModel()
if allOldChats != []:
    chat = model.start_chat(history=allOldChats)
else:
    chat = model.start_chat(history=[])
    

def getAIResponce():
    entryBoxInput = entryBox.get("1.0", tkinter.END).strip()

    hasContent = False

    for char in entryBoxInput:
        if char in string.ascii_letters:
            hasContent = True

    if hasContent:
        result = chat.send_message(entryBoxInput, stream=True)

        outputBox.config(state='normal')
        outputBox.insert(tkinter.END, f'USER: {entryBoxInput}\n\n', 'user')
        outputBox.insert(tkinter.END, f'GEMINI: ', 'gemini')
        # {result.text.strip().replace('*', '')}\n\n
        for i in result:
            outputBox.insert(tkinter.END, (i.text.replace('*', '')), 'gemini')
            # print(i.text)
            outputBox.update_idletasks()
            outputBox.see(tkinter.END)
        outputBox.insert(tkinter.END, '\n')
        outputBox.config(state='disabled')  
    else:  
        outputBox.config(state='normal')
        outputBox.insert(tkinter.END, f'GEMINI: :sob:')
        outputBox.config(state='disabled')  
    
    entryBox.delete("1.0", tkinter.END)



root = tkinter.Tk()
root.title("AI Wrapper")
root.geometry('1000x500')

frame = tkinter.Frame(root)
frame.pack(fill='both', expand=True, padx=10, pady=10)

# Scrollbar
scrollbar = tkinter.Scrollbar(frame)
scrollbar.pack(side='right', fill='y')

# Text widget for output
outputBox = tkinter.Text(frame, wrap='word', yscrollcommand=scrollbar.set, state='disabled')
outputBox.pack(side='left', fill='both', expand=True)
outputBox.tag_config("user", foreground="blue")
outputBox.tag_config("gemini", foreground="green")


# Connect scrollbar
scrollbar.config(command=outputBox.yview)

entryBox = tkinter.Text(root, height=3, width=30)
entryBox.pack(pady=10)

def keyInput(event):
    if event.keysym == 'Return' and not (event.state & 0x0001):
        getAIResponce()
        return "break"

entryBox.bind("<Return>", keyInput)

submitButton = tkinter.Button(root, text="Submit", command=getAIResponce)
submitButton.pack(pady=5)

if chat.history != []:
    outputBox.config(state='normal')
    for msg in chat.history:
        temp = ''
        for i in msg.parts:
            if hasattr(i, 'text'):
                temp += i.text
        outputBox.insert(tkinter.END, f'{'USER' if msg.role == 'user' else 'GEMINI'}: {temp.strip().replace('*', '')}\n\n', ('user' if msg.role == 'user' else 'gemini'))
    outputBox.config(state='disabled')  
    outputBox.see(tkinter.END)


root.mainloop()

jsonHistory = []
for msg in chat.history:
    msgDict = {
        'role': msg.role,
        'parts': []
    }

    for part in msg.parts:
        if hasattr(part, 'text'):
            msgDict['parts'].append({'text': part.text})
    jsonHistory.append(msgDict)

with open('chatHistory.txt','w') as f:
    json.dump(jsonHistory, f, ensure_ascii=False, indent=2)