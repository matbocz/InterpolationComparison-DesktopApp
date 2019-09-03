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
        self.btn1 = QPushButton("START!")

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
        self.layout.addWidget(self.btn1, 6, 1)

        # Set layout
        self.setLayout(self.layout)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = InterpolationComparison()
    sys.exit(app.exec_())