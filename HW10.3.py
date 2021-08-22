class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __str__(self):
        return f"{self.cell}"

    def __add__(self, other):
        print("Sum of Cell is:")
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        print("Sub of Cell is:")
        return Cell(self.cell - other.cell) if self.cell - other.cell > 0 \
            else "Во второй клетке ячеек больше, чем в первой"

    def __mul__(self, other):
        print("Mul of Cell is:")
        return Cell(self.cell * other.cell)

    def __floordiv__(self, other):
        print("Floordiv of Cell is:")
        return Cell(self.cell // other.cell)

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.cell // rows)]) + '\n' + '*' * (self.cell % rows)


cell_1 = Cell(15)
cell_2 = Cell(12)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_2.make_order(6))