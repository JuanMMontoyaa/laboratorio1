import tkinter as tk
from model.conjunto import Conjunto
from printDiagram import printDiagram

def mostrar_texto():
    texto = int(entry.get())
    if texto == 2:
        for widget in contenedor.winfo_children():
            widget.destroy()
        
        textC1 = tk.Label(contenedor, text="Ingresa el conjunto 1: ")
        textC1.pack()
        conjunto1 = tk.Entry(contenedor)
        conjunto1.pack()
        
        textC2 = tk.Label(contenedor, text="Ingresa el conjunto 2: ")
        textC2.pack()
        conjunto2 = tk.Entry(contenedor)
        conjunto2.pack()
        textC3 = tk.Label(contenedor, text="escribe la operacion que deseas hacer")
        textC3.pack()
        resultado = tk.Entry(contenedor)
        resultado.pack()
        resolver= tk.Button(contenedor, text="resolver", command= lambda: calcular2(conjunto1, conjunto2, resultado))
        resolver.pack()

    elif texto == 3:
        for widget in contenedor.winfo_children():
        # Destruir cada widget
            widget.destroy()
        textC1 = tk.Label(contenedor, text="Ingresa el conjunto 1: ")
        textC1.pack()
        conjunto1 = tk.Entry(contenedor)
        conjunto1.pack()
        
        textC2 = tk.Label(contenedor, text="Ingresa el conjunto 2: ")
        textC2.pack()
        conjunto2 = tk.Entry(contenedor)
        conjunto2.pack()
        
        textC3 = tk.Label(contenedor, text="Ingresa el conjunto 3: ")
        textC3.pack()
        conjunto3 = tk.Entry(contenedor)
        conjunto3.pack()
        textC4 = tk.Label(contenedor, text="escribe la operacion que deseas hacer")
        textC4.pack()
        resultado = tk.Entry(contenedor)
        resultado.pack()
        resolver= tk.Button(contenedor, text="resolver", command=lambda:calcular3(conjunto1, conjunto2, conjunto3, resultado))
        resolver.pack()

    else:
        for widget in contenedor.winfo_children():
        # Destruir cada widget
            widget.destroy()
        textC3 = tk.Label(contenedor, text="solo se pueden de a 2 o 3 conjuntos")
        textC3.pack()



def calcular2(conjunto1, conjunto2, operacion):
    con1 = conjunto1.get()
    con2 = conjunto2.get()
    oper = operacion.get()

    A = []
    B = []
    for i in range(len(con1)):
        if con1[i] != ',' and con1[i] != ' ':
            A.append(con1[i])
    
    for i in range(len(con2)):
        if con2[i] != ',' and con2[i] != ' ':
            B.append(con2[i])

    conjunto_a = Conjunto(A)
    conjunto_b = Conjunto(B)

    operIsOperation = isOperation(oper)

    if operIsOperation:
        response = executeOperationForTwo(oper, conjunto_a, conjunto_b)
    else:
        executeFunctionalitiesForTwo(oper, conjunto_a, conjunto_b)
        
    if operIsOperation:
        print("response: ", response)
        printDiagram(oper, conjunto_a, conjunto_b, response)


def calcular3(conjunto1, conjunto2, conjunto3, operacion):
    con1 = conjunto1.get()
    con2 = conjunto2.get()
    con3 = conjunto3.get()
    oper = operacion.get()

    A = []
    B = []
    C = []
    for i in range(len(con1)):
        if con1[i] != ',' and con1[i] != ' ':
            A.append(con1[i])
    print(A)
    
    for i in range(len(con2)):
        if con2[i] != ',' and con2[i] != ' ':
            B.append(con2[i])
    print(B)
    for i in range(len(con3)):
        if con3[i] != ',' and con3[i] != ' ':
            C.append(con3[i])
    print(C)

    conjunto_a = Conjunto(A)
    conjunto_b = Conjunto(B)
    conjunto_c = Conjunto(C)
    executeFunctionalitiesForTwo(oper, conjunto_a, conjunto_b, conjunto_c)
    union = conjunto_a.interseccion(conjunto_b.interseccion(conjunto_C))
    print(union)


