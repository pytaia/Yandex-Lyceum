# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.coffee_table = QtWidgets.QTableWidget(self.centralwidget)
        self.coffee_table.setGeometry(QtCore.QRect(20, 20, 711, 621))
        self.coffee_table.setObjectName("coffee_table")
        self.coffee_table.setColumnCount(0)
        self.coffee_table.setRowCount(0)
        self.Error_label = QtWidgets.QLabel(self.centralwidget)
        self.Error_label.setGeometry(QtCore.QRect(760, 490, 221, 91))
        self.Error_label.setObjectName("Error_label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(760, 200, 221, 251))
        self.layoutWidget.setObjectName("layoutWidget")
        self.add_layout = QtWidgets.QGridLayout(self.layoutWidget)
        self.add_layout.setContentsMargins(0, 0, 0, 0)
        self.add_layout.setObjectName("add_layout")
        self.taste_description_line = QtWidgets.QLineEdit(self.layoutWidget)
        self.taste_description_line.setObjectName("taste_description_line")
        self.add_layout.addWidget(self.taste_description_line, 4, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.add_layout.addWidget(self.label_8, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.add_layout.addWidget(self.label_2, 2, 0, 1, 1)
        self.id_edit_line = QtWidgets.QLineEdit(self.layoutWidget)
        self.id_edit_line.setObjectName("id_edit_line")
        self.add_layout.addWidget(self.id_edit_line, 0, 1, 1, 1)
        self.price_line = QtWidgets.QLineEdit(self.layoutWidget)
        self.price_line.setObjectName("price_line")
        self.add_layout.addWidget(self.price_line, 5, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.add_layout.addWidget(self.label_5, 5, 0, 1, 1)
        self.sort_name_line = QtWidgets.QLineEdit(self.layoutWidget)
        self.sort_name_line.setObjectName("sort_name_line")
        self.add_layout.addWidget(self.sort_name_line, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.add_layout.addWidget(self.label_3, 3, 0, 1, 1)
        self.volume_line = QtWidgets.QLineEdit(self.layoutWidget)
        self.volume_line.setObjectName("volume_line")
        self.add_layout.addWidget(self.volume_line, 6, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.add_layout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.add_layout.addWidget(self.label_6, 6, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.add_layout.addWidget(self.label, 1, 0, 1, 1)
        self.add_button = QtWidgets.QPushButton(self.layoutWidget)
        self.add_button.setObjectName("add_button")
        self.add_layout.addWidget(self.add_button, 8, 0, 1, 2)
        self.edit_button = QtWidgets.QPushButton(self.layoutWidget)
        self.edit_button.setObjectName("edit_button")
        self.add_layout.addWidget(self.edit_button, 9, 0, 1, 2)
        self.roasting_box = QtWidgets.QComboBox(self.layoutWidget)
        self.roasting_box.setObjectName("roasting_box")
        self.add_layout.addWidget(self.roasting_box, 2, 1, 1, 1)
        self.coffe_type_box = QtWidgets.QComboBox(self.layoutWidget)
        self.coffe_type_box.setObjectName("coffe_type_box")
        self.add_layout.addWidget(self.coffe_type_box, 3, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(-4, 0, 1051, 711))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("image for label/1663577115_34-top-fon-com-p-serii-fon-grafichnii-foto-59.jpg"))
        self.label_7.setObjectName("label_7")
        self.label_7.raise_()
        self.coffee_table.raise_()
        self.layoutWidget.raise_()
        self.Error_label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Error_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">id для изменения</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Степень прожарки</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Цена</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Тип кофе</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Описание вкуса</p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Обьём</p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Название сорта</p></body></html>"))
        self.add_button.setText(_translate("MainWindow", "Добавить"))
        self.edit_button.setText(_translate("MainWindow", "Изменить"))