import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

        self.btn.clicked.connect(self.run)

        self.con = sqlite3.connect('coffee.db')
        cur = self.con.cursor()
        result = cur.execute("""SELECT id FROM espresso""").fetchall()
        self.lines = result[0][-1]

        self.model = QStandardItemModel(self.lines, 7)
        self.model.setHorizontalHeaderLabels(['id', 'name', 'degree', 'ground/grains', 'taste',
                                              'prize', 'size'])

    def run(self):
        cur = self.con.cursor()
        result = cur.execute("""SELECT * FROM espresso""").fetchall()
        for row in range(self.lines):
            for line in range(7):
                item = QStandardItem(str(result[row][line]))
                self.model.setItem(row, line, item)
        self.result.setModel(self.model)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
