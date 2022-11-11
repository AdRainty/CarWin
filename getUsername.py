from PyQt5.QtWidgets import QMainWindow


class Ui_Form(object):
  def setupUi(self, Form):
    Form.setObjectName("Form")
    Form.resize(382, 190)
    font = QtGui.QFont()
    font.setPointSize(9)
    font.setBold(False)
    font.setWeight(50)
    Form.setFont(font)
    self.GetIntlineEdit = QtWidgets.QLineEdit(Form)
    self.GetIntlineEdit.setGeometry(QtCore.QRect(150, 30, 150, 31))
    self.GetIntlineEdit.setText("")
    self.GetIntlineEdit.setObjectName("GetIntlineEdit")
    self.GetstrlineEdit = QtWidgets.QLineEdit(Form)
    self.GetstrlineEdit.setGeometry(QtCore.QRect(150, 80, 150, 31))
    self.GetstrlineEdit.setObjectName("GetstrlineEdit")
    self.GetItemlineEdit = QtWidgets.QLineEdit(Form)
    self.GetItemlineEdit.setGeometry(QtCore.QRect(150, 130, 150, 31))
    self.GetItemlineEdit.setObjectName("GetItemlineEdit")
    self.getIntButton = QtWidgets.QPushButton(Form)
    self.getIntButton.setGeometry(QtCore.QRect(50, 30, 80, 31))
    self.getIntButton.setObjectName("getIntButton")
    self.getStrButton = QtWidgets.QPushButton(Form)
    self.getStrButton.setGeometry(QtCore.QRect(50, 80, 80, 31))
    self.getStrButton.setObjectName("getStrButton")
    self.getItemButton = QtWidgets.QPushButton(Form)
    self.getItemButton.setGeometry(QtCore.QRect(50, 130, 80, 31))
    self.getItemButton.setObjectName("getItemButton")
    self.retranslateUi(Form)
    QtCore.QMetaObject.connectSlotsByName(Form)
  def retranslateUi(self, Form):
    _translate = QtCore.QCoreApplication.translate
    Form.setWindowTitle(_translate("Form", "QInputDialog例子"))
    self.getIntButton.setText(_translate("Form", "获取整数"))
    self.getStrButton.setText(_translate("Form", "获取字符串"))
    self.getItemButton.setText(_translate("Form", "获取列表选项"))
class MyMainForm(QMainWindow, Ui_Form):
  def __init__(self, parent=None):
    super(MyMainForm, self).__init__(parent)
    self.setupUi(self)
    self.getIntButton.clicked.connect(self.getInt)
    self.getStrButton.clicked.connect(self.getStr)
    self.getItemButton.clicked.connect(self.getItem)