
"""

    图像民国风

"""

import time

import cv2
from PyQt5.QtGui import QIcon, QPixmap, QPainter
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QFileDialog, QDialog, QMessageBox


class Picture(QWidget):
    def __init__(self):
        super().__init__()
        self.file_url = ''
        self.file_type = ''
        self.pix_map = ''
        self.setWindowTitle('民国风转化')
        self.setWindowIcon(QIcon(r'./img/img.png'))
        self.setGeometry(200, 100, 1300, 800)

        self.open_btn_left = QPushButton('打开文件', self)  # 控件显示的名称
        self.open_btn_left.setGeometry(10, 10, 100, 30)  # 将按钮摆放对应的位置
        self.open_btn_left.clicked.connect(self.showDialog1)  # 设置按钮对应的事件

        self.open_btn_left.setStyleSheet("""
                padding-left: 10px;
                padding-right: 10px;
                padding-top: 1px;
                padding-bottom: 1px;
                border:1px solid #0073df;
                border-radius:5px;
                background: #167ce9;
                color: #fff;
            """)

        self.open_btn_right = QPushButton('民国风', self)  # 控件显示的名称
        self.open_btn_right.setGeometry(660, 10, 100, 30)  # 将按钮摆放对应的位置
        self.open_btn_right.clicked.connect(self.showDialog2)  # 设置按钮对应的事件

        self.open_btn_right.setStyleSheet("""
                        padding-left: 10px;
                        padding-right: 10px;
                        padding-top: 1px;
                        padding-bottom: 1px;
                        border:1px solid #0073df;
                        border-radius:5px;
                        background: #167ce9;
                        color: #fff;
                    """)

        self.left_label = QLabel('原图', self)  # 控件显示的名称
        self.left_label.setGeometry(10, 50, 600, 600)  # 将按钮摆放对应的位置

        self.left_label.setStyleSheet("border: 1px solid black;opacity:0.6;filter:alpha(opacity=60);"
                                      "font-size:40px;font-weight:bold;font-family:Roman times;"
                                      "opacity:0.4;"
                                      "background-color: gray;")

        self.right_label = QLabel('修改后的图', self)  # name-控件显示的名称
        self.right_label.setGeometry(650, 50, 600, 600)  # 将按钮摆放对应的位置

        self.right_label.setStyleSheet("border: 1px solid black;opacity:0.6;filter:alpha(opacity=60);"
                                       "font-size:40px;font-weight:bold;font-family:Roman times;"
                                       "opacity:0.4;"
                                       "background-color: gray;")

        self.open_return = QPushButton('返回主菜单', self)  # 控件显示的名称
        self.open_return.setGeometry(550, 700, 100, 40)  # 将按钮摆放对应的位置
        self.open_return.clicked.connect(self.close)  # 设置按钮对应的事件

        self.open_return.setStyleSheet("""
                                padding-left: 10px;
                                padding-right: 10px;
                                padding-top: 1px;
                                padding-bottom: 1px;
                                border:1px solid #0073df;
                                border-radius:5px;
                                background: #167ce9;
                                color: #fff;
                            """)

    # 打开文件对应的函数
    def showDialog1(self):
        self.file_url, self.file_type = QFileDialog.getOpenFileName(
            self,
            "打开图片",
            "./",
            "All Files (*);;PNG Files (*.png);;JPG Files (*.jpg);;BMP Files (*.bmp)"
        )
        # 判断图片是否符合格式
        if str(self.file_url[-3:]).upper() in ['JPG', 'PNG', 'BMP']:
            self.pix_map = QPixmap(self.file_url)
            self.left_label.setPixmap(self.pix_map)
            self.left_label.setScaledContents(True)
        else:
            # 显示弹窗 文件格式不正确
            QMessageBox.warning(self, '警告', '请选择正确的图片格式！')

    def showDialog2(self):
        # 判断图片是否存在
        if self.file_url:
            # 若存在 转化为灰白
            img = cv2.imread(self.file_url)
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img_path = f"./img/gray{time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))}.jpg"
            # 保存图片并改名
            cv2.imwrite(img_path, img_gray)
            pixmap = QPixmap(img_path)
            self.right_label.setPixmap(pixmap)
            self.right_label.setScaledContents(True)
            # 显示弹窗 转化完成
            QMessageBox.information(self, '提示', '恭喜，转化完成！图片已经保存到img目录下！')
        else:
            # 显示弹窗 先导入图片
            QMessageBox.warning(self, '警告', '请先导入要转化的图片！')

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap("./img/bg2.jpg")
        painter.drawPixmap(self.rect(), pixmap)