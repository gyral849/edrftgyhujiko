import random

class matrica:
    def __init__(self, stroki=2, stolbik=2):
        self.stroki = stroki
        self.stolbik = stolbik
        self.elements = self.stroika()


    def stroika(self):
        matrica_A = [[random.randint(1, 5)for i in range(self.stolbik)]for g in range(self.stroki)]

        return matrica_A

    def umnojenia_na_chislo(self, num=5):
        matric_C = matrica(self.stroki, self.stolbik)
        for l in range(self.stroki):
            for k in range(self.stolbik):
                matric_C.elements[l][k] = self.elements[l][k] * num
            print(matric_C)
        return matric_C
    def subtraction(self, matrica_b):
        matric_B = matrica(self.stroki, self.stolbik)
        for l in range(self.stroki):
            for k in range(self.stolbik):
                matric_B.elements[l][k] = (self.elements[l][k] - matrica_b.elements[l][k])
        return matric_B
    def print_matric (self):
        for l in range(self.stroki):
            for k in range(self.stolbik):
                print(self.elements[l][k], end=' ')
            print()
    def transpor (self):
        matrica_d = [lo[:] for lo in self.elements.copy()]
        matrica_copy = [[0 for k in range(len(matrica_d))]for l in range(len(matrica_d[0]))]
        for l in range(len(matrica_d)):
            for k in range(len(matrica_d[0])):
                matrica_copy[k][l] = matrica_d[l][k]
        print(matrica_copy)
        print(matrica_d)
        return matrica_copy
    def umnojemie_matr(self, matrica_B):
        res_stroki = self.stroki
        res_stolbik = matrica_B.stolbik
        matrica_res = matrica(res_stroki, res_stolbik)
        if self.stolbik != matrica_B.stroki:
            return None

        for i in range(res_stroki):
            for j in range(res_stolbik):
                matrica_res.elements[i][j] = sum((self.elements[i][v] * matrica_B.elements[v][j] for v in range(len(matrica_B.elements[0]))))
        matrica_res.print_matric()
        return matrica_res

f = matrica(5, 3)
h = matrica(3, 5)
f.print_matric()
print()
new_matrix = f.umnojenia_na_chislo(3)
print()
f.print_matric()
print()
new_matrix.print_matric()
print()
k = f.subtraction(h)
k.print_matric()
print('transponirovanie matrici')
f.transpor()
f.umnojemie_matr(h)
