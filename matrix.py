class Matrix:
    def __init__(self,x):
        self.matrix = x
    
    def show(self):
        column = len(self.matrix)
        for i in range(column):
            print(self.matrix[i])
    
kotak = Matrix([
    [1,2],
    [3,4]
])

kotak.show()
