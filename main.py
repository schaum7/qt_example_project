import sys
from qtpy import QtWidgets


app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QMainWindow()
window.setWindowTitle("Testanwendung")

button = QtWidgets.QPushButton(window)
button.setText("Klick mich!")
button.show()

checkbox = QtWidgets.QCheckBox(window)
checkbox.setText("ich bin die Checkbox")
checkbox.setGeometry(30, 100, 200, 100)
checkbox.show()

window.show()

sys.exit(app.exec_())
