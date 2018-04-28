import sys
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtCore import QUrl, pyqtSlot, pyqtSignal, Qt

# This will automatically load qrc
import core_rc

class GPSView(QWebEngineView):
    def __init__(self, parent):
        super(QWebEngineView, self).__init__(parent)

        self.pageReady = False

        # Settings
        self.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        self.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)

        self.loadFinished.connect(self.pageLoaded)

        # Load file from qrc
        self.setUrl(QUrl('qrc:/OpenIMU/html/map.html'))

    def setCurrentPosition(self, latitude, longitude):
        if self.pageReady is True:
            self.page().runJavaScript('setCurrentPosition(' + str(latitude) + ',' + str(longitude) + ');')
        else:
            print('Cannot set position, page not ready')


    @pyqtSlot(bool)
    def pageLoaded(self, state):
        print('page loaded:', state)

        if state is True:
            self.pageReady = True
            # 3IT = 45.3790193,-71.9430778
            self.setCurrentPosition(45.3790193, -71.9430778)


# Testing app
if __name__ == '__main__':

    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtWidgets import QMainWindow, QPushButton
    from PyQt5.QtCore import Qt

    app = QApplication(sys.argv)

    window = QMainWindow()
    window.setWindowTitle('GPSView - Test')
    window.resize(640, 480)

    view = GPSView(window)
    # view.setCurrentPosition(latitude=0, longitude=0)
    window.setCentralWidget(view)
    window.show()

    sys.exit(app.exec_())

