import sys
import random
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.circles = []
        self.pushButton.clicked.connect(self.draw_circles)

    def draw_circles(self):
        self.circles = []
        w = self.width()
        h = self.height()
        for _ in range(10):
            d = random.randint(20, 120)
            x = random.randint(0, max(1, w - d))
            y = random.randint(0, max(1, h - d))
            self.circles.append((x, y, d))
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setBrush(QColor("yellow"))
        for x, y, d in self.circles:
            painter.drawEllipse(x, y, d, d)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())