from PIL import Image,ImageQt,ImageDraw,ImageFont
from PyQt6 import QtCore,QtGui,QtWidgets
import os

class Ui_MainWindow(QtWidgets.QMainWindow):


    def setupUi(self, MainWindow):
        # self.init()
        self.pic = Image.new('RGBA',(800,400))

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        # MainWindow.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        # MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.cn_event = QtWidgets.QLineEdit(self.centralwidget)
        self.cn_event.setGeometry(QtCore.QRect(100, 50, 161, 21))
        self.cn_event.setObjectName("cn_event")
        self.cn_event.textChanged.connect(self.image_update)

        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(10, 10, 281, 21))
        self.title.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.title.setObjectName("title")
        
        self.cn_tip = QtWidgets.QLabel(self.centralwidget)
        self.cn_tip.setGeometry(QtCore.QRect(80, 50, 271, 16))
        self.cn_tip.setObjectName("cn_tip")
        

        self.cn_num = QtWidgets.QLineEdit(self.centralwidget)
        self.cn_num.setGeometry(QtCore.QRect(300, 50, 41, 21))
        self.cn_num.setObjectName("cn_num")
        self.cn_num.textChanged.connect(self.image_update)

        self.cn_unit = QtWidgets.QLineEdit(self.centralwidget)
        self.cn_unit.setGeometry(QtCore.QRect(350, 50, 61, 21))
        self.cn_unit.setObjectName("cn_unit")
        self.cn_unit.textChanged.connect(self.image_update)

        self.en_tip = QtWidgets.QLabel(self.centralwidget)
        self.en_tip.setGeometry(QtCore.QRect(300, 80, 72, 15))
        self.en_tip.setObjectName("en_tip")

        self.en_event = QtWidgets.QLineEdit(self.centralwidget)
        self.en_event.setGeometry(QtCore.QRect(80, 80, 211, 21))
        self.en_event.setObjectName("en_event")
        self.en_event.textChanged.connect(self.image_update)

        self.en_num = QtWidgets.QLineEdit(self.centralwidget)
        self.en_num.setGeometry(QtCore.QRect(330, 80, 41, 21))
        self.en_num.setObjectName("en_num")
        self.en_num.textChanged.connect(self.image_update)

        self.en_unit = QtWidgets.QLineEdit(self.centralwidget)
        self.en_unit.setGeometry(QtCore.QRect(380, 80, 81, 21))
        self.en_unit.setObjectName("en_unit")
        self.en_unit.textChanged.connect(self.image_update)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # save = QtWidgets.QPushButton('导出',self)
        # save.setGeometry(50, 50, 200, 100)

        self.save = QtWidgets.QPushButton('导出', MainWindow)
        self.save.setGeometry(QtCore.QRect(670, 470, 93, 28))
        self.save.setObjectName("save")
        self.save.clicked.connect(self.s)

        

        self.im = QtWidgets.QLabel(self.centralwidget)
        self.im.setGeometry(QtCore.QRect(20, 120, 800, 400))
        self.im.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.im.setObjectName("im")


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
    
        # path,yes = QtWidgets.QFileDialog.getSaveFileName(MainWindow,'保存','','PNG(*.png)')
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cn_event.setText(_translate("MainWindow", "空间站坠毁"))
        self.title.setText(_translate("MainWindow", "<html><head/><body><p>流浪地球倒计时生成</p><p><br/></p></body></html>"))
        self.cn_tip.setText(_translate("MainWindow", "距\t\t\t           还有"))
        self.cn_num.setText(_translate("MainWindow", "35"))
        self.cn_unit.setText(_translate("MainWindow", "分钟"))
        self.en_tip.setText(_translate("MainWindow", "IN"))
        self.en_event.setText(_translate("MainWindow", "THE SPACE STATION CRASH"))
        self.en_num.setText(_translate("MainWindow", "35"))
        self.en_unit.setText(_translate("MainWindow", "MINUTES"))
        self.save.setText(_translate("MainWindow", "导出"))
        # self.im.setText(_translate("MainWindow", "AAAAAAAAAAAAAAAAAA"))

    def image_update (self):

        print('Image Update')
        
        self.pic = Image.new('RGBA', (800, 400))
        draw = ImageDraw.Draw(self.pic)
        font = ImageFont.truetype('{}\\font\\zh-cn.ttf'.format(os.path.dirname(__file__)),size=34)
        
        font2 = ImageFont.truetype('{}\\font\\en-nu.ttf'.format(os.path.dirname(__file__)),size=84)

        draw.text((10, 10), "距{}".format(self.cn_event.text()), font=font, fill=(255, 255, 255))
        a = (len(self.cn_event.text()) - 2) * 34
        draw.rectangle([(a + 33,54), (a + 33 + 4,75 + 54)], fill='red')
        draw.text((a + 43, 50), "还剩", font=font, fill=(255, 255, 255))
        draw.text((a + 115, 0), self.cn_num.text(), font=font2, fill='red')
        draw.text((a + 115 + len(str(self.cn_num.text())) * 40 + 5, 50), self.cn_unit.text(), font=font, fill=(255, 255, 255))

        long = 0
        for i in self.en_event.text():
            if i == ' ':
                long += 0.5
            else:
                long += 1
            
            # pass
        # print(long)
        if long != 0:
            b = len(str(self.cn_num.text())) * 40 + 115
            
            # print(b)
            size = int(b / long * 1.9293)
            font3 = ImageFont.truetype('{}\\font\\en-nu.ttf'.format(os.path.dirname(__file__)),size=size)
            print(size)
            draw.text((a + 47, 90),self.en_event.text(),font=font3)
            draw.text((a + 47, 110),'IN {} {}'.format(self.en_num.text(),self.en_unit.text()),font=font3)

        qimage = QtGui.QPixmap.fromImage(ImageQt.toqimage(self.pic))
        self.im.setPixmap(qimage)
        
    def s (self):
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, '导出', '', 'PNG(*.png)')
        if file_path:
            self.pic.save(file_path, "PNG")

if __name__ == "__main__":
    # print(os.path.dirname(__file__))
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
