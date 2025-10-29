from PySide6.QtGui import QIcon, QPalette, QColor
from PySide6.QtWidgets import QPushButton, QHBoxLayout, QWidget
from custom_functions.load_css import LoadCss # используем мое самописное решение для стилей\
from popups.directory import DirectoryWindow


class RockWidget(QWidget, LoadCss):
    def __init__(self):

        super().__init__() # вызываем конструктор родительского класса (унаследовавшись от QMainWindow, теперь можем использовать его методы)

        self.setWindowTitle("Capustco - Конфигурация") # устанавливаем заголовок окна
        self.setFixedWidth(320)
        self.setFixedHeight(80)
        self.setStyleSheet(LoadCss().load_file('styles/button_styles.css'))    
        self.setWindowIcon(QIcon('images/logo.png'))

        button1 = QPushButton("Создать справочник")
        button1.setFixedSize(150, 40)
        button1.clicked.connect(self.create_directory)
        button2 = QPushButton("Добавить документ")
        button2.setFixedSize(150, 40)
        button2.clicked.connect(lambda: print("Нажали добавить источник"))


        widget_layout = QHBoxLayout() # используем лэйаут горизонтальный
        widget_layout.addWidget(button1) # добавляем кнопки
        widget_layout.addWidget(button2)
        self.setLayout(widget_layout)  # устанавливаем наш лэйаут как главный лэйаут
    def create_directory(self):
        self.window = DirectoryWindow() # используем мой класс, который создает новое окно для работы со справочниками
        self.window.show() # отображаем его (обязательно через self а то его удаляет очень быстро сборщик мусора)
        self.close() # закрываем окошко выбора действия
        