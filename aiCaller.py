from apiKey import key
import google.generativeai as genAI
import tkinter
import time
import string
import json
import os

from SCWindow import SCWindow, runIfLocal

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


class AIWindow(SCWindow):
    def __init__(self, parent=None, title='Stellar Client AI', geometry="800x600"):
        super().__init__(parent, title, geometry)
        if chat.history != []:
            self.outputBox.config(state='normal')
            for msg in chat.history:
                temp = ''
                for i in msg.parts:
                    if hasattr(i, 'text'):
                        temp += i.text
                self.outputBox.insert(tkinter.END, f'{'USER' if msg.role == 'user' else 'GEMINI'}: {temp.strip().replace('*', '')}\n\n', ('user' if msg.role == 'user' else 'gemini'))
            self.outputBox.config(state='disabled')  
            self.outputBox.see(tkinter.END)

    
    def createCustomWidgets(self, mainFrame):
        frame = tkinter.Frame(mainFrame)
        frame.pack(fill='both', expand=True, padx=10, pady=10)

        # Scrollbar
        scrollbar = tkinter.Scrollbar(frame)
        scrollbar.pack(side='right', fill='y')

        # Text widget for output
        self.outputBox = tkinter.Text(frame, wrap='word', yscrollcommand=scrollbar.set, state='disabled')
        self.outputBox.pack(side='left', fill='both', expand=True)
        self.outputBox.tag_config("user", foreground="blue")
        self.outputBox.tag_config("gemini", foreground="green")


        # Connect scrollbar
        scrollbar.config(command=self.outputBox.yview)

        self.entryBox = tkinter.Text(mainFrame, height=3, width=30)
        self.entryBox.pack(pady=10)
        submitButton = tkinter.Button(mainFrame, text="Submit", command=self.getAIResponce)
        submitButton.pack(pady=5)

        resetButton = tkinter.Button(mainFrame, text="Reset", command=self.resetChat)
        resetButton.pack(pady=5)
        self.entryBox.bind("<Return>", self.keyInput)
        
    def getAIResponce(self):
        entryBoxInput = self.entryBox.get("1.0", tkinter.END).strip()

        hasContent = False

        for char in entryBoxInput:
            if char in string.ascii_letters:
                hasContent = True

        if hasContent:
            result = chat.send_message(entryBoxInput, stream=True)

            self.outputBox.config(state='normal')
            self.outputBox.insert(tkinter.END, f'USER: {entryBoxInput}\n\n', 'user')
            self.outputBox.insert(tkinter.END, f'GEMINI: ', 'gemini')
            # {result.text.strip().replace('*', '')}\n\n
            for i in result:
                self.outputBox.insert(tkinter.END, (i.text.replace('*', '')), 'gemini')
                # print(i.text)
                self.outputBox.update_idletasks()
                self.outputBox.see(tkinter.END)
            self.outputBox.insert(tkinter.END, '\n')
            self.outputBox.config(state='disabled')  
        else:  
            self.outputBox.config(state='normal')
            self.outputBox.insert(tkinter.END, f'GEMINI: :sob:')
            self.outputBox.config(state='disabled')  
        
        self.entryBox.delete("1.0", tkinter.END)

    def keyInput(self, event):
        if event.keysym == 'Return' and not (event.state & 0x0001):
            self.getAIResponce()
            return "break"

    def resetChat(self):
        chat.history.clear()
        self.outputBox.config(state='normal')
        self.outputBox.delete("1.0", tkinter.END)
        self.outputBox.config(state='disabled')

    def onClose(self):
        super().onClose()
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

runIfLocal(AIWindow, __name__)