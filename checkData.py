import cv2


def check(user):
    Classifier_path = r'.\xml\haarcascade_frontalface_default.xml'
    face_count = 0  # 达到准确率的次数
    recongnizer = cv2.face.LBPHFaceRecognizer_create()
    recongnizer.read(f'./yml/{user}.yml')
    capture = cv2.VideoCapture(0)
    while True:
        ref, frame = capture.read()
        if ref:
            # 2.灰度处理
            img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # 3.创建级联分类器---人脸
            face_detector = cv2.CascadeClassifier(Classifier_path)
            # 4.检测灰度图片人脸位置 image, scaleFactor=None, minNeighbors=None,
            # flags=None, minsize=None, maxsize=None
            faces = face_detector.detectMultiScale(img_gray, 1.1, 3, cv2.CASCADE_SCALE_IMAGE, (200, 200), (300, 300))

            for x, y, width, height in faces:
                # 6.1矩形框定
                # img, pt1左上角坐标，pt2右下角坐标,
                # color线色， thickness=None粗细，l ineType=None线类型，
                cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 0, 0), 1, cv2.LINE_AA)
                # 6.2抠图区域(X, y) (x+width， y+height)---矩阵
                img_face_array = img_gray[y:y + height, x:x + width]
                # 6.3 预测
                res = recongnizer.predict(img_face_array)
                if 100 - res[1] > 50:
                    face_count += 1
            if face_count >= 10:
                capture.release()
                cv2.destroyAllWindows()
                return str(res[0])
            cv2.imshow("face", frame)
        c = cv2.waitKey(30)
        if c == 27 or cv2.getWindowProperty('face', cv2.WND_PROP_AUTOSIZE) < 1:
            capture.release()
            cv2.destroyAllWindows()
            return False


if __name__ == '__main__':
    check()
