import tkinter as tk

from SCWindow import SCWindow, runIfLocal

def isSorted(lis:list):
    for i in range(len(lis)-1):
        if type(lis[i]) != type(lis[i+1]) or lis[i] > lis[i+1]:
            return False
    else:
        return True

def bubSort(lis: list):
    lists = []
    for i in lis:
        for j in lists:
            if type(j[0]) == type(i):
                j.append(i)
                break
        else:
            lists.append([i])
    for j in lists:
        while not isSorted(j):
            for i in range(len(j)-1):
                if j[i] > j[i+1]:
                    j[i], j[i+1] = j[i+1], j[i]
    finalList = []
    for i in lists:
        for j in i:
            finalList.append(j)
    return finalList

def qSort(lis: list):
    lists = []
    for i in lis:
        for j in lists:
            if type(j[0]) == type(i):
                j.append(i)
                break
        else:
            lists.append([i])
    def pivotSplit(lis2: list):
        result = []
        pivot = lis2.pop(len(lis2)//2)
        l1 = []
        l2 = []
        for i in lis2:
            if i < pivot:
                l1.append(i)
            else:
                l2.append(i)
        if len(l1) > 0:
            result.append(l1)
        result.append(pivot)
        if len(l2) > 0:
            result.append(l2)
        return result
    for k in lists:
        duck = pivotSplit(k)
        while not isSorted(duck):
            for i in duck:
                if type(i) == list:
                    pos = duck.index(i)
                    result = pivotSplit(duck.pop(pos))
                    for j in result:
                        duck.insert(pos + result.index(j), j)
        lists[lists.index(k)] = duck
    
    finalList = []
    for i in lists:
        for j in i:
            finalList.append(j)
    return finalList

class sortingPage(SCWindow):
    def __init__(self, parent=None, title='Stellar Client Sorter', geometry="800x600"):
        super().__init__(parent, title, geometry)

    def createCustomWidgets(self, mainFrame):
        sortingHeaderFrame = tk.Frame(mainFrame, bg='white')
        sortingHeaderFrame.pack(fill='x', pady=(0, 10))

        sortingHeader = tk.Label(
            sortingHeaderFrame,
            text='Sorting',
            font=(
                'Castellar',
                16,
                'bold'
            ),
            bg='white',
            fg='black'
        )
        sortingHeader.pack()

        contentFrame = tk.Frame(mainFrame)
        contentFrame.pack(fill='x', pady=(0, 10))

        self.listInputBox = tk.Text(
            contentFrame,
            font=(
                'Cascadia Code',
                12
            ),
            bg='lightgray',
            fg='black',
            height=2
        )
        self.listInputBox.pack(pady=(0, 10))

        sortButton = tk.Button(
            contentFrame,
            font=(
                'Cascadia Code',
                12
            ),
            text="↓ Sort ↓",
            bg='gray',
            fg='black',
            height=2,
            command=self.sortBox
        )
        sortButton.pack(pady=(0, 10))

        self.outputBox = tk.Text(
            contentFrame,
            font=(
                'Cascadia Code',
                12
            ),
            bg='lightgray',
            fg='black',
            height=2
        )
        self.outputBox.pack(pady=(0, 10))
        self.outputBox.config(state='disabled')

    
    def sortBox(self):
        iLis = self.listInputBox.get('1.0', tk.END).strip().split(',')

        newLis = []
        for item in iLis:
            item = item.strip().strip("'")
            if item.isdigit():
                newLis.append(int(item))
            else:
                newLis.append(item)
        lis = qSort(newLis)
        sLis = ''
        for i in lis:
            if type(i) == str and i != '' and i != ' ' and i != None:
                sLis += f', {i.strip()}'
            else:
                sLis += f', {i}'
        self.outputBox.config(state='normal')
        self.outputBox.delete("1.0", tk.END)
        self.outputBox.insert("1.0", str(sLis).strip('[').strip(']'))
        self.outputBox.config(state='disabled')


runIfLocal(sortingPage, __name__)