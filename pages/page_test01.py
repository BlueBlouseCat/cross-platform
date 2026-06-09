# -*- coding: utf-8 -*-
"""
@Time ： 2026/5/28 16:03
@Auth ： 周瑞东 Ryan.Zhou
@File ： page_test01.py
"""
from PyQt5.QtWidgets import QWidget
from modular_template_2026.ui.page_test01_ui import Ui_Form


class PageTest01(QWidget, Ui_Form):
    def __init__(self, number=2026, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.number = number
        self.lb_number.setText(str(self.number))

        self.connect_signals()

    def connect_signals(self):
        self.pb_inc.clicked.connect(self.increase_number)
        self.pb_dec.clicked.connect(self.decrease_number)
        self.horizontalSlider.valueChanged.connect(self.progressBar.setValue)

    def increase_number(self):
        self.number += 1
        self.lb_number.setText(str(self.number))

    def decrease_number(self):
        self.number -= 1
        self.lb_number.setText(str(self.number))