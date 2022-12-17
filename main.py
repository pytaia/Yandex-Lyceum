import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import uic, QtWidgets
import sqlite3


class CoffeeWindow(QMainWindow):
    def __init__(self):
        super(CoffeeWindow, self).__init__()
        uic.loadUi('Coffee_window_only_table.ui', self)
        self.setFixedSize(700, 700)
        self.setWindowTitle('Много кофе не бывает')
        self.loading_table()

    def Coffee_console_open(self):
        self.Coffee_information_console = sqlite3.connect('Coffee.db')
        self.Coffee_information_cur = self.Coffee_information_console.cursor()

    def Coffee_console_close(self):
        self.Coffee_information_console.commit()
        self.Coffee_information_cur.close()

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CoffeeWindow()
    ex.show()
    sys.exit(app.exec())
