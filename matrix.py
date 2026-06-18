class Matrix:
    def __init__(self,x):
        self.matrix = x
        self.column = len(self.matrix[0])
        self.row = len(self.matrix)
    
    def show(self):
        column = len(self.matrix)
        for i in range(column):
            print(self.matrix[i])

    def transpose(self):
        result = []
        for i in range(self.row):
            d
    
kotak = Matrix([
    [1,2,3],
    [4,5,6]
])

kotak.show()
