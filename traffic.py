# 车流识别
import cv2
import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon, QImage, QPixmap, QPainter
from PyQt5.QtWidgets import QWidget, QPushButton, QFileDialog, QLabel, QApplication


class Photo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('车流识别')
        self.setWindowIcon(QIcon(r'./img/vehicle.ico'))
        self.btn = QPushButton('打开文件', self)  # 控件显示的名称
        self.btn.setGeometry(10, 10, 100, 30)  # 将按钮摆放对应的位置
        self.btn.clicked.connect(self.slotStart)
        self.frame = []  # 存图片
        self.detectFlag = False  # 检测flag
        self.cap = []
        self.timer_camera = QTimer()  # 定义定时器

        self.btn.setStyleSheet("""
                                padding-left: 10px;
                                padding-right: 10px;
                                padding-top: 1px;
                                padding-bottom: 1px;
                                border:1px solid #0073df;
                                border-radius:5px;
                                background: #167ce9;
                                color: #fff;
                            """)

        self.button_return = QPushButton('返回主菜单', self)  # 控件显示的名称
        self.button_return.setGeometry(550, 700, 100, 40)  # 将按钮摆放对应的位置
        self.button_return.clicked.connect(self.close)  # 设置按钮对应的事件

        self.button_return.setStyleSheet("""
                                        padding-left: 10px;
                                        padding-right: 10px;
                                        padding-top: 1px;
                                        padding-bottom: 1px;
                                        border:1px solid #0073df;
                                        border-radius:5px;
                                        background: #167ce9;
                                        color: #fff;
                                    """)

        self.setGeometry(200, 100, 1300, 800)
        self.Classifier_path = './xml/cars.xml'
        self.file_url = ''
        self.file_type = ''
        self.file_path = 'img/carMove.mp4'

        self.label = QLabel(self)
        self.label.setFixedSize(600, 600)
        self.label.move(300, 80)
        self.label.setText("显示录像")
        self.label.setStyleSheet("QLabel{background:gray;}"
                                 "QLabel{color:rgb(300,300,300,120);font-size:30px;font-weight:bold;font-family:宋体;}"
                                 )

    def slotStart(self):
        videoName, _ = QFileDialog.getOpenFileName(self, "Open", "", "*.avi;;*.mp4;;All Files(*)")
        if videoName != "":
            self.cap = cv2.VideoCapture(videoName)
            self.timer_camera.start(100)
            self.timer_camera.timeout.connect(self.openFrame)

    def openFrame(self):
        if self.cap.isOpened():
            ret, self.frame = self.cap.read()
            if ret:
                frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
                car_detector = cv2.CascadeClassifier(self.Classifier_path)
                cars = car_detector.detectMultiScale(frame, 1.1, 3, cv2.CASCADE_SCALE_IMAGE, (30, 30), (120, 120))

                for item in cars:
                    x = item[0]
                    y = item[1]
                    vedio_width = item[2]
                    vedio_height = item[3]
                    # img, pt1左上角坐标，pt2右下角坐标,
                    # color线色， thickness=None粗细，l ineType=None线类型，
                    cv2.rectangle(frame, (x, y), (x + vedio_width, y + vedio_height), (0, 0, 0), 1, cv2.LINE_AA)

                height, width, bytesPerComponent = frame.shape
                bytesPerLine = bytesPerComponent * width
                q_image = QImage(frame.data, width, height, bytesPerLine,
                                 QImage.Format_RGB888).scaled(self.label.width(), self.label.height())
                self.label.setPixmap(QPixmap.fromImage(q_image))
            else:
                self.cap.release()
                self.timer_camera.stop()  # 停止计时器

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap("./img/bg4.jpg")
        painter.drawPixmap(self.rect(), pixmap)
        
 
if __name__ == '__main__':
    app = QApplication(sys.argv) 
    my_photo = Photo()
    my_photo.show()
    sys.exit(app.exec_())
    