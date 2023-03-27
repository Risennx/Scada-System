from PyQt5 import QtCore, QtGui, QtWidgets
import snap7
from snap7 import util

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(980, 430)
        MainWindow.setStyleSheet("background-color: rgb(182, 182, 182);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(750, 10, 125, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 50, 424, 114))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setEnabled(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_10.addWidget(self.label)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.i_PV = QtWidgets.QLCDNumber(self.layoutWidget)
        self.i_PV.setObjectName("i_PV")
        self.horizontalLayout_6.addWidget(self.i_PV)
        self.verticalLayout_10.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7.addLayout(self.verticalLayout_10)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 180, 234, 131))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_9.addWidget(self.label_7)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_15 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_8.addWidget(self.label_15)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_8.addWidget(self.label_14)
        self.horizontalLayout_5.addLayout(self.verticalLayout_8)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.i_SP = QtWidgets.QLCDNumber(self.layoutWidget1)
        self.i_SP.setObjectName("i_SP")
        self.verticalLayout_7.addWidget(self.i_SP)
        self.o_SP = QtWidgets.QLineEdit(self.layoutWidget1)
        self.o_SP.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.o_SP.setObjectName("o_SP")
        self.verticalLayout_7.addWidget(self.o_SP)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)
        self.load_SP = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.load_SP.setFont(font)
        self.load_SP.setObjectName("load_SP")
        self.verticalLayout_9.addWidget(self.load_SP)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(30, 340, 295, 35))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.o_stop = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.o_stop.setFont(font)
        self.o_stop.setObjectName("o_stop")
        self.horizontalLayout_4.addWidget(self.o_stop)
        self.o_start = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.o_start.setFont(font)
        self.o_start.setObjectName("o_start")
        self.horizontalLayout_4.addWidget(self.o_start)
        self.o_reset = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.o_reset.setFont(font)
        self.o_reset.setObjectName("o_reset")
        self.horizontalLayout_4.addWidget(self.o_reset)
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(470, 50, 475, 248))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.o_P1 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.o_P1.setAutoFillBackground(False)
        self.o_P1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.o_P1.setObjectName("o_P1")
        self.verticalLayout_2.addWidget(self.o_P1)
        self.o_I1 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.o_I1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.o_I1.setObjectName("o_I1")
        self.verticalLayout_2.addWidget(self.o_I1)
        self.o_D1 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.o_D1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.o_D1.setObjectName("o_D1")
        self.verticalLayout_2.addWidget(self.o_D1)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.i_P1 = QtWidgets.QLCDNumber(self.layoutWidget3)
        self.i_P1.setObjectName("i_P1")
        self.verticalLayout.addWidget(self.i_P1)
        self.i_I1 = QtWidgets.QLCDNumber(self.layoutWidget3)
        self.i_I1.setObjectName("i_I1")
        self.verticalLayout.addWidget(self.i_I1)
        self.i_D1 = QtWidgets.QLCDNumber(self.layoutWidget3)
        self.i_D1.setObjectName("i_D1")
        self.verticalLayout.addWidget(self.i_D1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.load_PID1 = QtWidgets.QPushButton(self.layoutWidget3)
        self.load_PID1.setObjectName("load_PID1")
        self.gridLayout.addWidget(self.load_PID1, 1, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_4.addWidget(self.label_11)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_5.addWidget(self.label_12)
        self.o_P2 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.o_P2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.o_P2.setObjectName("o_P2")
        self.verticalLayout_5.addWidget(self.o_P2)
        self.o_I2 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.o_I2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.o_I2.setObjectName("o_I2")
        self.verticalLayout_5.addWidget(self.o_I2)
        self.o_D2 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.o_D2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.o_D2.setObjectName("o_D2")
        self.verticalLayout_5.addWidget(self.o_D2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_6.addWidget(self.label_13)
        self.i_P2 = QtWidgets.QLCDNumber(self.layoutWidget3)
        self.i_P2.setObjectName("i_P2")
        self.verticalLayout_6.addWidget(self.i_P2)
        self.i_I2 = QtWidgets.QLCDNumber(self.layoutWidget3)
        self.i_I2.setObjectName("i_I2")
        self.verticalLayout_6.addWidget(self.i_I2)
        self.i_D2 = QtWidgets.QLCDNumber(self.layoutWidget3)
        self.i_D2.setObjectName("i_D2")
        self.verticalLayout_6.addWidget(self.i_D2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.load_PID2 = QtWidgets.QPushButton(self.layoutWidget3)
        self.load_PID2.setObjectName("load_PID2")
        self.gridLayout_2.addWidget(self.load_PID2, 1, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_11.addLayout(self.horizontalLayout_3)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_11.addWidget(self.comboBox)
        self.connect = QtWidgets.QPushButton(self.centralwidget)
        self.connect.setGeometry(QtCore.QRect(30, 10, 201, 33))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.connect.setFont(font)
        self.connect.setObjectName("connect")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 980, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuedit = QtWidgets.QMenu(self.menubar)
        self.menuedit.setObjectName("menuedit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionnew = QtWidgets.QAction(MainWindow)
        self.actionnew.setObjectName("actionnew")
        self.actionedit = QtWidgets.QAction(MainWindow)
        self.actionedit.setObjectName("actionedit")
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setObjectName("actionsave")
        self.actionsave_as = QtWidgets.QAction(MainWindow)
        self.actionsave_as.setObjectName("actionsave_as")
        self.menuFile.addAction(self.actionnew)
        self.menuFile.addAction(self.actionedit)
        self.menuFile.addAction(self.actionsave)
        self.menuFile.addAction(self.actionsave_as)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuedit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Proces napełniania zbiornika</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Aktualne napełnienie: </span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Wartość zadana: </span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Aktualna:</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Nowa:</span></p></body></html>"))
        self.o_SP.setText(_translate("MainWindow", "0"))
        self.load_SP.setText(_translate("MainWindow", "Zapisz"))
        self.o_stop.setText(_translate("MainWindow", "STOP"))
        self.o_start.setText(_translate("MainWindow", "START"))
        self.o_reset.setText(_translate("MainWindow", "RESET"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">PID 1</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Wprowadź<br/>nastawy:</span></p></body></html>"))
        self.o_P1.setText(_translate("MainWindow", "0"))
        self.o_I1.setText(_translate("MainWindow", "0"))
        self.o_D1.setText(_translate("MainWindow", "0"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Aktualne <br/>nastawy:</span></p></body></html>"))
        self.load_PID1.setText(_translate("MainWindow", "Zapisz"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">PID 2</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Wprowadź<br/>nastawy:</span></p></body></html>"))
        self.o_P2.setText(_translate("MainWindow", "0"))
        self.o_I2.setText(_translate("MainWindow", "0"))
        self.o_D2.setText(_translate("MainWindow", "0"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Aktualne <br/>nastawy:</span></p></body></html>"))
        self.load_PID2.setText(_translate("MainWindow", "Zapisz"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Automatyczne nastawy PID"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Manualne nastawy PID"))
        self.connect.setText(_translate("MainWindow", "Połącz z PLC"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuedit.setTitle(_translate("MainWindow", "edit"))
        self.actionnew.setText(_translate("MainWindow", "new"))
        self.actionedit.setText(_translate("MainWindow", "edit"))
        self.actionsave.setText(_translate("MainWindow", "save"))
        self.actionsave_as.setText(_translate("MainWindow", "save as"))


    def refValue(self):
        global i_PV, i_SPOINT, i_P1, i_I1, i_D1, i_P2, i_I2, i_D2, mode
        self.i_PV.display(i_PV)
        self.i_SP.display(i_SPOINT)
        self.i_P1.display(i_P1)
        self.i_I1.display(i_I1)
        self.i_D1.display(i_D1)
        self.i_P2.display(i_P2)
        self.i_I2.display(i_I2)
        self.i_D2.display(i_D2)

    def loadValueSp(self):
        global o_SPOINT, mode
        o_SPOINT = float(self.o_SP.text())
        mode = self.comboBox.currentIndex()

    def loadValuePid1(self):
        global o_P1, o_I1, o_D1
        o_P1 = float(self.o_P1.text())
        o_I1 = float(self.o_I1.text())
        o_D1 = float(self.o_D1.text())


    def loadValuePid2(self):
        global o_P2, o_I2, o_D2
        o_P2 = float(self.o_P2.text())
        o_I2 = float(self.o_I2.text())
        o_D2 = float(self.o_D2.text())

######################################################################################################

def plcConnect():
    try:
        plc.connect(IP, RACK, SLOT)
        print(plc.get_cpu_state())
    except:
        print('Unreachable peer')


def writeInt(db_num, start, value):
    data = bytearray(2)
    snap7.util.set_int(data, 0, value)
    plc.db_write(db_num, start, data)


def writeReal(db_num, start, value):
    try:
        data = bytearray(4)
        snap7.util.set_real(data, 0, value)
        plc.db_write(db_num, start, data)
    except:
        print('write real failure')

def writeByte(db_num, start, value):
    data = bytearray(1)
    snap7.util.set_byte(data, 0, value)
    plc.db_write(db_num, start, data)


def writeBool(db_num, start, index, value):
    data = bytearray(1)
    snap7.util.set_bool(data, 0, index, value)
    plc.db_write(db_num, start, data)

global i_PV, i_SPOINT, i_P1, i_I1, i_D1, i_P2, i_I2, i_D2,mode
i_PV=0
i_SPOINT=0
i_P1=0
i_I1=0
i_D1=0
i_P2=0
i_I2=0
i_D2=0
mode=0

global o_SPOINT, o_P1, o_I1, o_D1, o_P2, o_I2, o_D2
o_SPOINT=0
o_P1=0
o_I1=0
o_D1=0
o_P2=0
o_I2=0
o_D2=0



def getFromPlc():
    global i_PV, i_SPOINT, i_P1, i_I1, i_D1, i_P2, i_I2, i_D2
    if plc.get_cpu_state() == 'S7CpuStatusRun':
        try:
            i_SPOINT = util.get_real(plc.db_read(DB, 138, 4), 0)
            i_PV = util.get_real(plc.db_read(DB, 142, 4), 0)
            i_P1 = util.get_real(plc.db_read(DB, 150, 4), 0)
            i_I1 = util.get_real(plc.db_read(DB, 154, 4), 0)
            i_D1 = util.get_real(plc.db_read(DB, 158, 4), 0)
            i_P2 = util.get_real(plc.db_read(DB, 214, 4), 0)
            i_I2 = util.get_real(plc.db_read(DB, 218, 4), 0)
            i_D2 = util.get_real(plc.db_read(DB, 222, 4), 0)
            print(i_SPOINT)
        except:
            print("read error")



def sendValueSp():
    global o_SPOINT
    try:
        writeReal(DB, 2, o_SPOINT)
    except:
        print("unable to write set point")

def sendValuePid1():
    global o_P1, o_I1, o_D1
    try:
        writeReal(DB, 8, o_P1)
        writeReal(DB, 12, o_I1)
        writeReal(DB, 16, o_D1)
    except:
        print("unable to write to pid1")

def sendValuePid2():
    global o_P2, o_I2, o_D2
    try:
        writeReal(DB, 72, o_P2)
        writeReal(DB, 76, o_I2)
        writeReal(DB, 80, o_D2)
    except:
        print('unable to write to pid2')

def startClick():
    try:
        writeBool(DB, 0, 2, 1)
    except:
        print('Unable to set start')

def stopClick():
    try:
        writeBool(DB, 0, 3, 1)
    except:
        print('unable to stop')

def resetClick():
    try:
        writeBool(DB, 0, 4, 1)
    except:
        print('unable to stop')

def sendModeData():
    if plc.get_cpu_state() == 'S7CpuStatusRun':
        try:
            writeInt(DB, 6, mode)
        except:
            print('unable to send data')


########## ZMIENNE PLC
IP = '192.168.0.1'
RACK = 0
SLOT = 0
DB = 100
plc = snap7.client.Client()
###########


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ########## function declarations
    ui.connect.clicked.connect(plcConnect)
    ui.load_SP.clicked.connect(sendValueSp)
    ui.load_PID1.clicked.connect(sendValuePid1)
    ui.load_PID2.clicked.connect(sendValuePid2)
    ui.o_start.clicked.connect(startClick)
    ui.o_stop.clicked.connect(stopClick)
    ui.o_reset.clicked.connect(resetClick)
    fps = 10
    timer = QtCore.QTimer()
    timer.timeout.connect(getFromPlc)
    timer.timeout.connect(ui.loadValueSp)
    timer.timeout.connect(ui.loadValuePid1)
    timer.timeout.connect(ui.loadValuePid2)
    timer.timeout.connect(sendModeData)
    timer.timeout.connect(ui.refValue)
    timer.setInterval(int(1000 / fps))
    timer.start()
    ##########
    MainWindow.show()
    sys.exit(app.exec_())
