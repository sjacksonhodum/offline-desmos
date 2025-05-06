import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import os

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("offline desmos")
        self.setMinimumSize(1000, 700)  # Starting window size

        # Create the browser view
        browser = QWebEngineView()
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "index.html"))
        browser.load(QUrl.fromLocalFile(file_path))

        self.setCentralWidget(browser)

# Run the app
app = QApplication(sys.argv)
window = Browser()
window.show()
sys.exit(app.exec_())
