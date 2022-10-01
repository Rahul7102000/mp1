import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
# noinspection PyUnresolvedReferences
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
import pyrebase
from pygame import *
from PyQt5.QtWidgets import *
from playsound import playsound
from PyQt5.QtGui import *
from PyQt5.Qt import *
import webbrowser
from tkinter import *
import pygame

class sss(QMainWindow):
    def __init__(self):
        super(sss, self).__init__()
        loadUi("subah subah song.ui", self)

        #BackButtons
        self.backhomepage.clicked.connect(self.backhomepagefunction)
        self.backcategory.clicked.connect(self.backcategoryfunction)

        # Song 1
        self.play50.clicked.connect(self.playfunction50)
        self.pause50.clicked.connect(self.pausefunction50)
        self.resume50.clicked.connect(self.resumefunction50)

    def playfunction50(self):
        pygame.mixer.init()
        pygame.mixer.music.load("C:\\Users\\igthe\\Desktop\\Mp1\\music\\Arijit Singh\\Subah-Subah.mp3")
        pygame.mixer.music.play()

    def pausefunction50(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def resumefunction50(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

    def backhomepagefunction(self):
        sys.path.append('C:\\Users\\igthe\\Desktop\\Mp1\\Final\\homepage.py')
        import homepage

    def backcategoryfunction(self):
        sys.path.append('C:\\Users\\igthe\\Desktop\\Mp1\\Final\\categoryofsongs.py')
        import categoryofsongs

app = QApplication(sys.argv)
mainwindow = sss()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1371)
widget.setFixedHeight(811)
widget.showMaximized()
app.exec_()