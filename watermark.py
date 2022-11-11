
"""

    图片添加水印

"""
import sys
import time

import cv2
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QIntValidator, QPixmap, QPainter, QColor
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QDialog, QFileDialog, QMessageBox, QColorDialog, \
    QApplication


class Change(QWidget):
    def __init__(self):
        super().__init__()
        self.file_url, self.file_type = '', ''
        self.pix_map = ''
        self.setWindowTitle('图片添加水印')
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

        self.start = QPushButton('添加水印', self)  # 控件显示的名称
        self.start.setGeometry(400, 10, 100, 30)  # 将按钮摆放对应的位置
        self.start.clicked.connect(self.control)  # 设置按钮对应的事件

        self.start.setStyleSheet("""
                                padding-left: 10px;
                                padding-right: 10px;
                                padding-top: 1px;
                                padding-bottom: 1px;
                                border:1px solid #0073df;
                                border-radius:5px;
                                background: #167ce9;
                                color: #fff;
                            """)

        self.label_color = QLabel(self)
        self.label_color.setGeometry(30, 80, 90, 40)
        self.label_color.setText('颜色设置：')
        self.label_color.setStyleSheet(
            "border: 1px solid black;opacity:0.6;filter:alpha(opacity=60);"
            "font-size:15px;font-weight:bold;font-family:Roman times;"
            "background-color: gray;"
        )

        self.color = QColor(0, 0, 0)
        self.button_color = QPushButton('点击更改：', self)
        self.button_color.setFocusPolicy(Qt.NoFocus)
        self.button_color.setGeometry(170, 80, 90, 40)
        self.button_color.clicked.connect(self.showDialog)
        self.button_color.setStyleSheet(
            "border: 1px solid black;opacity:0.6;filter:alpha(opacity=60);"
            "font-size:15px;font-weight:bold;font-family:Roman times;"
            f"background-color: {self.color};"
        )

        self.color_label = QLineEdit('0', self)
        self.color_label.setGeometry(240, 135, 50, 40)
        self.color_label.setObjectName("x")

        self.label_position = QLabel(self)
        self.label_position.move(30, 135)
        self.label_position.resize(90, 40)
        self.label_position.setText('位置设置：')
        self.label_position.setStyleSheet(
            "border: 1px solid black;opacity:0.6;filter:alpha(opacity=60);"
            "font-size:15px;font-weight:bold;font-family:Roman times;"
            "background-color: gray;"
        )

        self.label_text = QLabel(self)
        self.label_text.move(30, 200)
        self.label_text.resize(90, 40)
        self.label_text.setText('文字设置：')
        self.label_text.setStyleSheet(
            "border: 1px solid black;opacity:0.6;filter:alpha(opacity=60);"
            "font-size:15px;font-weight:bold;font-family:Roman times;"
            "background-color: gray;"
        )

        self.label_x = QLabel(self)
        self.label_x.move(170, 135)
        self.label_x.resize(60, 40)
        self.label_x.setText('x：')
        self.label_x.setStyleSheet(
            "border: 1px solid black;opacity:0.6;filter:alpha(opacity=60);"
            "font-size:15px;font-weight:bold;font-family:Roman times;"
            "background-color: gray;"
        )

        self.label_y = QLabel(self)
        self.label_y.move(360, 135)
        self.label_y.resize(60, 40)
        self.label_y.setText('y：')
        self.label_y.setStyleSheet(
            "border: 1px solid black;opacity:0.6;filter:alpha(opacity=60);"
            "font-size:15px;font-weight:bold;font-family:Roman times;"
            "background-color: gray;"
        )

        self.let_x = QLineEdit('0', self)
        self.let_x.setGeometry(240, 135, 50, 40)
        self.let_x.setObjectName("x")

        self.let_msg = QLineEdit('', self)
        self.let_msg.setGeometry(170, 200, 300, 40)
        self.let_msg.setObjectName("msg")

        self.let_y = QLineEdit('0', self)
        self.let_y.setGeometry(430, 135, 50, 40)
        self.let_y.setObjectName("y")

        self.left_label = QLabel('原图', self)  # 控件显示的名称
        self.left_label.setGeometry(100, 300, 400, 400)  # 将按钮摆放对应的位置

        self.left_label.setStyleSheet("border: 1px solid black;opacity:0.6;filter:alpha(opacity=60);"
                                      "font-size:40px;font-weight:bold;font-family:Roman times;"
                                      "opacity:0.4;"
                                      "background-color: gray;")

        self.right_label = QLabel('修改后的图', self)  # name-控件显示的名称
        self.right_label.setGeometry(650, 300, 400, 400)  # 将按钮摆放对应的位置

        self.right_label.setStyleSheet("border: 1px solid black;opacity:0.6;filter:alpha(opacity=60);"
                                       "font-size:40px;font-weight:bold;font-family:Roman times;"
                                       "opacity:0.4;"
                                       "background-color: gray;")

        self.open_return = QPushButton('返回主菜单', self)  # 控件显示的名称
        self.open_return.setGeometry(550, 750, 100, 40)  # 将按钮摆放对应的位置
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

    def showDialog(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.color = (col.blue(), col.green(), col.red())
        self.button_color.setStyleSheet(
            f"background-color: {col.name()};"
        )

    def control(self):
        if not self.file_url:
            # 显示弹窗 先导入图片
            QMessageBox.warning(self, '警告', '请先导入要转化的图片！')
            return

        msg = self.let_msg.text()
        x = self.let_x.text()
        y = self.let_y.text()
        flag2 = False

        try:
            x = eval(x) + 0
            y = eval(y) + 0
            if int(x) == x and int(y) == y and 0 <= int(x) and 0 <= int(y):
                position = (int(x), int(y))
                flag2 = True
            else:
                QMessageBox.warning(self, '警告', '请输入正确的坐标值！')
        except:
            QMessageBox.warning(self, '警告', '请输入正确的坐标值！')

        if flag2:
            img = cv2.imread(self.file_url)
            img_add = cv2.putText(img, msg, position, cv2.FONT_HERSHEY_PLAIN, 2, self.color, 1, cv2.LINE_AA)
            img_path = f"./img/mark{time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))}.jpg"
            cv2.imwrite(img_path, img_add)
            pixmap = QPixmap(img_path)
            self.right_label.setPixmap(pixmap)
            self.right_label.setScaledContents(True)
            # 显示弹窗 转化完成
            QMessageBox.information(self, '提示', '恭喜，转化完成！图片已经保存到img目录下！')

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap("./img/bg3.jpg")
        painter.drawPixmap(self.rect(), pixmap)

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_change = Change()
    my_change.show()
    sys.exit(app.exec_())
