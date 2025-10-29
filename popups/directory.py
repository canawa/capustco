from PySide6.QtGui import QPalette, QColor, QIcon
from PySide6.QtWidgets import QMainWindow, QPushButton, QHBoxLayout, QWidget
class DirectoryWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Новый справочник')
        self.setGeometry(0, 0, 1600, 900)
        self.setWindowIcon(QIcon('images/logo.png')) # ставим иконки
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&Файл') # создаем меню (которое сверху во всех прогах)
        file_menu.addAction('Загрузить из CSV')
        file_menu.addAction('Сохранить') # добавляем опции внутри этого меню
        quit_action = file_menu.addAction('Выйти') # добавляем опции внутри этого меню
        quit_action.triggered.connect(self.close)
        edit_menu = menu_bar.addMenu('Редактировать')
        edit_menu.addAction('Шаг назад')
        edit_menu.addAction('Шаг вперед')