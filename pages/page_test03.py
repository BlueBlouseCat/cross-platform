# -*- coding: utf-8 -*-
"""
@Time ： 2026/5/28 16:03
@Auth ： 周瑞东 Ryan.Zhou
@File ： page_test03.py
"""
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QTimer
import serial
import serial.tools.list_ports
import resources_rc

# 导入你生成的UI文件
from modular_template_2026.ui.page_test03_serial_ui import Ui_Form


class PageTest03(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # 串口相关变量初始化
        self.ser = None  # 串口对象
        self.serial_is_open = False  # 串口状态

        # 初始化下拉框内容
        self.init_serial_params()

        # 绑定信号槽
        self.connect_signals()

        # 定时刷新串口列表
        self.serial_timer = QTimer(self)
        self.serial_timer.timeout.connect(self.refresh_serial_ports)
        self.serial_timer.start(1000)

    def init_serial_params(self):
        """初始化串口参数下拉框"""
        # 波特率
        baudrates = ["9600", "19200", "38400", "57600", "115200"]
        self.comboBox_baudrate.addItems(baudrates)
        self.comboBox_baudrate.setCurrentText("115200")

        # 校验位
        parities = ["None", "Odd", "Even", "Mark", "Space"]
        self.comboBox_parity.addItems(parities)

        # 刷新串口列表
        self.refresh_serial_ports()

    def refresh_serial_ports(self):
        """自动刷新可用串口列表"""
        current_ports = [self.comboBox_serial_name.itemText(i) for i in range(self.comboBox_serial_name.count())]
        ports = [str(port) for port in serial.tools.list_ports.comports()]

        if ports != current_ports:
            self.comboBox_serial_name.clear()
            self.comboBox_serial_name.addItems(ports)

    def connect_signals(self):
        """绑定按钮信号"""
        self.pushButton_open_serial.clicked.connect(self.open_serial)
        self.pushButton_close_serial.clicked.connect(self.close_serial)
        self.pushButton_send_data.clicked.connect(self.send_data)
        self.pushButton_clear_console.clicked.connect(self.clear_console)

    def open_serial(self):
        """打开串口"""
        if self.serial_is_open:
            self.textBrowser.append("串口已打开")
            return

        try:
            port_name = self.comboBox_serial_name.currentText().split(" ")[0]
            baudrate = int(self.comboBox_baudrate.currentText())
            parity = self.comboBox_parity.currentText()

            self.ser = serial.Serial()
            self.ser.port = port_name
            self.ser.baudrate = baudrate
            self.ser.parity = parity[0] if parity != "None" else serial.PARITY_NONE
            self.ser.timeout = 0.5

            self.ser.open()
            self.serial_is_open = True
            self.textBrowser.append(f"✅ 成功打开串口：{port_name}")

        except Exception as e:
            self.textBrowser.append(f"❌ 打开串口失败：{str(e)}")

    def close_serial(self):
        """关闭串口"""
        if not self.serial_is_open:
            self.textBrowser.append("串口未打开")
            return

        try:
            self.ser.close()
            self.serial_is_open = False
            self.textBrowser.append("❌ 已关闭串口")
        except Exception as e:
            self.textBrowser.append(f"关闭串口失败：{str(e)}")

    def send_data(self):
        """发送数据"""
        if not self.serial_is_open:
            self.textBrowser.append("请先打开串口")
            return

        data = self.lineEdit.text().strip()
        if not data:
            self.textBrowser.append("发送内容不能为空")
            return

        try:
            self.ser.write((data + "\r\n").encode("utf-8"))
            self.textBrowser.append(f"➡️ 发送：{data}")
        except Exception as e:
            self.textBrowser.append(f"发送失败：{str(e)}")

    def clear_console(self):
        """清空接收区"""
        self.textBrowser.clear()