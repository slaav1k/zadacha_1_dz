import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class DBSample(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.connection = sqlite3.connect("coffee.sqlite")
        # По умолчанию будем выводить все данные из таблицы films
        '''self.select_data()'''
        res = self.connection.cursor().execute("""SELECT ID,
       название_сорта,
       степень_обжарки,
       молотый_или_в_зернах,
       описание_вкуса,
       цена,
       объем_упаковки
  FROM all_information""").fetchall()
        # Заполним размеры таблицы
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'название сорта', 'степень обжарки',
                                                    ' молот./в зернах', 'описание вкуса', 'цена', 'объем упаковки'])
        self.tableWidget.setRowCount(0)
        # Заполняем таблицу элементами
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def closeEvent(self, event):
        # При закрытии формы закроем и наше соединение
        # с базой данных
        self.connection.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DBSample()
    ex.show()
    sys.exit(app.exec())
'''con = sqlite3.connect("coffee.sqlite")
cur = con.cursor()
result1 = list(cur.execute("""SELECT ID,
       название_сорта,
       степень_обжарки,
       молотый_или_в_зернах,
       описание_вкуса,
       цена,
       объем_упаковки
  FROM all_information""").fetchall())
con.close()
for j in result1:
    print(j)
'''