from PySide6.QtGui import QPalette, QColor, QIcon
from PySide6.QtWidgets import QDockWidget, QPushButton, QHBoxLayout, QTableView, QWidget, QTableWidget, QHeaderView
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

        create_button = QPushButton('Создать')
        create_button.setGeometry(0,0,240,180)
# РАБОТА С ТАБЛИЦЕЙ И ЕЕ НАСТРОЙКИ
        self.table = QTableWidget(5,3) # табличка 5 на 3
        self.table.setHorizontalHeaderLabels(['Дата', 'Наименование', 'Цена']) # переименовываем колонки
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers) # хз как это работает, но не дает редактировать, но можно копировать
        self.table_resize()

        container.layout().addWidget(self.table) # добавляем кнопку в макет
        container.layout().addWidget(create_button)
        self.setWidget(container) # Не addWidget, в QDockWidget нет addWidget, только setWidget, единственный виджет который можно добавить
    def table_resize(self):
        header = self.table.horizontalHeader() # берет объект который отвечает за строку с названиями колонок
        
        for i in range(header.count() - 1):
            header.setSectionResizeMode(i, QHeaderView.ResizeToContents) # для всех делаем растяжение по содержимому, кроме последнего.
        
        header.setSectionResizeMode(header.count() - 1, QHeaderView.Stretch) # для последнего делаем растяжение по длине.
        