import sys
from functools import partial

from PyQt5 import QtSql, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication, QHeaderView, QLabel, QPushButton, QFileDialog


class CatalogMainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        self.DB_NAME = "dbls7.sqlite"

        # Структура главного окна
        # Создаем меню
        self.menu_bar = self.menuBar()

        # Создаем блоки меню
        # Блок меню 'Учет движения товаров'
        self.gma_menu = self.menu_bar.addMenu('Учет движения товаров')
        self.ao_open_btn = QAction(self)
        self.ao_open_btn.setText('Категории товаров')
        self.bo_open_btn = QAction(self)
        self.bo_open_btn.setText('Единицы измерения товаров')
        self.co_open_btn = QAction(self)
        self.co_open_btn.setText('Должности')
        self.gma_menu.addAction(self.ao_open_btn)
        self.gma_menu.addAction(self.bo_open_btn)
        self.gma_menu.addAction(self.co_open_btn)

        self.do_open_btn = QAction(self)
        self.do_open_btn.setText('Товары')
        self.eo_open_btn = QAction(self)
        self.eo_open_btn.setText('Сотрудники')
        self.fo_open_btn = QAction(self)
        self.fo_open_btn.setText('Поставщики')
        self.gma_menu.addAction(self.do_open_btn)
        self.gma_menu.addAction(self.eo_open_btn)
        self.gma_menu.addAction(self.fo_open_btn)

        # Table without adding info to ds:
        self.qt_sql_table = QtWidgets.QTableView(self)

        self.qt_sql_table.resize(620, 320)
        self.qt_sql_table.move(20, 100)
        self.qt_sql_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.lbl1 = QLabel(self.DB_NAME, self)
        self.lbl1.resize(1000, 20)
        self.lbl1.move(20, 20)

        self.fileButton = QPushButton("Файл базы данных", self)
        self.fileButton.move(20, 50)
        self.fileButton.resize(300, 20)
        self.fileButton.pressed.connect(self.file_btn_pressed)

        self.fileButton = QPushButton("Удалить запись", self)
        self.fileButton.move(20, 450)
        self.fileButton.resize(300, 50)

        self.fileButton = QPushButton("Добавить запись", self)
        self.fileButton.move(340, 450)
        self.fileButton.resize(300, 50)

        self.actions_button_init()

    def actions_button_init(self):
        self.ao_open_btn.triggered.connect(partial(dbsqlite_connection, self.qt_sql_table, 'categories', self.DB_NAME))
        self.bo_open_btn.triggered.connect(partial(dbsqlite_connection, self.qt_sql_table, 'units', self.DB_NAME))
        self.co_open_btn.triggered.connect(partial(dbsqlite_connection, self.qt_sql_table, 'positions', self.DB_NAME))
        self.do_open_btn.triggered.connect(partial(dbsqlite_connection, self.qt_sql_table, 'goods', self.DB_NAME))
        self.eo_open_btn.triggered.connect(partial(dbsqlite_connection, self.qt_sql_table, 'employees', self.DB_NAME))
        self.fo_open_btn.triggered.connect(partial(dbsqlite_connection, self.qt_sql_table, 'vendors', self.DB_NAME))

    def file_btn_pressed(self):
        self.DB_NAME = QFileDialog.getOpenFileName(self, 'Open file')[0]
        self.lbl1.setText(self.DB_NAME)
        self.actions_button_init()


def dbsqlite_connection(query_table, db_table, name):
    conn = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    conn.setDatabaseName(name)
    if conn.open():

        query_model = QtSql.QSqlQueryModel(parent=query_table)
        query_model.setQuery(f"select * from {db_table}")
        query_table.setModel(query_model)

    conn.close()


# Отобразить главное окно
if __name__ == "__main__":
    app = QApplication(sys.argv)
    CMW = CatalogMainWindow()
    CMW.setWindowTitle('Складской учет')
    CMW.setFixedSize(1200, 800)
    CMW.show()
    sys.exit(app.exec_())
