class Matrix:
    def __init__(self,x):
        self.matrix = x
        self.column = len(self.matrix[0])
        self.row = len(self.matrix)
    
    def show(self):
        column = len(self.matrix)
        for i in range(column):
            print(self.matrix[i])
        print()

    def transpose(self):
        result = []
        for i in range(self.column):
            rows = []
            for j in range(self.row):
                rows.append(self.matrix[j][i])
            result.append(rows)

        print("---",self.row,self.column)
        return Matrix(result)

    def add(self, val):
        if(self.row == val.row and self.column == self.row):
            result
       
kotak = Matrix([
    [2,3,3],
    [5,6,9]
])

kotak.show()
kotakT = kotak.transpose()
kotak.show()
kotak.add(kotakT)
