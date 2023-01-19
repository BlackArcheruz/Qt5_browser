import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QLineEdit, QVBoxLayout, QAction, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Browser")

        # Create a QTabWidget for holding tabs
        self.tabs = QTabWidget(self)

        # Create a QLineEdit for the URL bar
        self.url_bar = QLineEdit(self)
        self.url_bar.returnPressed.connect(self.load_url)

        # Create a QWebEngineView for displaying web pages
        self.web_view = QWebEngineView(self)
        self.web_view.loadFinished.connect(self.update_url_bar)
        self.tabs.addTab(self.web_view, "New Tab")

        # Create actions for going back, going forward, and adding a new tab
        self.back_action = self.web_view.page().action(QWebEnginePage.Back)
        self.forward_action = self.web_view.page().action(QWebEnginePage.Forward)
        self.new_tab_action = QAction("New Tab", self)
        self.new_tab_action.triggered.connect(self.add_new_tab)

        # Add the actions to the browser's toolbar
        self.toolbar = self.addToolBar("Navigation")
        self.toolbar.addAction(self.back_action)
        self.toolbar.addAction(self.forward_action)
        self.toolbar.addAction(self.new_tab_action)
        
        # Create a layout to hold the URL bar and the QTabWidget
        layout = QVBoxLayout()
        layout.addWidget(self.url_bar)
        layout.addWidget(self.tabs)

        # Set the layout for the main window
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
        self.show()

    def load_url(self):
        url = QUrl(self.url_bar.text())
        self.web_view.load(url)

    def update_url_bar(self):
        self.url_bar.setText(self.web_view.url().toString())

    def add_new_tab(self):
        # Create a new QWebEngineView
        new_web_view = QWebEngineView()

        # Add the new view to the QTabWidget
        self.tabs.addTab(new_web_view, "New Tab")

        # Make the new tab the current tab
        self.tabs.setCurrentWidget(new_web_view)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = Browser()
    sys.exit(app.exec_())
