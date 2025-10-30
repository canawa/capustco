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

        # кнопки
        names = [
            'Еденицы измерения',
            'Контрагенты',
            'Товары и услуги',
            'Склады и места хранения',
            'Сотрудники'
        ]

        for name in names:
            btn = QPushButton(name)
            btn.clicked.connect(self.open_directory)
            list_widget.layout().addWidget(btn)

        widget.layout().addWidget(list_widget)

        self.setWindowTitle('Список справочников')
        self.setWindowIcon(QIcon('images/logo.png'))

    def open_directory(self):
        print('Открываем справочник')
        self.directory = DirectoryWindow()
        self.setCentralWidget(self.directory)
