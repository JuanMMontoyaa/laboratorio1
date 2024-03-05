class Conjunto:
    def __init__(self, elementos):
        self.elementos = elementos
    
    def union(self, otro_conjunto):
        otrosElementos = [elemento for elemento in otro_conjunto.elementos if elemento not in self.elementos]
        return Conjunto(self.elementos + otrosElementos)
    
    def interseccion(self, otro_conjunto):
        return Conjunto([elemento for elemento in self.elementos if elemento in otro_conjunto.elementos])
    
    def diferencia(self, otro_conjunto):
        return Conjunto([elemento for elemento in self.elementos if elemento not in otro_conjunto.elementos])
    
    def complemento(self, universo):
        return Conjunto([elemento for elemento in universo.elementos if elemento not in self.elementos])
    
    def cardinalidad(self):
        return len(self.elementos)
    
    def es_subconjunto(self, otro_conjunto):
        return all(elemento in otro_conjunto.elementos for elemento in self.elementos)
    
    def es_disjunto(self, otro_conjunto):
        return all(elemento not in otro_conjunto.elementos for elemento in self.elementos)
    
    def __str__(self):
        return str(self.elementos)

    def totalData(self):
        return len(self.elementos)

    def getElements(self):
        return self.elementos

    def diferencia(self, otro_conjunto):
        return Conjunto([x for x in self.elementos if x not in otro_conjunto.elementos]).getElements()
