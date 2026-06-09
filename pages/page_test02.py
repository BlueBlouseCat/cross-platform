# -*- coding: utf-8 -*-
"""
@Time ： 2026/5/28 16:03
@Auth ： 周瑞东 Ryan.Zhou
@File ： page_test02.py
"""
from PyQt5.QtWidgets import QWidget
from modular_template_2026.ui.page_test02_ui import Ui_Form


class PageTest02(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.connect_signals()

    def connect_signals(self):
        pass