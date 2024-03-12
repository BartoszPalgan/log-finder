import sys, time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QSplashScreen
from PyQt5.QtGui import QIcon, QCursor, QPixmap, QPainter, QMovie
from PyQt5.QtCore import Qt, QSize
import style


class MovieSplashScreen(QSplashScreen):
    def __init__(self, movie, parent=None):
        movie.jumpToFrame(0)
        pixmap = QPixmap(QSize(720, 405))
        QSplashScreen.__init__(self, pixmap)
        self.movie = movie
        self.movie.frameChanged.connect(self.repaint)

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = self.movie.currentPixmap()
        pixmap_scaled = pixmap.scaled(720, 405)
        self.setMask(pixmap_scaled.mask())
        painter.drawPixmap(0, 0, pixmap_scaled)


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        app_icon = QIcon("icon.png")
        self.setWindowIcon(app_icon)

        self.setWindowTitle("Log Finder")
        self.setGeometry(800, 400, 800, 400)
        self.setFixedSize(800, 400)

        self.setStyleSheet(style.style)

        self.drop_area_button = QPushButton("Wybierz plik", self)
        self.drop_area_button.setFixedSize(100, 50)
        self.drop_area_button.move(350, 175)
        self.drop_area_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.drop_area_button.clicked.connect(self.open_file)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Wybierz plik", "", "Pliki wszystkich typów (*)")
        if file_path:
            pass

if __name__ == "__main__":

    app = QApplication(sys.argv)
    movie = QMovie("splash_video.gif")
    splash = MovieSplashScreen(movie)
    splash.show()
    splash.movie.start()
    start = time.time()
    while movie.state() == QMovie.Running and time.time() < start + 3.2:

        app.processEvents()
    window = App()
    window.show()
    splash.finish(window)

    sys.exit(app.exec_())


