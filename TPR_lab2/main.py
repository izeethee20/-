from PyQt5.QtWidgets import QApplication, QWidget
import window
from core import MathFpik


class WindowForm(QWidget, window.Ui_Form):
    def __init__(self):
        super(WindowForm, self).__init__()
        self.setupUi(self)
        self.matrix_btn.clicked.connect(self.create_item)
        self.export_btn.clicked.connect(self.export)
        self.export_btn.setEnabled(False)

    def create_item(self):
        self.e, self.f = (int(self.e_le.text()), int(self.f_le.text()))
        self.export_btn.setEnabled(True)
        self.tableWidget.setRowCount(self.e+1)
        self.tableWidget.setColumnCount(self.f)
        self.tableWidget.setHorizontalHeaderLabels(['S{}'.format(i) for i in range(1, self.f+1)])
        self.tableWidget.setVerticalHeaderLabels(['П{}'.format(i) for i in range(1, self.e+1)])
        [self.tableWidget.setColumnWidth(i, 40) for i in range(self.f)]
        # self.tableWidget.setItem(0, 0, QTableWidgetItem("TEXT"))

    def export(self):
        matrix = []
        q = []
        for i in range(self.e):
            self.tableWidget.selectRow(i)
            tmp=[]
            for j in self.tableWidget.selectedItems():
                tmp.append(int(j.text()))
            matrix.append(tmp)
        self.tableWidget.selectRow(int(self.e_le.text()))
        q = [float(j.text()) for j in self.tableWidget.selectedItems()]
        a = MathFpik(self.e, self.f, matrix)
        self.export_te.setPlainText('{}\n{}'.format(a.min_max(), a.beits_laplas(q)))


if __name__ == '__main__':
    app = QApplication([])
    w = WindowForm()
    w.show()
    app.exec_()