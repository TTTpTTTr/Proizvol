import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor
from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
            color = QColor(random.randint(0, 255),
                           random.randint(0, 255),
                           random.randint(0, 255))
            self.circles.append((x, y, d, color))
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        for x, y, d, color in self.circles:
            painter.setBrush(color)
            painter.drawEllipse(x, y, d, d)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())