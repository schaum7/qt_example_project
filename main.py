import sys
from qtpy import QtWidgets
from ui.mainwindow import Ui_MainWindow


app = QtWidgets.QApplication(sys.argv)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Testanwendung")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pb_vergleiche.clicked.connect(self.on_pb_vergleiche_click)
        self.ui.pb_berechne_bmi.clicked.connect(self.on_pb_berechne_bmi_click)

    def on_pb_vergleiche_click(self):
        result = ""

        if self.ui.le_input1.text() == "" or self.ui.le_input2.text() == "":
            result = "FEHLER!! Eins der Felder ist leer!"
            self.ui.tb_result.setTextColor("red")
        else:
            if self.ui.le_input1.text() == self.ui.le_input2.text():
                result = "GLEICH"
            else:
                result = "UNGLEICH"

        self.ui.tb_result.setText(result)

    def on_pb_berechne_bmi_click(self):
        groesse_m = float(self.ui.le_height_m.text())
        gewicht_kg = float(self.ui.le_weight_kg.text())
        if groesse_m == 0.0:
            self.ui.lbl_bmi.setText("Größe darf nicht 0 sein!")
        else:
            bmi = gewicht_kg/(groesse_m**2)

            self.ui.lbl_bmi.setText("BMI {0:.3f}".format(bmi))


window = MainWindow()
window.show()

sys.exit(app.exec_())