def executeFunctionalitiesForTwo(operation, conjunto_a, conjunto_b):
    if operation.lower() == "cardinalidad":
        tk.Label(contenedor, text="Conjunto A: " + str(conjunto_a.cardinalidad())).pack()
        tk.Label(contenedor, text="Conjunto B: " + str(conjunto_b.cardinalidad())).pack()
        print(conjunto_a.cardinalidad())
        print(conjunto_b.cardinalidad())
    elif operation.lower() == "subconjunto":
        tk.Label(contenedor, text="¿A es subconjunto de B? " + str(conjunto_a.es_subconjunto(conjunto_b))).pack()
        print("¿A es subconjunto de B?", conjunto_a.es_subconjunto(conjunto_b))
    elif operation.lower() == "disjunto":
        tk.Label(contenedor, text="¿A y B son disjuntos? " + str(conjunto_a.es_disjunto(conjunto_b))).pack()
        print("¿A y B son disjuntos?", conjunto_a.es_disjunto(conjunto_b))

def executeFunctionalitiesForThree(operation, conjunto_a, conjunto_b, conjunto_c):
    if isOperation(operation):
        executeOperationForThree(operation, conjunto_a, conjunto_b, conjunto_c)
    elif operation.lower() == "cardinalidad":
        print(conjunto_a.cardinalidad())
        print(conjunto_b.cardinalidad())
        print(conjunto_c.cardinalidad())
    elif operation.lower() == "subconjunto":
        validSubConjuntoOfThree(conjunto_a, conjunto_b, conjunto_c)        
    elif operation.lower() == "disjunto":
        print("¿A y C son disjuntos?", conjunto_a.es_disjunto(conjunto_c))

def validSubConjuntoOfThree(conjunto_a, conjunto_b, conjunto_c):
    if conjunto_a.es_subconjunto(conjunto_b):
        print("A es subconjunto de B")
    elif conjunto_b.es_subconjunto(conjunto_c):
        print("B es subconjunto de C")
    else:
        print("Ninguno de los conjuntos es subconjunto del otro")

def validDisjuntoOfThree(conjunto_a, conjunto_b, conjunto_c):
    if conjunto_a.es_disjunto(conjunto_b):
        print("A es disjunto de B")
    elif conjunto_b.es_disjunto(conjunto_c):
        print("B es disjunto de C")
    else:
        print("Ninguno de los conjuntos es subconjunto del otro")

def isOperation(operation):
    if operation.lower() == "union" or operation.lower() == "interseccion" or operation.lower() == "diferencia" or operation.lower() == "complemento":
        return True
    else:
        return False   

def executeOperationForTwo(operation, conjunto_a, conjunto_b):
    if operation.lower() == "union":
        return conjunto_a.union(conjunto_b)
    elif operation.lower() == "interseccion":
        return conjunto_a.interseccion(conjunto_b)
    elif operation.lower() == "diferencia":
        return conjunto_a.diferencia(conjunto_b)
    elif operation.lower() == "complemento":
        return conjunto_a.complemento(conjunto_b)

def executeOperationForThree(operation, conjunto_a, conjunto_b, conjunto_C):
    if operation.lower() == "union":
        return conjunto_a.union(conjunto_b.union(conjunto_C))
    elif operation.lower() == "interseccion":
        return conjunto_a.interseccion(conjunto_b.interseccion(conjunto_C))
    elif operation.lower() == "diferencia":
        return conjunto_a.diferencia(conjunto_b.diferencia(conjunto_C))
    elif operation.lower() == "complemento":
        return conjunto_a.complemento(conjunto_b.complemento(conjunto_C))

root = tk.Tk()
root.geometry("400x400")
etiqueta = tk.Label(root, text="ingresa la cantidad de conjuntos (entre 2 y 3)")
etiqueta.pack()
entry = tk.Entry(root)
entry.pack()
# Crear un botón para mostrar el texto ingresado
boton = tk.Button(root, text="verificar", command=mostrar_texto)
boton.pack()
contenedor = tk.Frame(root, borderwidth=2, relief="groove")
contenedor.pack(padx=10, pady=10)
root.mainloop()