import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from labApp import LabApp


def main():
     # Создание приложения
    app = QtWidgets.QApplication(sys.argv)
    #отрисовать окно
    window = LabApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()


