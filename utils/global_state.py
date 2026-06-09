# -*- coding: utf-8 -*-
"""
@Time ： 2024/10/21 10:06
@Auth ： 周瑞东 Ryan.Zhou
@File ：global_state.py
"""
import queue
from enum import Enum, auto
from threading import Lock
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QPointF, Qt, QRectF, QObject


'''
使用常量方式集中管理设备名称
方便后期对名称进行refactor rename
'''
class DeviceName:
    DAQ = "daq"
    PLC_J_D = "plc_j_d"
    DAS_CTRL_1 = "das_ctrl_1"
    DAS_CTRL_2 = "das_ctrl_2"
    WIRELESS_CHN_1 = "wireless_chn_1"
    WIRELESS_CHN_2 = "wireless_chn_2"
    WIRELESS_CHN_3 = "wireless_chn_3"
    S_L_ALARM = "sound_light_alarm"


class DeviceState(Enum):
    # 用于传感器连接状态
    DISCONNECTED = auto()
    PORT_AVAILABLE = auto()
    PING_SUCCESS = auto()
    INITIALIZING = auto()

    WORKING = auto()

class Serial:
    def __init__(self):
        self.sn = 'A28956LTA'


class Common:
    def __init__(self):
        # 软件导出数据的根目录
        self.path_data_export_root = "D:\data_export"

        self.ip_addr_local = "192.168.1.182"
        self.ip_addr_das_controller_1 = "192.168.1.6"
        self.ip_addr_das_controller_2 = "192.168.1.7"
        self.ip_addr_j_d_plc = "192.168.1.8" # 安装在接箍检测防爆控制箱中的PLC，用于控制箱体上的灯和蜂鸣器
        self.port_j_d_plc = 502

        self.flag_das_use_simulator = False

        self.timer_interval_das_wired_ms = 1500
        self.flag_pc_info_check_success = False

        # 井架配置页面相关参数
        # -------------------------
        # 全局显示比例1 pix = 20mm
        self.scaling = 20
        # self.path_database_file_path = "\\database\\frost_db_20241224"


class GlobalState:
    _instance = None
    _lock = Lock()

    '''
        __new__ 是 构造方法，在实例化时最先被调用。
    
        负责 创建对象，返回这个对象（cls._instance = super().__new__(cls)）。
        
        决定是否要返回一个新对象，还是返回之前的（这就是单例能在这里实现的原因）。
    '''

    '''
        这是经典的 双重检查锁定（Double-Checked Locking） 模式。
        第一次检查：
        避免每次都进入加锁（锁的开销大）。如果已经有实例，直接返回，效率高。
        第二次检查：
        假设两个线程同时执行到第一次检查，都发现 _instance is None，于是都试图去创建实例。
        进入锁之后，只有第一个线程会真正创建实例。
        第二个线程在锁内再检查一次，发现 _instance 已经不是 None 了，就不会再创建。
    
        👉 没有第二次检查，就可能在多线程下创建多个实例，破坏单例。
    '''
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)

        return cls._instance

    '''
        __init__ 是 初始化方法，在 __new__ 返回对象之后被调用。
    
        负责给对象设置属性、初始化状态。
        
        可能会被多次调用（因为每次 SignalBus() 都会执行 __init__，即使返回的是同一个实例）。
        
        所以我们一般加 _initialized 标志来避免重复初始化。
    '''
    def __init__(self):
        if not hasattr(self, '_initialized'):
            self._initialized = True

            # 初始化全局状态
            self.common = Common()
            self.serial = Serial()
            # 保存所有设备的状态：{设备名: 状态}
            self.device_info = {}

    @classmethod
    def get_instance(cls):
        return cls()

# 提前实例化一个全局变量
gs = GlobalState.get_instance()
