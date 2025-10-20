import tkinter as tk

from SCWindow import SCWindow, runIfLocal

class worldInfoScreen(SCWindow):
    def __init__(self, parent=None, title='Stellar Client World Info', geometry="800x600", periodicRate=1):
        super().__init__(parent, title, geometry, periodicRate)