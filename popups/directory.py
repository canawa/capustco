from PySide6.QtGui import QPalette, QColor, QIcon
from PySide6.QtWidgets import QDockWidget, QPushButton, QHBoxLayout, QWidget
from custom_functions.load_css import LoadCss
class DirectoryWindow(QDockWidget): # QDockWidget это рамка + механика состыковки, потому надо внутри добавить QWidget
    def __init__(self):
        super().__init__()
        self.setStyleSheet(LoadCss().load_file('styles/dashboard_styles.css')) # используем мою самописную гениальную технологию
        self.setWindowTitle('Новый справочник')
        self.setWindowIcon(QIcon('images/logo.png')) # ставим иконки
        # QDockWidget это обертка для моего контейнера
        container = QWidget() # создаем контейнер для кнопки
        container.setLayout(QHBoxLayout()) # создаем макет для кнопки
        container.layout().addWidget(QPushButton('ТЕСТ')) # добавляем кнопку в макет
        self.setWidget(container) # Не addWidget, в QDockWidget нет addWidget, только setWidget, единственный виджет который можно добавить