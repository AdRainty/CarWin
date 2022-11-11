from PyQt5.QtGui import QIcon, QPixmap, QPainter
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
import sys

from ethos import Picture
from watermark import Change
from traffic import Photo


# 主页面
class Home(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('主页面')
        self.setWindowIcon(QIcon(r'./img/menu.png'))
        self.setGeometry(200, 100, 1300, 800)

        self.open_picture = QPushButton('民国风转化', self)
        self.open_picture.setGeometry(150, 250, 300, 70)  # 将按钮摆放对应的位置
        self.open_picture.setStyleSheet("""
                                border:1px solid #0073df;
                                border-radius:5px;
                                background: #167ce9;
                                color: #fff;
                            """)
        self.open_picture.clicked.connect(self.close)  # 设置按钮对应的事件

        self.open_photo = QPushButton('车流识别', self)
        self.open_photo.setGeometry(190, 470, 300, 70)  # 将按钮摆放对应的位置
        self.open_photo.setStyleSheet("""
                                        border:1px solid #0073df;
                                        border-radius:5px;
                                        background: #167ce9;
                                        color: #fff;
                                    """)
        self.open_photo.clicked.connect(self.close)  # 设置按钮对应的事件

        self.open_change = QPushButton('图片添加水印', self)
        self.open_change.setGeometry(170, 360, 300, 70)  # 将按钮摆放对应的位置
        self.open_change.setStyleSheet("""
                                        border:1px solid #0073df;
                                        border-radius:5px;
                                        background: #167ce9;
                                        color: #fff;
                                    """)
        self.open_change.clicked.connect(self.close)  # 设置按钮对应的事件

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap("./img/bg.jpg")
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

    # 切换页面实践
    my_home.open_picture.clicked.connect(my_picture.show)
    my_home.open_photo.clicked.connect(my_photos.show)
    my_home.open_change.clicked.connect(my_change.show)
    my_picture.open_return.clicked.connect(my_home.show)
    my_change.open_return.clicked.connect(my_home.show)
    my_photos.button_return.clicked.connect(my_home.show)

    my_home.show()

    sys.exit(app.exec())
