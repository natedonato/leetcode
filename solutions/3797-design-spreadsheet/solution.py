class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet = {}

    def setCell(self, cell: str, value: int) -> None:
        self.sheet[cell] = value

    def resetCell(self, cell: str) -> None:
        self.sheet[cell] = 0

    def getValue(self, formula: str) -> int:
        x,y = formula[1:].split("+")
        if x in self.sheet:
            x_v = self.sheet[x]
        elif x.isdigit():
            x_v = int(x)
        else:
            x_v = 0

        if y in self.sheet:
            y_v = self.sheet[y]
        elif y.isdigit():
            y_v = int(y)
        else:
            y_v = 0
        return x_v + y_v

