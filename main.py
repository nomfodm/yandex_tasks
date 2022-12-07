import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
import sqlite3


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        uic.loadUi("main.ui", self)

        self.query = "SELECT * FROM coffee"
        self.connection = sqlite3.connect("coffee.sqlite3")

        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.updateTable)

    def updateTable(self):
        self.tableWidget.clear()
        res = self.connection.cursor().execute(self.query).fetchall()

        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)

        self.tableWidget.setHorizontalHeaderLabels(
            ["ID", "Сорт", "Степень обжарки", "Молотый/в зернах", "Вкус", "Цена", "Объем упаковки"])

        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.horizontalHeader().setStretchLastSection(True)


app = QApplication(sys.argv)

w = Window()
w.show()

sys.exit(app.exec())
