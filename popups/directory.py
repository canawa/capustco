from ast import Load
from datetime import datetime
from PySide6.QtCore import QSize
from PySide6.QtGui import QPalette, QColor, QIcon, QTextBlock
from PySide6.QtWidgets import QDockWidget, QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout, QTableView, QTextEdit, QVBoxLayout, QWidget, QTableWidget, QHeaderView, QLabel, QTableWidgetItem
from custom_functions.load_css import LoadCss
class DirectoryWindow(QWidget): 
    def __init__(self, columns):
        super().__init__()
        self.columns = columns
        self.setLayout(QVBoxLayout()) # уставноит лэйаут объекту класса
        self.setStyleSheet(LoadCss().load_file('styles/dashboard_styles.css')) # используем мою самописную гениальную технологию
        self.setWindowTitle('Новый справочник')
        self.setWindowIcon(QIcon('images/logo.png')) # ставим иконки
        create_button = QPushButton('Создать')
        create_button.setGeometry(0,0,240,180)
        create_button.clicked.connect(self.add_data)
# РАБОТА С ТАБЛИЦЕЙ И ЕЕ НАСТРОЙКИ
        self.table = QTableWidget(0,len(self.columns)) # табличка 5 на 3
        self.table.setHorizontalHeaderLabels(self.columns) # переименовываем колонки
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers) # хз как это работает, но не дает редактировать, но можно копировать
        self.table_resize()

        self.layout().addWidget(self.table) # добавляем кнопку в макет
        self.layout().addWidget(create_button)

    def table_resize(self): # функция чтобы табличка растянулась
        header = self.table.horizontalHeader() # берет объект который отвечает за строку с названиями колонок
        
        for i in range(header.count() - 1):
            header.setSectionResizeMode(i, QHeaderView.ResizeToContents) # для всех делаем растяжение по содержимому, кроме последнего.
        
        header.setSectionResizeMode(header.count() - 1, QHeaderView.Stretch) # для последнего делаем растяжение по длине.
        # ТУТ ДОБАВЛЯЮТСЯ ДАННЫЕ В ТАБЛИЦУ
    def add_data(self):
        self.window = QWidget() # создаем виджет
        self.window.setLayout(QVBoxLayout())
        self.window.setWindowTitle('Добавить запись')
        self.window.setWindowIcon(QIcon('images/logo.png'))

        # получим сколько у нас столбиков
        header = self.table.horizontalHeader() # получаем объект, который хранит инфу о шапке таблицы
        self.window.setStyleSheet(LoadCss().load_file('styles/input_data.css')) # стили надо для каждого виджета отдельно


        self.input_fields = []
        for i in range(0, header.count()): # тут создаем поля для ввода
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
            self.input_fields.append(input)
            self.window.layout().addWidget(field_container) # это чуть потом перепишем, чтобы можно было к любому количеству столбиков задавать значения, через цикл сделаю
        
        save_button = QPushButton('Сохранить')
        save_button.clicked.connect(lambda: self.save_and_quit(quit=False))
        save_and_quit_button = QPushButton('Сохранить и выйти')
        save_and_quit_button.clicked.connect(lambda: self.save_and_quit(quit=True))
        button_holder = QWidget()
        button_holder.setLayout(QHBoxLayout())
        button_holder.layout().addWidget(save_button)
        button_holder.layout().addWidget(save_and_quit_button)
        button_holder.setFixedSize(QSize(600, 100))

        self.window.layout().addWidget(button_holder)
        # self.window.setFixedSize(600, header.count()*40) # устанавливаю фиксированный размер, чтобы его нельзя было поменять
        self.window.show()

    def save_and_quit(self, quit=False): # тут отлавливаем введенные данные и закрываем окно
        self.table.insertRow(self.table.rowCount()) # чтобы добавить новую строку
        for i in range(len(self.input_fields)):
            data = self.input_fields[i].toPlainText() # получаем данные из полей, здесь построчно и сразу построчно добавляем в таблицу
            self.table.setItem(self.table.rowCount()-1 , i, QTableWidgetItem(data)) # i+1 потому что нулевая колонка это дата
            self.input_fields[i].clear()
        # self.table.setItem(self.table.rowCount() - 1, 0, QTableWidgetItem(datetime.now().strftime('%d.%m.%Y %H:%M')))
        self.table.resizeRowsToContents() # чтобы строки растянулись по содержимому
        if quit == True:
            self.window.close()
        