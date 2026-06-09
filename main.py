from PyQt5.QtWidgets import QMainWindow, QApplication

from modular_template_2026.pages.page_test01 import PageTest01
from modular_template_2026.pages.page_test02 import PageTest02
from modular_template_2026.pages.page_test03 import PageTest03
from modular_template_2026.ui.main_frame_ui import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.load_pages()
        self.connect()

    def load_pages(self):
        self.page_test01 = PageTest01()
        self.page_test02 = PageTest02()
        self.page_test03 = PageTest03()
        self.stackedWidget.addWidget(self.page_test01)
        self.stackedWidget.addWidget(self.page_test02)
        self.stackedWidget.addWidget(self.page_test03)

    def connect(self):
        self.pb_navi_1.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.pb_navi_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.pb_navi_3.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))

app = QApplication([])
mainwindow = MainWindow()
mainwindow.show()
app.exec()