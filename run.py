import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QCoreApplication

from ui_others import Ui_Login

if __name__ == "__main__":

    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./bms.jpg"))
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    ui_login = Ui_Login()
    ui_login.show()
    sys.exit(app.exec_())
