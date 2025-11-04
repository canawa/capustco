from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QDialog, QTextEdit, QLabel
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QTextLine
from popups.directory import DirectoryWindow
import sqlite3 as sq
import json
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
        with sq.connect('database.db') as con:
            cur = con.cursor()
            cur.execute('CREATE TABLE IF NOT EXISTS directories (id INTEGER PRIMARY KEY, name TEXT, columns TEXT)')
            cur.execute('SELECT name, columns FROM directories')
            self.names = cur.fetchall()

        print(self.names)

        create_dir_button = QPushButton('Создать справочник')
        create_dir_button.clicked.connect(self.create_directory)
        list_widget.layout().addWidget(create_dir_button)


        for name in self.names: # перебираем все названия справочников
            btn = QPushButton(name[0])
            btn.clicked.connect(lambda checked, n=name: self.open_directory(n[0], json.loads(n[1]))) # открываем справочник, и расшифровываем вторую часть кортежа через json
            list_widget.layout().addWidget(btn)

        widget.layout().addWidget(list_widget)

        self.setWindowTitle('Список справочников')
        self.setWindowIcon(QIcon('images/logo.png'))

    def open_directory(self, name, columns):
        # self.setWindowTitle(name)
        self.directory = DirectoryWindow(name, columns)
        self.setCentralWidget(self.directory)

    def create_directory(self):

        self.columns = []
        self.create_dir_dialog = QDialog()
        self.create_dir_dialog.setLayout(QVBoxLayout())
        self.create_dir_dialog.setWindowTitle('Создание справочника')
        self.create_dir_dialog.setWindowIcon(QIcon('images/logo.png'))
        self.create_dir_dialog.setFixedSize(QSize(400, 200))
        self.create_dir_dialog.show()
        label = QLabel('Введите название справочника')
        label.setFixedSize(QSize(350, 20))
        self.set_dir_name = QTextEdit()
        self.set_dir_name.setFixedSize(QSize(350, 30))
        self.create_dir_dialog.layout().addWidget(label)
        self.create_dir_dialog.layout().addWidget(self.set_dir_name)
        
        columns_label = QLabel('Введите названия колонок через запятую: col1, col2...')
        columns_label.setFixedSize(QSize(350, 20))
        self.columns_text = QTextEdit()
        self.columns_text.setFixedSize(QSize(350, 60))
        self.create_dir_dialog.layout().addWidget(columns_label)
        self.create_dir_dialog.layout().addWidget(self.columns_text)

        accept_button = QPushButton('Создать')
        accept_button.clicked.connect(self.create_directory_accept)
        self.create_dir_dialog.layout().addWidget(accept_button)

        
    def create_directory_accept(self):
        self.columns = self.columns_text.toPlainText().split('\n') # сплитуем текст на массив по запятой и запихиваем в columns массив
        self.columns = self.columns_text.toPlainText().split(',') # сплитуем текст на массив по запятой и запихиваем в columns массив
        self.columns = [column.strip() for column in self.columns] # удаляем пробелы из массива по краям
        self.create_dir_dialog.close()
        with sq.connect('database.db') as con:
            cur = con.cursor()
            cur.execute('CREATE TABLE IF NOT EXISTS directories (id INTEGER PRIMARY KEY, name TEXT UNIQUE, columns TEXT)')
            cur.execute('INSERT INTO directories (name, columns) VALUES (?, ?)', (self.set_dir_name.toPlainText(), json.dumps(self.columns)))
        
        self.open_directory(self.set_dir_name.toPlainText(), self.columns)
        