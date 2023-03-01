import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import uic, QtWidgets
import sqlite3


class CoffeeWindow(QMainWindow):
    def __init__(self):
        super(CoffeeWindow, self).__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.setFixedSize(1000, 700)
        self.setWindowTitle('Много кофе не бывает')
        self.loading_table()
        self.add_and_edit_init()
        self.add_button.clicked.connect(self.add_coffe)
        self.edit_button.clicked.connect(self.edit_coffe)

    def Coffee_console_open(self):
        self.Coffee_information_console = sqlite3.connect('Coffee.db')
        self.Coffee_information_cur = self.Coffee_information_console.cursor()

    def Coffee_console_close(self):
        self.Coffee_information_console.commit()
        self.Coffee_information_cur.close()

    def add_and_edit_init(self):
        self.Coffee_console_open()
        self.roasting_box.addItems([i[0] for i in self.Coffee_information_cur.execute('''SELECT roasting 
                        FROM Roasting''').fetchall()])

        self.coffe_type_box.addItems([i[0] for i in self.Coffee_information_cur.execute('''SELECT coffee_type 
                                FROM Coffee_types''').fetchall()])
        self.Coffee_console_close()

    def loading_table(self):
        self.Coffee_console_open()
        self.coffee_table.setColumnCount(6)
        self.coffee_table.setHorizontalHeaderLabels(
            ["Название", "Степень обжарки", "Тип кофе", "Описание вкуса", "Цена", "Объем упаковки"])
        self.coffee_table.setRowCount(len(self.Coffee_information_cur.execute('SELECT * FROM Coffee').fetchall()))
        for i, row in enumerate(
                [list(i) for i in self.Coffee_information_cur.execute('SELECT * FROM Coffee').fetchall()]):
            for j, elem in enumerate(row):
                if j == 2:
                    elem = list(self.Coffee_information_cur.execute(
                        '''SELECT roasting FROM Roasting WHERE id like {}'''.format(elem)).fetchall())[0][0]
                elif j == 3:
                    elem = list(self.Coffee_information_cur.execute(
                        '''SELECT coffee_type FROM Coffee_types WHERE id like {}'''.format(elem)).fetchall())[0][0]
                if j != 0:
                    self.coffee_table.setItem(i, j - 1, QTableWidgetItem(str(elem)))
        self.coffee_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.coffee_table.resizeColumnsToContents()
        self.Coffee_console_close()

    def coffe_in_base(self):
        self.Coffee_console_open()
        result = self.Coffee_information_cur.execute('''SELECT * FROM Coffee WHERE sort_name like "{}" 
                and roasting like (SELECT id FROM Roasting WHERE roasting like "{}") and coffe_type like 
                (SELECT id FROM Coffee_types WHERE coffee_type like "{}") and taste_description like "{}" 
                and price like "{}" and volume like "{}"'''.format(self.sort_name_line.text(),
                                                                    self.roasting_box.currentText(),
                                                                    self.coffe_type_box.currentText(),
                                                                    self.taste_description_line.text(),
                                                                    self.price_line.text(),
                                                                    self.volume_line.text())).fetchall()
        if not self.id_edit_line.text():
            if not result:
                self.Coffee_console_close()
                return True
        elif result:
            self.Coffee_console_close()
            return True
        self.Coffee_console_close()
        return False

    def add_coffe(self):
        if all([self.sort_name_line.text(), self.roasting_box.currentText(),
                self.coffe_type_box.currentText(),
                self.taste_description_line.text(), self.price_line.text(),
                self.volume_line.text()]) and self.coffe_in_base():
            self.Coffee_console_open()
            self.Coffee_information_cur.execute('''INSERT INTO Coffee (sort_name, roasting, coffe_type, 
            taste_description, price, volume) VALUES ("{}", (SELECT id FROM Roasting WHERE roasting like "{}"), 
            (SELECT id FROM Coffee_types WHERE coffee_type like "{}"), 
            "{}", "{}", "{}")'''.format(self.sort_name_line.text(), self.roasting_box.currentText(),
                                                          self.coffe_type_box.currentText(),
                                                          self.taste_description_line.text(), self.price_line.text(),
                                                          self.volume_line.text()))
            self.Coffee_console_close()

            self.Error_label.setText('Успешо добавлен')
            self.loading_table()
        else:
            self.Error_label.setText('Ошибка запроса')
        self.Coffee_console_close()

    def edit_coffe(self):
        if all([self.id_edit_line.text(), self.sort_name_line.text(), self.roasting_box.currentText(),
                self.coffe_type_box.currentText(),
                self.taste_description_line.text(), self.price_line.text(),
                self.volume_line.text()]):
            self.Coffee_console_open()
            self.Coffee_information_cur.execute('''UPDATE Coffee SET sort_name = "{}", 
            roasting = (SELECT id FROM Roasting WHERE roasting like "{}"), coffe_type = (SELECT id FROM Coffee_types 
            WHERE coffee_type like "{}"), taste_description = "{}", price = "{}", volume = "{}" WHERE id like {}
            '''.format(self.sort_name_line.text(), self.roasting_box.currentText(), self.coffe_type_box.currentText(),
                        self.taste_description_line.text(), self.price_line.text(), self.volume_line.text(),
                        self.id_edit_line.text()))
            self.Coffee_console_close()
            self.Error_label.setText('Успешо изменено')
            self.loading_table()
        else:
            self.Error_label.setText('Ошибка запроса')

        self.Coffee_console_close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CoffeeWindow()
    ex.show()
    sys.exit(app.exec())

