import os
import sys

import cv2
import numpy
from PIL import Image
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon, QPainter, QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMessageBox, QInputDialog
from face import acquire
from checkData import check

from ethos import Picture
from watermark import Change
from traffic import Photo
from CarWin import Home


class Registerer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('欢迎界面')
        self.setWindowIcon(QIcon(r'./img/menu.png'))
        self.setGeometry(200, 100, 1300, 800)

        self.reg = QPushButton('人脸注册', self)  # 控件显示的名称
        self.reg.setGeometry(200, 300, 100, 40)  # 将按钮摆放对应的位置
        self.reg.clicked.connect(self.faceData)  # 设置按钮对应的事件

        self.reg.setStyleSheet("""
                                                border:1px solid #0073df;
                                                border-radius:5px;
                                                background: #167ce9;
                                                color: #fff;
                                            """)

        self.log = QPushButton('人脸登录', self)  # 控件显示的名称
        self.log.setGeometry(300, 500, 100, 40)  # 将按钮摆放对应的位置
        self.log.clicked.connect(self.checkMes)  # 设置按钮对应的事件

        self.log.setStyleSheet("""
                                                        border:1px solid #0073df;
                                                        border-radius:5px;
                                                        background: #167ce9;
                                                        color: #fff;
                                                    """)

        self.user = ''

    def getStr(self):
        self.user, ok = QInputDialog.getText(self, '对话窗', '输入用户名：')
        if ok and self.user:
            return True
        else:
            return False

    def faceData(self):
        if self.getStr():
            if (str(self.user) + '.yml') in os.listdir('./yml'):
                QMessageBox.warning(self, '警告', '你的用户名已经被注册了!')
                return
        else:
            QMessageBox.warning(self, '警告', '请输入正确的用户名!')
            return
        acquire()
        img_path = "./faceData"
        img_list = os.listdir(img_path)
        feature_list = []
        label_list = []
        # 矩阵信息
        for i in img_list:
            # 图片转矩阵
            pil_img = Image.open(img_path + "/" + i).convert("L")
            img_array = numpy.array(pil_img, 'uint8')
            feature_list.append(img_array)
            label_list.append(0)

        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.train(feature_list, numpy.array(label_list))
        recognizer.write(f'./yml/{self.user}.yml')
        # 删除获取到的照片
        for i in range(10):
            if os.path.exists(img_path + '/' + f'{str(i)}.jpg'):
                os.remove(img_path + '/' + f'{str(i)}.jpg')
        QMessageBox.information(self, '提示', '注册成功!')

    def checkMes(self):
        if self.getStr():
            if (str(self.user) + '.yml') not in os.listdir('./yml'):
                QMessageBox.warning(self, '警告', '此用户名不在注册列表中!')
                return
        else:
            QMessageBox.warning(self, '警告', '请输入正确的用户名!')
            return
        isOk = check(self.user)
        if isOk:
            QMessageBox.information(self, '提示', f'欢迎您,{self.user}!')
            my_home.show()
            self.close()
        else:
            QMessageBox.warning(self, '警告', '没有识别到注册信息!')

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap("./img/bg5.jpg")
        painter.drawPixmap(self.rect(), pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 主页面
    my_home = Home()
    my_home.paintEngine()
    # 图片民国风
    my_picture = Picture()
    my_picture.paintEngine()
    # 图片添加水印
    my_change = Change()
    my_change.paintEngine()
    # 车流识别
    my_photos = Photo()
    my_photos.paintEngine()
    # 登录界面
    my_id = Registerer()
    my_id.paintEngine()

    # 切换页面实践
    my_home.open_picture.clicked.connect(my_picture.show)
    my_home.open_photo.clicked.connect(my_photos.show)
    my_home.open_change.clicked.connect(my_change.show)
    my_picture.open_return.clicked.connect(my_home.show)
    my_change.open_return.clicked.connect(my_home.show)
    my_photos.button_return.clicked.connect(my_home.show)

    # 显示主页面
    my_id.show()
    sys.exit(app.exec())

