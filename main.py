import sys
from qtpy import QtWidgets
from ui.mainwindow import Ui_MainWindow


app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QMainWindow()
window.setWindowTitle("Testanwendung")


def on_button_click():
    result = ""

    if ui_window.le_input1.text() == "" or ui_window.le_input2.text() == "":
        result = "FEHLER!! Eins der Felder ist leer!"
    else:
        if ui_window.le_input1.text() == ui_window.le_input2.text():
            result = "GLEICH"
        else:
            result = "UNGLEICH"

    ui_window.tb_result.setText(result)


ui_window = Ui_MainWindow()
ui_window.setupUi(window)
ui_window.pb_vergleiche.clicked.connect(on_button_click)


window.show()

sys.exit(app.exec_())
