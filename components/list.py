from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from popups.directory import DirectoryWindow
class List(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        widget.setLayout(QVBoxLayout())
        self.setCentralWidget(widget)

        # контейнер для кнопок
        list_widget = QWidget()
        list_widget.setLayout(QVBoxLayout())
        list_widget.setFixedSize(QSize(400, 500))

        # кнопки и названия справочников (+ названия колонок)
        names = { 

            'Еденицы измерения': ['Еденицы измерения'],
            'Контрагенты': ['ИНН', 'Наименование', 'Адрес', 'Телефон', 'Email', 'Комментарий'],
            'Товары и услуги': ['Наименование', 'Описание', 'Цена', 'Количество', 'Еденица измерения'],
            'Склады и места хранения': ['Наименование', 'Описание', 'Адрес', 'Телефон', 'Email', 'Комментарий'],
            'Сотрудники': ['ФИО', 'Должность', 'Телефон', 'Email', 'Комментарий'],
        }

        for name in names: # перебираем все названия справочников
            btn = QPushButton(name)
            btn.clicked.connect(lambda checked, n=name: self.open_directory(names[n])) # открываем справочник
            list_widget.layout().addWidget(btn)

        widget.layout().addWidget(list_widget)

        self.setWindowTitle('Список справочников')
        self.setWindowIcon(QIcon('images/logo.png'))

    def open_directory(self, columns):
        self.setWindowTitle(columns[0])
        self.directory = DirectoryWindow(columns)
        self.setCentralWidget(self.directory)
