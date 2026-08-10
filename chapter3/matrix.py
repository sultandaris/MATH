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

        return Matrix(result)

    def add(self, val):
        if(self.row == val.row and self.column == self.row):
            for i in range(self.row):
                for j in range(self.column):
                    self.matrix[i][j] = self.matrix[i][j] + val.matrix[i][j]
        else:
            print("Matrix tidak bisa dijumlahkan karena ukuran berbeda!!! \n")
            print("Ukuran matrix awal : ", self.row, "x", self.column)
            print("Ukuran matrix input : ", val.row, "x", val.column)
            print("Silahkan masukkan matrix dengan ukuran yang sama untuk dijumlahkan \n")

    def multiply(self, val):
        if (self.row == val.column):
            newM = []
            for i in range(self.row):
                elemen = []
                for j in range(val.column):
                    final = 0
                    for l in range(self.column):
                        final = final + (self.matrix[i][l] * val.matrix[l][j])
                    elemen.append(final)
                newM.append(elemen)
            return Matrix(newM)
        else:
            print("gabisa")
            return Matrix(self.matrix)

    def saring(self,b_row,b_column):
        list = []
        for i in range(self.row):
            if(i == b_row):
                i += 1
                continue
            rows = []
            for j in range(self.column):
                if(i == b_row or j == b_column):
                    continue
                else:
                    rows.append(self.matrix[i][j])
            list.append(rows)
        return Matrix(list)

    def determinant(self):
        if(self.row == self.column):
            if(self.row == 1):
                return self.matrix[0][0]
            else:
                total = 0
                for i in range(1):
                    for j in range(self.column):
                        if((i + j) % 2 == 0):
                            baru = self.saring(i,j)
                            total += self.matrix[i][j] * baru.determinant()
                        else:
                            baru = self.saring(i,j)
                            total -= self.matrix[i][j] * baru.determinant()
                return total
        else:
            print("tidak bisa dihitung", self.row, "x", self.column)

    def cekNol(self,row,column):
        val = row
        while val < self.row:
            if(self.matrix[val][column] != 0):
                return val
            val+=1
        return row

    def tukarBaris(self,pivot,row):
        salinan = []
        for j in range(self.column):
            salinan.append(self.matrix[row][j])
            self.matrix[row][j] = self.matrix[pivot][j]
            self.matrix[pivot][j] = salinan[j]
            j+=1

    def pembagian(self,row,column):
        pembagi = self.matrix[row][column]
        if(pembagi != 0):
            for j in range(self.column):
                self.matrix[row][j] = self.matrix[row][j] / pembagi

    def pengurangan(self,row,column):
        for i in range(self.row):
            faktor = self.matrix[i][column]
            for j in range(self.column):
                if(i != row):
                    self.matrix[i][j] = self.matrix[i][j] - (faktor * self.matrix[row][j])
                else:
                    break

    def REF(self):
        row = 0
        for column in range(self.column):
            kolom_pivot = self.cekNol(row,column)
            if(kolom_pivot != row):
                self.tukarBaris(kolom_pivot,row)
            self.pembagian(row,column)
            self.pengurangan(row,column)
            row = row + 1

kotak = Matrix([
    [1,2],
    [3,4]
])

kotak.show()
kotakT = kotak.transpose()
kotakT.show()
kotakM = kotak.multiply(kotakT)
kotakM.show()
print(kotak.determinant())
kotak.REF()
kotak.show()
