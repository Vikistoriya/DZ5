import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QHBoxLayout, QFrame
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Авторизация")
        self.resize(300, 200)

        layout = QVBoxLayout()

        # Заголовок
        title = QLabel("Авторизация")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        # Поля ввода
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Введите имя пользователя")
        layout.addWidget(self.username_input)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Введите пароль")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_input)

        # Кнопка авторизации
        login_button = QPushButton("Войти", self)
        login_button.clicked.connect(self.login)
        layout.addWidget(login_button)

        self.setLayout(layout)

        # Применение стилей
        self.setStyleSheet("""
            QWidget {
                background-color: #f0f0f0;
                font-family: Arial, sans-serif;
            }
            QLabel {
                font-size: 20px;
                color: #333;
            }
            QLineEdit {
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 10px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3e8e41;
            }
        """)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Простейшая проверка (можно заменить на реальную логику)
        if username == "user" and password == "password":
            self.profile_window = ProfileWindow(username)
            self.profile_window.show()
            self.close()
        else:
            QMessageBox.warning(self, "Ошибка", "Неверное имя пользователя или пароль.")


class ProfileWindow(QWidget):
    def __init__(self, username):
        super().__init__()
        self.init_ui(username)

    def init_ui(self, username):
        self.setWindowTitle("Личный профиль")
        self.resize(400, 300)

        layout = QVBoxLayout()

        # Заголовок профиля
        title = QLabel(f"Добро пожаловать, {username}!")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        # Изображение профиля
        profile_image = QLabel(self)
        pixmap = QPixmap("path/to/your/image.jpg")  # Замените на путь к вашей картинке
        profile_image.setPixmap(pixmap.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio))
        profile_image.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(profile_image)

        # Кнопка выхода
        logout_button = QPushButton("Выйти", self)
        logout_button.clicked.connect(self.logout)
        layout.addWidget(logout_button)

        self.setLayout(layout)

        # Применение стилей
        self.setStyleSheet("""
            QWidget {
                background-color: #f0f0f0;                
                font-family: Arial, sans-serif;
            }
            QLabel {
                font-size: 20px;
                color: #333;
            }
            QPushButton {
                background-color: #f44336;
                color: white;
                padding: 10px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            QPushButton:hover {
                background-color: #e53935;
            }
            QPushButton:pressed {
                background-color: #d32f2f;
            }
        """)

    def logout(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())

