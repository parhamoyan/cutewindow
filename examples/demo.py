import sys

from PySide6.QtWidgets import QApplication

from qutewindow import CuteWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = CuteWindow()
    demo.show()
    sys.exit(app.exec())
