class Matrix:
    def __init__(self, rows, cols, default=0) -> None:
        self.rows = rows
        self.cols = cols
        self.matrix = [[default for i in range(rows)] for j in range(cols)]

    def __str__(self) -> str:
        output = ""
        for i in range(self.rows):
            for j in range(self. cols):
                output += str(self.matrix[i - 1][j - 1]) + " "
            output += "\n"
        return output