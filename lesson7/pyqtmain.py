import sys
from functools import partial

from PyQt5 import QtSql, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication, QHeaderView, QLabel, QPushButton, QFileDialog, QTextEdit


class CatalogMainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        self.DB_NAME = None

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

        self.lbl = QLabel("Выбранная БД:", self)
        self.lbl.resize(80, 20)
        self.lbl.move(20, 25)

        self.txt = QTextEdit(self.DB_NAME, self)
        self.txt.resize(800, 25)
        self.txt.move(100, 25)
        self.txt.setReadOnly(True)

        self.fileButton = QPushButton("Файл базы данных", self)
        self.fileButton.move(20, 55)
        self.fileButton.resize(300, 40)
        self.fileButton.pressed.connect(self.file_btn_pressed)

        self.deleteButton = QPushButton("Удалить запись", self)
        self.deleteButton.move(20, 450)
        self.deleteButton.resize(300, 50)

        self.submitButton = QPushButton("Добавить запись", self)
        self.submitButton.move(340, 450)
        self.submitButton.resize(300, 50)
        self.submitButton.pressed.connect(self.submit_btn)

        self.actions_button_init()

    def actions_button_init(self):
        self.ao_open_btn.triggered.connect(
            partial(self.dbsqlite_connection, self.qt_sql_table, 'categories', self.DB_NAME))
        self.bo_open_btn.triggered.connect(partial(self.dbsqlite_connection, self.qt_sql_table, 'units', self.DB_NAME))
        self.co_open_btn.triggered.connect(
            partial(self.dbsqlite_connection, self.qt_sql_table, 'positions', self.DB_NAME))
        self.do_open_btn.triggered.connect(partial(self.dbsqlite_connection, self.qt_sql_table, 'goods', self.DB_NAME))
        self.eo_open_btn.triggered.connect(
            partial(self.dbsqlite_connection, self.qt_sql_table, 'employees', self.DB_NAME))
        self.fo_open_btn.triggered.connect(
            partial(self.dbsqlite_connection, self.qt_sql_table, 'vendors', self.DB_NAME))

    def file_btn_pressed(self):
        self.DB_NAME = QFileDialog.getOpenFileName(self, 'Open file')[0]
        self.txt.setText(self.DB_NAME)
        self.actions_button_init()

    def dbsqlite_connection(self, query_table, db_table, name):
        conn = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        conn.setDatabaseName(name)
        if conn.open():
            # Just to see what is in the DB:
            # query_model = QtSql.QSqlQueryModel(parent=query_table)
            # query_model.setQuery(f"select * from {db_table}")
            # query_table.setModel(query_model)
            # Edit the DB:
            self.model_table = QtSql.QSqlTableModel()
            self.model_table.setTable(f"{db_table}")
            self.model_table.select()

            query_table.setModel(self.model_table)

        conn.close()

    def submit_btn(self):
        self.model_table.select()


# Отобразить главное окно
if __name__ == "__main__":
    app = QApplication(sys.argv)
    CMW = CatalogMainWindow()
    CMW.setWindowTitle('Складской учет')
    CMW.setFixedSize(1200, 800)
    CMW.show()
    sys.exit(app.exec_())
