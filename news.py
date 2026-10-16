import tkinter as tk
from dotenv import load_dotenv
import requests
import trafilatura
import os
import pprint

from SCWindow import SCWindow, runIfLocal

class ArticleWindow(SCWindow):
    def __init__(self, text, parent=None, title = 'Stellar Client Article', geometry = "900x700", periodicRate = 1, doesPeriodic = True):
        super().__init__(parent, f"{title} (Stellar Client Article)", geometry, periodicRate, doesPeriodic)
        self.text = text
    
    def createCustomWidgets(self, mainFrame):
        self.articleFrame = tk.Frame(
            mainFrame,
            bg='white'
        )
        self.articleFrame.pack(fill='x', pady=(0, 10))

        self.textBox = tk.Text(
            self.articleFrame,
            font=(
                'Arial',
                14
            ),
            bg='white',
            fg='black',
            state='normal',
            wrap=tk.WORD,
            width=100,
            height=200,
        )
        self.textBox.pack(pady=(0, 10))
        self.textBox.config(state='normal')
        self.textBox.insert("1.0", self.text)
        self.textBox.config(state='disabled')

class NewsWindow(SCWindow):
    def __init__(self, parent=None, title='Stellar Client News', geometry="800x800"):
        super().__init__(parent, title, geometry)
        self.articleButtons = []
        self.articleWindows = []
    
    def createCustomWidgets(self, mainFrame):
        self.newsFrame = tk.Frame(
            mainFrame,
            bg='white'
        )
        self.newsFrame.pack(fill='x', pady=(0, 10))

        title = tk.Label(
            self.newsFrame,
            font=(
                'Castellar',
                30
            ),
            bg='white',
            fg='black',
            state='normal',
            text="News"
        )
        title.pack(pady=(0, 10))

        self.searchBox = tk.Text(
            self.newsFrame,
            font=(
                'Arial',
                14
            ),
            bg='white',
            fg='black',
            state='normal',
            wrap=tk.WORD,
            width=30,
            height=2
        )
        self.searchBox.pack(pady=(0, 10))

        self.searchButton = tk.Button(
            self.newsFrame,
            font=(
                'Arial',
                16
            ),
            bg='white',
            fg='black',
            text="Search",
            command=self.search         
        )
        self.searchButton.pack(pady=(0, 10))
            
    def makeArticleWindow(self, title, url):
        print(url)
        dt = self.getArticleData(url)
        for i in self.articleWindows:
            if i.text == dt:
                i.show()
                return
        self.articleWindows.append(
            ArticleWindow(dt, title=title, parent=self.window)
        )
        self.articleWindows[len(self.articleWindows) - 1].show()

    def getArticleData(self, url:str):
        article = requests.get(url).text
        return trafilatura.extract(article)

    def compileSources(self):
        load_dotenv()

        NEWS_KEY = os.getenv("NEWS_KEY")

        if NEWS_KEY == None:
            raise LookupError("News key is None")
        dt = (requests.get(f"https://gnews.io/api/v4/search?apikey={NEWS_KEY}&q={self.searchBox.get('1.0', tk.END).replace(" ", "_")}&lang=en&max=10&in=title,description")).json()
        options = []
        optionsStr = ""
        # pprint.pprint(dt)
        for i in dt["articles"]:
            options.append((i["title"], i["url"]))
            optionsStr += f'{i["title"]}, {i["url"]}\n'
        return options

    def search(self):
        for i in range(len(self.articleButtons)):
            self.articleButtons[i].destroy()
        self.articleButtons = []
        self.window.children.clear()
        options = self.compileSources()
        for i in range(len(options)):
                self.newsFrame,
                self.articleButtons.append(
                    tk.Button(
                        self.newsFrame,
                        font=(
                            'Arial',
                            16
                        ),
                        bg='white',
                        fg='black',
                        text=options[i][0],
                        command= lambda article=options[i]: self.makeArticleWindow(article[0], article[1])                         
                    )
                )
                self.articleButtons[i].pack(pady=(0, 10))
            

    # def onStart(self):
    #     self.update()


runIfLocal(NewsWindow, __name__)