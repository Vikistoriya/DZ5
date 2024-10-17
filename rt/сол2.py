import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton, QMessageBox, QHBoxLayout)

class FoodApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Еда, Я люблю тебя!")
        self.resize(400, 300)

        layout = QVBoxLayout()

        self.food_list = QListWidget(self)
        self.food_list.addItems([
            "Пицца - Вкусная итальянская пицца с различными начинками.",
            "Суши - Японские суши с рыбой и овощами.",
            "Бургер - Классический бургер с мясом и овощами.",
            "Салат - Свежий салат с зеленью и овощами.",
            "Паста - Итальянская паста с томатным соусом."
        ])
        layout.addWidget(self.food_list)

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

    def add_to_favorites(self):
        selected_item = self.food_list.currentItem()
        if selected_item:
            food_name = selected_item.text()
            if food_name not in self.favorites:
                self.favorites.append(food_name)
                QMessageBox.information(self, "Готово", f"{food_name} добавлено в избранное!")
            else:
                QMessageBox.warning(self, "Ошибка", f"{food_name} уже в избранном!")
        else:
            QMessageBox.warning(self, "Ошибка", "Выберите блюдо для добавления в избранное.")

    def show_favorites(self):
        if self.favorites:
            favorites_str = "n".join(self.favorites)
            QMessageBox.information(self, "Избранное", favorites_str)
        else:
            QMessageBox.information(self, "Избранное", "избранное пусто.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    food_app = FoodApp()
    food_app.show()
    sys.exit(app.exec())
