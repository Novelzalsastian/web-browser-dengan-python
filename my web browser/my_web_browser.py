#Importing the libraries
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
import os
import sys

#for main window
class MainWindow(QMainWindow):

    #the Constructor
    def __init__(self, *args , **kwargs):
        super(MainWindow,self).__init__(*args,**kwargs)

        #Qwebengine
        self.browser = QWebEngineView()

        #Setting Default Browser Google
        self.browser.setUrl(QUrl("https://google.com"))

        #Adding Action after Url is change
        self.browser.urlChanged.connect(self.update_urlbar)

        #Adding Action When Loading Is Finished
        self.browser.loadFinished.connect(self.update_title)

        #Setting Browser As Main Window
        self.setCentralWidget(self.browser)

        #Creating A Status Bar Object
        self.status = QStatusBar()

        #Adding Status Bar To Main Window
        self.setStatusBar(self.status)

        #Creating Qtoolbar 
        navtb = QToolBar("Navigation")

        #Adding The Toolbar To The Main Window
        self.addToolBar(navtb)

        #Adding Actions For The ToolBar
        back_btn = QAction("Back",self)
        back_btn.setStatusTip("Back To The Previos Page")
        back_btn.triggered.connect(self.browser.back)
        navtb.addAction(back_btn)

        next_btn = QAction("Forward",self)
        next_btn.setStatusTip("Fast Forward To Next Page")
        next_btn.triggered.connect(self.browser.forward)
        navtb.addAction(next_btn)

        reload_btn = QAction("Reload",self)
        reload_btn.setStatusTip("Reload The Page")
        reload_btn.triggered.connect(self.browser.reload)
        navtb.addAction(reload_btn)

        home_btn = QAction("Home",self)
        home_btn.setStatusTip("Go To Home")
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)

        #Adding A Seperator 
        navtb.addSeparator()

        #Creating A Line Edit
        self.urlbar = QLineEdit()

        #Adding Action When Return Key Is Pressed
        self.urlbar.returnPressed.connect(self.navigate_to_url)

        #Adding to the toolbar
        navtb.addWidget(self.urlbar)

        #Adding Stopping Action To the toolbar
        stop_btn = QAction("Stop", self)
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.triggered.connect(self.browser.stop)
        navtb.addAction(stop_btn)

        #Show All The Components
        self.show()

    #updating The title
    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle("% s - My Browser "% title)

    #method called by the home action
    def navigate_home(self):
        #opening the google
        self.browser.setUrl(QUrl("https://www.google.com"))

    #method called by the edit
    def navigate_to_url(self):
        #convert to qurl
        q = QUrl(self.urlbar.text())
        #if scheme is blank
        if q.scheme() == "":
            q.setScheme("http")
        #set url to browser
        self.browser.setUrl(q)

    #method for updating url
    def update_urlbar(self,q):
        #setting text to url
        self.urlbar.setText(q.toString())
        #setting the cursor position to the url bar
        self.urlbar.setCursorPosition(0)

#creating the PyQt5 app
app = QApplication(sys.argv)

#setting the name of the application
app.setApplicationName("Python Browser ")

#create a main window object
window = MainWindow()

#loop
app.exec_()






