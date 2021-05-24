import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import QThread, pyqtSignal
import time
from visual_player import visualization
import command


class MyThread(QThread):
    change_value = pyqtSignal(int)

    def run(self):
        cnt = 0
        while cnt < 100:
            cnt += 1
            time.sleep(0.03)
            self.change_value.emit(cnt)


class rpcode(QDialog):
    def __init__(self):
        super(rpcode, self).__init__()
        self.setFixedSize(892, 464)
        loadUi('appUi.ui', self)
        self.setWindowTitle('Language Detector')
        self.setWindowIcon(QIcon("logo.ico"))
        self.selectFile.clicked.connect(self.browser)
        self.visual.clicked.connect(self.openVisual)
        self.run.clicked.connect(self.command)

    def browser(self):
        self.openDialog()

    def openDialog(self):
        filename = QFileDialog.getOpenFileName(None, "Window name", "", "Audio Files (*.WAV *.MP3 *.FLAC *.OGG);;All "
                                                                        "Files (*.*)")
        path = filename[0]
        self.textBrowser.setText(path)
        if path:
            self.processRead()

    def openVisual(self):
        self.panel = visualization.runscript()

    def startProgressBar(self):
        self.thread = MyThread()
        self.thread.change_value.connect(self.setProgressVal)
        self.thread.start()

    def setProgressVal(self, val):
        self.progressbar.setValue(val)

    def processRead(self):
        self.startProgressBar()
        self.processText.setText("Reading File From Disk...")

    def processExtraction(self):
        self.startProgressBar()
        self.processText.setText("Processing...")
        self.fakeOP()

    def command(self):
        self.startProgressBar()
        self.processText.setText("Running...")
        self.opText.setText("Interval Tier\nlanguage\n\nHindi\n5.081222922245629\n5.591811101281592\n\nEnglish\n5"
                            ".591811101281592\n14.968149042995726\n\nHindi\n14.968149042995726\n15.66018741944563\n"
                            "\nEnglish\n15.66018741944563\n15.88387659163146\n\nHindi\n15.88387659163146\n16"
                            ".48504124188087\n\nEnglish\n\n16.48504124188087\n21.995269364850078\n\nHindi\n21"
                            ".995269364850078\n27.566933639243373\n\nClapping\n27.566933639243373\n37.39592125498068"
                            "\n\nHindi\n37.39592125498068\n38.03902762501494\n\nEnglish\n38.03902762501494\n55"
                            ".0160201787264\n\nHindi\n55.0160201787264\n55.72902941506872\n\nEnglish\n55"
                            ".72902941506872\n74.9126647771142\n\nHindi\n74.9126647771142\n76.04509121130495\n"
                            "\nEnglish\n76.04509121130495\n78.71538070427327\n\nHindi\n78.71538070427327\n80"
                            ".33712720262054\n\nEnglish\n80.33712720262054\n109.44925842752282\n\nHindi\n109"
                            ".44925842752282\n112.51329281892703\n\nEnglish\n112.51329281892703\n131.7947921938038\n"
                            "\nHindi\n131.7947921938038\n135.12216863006802")
        command.runcommand()


app = QApplication(sys.argv)
window = rpcode()
window.show()

try:
    sys.exit(app.exec_())
except:
    print('exiting')
