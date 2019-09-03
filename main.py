import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QComboBox, QPushButton


class InterpolationComparison(QWidget):
    def __init__(self):
        super().__init__()
        self.interface()

    def interface(self):
        self.setWindowTitle("Interpolation Comparison")
        self.resize(600, 1)

        # Layout
        layout = QGridLayout()

        # Labels
        lbl1 = QLabel("Enter starting value:")
        lbl2 = QLabel("Enter end value:")
        lbl3 = QLabel("Enter number of samples:")
        lbl4 = QLabel("Enter interpolated function (example: sin(x) + 2):")
        lbl5 = QLabel("Choose first kind of interpolation:")
        lbl6 = QLabel("Choose second kind of interpolation:")

        # LineEdits
        edit1 = QLineEdit()
        edit2 = QLineEdit()
        edit3 = QLineEdit()
        edit4 = QLineEdit()

        # ComboBoxs
        box1 = QComboBox()
        box1.addItems([
            "linear", "nearest", "zero", "slinear", "quadratic", "cubic",
            "previous", "next"
        ])
        box2 = QComboBox()
        box2.addItems([
            "linear", "nearest", "zero", "slinear", "quadratic", "cubic",
            "previous", "next"
        ])

        # Buttons
        btn1 = QPushButton("START!")

        # Labels to layout
        layout.addWidget(lbl1, 0, 0)
        layout.addWidget(lbl2, 1, 0)
        layout.addWidget(lbl3, 2, 0)
        layout.addWidget(lbl4, 3, 0)
        layout.addWidget(lbl5, 4, 0)
        layout.addWidget(lbl6, 5, 0)

        # LineEdits to layout
        layout.addWidget(edit1, 0, 1)
        layout.addWidget(edit2, 1, 1)
        layout.addWidget(edit3, 2, 1)
        layout.addWidget(edit4, 3, 1)

        # ComboBoxs to layout
        layout.addWidget(box1, 4, 1)
        layout.addWidget(box2, 5, 1)

        # Buttons to layout
        layout.addWidget(btn1, 6, 1)

        # Set layout
        self.setLayout(layout)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = InterpolationComparison()
    sys.exit(app.exec_())