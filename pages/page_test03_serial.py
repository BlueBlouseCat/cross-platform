# -*- coding: utf-8 -*-
"""
@Time ： 2026/5/28 16:03
@Auth ： 周瑞东 Ryan.Zhou
@File ： page_test03.py
"""
from PyQt5.QtWidgets import QWidget
from modular_template_2026.ui.page_test03_serial_ui import Ui_Form
from modular_template_2026.utils.global_state import gs

class PageTest03(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connect_signals()

        print(f"当前序列号:{gs.serial.sn}")

    def connect_signals(self):
        pass
