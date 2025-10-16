import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ventana import Ui_MainWindow
# from recetas import lista_de_recetas # Lo usaremos mas adelante

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Conectamos los nuevos botones a funciones
        self.ui.btn_menu.clicked.connect(self.alternar_menu)
        self.ui.btn_ver_receta.clicked.connect(self.ver_receta_del_dia)

    def alternar_menu(self):
        print("Boton de menu presionado")

    def ver_receta_del_dia(self):
        print("Boton de ver receta presionado")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec())
