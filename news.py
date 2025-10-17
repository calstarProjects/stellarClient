import tkinter as tk
from newspaper import Article

from SCWindow import SCWindow, runIfLocal

class newsWindow(SCWindow):
    def __init__(self, parent=None, title='Stellar Client News', geometry="800x600"):
        super().__init__(parent, title, geometry)
    
    def createCustomWidgets(self, mainFrame):
        self.newsFrame = tk.Frame(
            mainFrame,
            bg='white'
        )
        self.newsFrame.pack(fill='x', pady=(0, 10))
        
        self.articleText = tk.Text(
            self.newsFrame,
            font=(
                'Arial',
                16
            ),
            bg='white',
            fg='black',
            state='disabled',
            wrap=tk.WORD
        )
        self.articleText.pack(pady=(0, 10))

    def getArticleData(self, url:str):
        article = Article(url)
        article.download()
        article.parse()
        # print("**Headline:**", article.title)
        # print("**Authors:**", article.authors)
        # print("**Publication Date:**", article.publish_date)
        # print("**Main Text:**", article.text)

        result = {
            'Title': article.title,
            'Author': article.authors if article.authors != [] else 'No authors detected',
            'Date': article.publish_date,
            'Text': article.text
        }
        return result

    def update(self):
        dt = self.getArticleData('https://www.bbc.com/future/article/20251015-perovskite-the-wonder-material-that-could-transform-solar-energy')
        self.articleText.config(state='normal')
        self.articleText.delete('1.0', tk.END)
        self.articleText.insert(
            '1.0',
            f'**{dt['Title']}**\n*{dt["Author"]}*\nDate: {dt["Date"]}\n{dt["Text"]}'
        )
        self.articleText.config(state='disabled')
    
    def onStart(self):
        self.update()


runIfLocal(newsWindow, __name__)