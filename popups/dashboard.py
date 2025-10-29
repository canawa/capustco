from re import S
import PySide6
from PySide6.QtGui import QIcon, QPalette, QColor
from PySide6.QtWidgets import QPushButton, QHBoxLayout, QWidget, QMainWindow, QToolBar
from custom_functions.load_css import LoadCss # используем мое самописное решение для стилей
from popups.directory import DirectoryWindow


class Dashboard(QMainWindow):
    def __init__(self):

        super().__init__() # вызываем конструктор родительского класса (унаследовавшись от QMainWindow, теперь можем использовать его методы)
        self.setStyleSheet(LoadCss().load_file('styles/dashboard_styles.css')) # используем мою самописную гениальную технологию
        self.setWindowIcon(QIcon('images/logo.png'))
        self.showMaximized() # максиммально растягиваем на весь экран, но не фул скрин
        self.setWindowTitle('Dashboard')
        menu_bar = self.menuBar() # создаем объект класса MenuBar

        file_menu = menu_bar.addMenu('Проект') # Пользуемся функцией addMenu из menuBar
        file_menu.addAction('Сохранить') # Создаем опции
        file_menu.addAction('Выйти', lambda: self.close())
        
        toolbar = QToolBar('Main toolbar') # создаем тулбар
        self.addToolBar(toolbar) # добавляем объект класса QToolBar в само приложение

        create_dir_button = QPushButton('Создать справочник')
        create_dir_button.setToolTip('Создаст новый справочник') # при наведении больше чем на секунду, вылазит подсказка с этим текстом
        toolbar.addWidget(create_dir_button)
        create_dir_button.clicked.connect(self.create_directory) # функция открывающая окно справочника
        toolbar.addSeparator()

    def create_directory(self):
        self.dir = DirectoryWindow() # сохраняем как переменную всего класса чтобы окно не закрывалось из за сборщика мусора
        self.dir.show()