from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QListWidgetItem # импортируем классы из PySide6.QtWidgets
import sys # импортируем модуль sys для работы с командной строкой
from popups.rockwidget import RockWidget


app = QApplication(sys.argv) # создаем экземпляр приложения, передаем sys.argv, чтобы приложение могло получать аргументы из командной строки
window = RockWidget() # теперь это объект класса RockWidget, который наследуется от QMainWindow
window.show() # показываем окно
app.exec() # запускаем приложение, чтобы оно не закрывалось сразу. Тут ивент луп, который обрабатывает события приложения. И в конце мы вызываем app.exec(), чтобы приложение запустилось.