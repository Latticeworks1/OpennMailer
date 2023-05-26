import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QMovie
from PyQt5.QtCore import Qt, QTimer
import subprocess

class DashboardWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Proxy Domain Email Server")
        self.setGeometry(400, 400, 400, 400)
        
        self.setup_ui()

    def setup_ui(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(5, 5, 5, 5)
        
        # Set background image
        background_label = QLabel(self)
        movie = QMovie("back2.gif")  # Replace with your animated background image path
        movie.setScaledSize(self.size())
        background_label.setMovie(movie)
        movie.start()
        
        # Add widgets to the layout
        layout.addWidget(background_label, alignment=Qt.AlignCenter)
        
        label = QLabel("Select a Site to Send an Email as:")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        button1 = QPushButton("Giardino.it")
        button1.setFixedWidth(200)
        button1.setFixedHeight(60)
        button1.setStyleSheet("padding: 10px;")
        button1.clicked.connect(self.run_giardino_script)
        layout.addWidget(button1, alignment=Qt.AlignCenter)

        button2 = QPushButton("Crestaifx")
        button2.setFixedWidth(200)
        button2.setFixedHeight(60)
        button2.setStyleSheet("padding: 10px;")
        button2.clicked.connect(self.run_crestaifx_script)
        layout.addWidget(button2, alignment=Qt.AlignCenter)

    def run_giardino_script(self):
        subprocess.Popen(["python", "giardino_script.py"])

    def run_crestaifx_script(self):
        subprocess.Popen(["python", "crestaifx_script.py"])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DashboardWindow()
    window.show()
    sys.exit(app.exec_())
