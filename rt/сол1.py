import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QStackedWidget, QHBoxLayout, QFileDialog)
from PyQt6.QtGui import QPixmap


class AuthWindow(QWidget):
    def __init__(self, switch_to_profile):
        super().__init__()
        self.switch_to_profile = switch_to_profile
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Введите имя пользователя")
        layout.addWidget(self.username_input)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Введите пароль")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_input)

        login_button = QPushButton("Войти", self)
        login_button.clicked.connect(self.handle_login)
        layout.addWidget(login_button)

        self.setLayout(layout)
        self.setWindowTitle("авторизация")

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Проверка логина (здесь можно добавить свою логику проверки)
        if username == "user" and password == "pass":
            self.switch_to_profile()
        else:
            QMessageBox.warning(self, "Ошибка", "Неверное имя пользователя или пароль.")


class ProfileWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.photo_label = QLabel("Фотография профиля:")
        layout.addWidget(self.photo_label)

        self.photo = QLabel(self)
        layout.addWidget(self.photo)

        upload_button = QPushButton("Загрузить фото", self)
        upload_button.clicked.connect(self.upload_photo)
        layout.addWidget(upload_button)

        self.setLayout(layout)
        self.setWindowTitle("Личный профиль")

    def upload_photo(self):
        options = QFileDialog.Option()
        file_name, _ = QFileDialog.getOpenFileName(self, "Загрузить фото", "",
                                                   "Images (*.png *.xpm *.jpg);;All Files (*)", options=options)

        if file_name:
            pixmap = QPixmap(file_name)
            self.photo.setPixmap(pixmap.scaled(200, 200))


class MainApp(QStackedWidget):
    def __init__(self):
        super().__init__()

        self.auth_window = AuthWindow(self.show_profile)
        self.profile_window = ProfileWindow()

        self.addWidget(self.auth_window)
        self.addWidget(self.profile_window)

    def show_profile(self):
        self.setCurrentWidget(self.profile_window)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.resize(300, 400)
    main_app.show()
    sys.exit(app.exec())
