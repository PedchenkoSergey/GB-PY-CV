import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication


class CatalogMainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

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

        self.ao_open_btn.triggered.connect(self.button_pressed)


    def button_pressed(self):
        print(f'button pressed')


# Отобразить главное окно
if __name__ == "__main__":
    app = QApplication(sys.argv)
    CMW = CatalogMainWindow()
    CMW.setWindowTitle('Складской учет')
    CMW.setFixedSize(1200, 800)
    CMW.show()
    sys.exit(app.exec_())
