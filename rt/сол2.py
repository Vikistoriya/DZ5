import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton, QMessageBox, QHBoxLayout
)
from PyQt6.QtCore import Qt

class FoodApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Приложение с едой")
        self.resize(400, 300)

        # Установка основного макета
        layout = QVBoxLayout()

        # Заголовок приложения
        title = QLabel("Выберите ваше блюдо:")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        # Список блюд
        self.food_list = QListWidget(self)
        self.food_list.addItems([
            "Пицца - Вкусная итальянская пицца с различными начинками.",
            "Суши - Японские суши с рыбой и овощами.",
            "Бургер - Классический бургер с мясом и овощами.",
            "Салат - Свежий салат с зеленью и овощами.",
            "Паста - Итальянская паста с томатным соусом."
        ])
        layout.addWidget(self.food_list)

        # Кнопки
        button_layout = QHBoxLayout()

        add_favorite_button = QPushButton("Добавить в избранное", self)
        add_favorite_button.clicked.connect(self.add_to_favorites)
        button_layout.addWidget(add_favorite_button)

        show_favorites_button = QPushButton("Показать избранное", self)
        show_favorites_button.clicked.connect(self.show_favorites)
        button_layout.addWidget(show_favorites_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)
        self.favorites = []

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
            QListWidget {
                background-color: #fff;
                border: 1px solid #ccc;
                padding: 10px;
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

    def add_to_favorites(self):
        selected_item = self.food_list.currentItem()
        if selected_item:
            food_name = selected_item.text()
            if food_name not in self.favorites:
                self.favorites.append(food_name)
                QMessageBox.information(self, "Успех", f"{food_name} добавлено в избранное!")
            else:
                QMessageBox.warning(self, "Ошибка", f"{food_name} уже в избранном!")
        else:
            QMessageBox.warning(self, "Ошибка", "Выберите блюдо для добавления в избранное.")

    def show_favorites(self):
        if self.favorites:
            favorites_str = "n".join(self.favorites)
            QMessageBox.information(self, "Избранное", favorites_str)
        else:
            QMessageBox.information(self, "Избранное", "Избранное пусто.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    food_app = FoodApp()
    food_app.show()
    sys.exit(app.exec())
