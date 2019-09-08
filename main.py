"""This is a module for interpolation comparison."""

import sys

from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel,
                             QLineEdit, QComboBox, QPushButton, QMessageBox)
from PyQt5.QtCore import Qt

import interpolation


class InterpolationComparison(QWidget):
    """This is a class for interpolation comparison."""
    def __init__(self):
        super().__init__()
        self.interface()

    def interface(self):
        """This is a function to create GUI."""

        self.setWindowTitle("Interpolation Comparison")
        self.resize(600, 1)

        # Layout
        self.layout = QGridLayout()

        # Labels
        self.lbl1 = QLabel("Enter starting value:")
        self.lbl2 = QLabel("Enter end value:")
        self.lbl3 = QLabel("Enter number of samples:")
        self.lbl4 = QLabel(
            "Enter interpolated function (example: sin(x) + 2):")
        self.lbl5 = QLabel("Choose first kind of interpolation:")
        self.lbl6 = QLabel("Choose second kind of interpolation:")

        # LineEdits
        self.edit1 = QLineEdit()
        self.edit2 = QLineEdit()
        self.edit3 = QLineEdit()
        self.edit4 = QLineEdit()

        # ComboBoxs
        self.box1 = QComboBox()
        self.box1.addItems([
            "linear", "nearest", "zero", "slinear", "quadratic", "cubic",
            "previous", "next"
        ])
        self.box2 = QComboBox()
        self.box2.addItems([
            "linear", "nearest", "zero", "slinear", "quadratic", "cubic",
            "previous", "next"
        ])

        # Buttons
        self.btn_start = QPushButton("START!")
        self.btn_start.clicked.connect(self.btn_start_clicked)
        self.btn_reset = QPushButton("RESET")
        self.btn_reset.clicked.connect(self.btn_reset_clicked)

        # Labels to layout
        self.layout.addWidget(self.lbl1, 0, 0)
        self.layout.addWidget(self.lbl2, 1, 0)
        self.layout.addWidget(self.lbl3, 2, 0)
        self.layout.addWidget(self.lbl4, 3, 0)
        self.layout.addWidget(self.lbl5, 4, 0)
        self.layout.addWidget(self.lbl6, 5, 0)

        # LineEdits to layout
        self.layout.addWidget(self.edit1, 0, 1)
        self.layout.addWidget(self.edit2, 1, 1)
        self.layout.addWidget(self.edit3, 2, 1)
        self.layout.addWidget(self.edit4, 3, 1)

        # ComboBoxs to layout
        self.layout.addWidget(self.box1, 4, 1)
        self.layout.addWidget(self.box2, 5, 1)

        # Buttons to layout
        self.layout.addWidget(self.btn_start, 6, 1)
        self.layout.addWidget(self.btn_reset, 6, 0)

        # Set layout
        self.setLayout(self.layout)

    def btn_start_clicked(self):
        """This is a function for handling btn_start clicks."""

        # Checking if the fields are not empty
        if self.edit1.text() == "" or self.edit2.text(
        ) == "" or self.edit3.text() == "" or self.edit4.text() == "":
            QMessageBox.warning(self, "Error", "You must complete all fields!",
                                QMessageBox.Ok)
            exit(1)

        # Assigning values ​​from fields
        try:
            start = float(self.edit1.text())
            stop = float(self.edit2.text())
            samples = int(self.edit3.text())
        except (ValueError):
            QMessageBox.warning(self, "Error",
                                "You have entered an invalid data type!",
                                QMessageBox.Ok)
            exit(1)
        function = self.edit4.text()
        first_kind = self.box1.currentText()
        second_kind = self.box2.currentText()

        # Checking if the START value is less than the STOP value
        if (start >= stop):
            QMessageBox.warning(
                self, "Error",
                "The stop value must be greater than the start value",
                QMessageBox.Ok)
            exit(1)

        # Checking if the number of samples is greater than 5
        if (samples <= 5):
            QMessageBox.warning(
                self, "Error", "The number of samples must be greater than 5!",
                QMessageBox.Ok)
            exit(1)

        # Run interpolation function
        interp_obj = interpolation.Interpolation(start, stop, samples,
                                                 function, first_kind,
                                                 second_kind)
        interp_obj.interpolation_graph()

    def btn_reset_clicked(self):
        """This is a function for handling btn_reset clicks."""

        self.edit1.clear()
        self.edit2.clear()
        self.edit3.clear()
        self.edit4.clear()
        self.box1.clear()
        self.box1.addItems([
            "linear", "nearest", "zero", "slinear", "quadratic", "cubic",
            "previous", "next"
        ])
        self.box2.clear()
        self.box2.addItems([
            "linear", "nearest", "zero", "slinear", "quadratic", "cubic",
            "previous", "next"
        ])

    def keyPressEvent(self, e):
        """This is a function to close app using the ESC key."""

        if e.key() == Qt.Key_Escape:
            self.close()


def main():
    """This is a function to run app."""

    app = QApplication(sys.argv)
    window = InterpolationComparison()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
