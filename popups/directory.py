from ast import Load
from PySide6.QtCore import QSize
from PySide6.QtGui import QPalette, QColor, QIcon, QTextBlock
from PySide6.QtWidgets import QDockWidget, QPushButton, QHBoxLayout, QVBoxLayout, QTableView, QTextEdit, QVBoxLayout, QWidget, QTableWidget, QHeaderView, QLabel
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
        create_button.clicked.connect(self.add_data)
# РАБОТА С ТАБЛИЦЕЙ И ЕЕ НАСТРОЙКИ
        self.table = QTableWidget(5,3) # табличка 5 на 3
        self.table.setHorizontalHeaderLabels(['Дата', 'Наименование', 'Цена']) # переименовываем колонки
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers) # хз как это работает, но не дает редактировать, но можно копировать
        self.table_resize()

        container.layout().addWidget(self.table) # добавляем кнопку в макет
        container.layout().addWidget(create_button)
        self.setWidget(container) # Не addWidget, в QDockWidget нет addWidget, только setWidget, единственный виджет который можно добавить

    def table_resize(self): # функция чтобы табличка растянулась
        header = self.table.horizontalHeader() # берет объект который отвечает за строку с названиями колонок
        
        for i in range(header.count() - 1):
            header.setSectionResizeMode(i, QHeaderView.ResizeToContents) # для всех делаем растяжение по содержимому, кроме последнего.
        
        header.setSectionResizeMode(header.count() - 1, QHeaderView.Stretch) # для последнего делаем растяжение по длине.
    def add_data(self):
        self.window = QWidget() # создаем виджет
        self.window.setLayout(QVBoxLayout())
        self.window.setWindowTitle('Добавить запись')
        self.window.setWindowIcon(QIcon('images/logo.png'))

        # получим сколько у нас столбиков
        header = self.table.horizontalHeader() # получаем объект, который хранит инфу о шапке таблицы
        self.window.setStyleSheet(LoadCss().load_file('styles/input_data.css')) # стили надо для каждого виджета отдельно

        for i in range(1, header.count()):
            input = QTextEdit('') # создаем поле для ввода
            input.setFixedSize(QSize(200, 30))  # устанавливаю фиксированный размер для поля
            
            field_container = QWidget()
            field_container.setLayout(QHBoxLayout())
            field_container.setFixedSize(QSize(300, 50))
            text_label = QLabel() # setText(header.sectionText(i)) для вывода текста
            text_label.setText(self.table.horizontalHeaderItem(i).text() + ':') # получаем текст из шапки таблицы (почему то через жопу а не через header ну ладно)
            text_label.setFixedSize(QSize(300, 40))
            field_container.layout().addWidget(text_label)
            field_container.layout().addWidget(input)
            field_container.setStyleSheet(LoadCss().load_file('styles/input_data.css'))

            self.window.layout().addWidget(field_container) # это чуть потом перепишем, чтобы можно было к любому количеству столбиков задавать значения, через цикл сделаю
        


        save_button = QPushButton('Сохранить')
        save_and_quit_button = QPushButton('Сохранить и выйти')

        button_holder = QWidget()
        button_holder.setLayout(QHBoxLayout())
        button_holder.layout().addWidget(save_button)
        button_holder.layout().addWidget(save_and_quit_button)
        button_holder.setFixedSize(QSize(600, 70))

        self.window.layout().addWidget(button_holder)
        self.window.setFixedSize(600, header.count()*40 + 70) # устанавливаю фиксированный размер, чтобы его нельзя было поменять
        self.window.show()