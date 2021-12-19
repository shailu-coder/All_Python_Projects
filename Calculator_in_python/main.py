import sys
from PyQt5.QtWidgets import QApplication
from calculator import CalculatorWindow
# This Project Is Developed By Shailendra Singh Admin Of @Python_Coderz_ Page - Instagram
# Dm Us If You Have Any Query- https://www.instagram.com/python_Coderz_/

app = QApplication(sys.argv)

calculator = CalculatorWindow()

sys.exit(app.exec_())
