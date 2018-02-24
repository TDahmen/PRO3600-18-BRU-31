# -*- coding: utf-8 -*-

"""
@author: Thomas Dahmen
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import echecs

class Ui_Dialog(object):
    def setupUi(self, Dialog):

        # Initialisation de la fenêtre
        Dialog.setObjectName("Dialog")
        Dialog.resize(772, 782)

        # Initialisation du plateau (sans les pièces)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 891, 761))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("board.png"))
        self.label.setObjectName("label")

        # Initialisation des pièces blanches
        self.tour1B = QtWidgets.QPushButton(Dialog) # C'est un bouton
        self.tour1B.setGeometry(QtCore.QRect(10, 670, 101, 91))
        self.tour1B.setText("")
        self.tour1B.setObjectName("tour1B")
        self.cavalier1B = QtWidgets.QPushButton(Dialog)
        self.cavalier1B.setGeometry(QtCore.QRect(100, 670, 101, 90))
        self.cavalier1B.setText("")
        self.cavalier1B.setObjectName("cavalier1B")
        self.fou1B = QtWidgets.QPushButton(Dialog)
        self.fou1B.setGeometry(QtCore.QRect(200, 670, 101, 91))
        self.fou1B.setText("")
        self.fou1B.setObjectName("fou1B")
        self.reineB = QtWidgets.QPushButton(Dialog)
        self.reineB.setGeometry(QtCore.QRect(290, 670, 101, 91))
        self.reineB.setText("")
        self.reineB.setObjectName("reineB")
        self.roiB = QtWidgets.QPushButton(Dialog)
        self.roiB.setGeometry(QtCore.QRect(380, 670, 101, 91))
        self.roiB.setText("")
        self.roiB.setObjectName("roiB")
        self.fou2B = QtWidgets.QPushButton(Dialog)
        self.fou2B.setGeometry(QtCore.QRect(470, 670, 101, 91))
        self.fou2B.setText("")
        self.fou2B.setObjectName("fou2B")
        self.cavalier2B = QtWidgets.QPushButton(Dialog)
        self.cavalier2B.setGeometry(QtCore.QRect(560, 670, 101, 91))
        self.cavalier2B.setText("")
        self.cavalier2B.setObjectName("cavalier2B")
        self.tour2B = QtWidgets.QPushButton(Dialog)
        self.tour2B.setGeometry(QtCore.QRect(650, 670, 101, 91))
        self.tour2B.setText("")
        self.tour2B.setObjectName("tour2B")
        self.pion1B = QtWidgets.QPushButton(Dialog)
        self.pion1B.setGeometry(QtCore.QRect(10, 580, 101, 91))
        self.pion1B.setText("")
        self.pion1B.setObjectName("pion1B")
        self.pion2B = QtWidgets.QPushButton(Dialog)
        self.pion2B.setGeometry(QtCore.QRect(100, 580, 101, 91))
        self.pion2B.setText("")
        self.pion2B.setObjectName("pion2B")
        self.pion3B = QtWidgets.QPushButton(Dialog)
        self.pion3B.setGeometry(QtCore.QRect(190, 580, 101, 91))
        self.pion3B.setText("")
        self.pion3B.setObjectName("pion3B")
        self.pion4B = QtWidgets.QPushButton(Dialog)
        self.pion4B.setGeometry(QtCore.QRect(290, 580, 101, 91))
        self.pion4B.setText("")
        self.pion4B.setObjectName("pion4B")
        self.pion5B = QtWidgets.QPushButton(Dialog)
        self.pion5B.setGeometry(QtCore.QRect(380, 580, 101, 91))
        self.pion5B.setText("")
        self.pion5B.setObjectName("pion5B")
        self.pion6B = QtWidgets.QPushButton(Dialog)
        self.pion6B.setGeometry(QtCore.QRect(470, 580, 101, 91))
        self.pion6B.setText("")
        self.pion6B.setObjectName("pion6B")
        self.pion7B = QtWidgets.QPushButton(Dialog)
        self.pion7B.setGeometry(QtCore.QRect(560, 580, 101, 91))
        self.pion7B.setText("")
        self.pion7B.setObjectName("pion7B")
        self.pion8B = QtWidgets.QPushButton(Dialog)
        self.pion8B.setGeometry(QtCore.QRect(650, 580, 101, 91))
        self.pion8B.setText("")
        self.pion8B.setObjectName("pion8B")

        # Initialisation des pièces noires
        self.pion1N = QtWidgets.QPushButton(Dialog)
        self.pion1N.setGeometry(QtCore.QRect(10, 120, 101, 91))
        self.pion1N.setText("")
        self.pion1N.setObjectName("pion1N")
        self.pion2N = QtWidgets.QPushButton(Dialog)
        self.pion2N.setGeometry(QtCore.QRect(100, 120, 101, 91))
        self.pion2N.setText("")
        self.pion2N.setObjectName("pion2N")
        self.pion3N = QtWidgets.QPushButton(Dialog)
        self.pion3N.setGeometry(QtCore.QRect(190, 120, 101, 91))
        self.pion3N.setText("")
        self.pion3N.setObjectName("pion3N")
        self.pion4N = QtWidgets.QPushButton(Dialog)
        self.pion4N.setGeometry(QtCore.QRect(290, 120, 101, 91))
        self.pion4N.setText("")
        self.pion4N.setObjectName("pion4N")
        self.pion5N = QtWidgets.QPushButton(Dialog)
        self.pion5N.setGeometry(QtCore.QRect(380, 120, 101, 91))
        self.pion5N.setText("")
        self.pion5N.setObjectName("pion5N")
        self.pion6N = QtWidgets.QPushButton(Dialog)
        self.pion6N.setGeometry(QtCore.QRect(470, 120, 101, 91))
        self.pion6N.setText("")
        self.pion6N.setObjectName("pion6N")
        self.pion7N = QtWidgets.QPushButton(Dialog)
        self.pion7N.setGeometry(QtCore.QRect(560, 120, 101, 91))
        self.pion7N.setText("")
        self.pion7N.setObjectName("pion7N")
        self.pion8N = QtWidgets.QPushButton(Dialog)
        self.pion8N.setGeometry(QtCore.QRect(650, 120, 101, 91))
        self.pion8N.setText("")
        self.pion8N.setObjectName("pion8N")
        self.tour1N = QtWidgets.QPushButton(Dialog)
        self.tour1N.setGeometry(QtCore.QRect(10, 30, 101, 91))
        self.tour1N.setText("")
        self.tour1N.setObjectName("tour1N")
        self.cavalier1N = QtWidgets.QPushButton(Dialog)
        self.cavalier1N.setGeometry(QtCore.QRect(100, 30, 101, 90))
        self.cavalier1N.setText("")
        self.cavalier1N.setObjectName("cavalier1N")
        self.fou1N = QtWidgets.QPushButton(Dialog)
        self.fou1N.setGeometry(QtCore.QRect(200, 30, 101, 91))
        self.fou1N.setText("")
        self.fou1N.setObjectName("fou1N")
        self.reineN = QtWidgets.QPushButton(Dialog)
        self.reineN.setGeometry(QtCore.QRect(290, 30, 101, 91))
        self.reineN.setText("")
        self.reineN.setObjectName("reineN")
        self.roiN = QtWidgets.QPushButton(Dialog)
        self.roiN.setGeometry(QtCore.QRect(380, 30, 101, 91))
        self.roiN.setText("")
        self.roiN.setObjectName("roiN")
        self.fou2N = QtWidgets.QPushButton(Dialog)
        self.fou2N.setGeometry(QtCore.QRect(470, 30, 101, 91))
        self.fou2N.setText("")
        self.fou2N.setObjectName("fou2N")
        self.cavalier2N = QtWidgets.QPushButton(Dialog)
        self.cavalier2N.setGeometry(QtCore.QRect(560, 30, 101, 91))
        self.cavalier2N.setText("")
        self.cavalier2N.setObjectName("cavalier2N")
        self.tour2N = QtWidgets.QPushButton(Dialog)
        self.tour2N.setGeometry(QtCore.QRect(650, 30, 101, 91))
        self.tour2N.setText("")
        self.tour2N.setObjectName("tour2N")

        # On assigne les images aux pièces

        self.tour1B.setFlat(True)
        self.tour1B.setStyleSheet('border:none')
        self.tour1B.setIcon(QtGui.QIcon("tour1B.png"))
        self.tour1B.setIconSize(QtCore.QSize(60, 60))

        self.cavalier1B.setFlat(True)
        self.cavalier1B.setStyleSheet('border:none')
        self.cavalier1B.setIcon(QtGui.QIcon("cavalier1B.png"))
        self.cavalier1B.setIconSize(QtCore.QSize(60, 60))

        self.fou1B.setFlat(True)
        self.fou1B.setStyleSheet('border:none')
        self.fou1B.setIcon(QtGui.QIcon("fou1B.png"))
        self.fou1B.setIconSize(QtCore.QSize(60, 60))

        self.reineB.setFlat(True)
        self.reineB.setStyleSheet('border:none')
        self.reineB.setIcon(QtGui.QIcon("reineB.png"))
        self.reineB.setIconSize(QtCore.QSize(60, 60))

        self.roiB.setFlat(True)
        self.roiB.setStyleSheet('border:none')
        self.roiB.setIcon(QtGui.QIcon("roiB.png"))
        self.roiB.setIconSize(QtCore.QSize(60, 60))

        self.tour2B.setFlat(True)
        self.tour2B.setStyleSheet('border:none')
        self.tour2B.setIcon(QtGui.QIcon("tour2B.png"))
        self.tour2B.setIconSize(QtCore.QSize(60, 60))

        self.cavalier2B.setFlat(True)
        self.cavalier2B.setStyleSheet('border:none')
        self.cavalier2B.setIcon(QtGui.QIcon("cavalier2B.png"))
        self.cavalier2B.setIconSize(QtCore.QSize(60, 60))

        self.fou2B.setFlat(True)
        self.fou2B.setStyleSheet('border:none')
        self.fou2B.setIcon(QtGui.QIcon("fou2B.png"))
        self.fou2B.setIconSize(QtCore.QSize(60, 60))

        self.pion1B.setFlat(True)
        self.pion1B.setStyleSheet('border:none')
        self.pion1B.setIcon(QtGui.QIcon("pion1B.png"))
        self.pion1B.setIconSize(QtCore.QSize(60, 60))

        self.pion2B.setFlat(True)
        self.pion2B.setStyleSheet('border:none')
        self.pion2B.setIcon(QtGui.QIcon("pion2B.png"))
        self.pion2B.setIconSize(QtCore.QSize(60, 60))

        self.pion3B.setFlat(True)
        self.pion3B.setStyleSheet('border:none')
        self.pion3B.setIcon(QtGui.QIcon("pion3B.png"))
        self.pion3B.setIconSize(QtCore.QSize(60, 60))

        self.pion4B.setFlat(True)
        self.pion4B.setStyleSheet('border:none')
        self.pion4B.setIcon(QtGui.QIcon("pion4B.png"))
        self.pion4B.setIconSize(QtCore.QSize(60, 60))

        self.pion5B.setFlat(True)
        self.pion5B.setStyleSheet('border:none')
        self.pion5B.setIcon(QtGui.QIcon("pion5B.png"))
        self.pion5B.setIconSize(QtCore.QSize(60, 60))

        self.pion6B.setFlat(True)
        self.pion6B.setStyleSheet('border:none')
        self.pion6B.setIcon(QtGui.QIcon("pion6B.png"))
        self.pion6B.setIconSize(QtCore.QSize(60, 60))

        self.pion7B.setFlat(True)
        self.pion7B.setStyleSheet('border:none')
        self.pion7B.setIcon(QtGui.QIcon("pion7B.png"))
        self.pion7B.setIconSize(QtCore.QSize(60, 60))

        self.pion8B.setFlat(True)
        self.pion8B.setStyleSheet('border:none')
        self.pion8B.setIcon(QtGui.QIcon("pion8B.png"))
        self.pion8B.setIconSize(QtCore.QSize(60, 60))

        self.tour1N.setFlat(True)
        self.tour1N.setStyleSheet('border:none')
        self.tour1N.setIcon(QtGui.QIcon("tour1N.png"))
        self.tour1N.setIconSize(QtCore.QSize(60, 60))

        self.cavalier1N.setFlat(True)
        self.cavalier1N.setStyleSheet('border:none')
        self.cavalier1N.setIcon(QtGui.QIcon("cavalier1N.png"))
        self.cavalier1N.setIconSize(QtCore.QSize(60, 60))

        self.fou1N.setFlat(True)
        self.fou1N.setStyleSheet('border:none')
        self.fou1N.setIcon(QtGui.QIcon("fou1N.png"))
        self.fou1N.setIconSize(QtCore.QSize(60, 60))

        self.reineN.setFlat(True)
        self.reineN.setStyleSheet('border:none')
        self.reineN.setIcon(QtGui.QIcon("reineN.png"))
        self.reineN.setIconSize(QtCore.QSize(60, 60))

        self.roiN.setFlat(True)
        self.roiN.setStyleSheet('border:none')
        self.roiN.setIcon(QtGui.QIcon("roiN.png"))
        self.roiN.setIconSize(QtCore.QSize(60, 60))

        self.tour2N.setFlat(True)
        self.tour2N.setStyleSheet('border:none')
        self.tour2N.setIcon(QtGui.QIcon("tour2N.png"))
        self.tour2N.setIconSize(QtCore.QSize(60, 60))

        self.cavalier2N.setFlat(True)
        self.cavalier2N.setStyleSheet('border:none')
        self.cavalier2N.setIcon(QtGui.QIcon("cavalier2N.png"))
        self.cavalier2N.setIconSize(QtCore.QSize(60, 60))

        self.fou2N.setFlat(True)
        self.fou2N.setStyleSheet('border:none')
        self.fou2N.setIcon(QtGui.QIcon("fou2N.png"))
        self.fou2N.setIconSize(QtCore.QSize(60, 60))

        self.pion1N.setFlat(True)
        self.pion1N.setStyleSheet('border:none')
        self.pion1N.setIcon(QtGui.QIcon("pion1N.png"))
        self.pion1N.setIconSize(QtCore.QSize(60, 60))

        self.pion2N.setFlat(True)
        self.pion2N.setStyleSheet('border:none')
        self.pion2N.setIcon(QtGui.QIcon("pion2N.png"))
        self.pion2N.setIconSize(QtCore.QSize(60, 60))

        self.pion3N.setFlat(True)
        self.pion3N.setStyleSheet('border:none')
        self.pion3N.setIcon(QtGui.QIcon("pion3N.png"))
        self.pion3N.setIconSize(QtCore.QSize(60, 60))

        self.pion4N.setFlat(True)
        self.pion4N.setStyleSheet('border:none')
        self.pion4N.setIcon(QtGui.QIcon("pion4N.png"))
        self.pion4N.setIconSize(QtCore.QSize(60, 60))

        self.pion5N.setFlat(True)
        self.pion5N.setStyleSheet('border:none')
        self.pion5N.setIcon(QtGui.QIcon("pion5N.png"))
        self.pion5N.setIconSize(QtCore.QSize(60, 60))

        self.pion6N.setFlat(True)
        self.pion6N.setStyleSheet('border:none')
        self.pion6N.setIcon(QtGui.QIcon("pion6N.png"))
        self.pion6N.setIconSize(QtCore.QSize(60, 60))

        self.pion7N.setFlat(True)
        self.pion7N.setStyleSheet('border:none')
        self.pion7N.setIcon(QtGui.QIcon("pion7N.png"))
        self.pion7N.setIconSize(QtCore.QSize(60, 60))

        self.pion8N.setFlat(True)
        self.pion8N.setStyleSheet('border:none')
        self.pion8N.setIcon(QtGui.QIcon("pion8N.png"))
        self.pion8N.setIconSize(QtCore.QSize(60, 60))

        # Initialisation des cases vides

        self.vide_1 = QtWidgets.QPushButton(Dialog)
        self.vide_1.setGeometry(QtCore.QRect(10, 490, 101, 91))
        self.vide_1.setText("")
        self.vide_1.setObjectName("vide_1")
        self.vide_2 = QtWidgets.QPushButton(Dialog)
        self.vide_2.setGeometry(QtCore.QRect(100, 490, 101, 91))
        self.vide_2.setText("")
        self.vide_2.setObjectName("vide_2")
        self.vide_3 = QtWidgets.QPushButton(Dialog)
        self.vide_3.setGeometry(QtCore.QRect(200, 490, 101, 91))
        self.vide_3.setText("")
        self.vide_3.setObjectName("vide_3")
        self.vide_4 = QtWidgets.QPushButton(Dialog)
        self.vide_4.setGeometry(QtCore.QRect(290, 490, 101, 91))
        self.vide_4.setText("")
        self.vide_4.setObjectName("vide_4")
        self.vide_5 = QtWidgets.QPushButton(Dialog)
        self.vide_5.setGeometry(QtCore.QRect(380, 490, 101, 91))
        self.vide_5.setText("")
        self.vide_5.setObjectName("vide_5")
        self.vide_6 = QtWidgets.QPushButton(Dialog)
        self.vide_6.setGeometry(QtCore.QRect(470, 490, 101, 91))
        self.vide_6.setText("")
        self.vide_6.setObjectName("vide_6")
        self.vide_7 = QtWidgets.QPushButton(Dialog)
        self.vide_7.setGeometry(QtCore.QRect(560, 490, 101, 91))
        self.vide_7.setText("")
        self.vide_7.setObjectName("vide_7")
        self.vide_8 = QtWidgets.QPushButton(Dialog)
        self.vide_8.setGeometry(QtCore.QRect(650, 490, 101, 91))
        self.vide_8.setText("")
        self.vide_8.setObjectName("vide_8")
        self.vide_9 = QtWidgets.QPushButton(Dialog)
        self.vide_9.setGeometry(QtCore.QRect(10, 390, 101, 91))
        self.vide_9.setText("")
        self.vide_9.setObjectName("vide_9")
        self.vide_10 = QtWidgets.QPushButton(Dialog)
        self.vide_10.setGeometry(QtCore.QRect(100, 390, 101, 91))
        self.vide_10.setText("")
        self.vide_10.setObjectName("vide_10")
        self.vide_11 = QtWidgets.QPushButton(Dialog)
        self.vide_11.setGeometry(QtCore.QRect(200, 390, 101, 91))
        self.vide_11.setText("")
        self.vide_11.setObjectName("vide_11")
        self.vide_12 = QtWidgets.QPushButton(Dialog)
        self.vide_12.setGeometry(QtCore.QRect(290, 390, 101, 91))
        self.vide_12.setText("")
        self.vide_12.setObjectName("vide_12")
        self.vide_13 = QtWidgets.QPushButton(Dialog)
        self.vide_13.setGeometry(QtCore.QRect(380, 390, 101, 91))
        self.vide_13.setText("")
        self.vide_13.setObjectName("vide_13")
        self.vide_14 = QtWidgets.QPushButton(Dialog)
        self.vide_14.setGeometry(QtCore.QRect(470, 390, 101, 91))
        self.vide_14.setText("")
        self.vide_14.setObjectName("vide_14")
        self.vide_15 = QtWidgets.QPushButton(Dialog)
        self.vide_15.setGeometry(QtCore.QRect(560, 390, 101, 91))
        self.vide_15.setText("")
        self.vide_15.setObjectName("vide_15")
        self.vide_16 = QtWidgets.QPushButton(Dialog)
        self.vide_16.setGeometry(QtCore.QRect(650, 390, 101, 91))
        self.vide_16.setText("")
        self.vide_16.setObjectName("vide_16")
        self.vide_17 = QtWidgets.QPushButton(Dialog)
        self.vide_17.setGeometry(QtCore.QRect(10, 300, 101, 91))
        self.vide_17.setText("")
        self.vide_17.setObjectName("vide_17")
        self.vide_18 = QtWidgets.QPushButton(Dialog)
        self.vide_18.setGeometry(QtCore.QRect(100, 300, 101, 91))
        self.vide_18.setText("")
        self.vide_18.setObjectName("vide_18")
        self.vide_19 = QtWidgets.QPushButton(Dialog)
        self.vide_19.setGeometry(QtCore.QRect(200, 300, 101, 91))
        self.vide_19.setText("")
        self.vide_19.setObjectName("vide_19")
        self.vide_20 = QtWidgets.QPushButton(Dialog)
        self.vide_20.setGeometry(QtCore.QRect(290, 300, 101, 91))
        self.vide_20.setText("")
        self.vide_20.setObjectName("vide_20")
        self.vide_21 = QtWidgets.QPushButton(Dialog)
        self.vide_21.setGeometry(QtCore.QRect(380, 300, 101, 91))
        self.vide_21.setText("")
        self.vide_21.setObjectName("vide_21")
        self.vide_22 = QtWidgets.QPushButton(Dialog)
        self.vide_22.setGeometry(QtCore.QRect(470, 300, 101, 91))
        self.vide_22.setText("")
        self.vide_22.setObjectName("vide_22")
        self.vide_23 = QtWidgets.QPushButton(Dialog)
        self.vide_23.setGeometry(QtCore.QRect(560, 300, 101, 91))
        self.vide_23.setText("")
        self.vide_23.setObjectName("vide_23")
        self.vide_24 = QtWidgets.QPushButton(Dialog)
        self.vide_24.setGeometry(QtCore.QRect(650, 300, 101, 91))
        self.vide_24.setText("")
        self.vide_24.setObjectName("vide_24")
        self.vide_25 = QtWidgets.QPushButton(Dialog)
        self.vide_25.setGeometry(QtCore.QRect(10, 210, 101, 91))
        self.vide_25.setText("")
        self.vide_25.setObjectName("vide_25")
        self.vide_26 = QtWidgets.QPushButton(Dialog)
        self.vide_26.setGeometry(QtCore.QRect(110, 210, 101, 91))
        self.vide_26.setText("")
        self.vide_26.setObjectName("vide_26")
        self.vide_27 = QtWidgets.QPushButton(Dialog)
        self.vide_27.setGeometry(QtCore.QRect(200, 210, 101, 91))
        self.vide_27.setText("")
        self.vide_27.setObjectName("vide_27")
        self.vide_28 = QtWidgets.QPushButton(Dialog)
        self.vide_28.setGeometry(QtCore.QRect(290, 210, 101, 91))
        self.vide_28.setText("")
        self.vide_28.setObjectName("vide_28")
        self.vide_29 = QtWidgets.QPushButton(Dialog)
        self.vide_29.setGeometry(QtCore.QRect(380, 210, 101, 91))
        self.vide_29.setText("")
        self.vide_29.setObjectName("vide_29")
        self.vide_30 = QtWidgets.QPushButton(Dialog)
        self.vide_30.setGeometry(QtCore.QRect(470, 210, 101, 91))
        self.vide_30.setText("")
        self.vide_30.setObjectName("vide_30")
        self.vide_31 = QtWidgets.QPushButton(Dialog)
        self.vide_31.setGeometry(QtCore.QRect(560, 210, 101, 91))
        self.vide_31.setText("")
        self.vide_31.setObjectName("vide_31")
        self.vide_32 = QtWidgets.QPushButton(Dialog)
        self.vide_32.setGeometry(QtCore.QRect(660, 210, 101, 91))
        self.vide_32.setText("")
        self.vide_32.setObjectName("vide_32")

        self.vide_1.setFlat(True)
        self.vide_1.setStyleSheet('border:none')
        self.vide_1.setIcon(QtGui.QIcon("vide.png"))
        self.vide_1.setIconSize(QtCore.QSize(60, 60))
        self.vide_2.setFlat(True)
        self.vide_2.setStyleSheet('border:none')
        self.vide_2.setIcon(QtGui.QIcon("vide.png"))
        self.vide_2.setIconSize(QtCore.QSize(60, 60))
        self.vide_3.setFlat(True)
        self.vide_3.setStyleSheet('border:none')
        self.vide_3.setIcon(QtGui.QIcon("vide.png"))
        self.vide_3.setIconSize(QtCore.QSize(60, 60))
        self.vide_4.setFlat(True)
        self.vide_4.setStyleSheet('border:none')
        self.vide_4.setIcon(QtGui.QIcon("vide.png"))
        self.vide_4.setIconSize(QtCore.QSize(60, 60))
        self.vide_5.setFlat(True)
        self.vide_5.setStyleSheet('border:none')
        self.vide_5.setIcon(QtGui.QIcon("vide.png"))
        self.vide_5.setIconSize(QtCore.QSize(60, 60))
        self.vide_6.setFlat(True)
        self.vide_6.setStyleSheet('border:none')
        self.vide_6.setIcon(QtGui.QIcon("vide.png"))
        self.vide_6.setIconSize(QtCore.QSize(60, 60))
        self.vide_7.setFlat(True)
        self.vide_7.setStyleSheet('border:none')
        self.vide_7.setIcon(QtGui.QIcon("vide.png"))
        self.vide_7.setIconSize(QtCore.QSize(60, 60))
        self.vide_8.setFlat(True)
        self.vide_8.setStyleSheet('border:none')
        self.vide_8.setIcon(QtGui.QIcon("vide.png"))
        self.vide_8.setIconSize(QtCore.QSize(60, 60))
        self.vide_9.setFlat(True)
        self.vide_9.setStyleSheet('border:none')
        self.vide_9.setIcon(QtGui.QIcon("vide.png"))
        self.vide_9.setIconSize(QtCore.QSize(60, 60))
        self.vide_10.setFlat(True)
        self.vide_10.setStyleSheet('border:none')
        self.vide_10.setIcon(QtGui.QIcon("vide.png"))
        self.vide_10.setIconSize(QtCore.QSize(60, 60))
        self.vide_11.setFlat(True)
        self.vide_11.setStyleSheet('border:none')
        self.vide_11.setIcon(QtGui.QIcon("vide.png"))
        self.vide_11.setIconSize(QtCore.QSize(60, 60))
        self.vide_12.setFlat(True)
        self.vide_12.setStyleSheet('border:none')
        self.vide_12.setIcon(QtGui.QIcon("vide.png"))
        self.vide_12.setIconSize(QtCore.QSize(60, 60))
        self.vide_13.setFlat(True)
        self.vide_13.setStyleSheet('border:none')
        self.vide_13.setIcon(QtGui.QIcon("vide.png"))
        self.vide_13.setIconSize(QtCore.QSize(60, 60))
        self.vide_14.setFlat(True)
        self.vide_14.setStyleSheet('border:none')
        self.vide_14.setIcon(QtGui.QIcon("vide.png"))
        self.vide_14.setIconSize(QtCore.QSize(60, 60))
        self.vide_15.setFlat(True)
        self.vide_15.setStyleSheet('border:none')
        self.vide_15.setIcon(QtGui.QIcon("vide.png"))
        self.vide_15.setIconSize(QtCore.QSize(60, 60))
        self.vide_16.setFlat(True)
        self.vide_16.setStyleSheet('border:none')
        self.vide_16.setIcon(QtGui.QIcon("vide.png"))
        self.vide_16.setIconSize(QtCore.QSize(60, 60))
        self.vide_17.setFlat(True)
        self.vide_17.setStyleSheet('border:none')
        self.vide_17.setIcon(QtGui.QIcon("vide.png"))
        self.vide_17.setIconSize(QtCore.QSize(60, 60))
        self.vide_18.setFlat(True)
        self.vide_18.setStyleSheet('border:none')
        self.vide_18.setIcon(QtGui.QIcon("vide.png"))
        self.vide_18.setIconSize(QtCore.QSize(60, 60))
        self.vide_19.setFlat(True)
        self.vide_19.setStyleSheet('border:none')
        self.vide_19.setIcon(QtGui.QIcon("vide.png"))
        self.vide_19.setIconSize(QtCore.QSize(60, 60))
        self.vide_20.setFlat(True)
        self.vide_20.setStyleSheet('border:none')
        self.vide_20.setIcon(QtGui.QIcon("vide.png"))
        self.vide_20.setIconSize(QtCore.QSize(60, 60))
        self.vide_21.setFlat(True)
        self.vide_21.setStyleSheet('border:none')
        self.vide_21.setIcon(QtGui.QIcon("vide.png"))
        self.vide_21.setIconSize(QtCore.QSize(60, 60))
        self.vide_22.setFlat(True)
        self.vide_22.setStyleSheet('border:none')
        self.vide_22.setIcon(QtGui.QIcon("vide.png"))
        self.vide_22.setIconSize(QtCore.QSize(60, 60))
        self.vide_23.setFlat(True)
        self.vide_23.setStyleSheet('border:none')
        self.vide_23.setIcon(QtGui.QIcon("vide.png"))
        self.vide_23.setIconSize(QtCore.QSize(60, 60))
        self.vide_24.setFlat(True)
        self.vide_24.setStyleSheet('border:none')
        self.vide_24.setIcon(QtGui.QIcon("vide.png"))
        self.vide_24.setIconSize(QtCore.QSize(60, 60))
        self.vide_25.setFlat(True)
        self.vide_25.setStyleSheet('border:none')
        self.vide_25.setIcon(QtGui.QIcon("vide.png"))
        self.vide_25.setIconSize(QtCore.QSize(60, 60))
        self.vide_26.setFlat(True)
        self.vide_26.setStyleSheet('border:none')
        self.vide_26.setIcon(QtGui.QIcon("vide.png"))
        self.vide_26.setIconSize(QtCore.QSize(60, 60))
        self.vide_27.setFlat(True)
        self.vide_27.setStyleSheet('border:none')
        self.vide_27.setIcon(QtGui.QIcon("vide.png"))
        self.vide_27.setIconSize(QtCore.QSize(60, 60))
        self.vide_28.setFlat(True)
        self.vide_28.setStyleSheet('border:none')
        self.vide_28.setIcon(QtGui.QIcon("vide.png"))
        self.vide_28.setIconSize(QtCore.QSize(60, 60))
        self.vide_29.setFlat(True)
        self.vide_29.setStyleSheet('border:none')
        self.vide_29.setIcon(QtGui.QIcon("vide.png"))
        self.vide_29.setIconSize(QtCore.QSize(60, 60))
        self.vide_30.setFlat(True)
        self.vide_30.setStyleSheet('border:none')
        self.vide_30.setIcon(QtGui.QIcon("vide.png"))
        self.vide_30.setIconSize(QtCore.QSize(60, 60))
        self.vide_31.setFlat(True)
        self.vide_31.setStyleSheet('border:none')
        self.vide_31.setIcon(QtGui.QIcon("vide.png"))
        self.vide_31.setIconSize(QtCore.QSize(60, 60))
        self.vide_32.setFlat(True)
        self.vide_32.setStyleSheet('border:none')
        self.vide_32.setIcon(QtGui.QIcon("vide.png"))
        self.vide_32.setIconSize(QtCore.QSize(60, 60))


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

        # Création du dictionnaire (correspondance avec le tableau du moteur de jeu)

        dict1 = {self.tour1B: (9,2), self.cavalier1B: (9,3), self.fou1B: (9,4), self.reineB: (9,5),
         self.roiB: (9,6), self.fou2B: (9,7), self.cavalier2B: (9,8), self.tour2B: (9,9), self.pion1B: (8,2),
         self.pion2B: (8,3), self.pion3B: (8,4), self.pion4B: (8,5), self.pion5B: (8,6), self.pion6B: (8,7),
         self.pion7B: (8,8), self.pion8B: (8,9), self.vide_25: (4,2), self.tour1N: (2,2), self.cavalier1N: (2,3), self.fou1N: (2,4), self.reineN: (2,5),
          self.roiN: (2,6), self.fou2N: (2,7), self.cavalier2N: (2,8), self.tour2N: (2,9), self.pion1N: (3,2),
          self.pion2N: (3,3), self.pion3N: (3,4), self.pion4N: (3,5), self.pion5N: (3,6), self.pion6N: (3,7),
          self.pion7N: (3,8), self.pion8N: (3,9), self.vide_25: (4,2),
         self.vide_26: (4,3),
         self.vide_27: (4,4),
         self.vide_28: (4,5),
         self.vide_29: (4,6),
         self.vide_30: (4,7),
         self.vide_31: (4,8),
         self.vide_32: (4,9),
         self.vide_17: (5,2),
         self.vide_18: (5,3),
         self.vide_19: (5,4),
         self.vide_20: (5,5),
         self.vide_21: (5,6),
         self.vide_22: (5,7),
         self.vide_23: (5,8),
         self.vide_24: (5,9),
         self.vide_9: (6,2),
         self.vide_10: (6,3),
         self.vide_11: (6,4),
         self.vide_12: (6,5),
         self.vide_13: (6,6),
         self.vide_14: (6,7),
         self.vide_15: (6,8),
         self.vide_16: (6,9),
         self.vide_1: (7,2),
         self.vide_2: (7,3),
         self.vide_3: (7,4),
         self.vide_4: (7,5),
         self.vide_5: (7,6),
         self.vide_6: (7,7),
         self.vide_7: (7,8),
         self.vide_8: (7,9),}

        dict2 = dict()

        for cle,valeur in dict1.items():
             dict2[valeur] = cle

        # On connecte les boutons à l'action chk (pour "checked")
        # On doit les connecter à une fonction, mais on veut passer en argument
        # le sender
        # Donc on utilise une fonction anonyme (qui renvoie le résultat de
        # chk(pièce)

        self.tour1B.pressed.connect(lambda: self.chk(self.tour1B,dict1, dict2))
        self.cavalier1B.pressed.connect(lambda: self.chk(self.cavalier1B,dict1, dict2))
        self.fou1B.pressed.connect(lambda: self.chk(self.fou1B,dict1, dict2))
        self.reineB.pressed.connect(lambda: self.chk(self.reineB,dict1, dict2))
        self.roiB.pressed.connect(lambda: self.chk(self.roiB,dict1, dict2))
        self.tour2B.pressed.connect(lambda: self.chk(self.tour2B,dict1, dict2))
        self.cavalier2B.pressed.connect(lambda: self.chk(self.cavalier2B,dict1, dict2))
        self.fou2B.pressed.connect(lambda: self.chk(self.fou2B,dict1, dict2))
        self.pion1B.pressed.connect(lambda: self.chk(self.pion1B,dict1, dict2))
        self.pion2B.pressed.connect(lambda: self.chk(self.pion2B,dict1, dict2))
        self.pion3B.pressed.connect(lambda: self.chk(self.pion3B,dict1, dict2))
        self.pion4B.pressed.connect(lambda: self.chk(self.pion4B,dict1, dict2))
        self.pion5B.pressed.connect(lambda: self.chk(self.pion5B,dict1, dict2))
        self.pion6B.pressed.connect(lambda: self.chk(self.pion6B,dict1, dict2))
        self.pion7B.pressed.connect(lambda: self.chk(self.pion7B,dict1, dict2))
        self.pion8B.pressed.connect(lambda: self.chk(self.pion8B,dict1, dict2))

        self.tour1N.pressed.connect(lambda: self.chk(self.tour1N,dict1, dict2))
        self.cavalier1N.pressed.connect(lambda: self.chk(self.cavalier1N,dict1, dict2))
        self.fou1N.pressed.connect(lambda: self.chk(self.fou1N,dict1, dict2))
        self.reineN.pressed.connect(lambda: self.chk(self.reineN,dict1, dict2))
        self.roiN.pressed.connect(lambda: self.chk(self.roiN,dict1, dict2))
        self.tour2N.pressed.connect(lambda: self.chk(self.tour2N,dict1, dict2))
        self.cavalier2N.pressed.connect(lambda: self.chk(self.cavalier2N,dict1, dict2))
        self.fou2N.pressed.connect(lambda: self.chk(self.fou2N,dict1, dict2))
        self.pion1N.pressed.connect(lambda: self.chk(self.pion1N,dict1, dict2))
        self.pion2N.pressed.connect(lambda: self.chk(self.pion2N,dict1, dict2))
        self.pion3N.pressed.connect(lambda: self.chk(self.pion3N,dict1, dict2))
        self.pion4N.pressed.connect(lambda: self.chk(self.pion4N,dict1, dict2))
        self.pion5N.pressed.connect(lambda: self.chk(self.pion5N,dict1, dict2))
        self.pion6N.pressed.connect(lambda: self.chk(self.pion6N,dict1, dict2))
        self.pion7N.pressed.connect(lambda: self.chk(self.pion7N,dict1, dict2))
        self.pion8N.pressed.connect(lambda: self.chk(self.pion8N,dict1, dict2))

        self.vide_1.pressed.connect(lambda: self.chk(self.vide_1,dict1, dict2))
        self.vide_2.pressed.connect(lambda: self.chk(self.vide_2,dict1, dict2))
        self.vide_3.pressed.connect(lambda: self.chk(self.vide_3,dict1, dict2))
        self.vide_4.pressed.connect(lambda: self.chk(self.vide_4,dict1, dict2))
        self.vide_5.pressed.connect(lambda: self.chk(self.vide_5,dict1, dict2))
        self.vide_6.pressed.connect(lambda: self.chk(self.vide_6,dict1, dict2))
        self.vide_7.pressed.connect(lambda: self.chk(self.vide_7,dict1, dict2))
        self.vide_8.pressed.connect(lambda: self.chk(self.vide_8,dict1, dict2))
        self.vide_9.pressed.connect(lambda: self.chk(self.vide_9,dict1, dict2))
        self.vide_10.pressed.connect(lambda: self.chk(self.vide_10,dict1, dict2))
        self.vide_11.pressed.connect(lambda: self.chk(self.vide_11,dict1, dict2))
        self.vide_12.pressed.connect(lambda: self.chk(self.vide_12,dict1, dict2))
        self.vide_13.pressed.connect(lambda: self.chk(self.vide_13,dict1, dict2))
        self.vide_14.pressed.connect(lambda: self.chk(self.vide_14,dict1, dict2))
        self.vide_15.pressed.connect(lambda: self.chk(self.vide_15,dict1, dict2))
        self.vide_16.pressed.connect(lambda: self.chk(self.vide_16,dict1, dict2))
        self.vide_17.pressed.connect(lambda: self.chk(self.vide_17,dict1, dict2))
        self.vide_18.pressed.connect(lambda: self.chk(self.vide_18,dict1, dict2))
        self.vide_19.pressed.connect(lambda: self.chk(self.vide_19,dict1, dict2))
        self.vide_20.pressed.connect(lambda: self.chk(self.vide_20,dict1, dict2))
        self.vide_21.pressed.connect(lambda: self.chk(self.vide_21,dict1, dict2))
        self.vide_22.pressed.connect(lambda: self.chk(self.vide_22,dict1, dict2))
        self.vide_23.pressed.connect(lambda: self.chk(self.vide_23,dict1, dict2))
        self.vide_24.pressed.connect(lambda: self.chk(self.vide_24,dict1, dict2))
        self.vide_25.pressed.connect(lambda: self.chk(self.vide_25,dict1, dict2))
        self.vide_26.pressed.connect(lambda: self.chk(self.vide_26,dict1, dict2))
        self.vide_27.pressed.connect(lambda: self.chk(self.vide_27,dict1, dict2))
        self.vide_28.pressed.connect(lambda: self.chk(self.vide_28,dict1, dict2))
        self.vide_29.pressed.connect(lambda: self.chk(self.vide_29,dict1, dict2))
        self.vide_30.pressed.connect(lambda: self.chk(self.vide_30,dict1, dict2))
        self.vide_31.pressed.connect(lambda: self.chk(self.vide_31,dict1, dict2))
        self.vide_32.pressed.connect(lambda: self.chk(self.vide_32,dict1, dict2))



    # Fonction d'action lorsqu'une pièce est sélectionnée

    def chk(self, button, dict1, dict2): # on passe en argument le sender
        global pChecked
        global nbVide
        global listeAcc
        if echecs.tour_blanc: # Joueur récupéré du moteur
            joueur = "B"
        else:
            joueur = "N"
        for bitonio in listeAcc:
            if "vide" in bitonio.objectName():
                bitonio.setIcon(QtGui.QIcon("vide.png"))
            else:
                bitonio.setIcon(QtGui.QIcon(bitonio.objectName() + ".png"))
            print(bitonio.objectName())
        name = button.objectName()
        if joueur in name or "vide" in name or (pChecked != "" and joueur in pChecked.objectName()):
            if pChecked == "": # Aucune pièce sélectionnée
                if not("vide" in name):
                    print(name + " sélectionné")
                    button.setIcon(QtGui.QIcon(name + "sel.png"))
                    ## Interaction avec echecs.py
                    coord = dict1[button]
                    print(coord)

                    (x,y) = coord
                    l = echecs.valeurs_accessibles(x,y)

                    for (m,n) in l:
                        butt = dict2[(m,n)]
                        listeAcc.append(butt)
                        buttName = butt.objectName()
                        if "vide" in buttName:
                            butt.setIcon(QtGui.QIcon("videsel.png"))
                        else:
                            butt.setIcon(QtGui.QIcon(buttName + "sel.png"))

                    ##
                    pChecked = button
            else: # Une pièce est déjà sélectionnée
                if button == pChecked: # On a sélectionné la pièce déjà sélectionnée
                    print(name + " dé-sélectionné")
                    button.setIcon(QtGui.QIcon(name + ".png"))
                    pChecked = ""
                else: # On a sélectionné une autre pièce
                    (u,v) = dict1[pChecked]
                    if "vide" in name and dict1[button] in echecs.valeurs_accessibles(u,v): # Déplacement d'une pièce sur une case vide
                        ## Interaction avec echecs.py
                        coord = dict1[button]
                        print(coord)

                        (x,y) = coord
                        l = echecs.valeurs_accessibles(x,y)

                        for (m,n) in l:
                            butt = dict2[(m,n)]
                            listeAcc.append(butt)
                            buttName = butt.objectName()
                            if "vide" in buttName:
                                butt.setIcon(QtGui.QIcon("videsel.png"))
                            else:
                                butt.setIcon(QtGui.QIcon(buttName + "sel.png"))

                        ##
                        ## On répercute le mouvement dans le moteur de jeu en appelant "move"
                        (a,b) = dict1[pChecked]
                        (c,d) = dict1[button]
                        echecs.move(a,b,c,d)
                        ##
                        ## On change les valeurs des dictionnaires
                        positionFinale = dict1[button]
                        positionInitiale = dict1[pChecked]
                        print("position initiale : " + str(positionInitiale))
                        print("position finale : " + str(positionFinale))
                        dict1[pChecked] = positionInitiale
                        dict2[positionInitiale] = pChecked
                        dict1[button] = positionFinale
                        dict2[positionFinale] = button
                        ##
                        strButtonName = button.objectName()
                        button.setObjectName(pChecked.objectName())
                        pChecked.setObjectName(strButtonName)
                        pChecked.setIcon(QtGui.QIcon("vide.png"))
                        button.setIcon(QtGui.QIcon(button.objectName() + ".png"))
                        pChecked = ""

                        print("blabla" + str(dict1[button]))

                        """

                        # On a déplacé la pièce

                        if joueur == "B":
                            if echecs.chess_B():
                                print("chess")
                                error_dialog.showMessage('Oh no!')
                        if joueur == "N":
                            if echecs.chess_W():
                                print("chess")
                                error_dialog.showMessage('Oh no!')
                        """

                    else:

                        if joueur in name: # on a sélectionné une autre pièce de la même couleur
                            print(pChecked.objectName() + " dé-sélectionné")
                            print(name + " sélectionné")
                            pChecked.setIcon(QtGui.QIcon(pChecked.objectName() + ".png"))
                            ## Interaction avec echecs.py
                            coord = dict1[button]
                            print(coord)

                            (x,y) = coord
                            l = echecs.valeurs_accessibles(x,y)

                            for (m,n) in l:
                                butt = dict2[(m,n)]
                                listeAcc.append(butt)
                                buttName = butt.objectName()
                                if "vide" in buttName:
                                    butt.setIcon(QtGui.QIcon("videsel.png"))
                                else:
                                    butt.setIcon(QtGui.QIcon(buttName + "sel.png"))

                            ##
                            pChecked = button
                            namePChecked = pChecked.objectName()
                            pChecked.setIcon(QtGui.QIcon(namePChecked + "sel.png"))
                            (u,v) = dict1[pChecked]
                        if not(joueur in name) and dict1[button] in echecs.valeurs_accessibles(u,v): # on a sélectionné une pièce adverse
                            print("Mangeons la pièce adverse !")
                            ## On répercute le mouvement dans le moteur de jeu en appelant "move"
                            (a,b) = dict1[pChecked]
                            (c,d) = dict1[button]
                            echecs.move(a,b,c,d)
                            ##
                            ## On change les valeurs des dictionnaires
                            positionFinale = dict1[button]
                            positionInitiale = dict1[pChecked]
                            print("position initiale : " + str(positionInitiale))
                            print("position finale : " + str(positionFinale))
                            dict1[pChecked] = positionInitiale
                            dict2[positionInitiale] = pChecked
                            dict1[button] = positionFinale
                            dict2[positionFinale] = button
                            ##
                            ## On répercute le mouvement dans le moteur de jeu en appelant "move"
                            (a,b) = dict1[pChecked]
                            (c,d) = dict1[button]
                            echecs.move(a,b,c,d)
                            ##
                            nbVide += 1 # on incrémente le nombre de cases vides
                            button.setObjectName(pChecked.objectName())
                            pChecked.setObjectName("vide_" + str(nbVide))
                            pChecked.setIcon(QtGui.QIcon("vide.png"))
                            button.setIcon(QtGui.QIcon(button.objectName() + ".png"))
                            pChecked = ""

                            # Verif chess
                            """
                            if joueur == "B":
                                if echecs.chess_B():
                                    print("chess")
                                    error_dialog.showMessage('Oh no!')
                            if joueur == "N":
                                if echecs.chess_W():
                                    print("chess")
                                    error_dialog.showMessage('Oh no!')
                            """

if __name__ == "__main__":
    global tour1B
    import sys
    pChecked = "" # Variable contenant la pièce sélectionnée
    nbVide = 32 # Nombre de cases vides
    listeAcc = []
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
