# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(834, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.group_receta_dia = QGroupBox(self.centralwidget)
        self.group_receta_dia.setObjectName(u"group_receta_dia")
        self.group_receta_dia.setGeometry(QRect(200, 20, 611, 511))
        font = QFont()
        font.setPointSize(10)
        self.group_receta_dia.setFont(font)
        self.label_imagen_receta = QLabel(self.group_receta_dia)
        self.label_imagen_receta.setObjectName(u"label_imagen_receta")
        self.label_imagen_receta.setGeometry(QRect(30, 40, 551, 281))
        self.label_imagen_receta.setFrameShape(QFrame.StyledPanel)
        self.label_imagen_receta.setAlignment(Qt.AlignCenter)
        self.label_titulo_receta = QLabel(self.group_receta_dia)
        self.label_titulo_receta.setObjectName(u"label_titulo_receta")
        self.label_titulo_receta.setGeometry(QRect(30, 340, 551, 41))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.label_titulo_receta.setFont(font1)
        self.label_titulo_receta.setAlignment(Qt.AlignCenter)
        self.btn_ver_receta = QPushButton(self.group_receta_dia)
        self.btn_ver_receta.setObjectName(u"btn_ver_receta")
        self.btn_ver_receta.setGeometry(QRect(240, 410, 131, 41))
        font2 = QFont()
        font2.setPointSize(11)
        self.btn_ver_receta.setFont(font2)
        self.btn_menu = QPushButton(self.centralwidget)
        self.btn_menu.setObjectName(u"btn_menu")
        self.btn_menu.setGeometry(QRect(20, 20, 51, 41))
        font3 = QFont()
        font3.setPointSize(14)
        self.btn_menu.setFont(font3)
        self.frame_menu_lateral = QFrame(self.centralwidget)
        self.frame_menu_lateral.setObjectName(u"frame_menu_lateral")
        self.frame_menu_lateral.setGeometry(QRect(10, 80, 181, 451))
        self.frame_menu_lateral.setFrameShape(QFrame.StyledPanel)
        self.frame_menu_lateral.setFrameShadow(QFrame.Raised)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 834, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Mi Recetario", None))
        self.group_receta_dia.setTitle(QCoreApplication.translate("MainWindow", u"Receta del D\u00eda", None))
        self.label_imagen_receta.setText(QCoreApplication.translate("MainWindow", u"Aqui va la imagen de la receta", None))
        self.label_titulo_receta.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo de la Receta", None))
        self.btn_ver_receta.setText(QCoreApplication.translate("MainWindow", u"Ver Receta", None))
        self.btn_menu.setText(QCoreApplication.translate("MainWindow", u"\u2630", None))
    # retranslateUi

