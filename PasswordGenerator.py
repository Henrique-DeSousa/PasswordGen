import random
import secrets
import sys
from string import ascii_letters, digits, punctuation

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox, QSystemTrayIcon, QHBoxLayout, QPushButton, \
    QCheckBox, QLabel, QLineEdit, QFrame, QVBoxLayout


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.label = QLabel("Password: ", self)
        self.text_box = QFrame(self)
        self.button = QPushButton("generate", self)
        self.size_field = QLineEdit("Password Size", self)
        self.CheckBox4 = QCheckBox("Special Characters", self)
        self.CheckBox3 = QCheckBox("Numbers", self)
        self.CheckBox2 = QCheckBox("Lower Case", self)
        self.CheckBox1 = QCheckBox("Upper Case", self)
        self.layout = QHBoxLayout()
        self.combo_box = QComboBox(self)
        width = 400
        height = 240
        self.setFixedSize(width, height)
        self.setWindowTitle("Password Generator")
        self.initUI()

    def initUI(self):
        self.setLayout(self.layout)

        self.CheckBox1.setChecked(True)
        self.CheckBox2.setChecked(True)
        self.CheckBox3.setChecked(True)
        self.CheckBox4.setChecked(True)

        self.CheckBox1.setGeometry(100, 25, 120, 30)
        self.CheckBox2.setGeometry(220, 25, 120, 30)
        self.CheckBox3.setGeometry(100, 50, 120, 30)
        self.CheckBox4.setGeometry(220, 50, 120, 30)

        self.layout.addWidget(self.CheckBox1)
        self.layout.addWidget(self.CheckBox2)
        self.layout.addWidget(self.CheckBox3)
        self.layout.addWidget(self.CheckBox4)

        self.combo_box.setGeometry(60, 100, 120, 30)
        self.combo_box.addItems(["Generator 1", "Generator 2"])
        self.layout.addWidget(self.combo_box)

        self.size_field.setGeometry(200, 100, 120, 30)
        self.size_field.echoMode()
        self.size_field.mousePressEvent = self.clear_text
        self.layout.addWidget(self.size_field)

        self.button.setGeometry(125, 150, 120, 30)
        self.button.pressed.connect(self.generate)

        self.label.setTextInteractionFlags(Qt.TextInteractionFlag(True))

        self.text_box.setGeometry(10, 190, 380, 40)
        self.text_box.setStyleSheet("background-color: lightgray;")
        vbox = QVBoxLayout(self.text_box)

        vbox.addWidget(self.label)

    def clear_text(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.size_field.clear()

    def generate(self):
        global size
        index = self.combo_box.currentIndex()
        upper_boolean = self.CheckBox1.isChecked()
        lower_boolean = self.CheckBox2.isChecked()
        numbers_boolean = self.CheckBox3.isChecked()
        special_boolean = self.CheckBox4.isChecked()
        string = self.size_field.text()

        if not string.isnumeric():
            exit(-1)
        else:
            size = int(string)
            if size > 50:
                size = 50
            if size < 15:
                size = 15

        if not lower_boolean and not upper_boolean and not numbers_boolean and not special_boolean:
            exit(-1)
        else:
            if index == 0:
                pass1(lower_boolean, upper_boolean, numbers_boolean, special_boolean, self)
            else:
                pass2(lower_boolean, upper_boolean, numbers_boolean, special_boolean, self)


def pass1(lower_boolean, upper_boolean, numbers_boolean, special_boolean, self):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = lower.upper()
    numbers = "0123456789"
    special = "!£$%^&*()_+=-@}{'#|/\~?><,.¬`¦[]:;€" + "'" + '"'

    character_list = ""

    if lower_boolean:
        character_list += lower
    if upper_boolean:
        character_list += upper
    if numbers_boolean:
        character_list += numbers
    if special_boolean:
        character_list += special

    password = "".join(random.sample(character_list, int(size)))
    self.label.setText(password)


def pass2(lower_boolean, upper_boolean, numbers_boolean, special_boolean, self):
    character_list = ''

    if lower_boolean:
        character_list += ascii_letters.lower()
    if upper_boolean:
        character_list += ascii_letters.upper()
    if numbers_boolean:
        character_list += digits
    if special_boolean:
        character_list += punctuation

    password = ''.join(secrets.choice(character_list) for _ in range(int(size)))
    self.label.setText(password)


def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    tray_icon = QSystemTrayIcon()
    tray_icon.setIcon(QIcon("passGen.png"))

    tray_icon.show()
    tray_icon.setVisible(True)
    win.setWindowIcon(QIcon("passGen.png"))

    win.show()
    sys.exit(app.exec())


window()
