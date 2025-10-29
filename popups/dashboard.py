from re import S
import PySide6
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon, QPalette, QColor
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
        
        settings_menu = menu_bar.addMenu('Настройки')
        settings_menu.addAction('Горячие клавиши')

        
        toolbar = QToolBar('Main toolbar') # создаем тулбар
        self.addToolBar(toolbar) # добавляем объект класса QToolBar в само приложение

        create_dir_action = QAction('Создать справочник', self) # action это как кнопка только круче, можно добавлять картинки и шорткаты
        create_dir_action.setShortcut('Ctrl+N') # создаем шорткат для кнопки
        create_dir_action.triggered.connect(self.create_directory)

        create_dir_action.setToolTip('Создаст новый справочник (Ctrl + N)') # при наведении больше чем на секунду, вылазит подсказка с этим текстом
        toolbar.addAction(create_dir_action)
        toolbar.addSeparator()

    def create_directory(self):
        dock = DirectoryWindow() # создаем объект класса DirectoryWindow
        self.addDockWidget(Qt.LeftDockWidgetArea, dock) # добавляем объект класса DirectoryWindow в само приложение