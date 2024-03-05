from matplotlib import pyplot as plt
from matplotlib_venn import venn2


def printDiagram(operation, conjunto_a, conjunto_b, response):

    if operation.lower() == "union":
        printUnion(response)
    elif operation.lower() == "interseccion":
        printInterseccion(operation, conjunto_a, conjunto_b, response)
    elif operation.lower() == "diferencia":
        printDiferencia(operation, conjunto_a, conjunto_b, response)
    elif operation.lower() == "complemento":
        printComplemento(response)
    


def printUnion(response):

    # Crea un diagrama de Venn
    venn_diagram = venn2(subsets=(response.totalData(), 0, 0),
        set_labels=('Union'))

    venn_diagram.get_label_by_id('10').set_text('\n'.join(map(str, response.elementos)))

    title = 'Diagrama de Venn' + '\n' + 'Union'
    plt.title(title)
    plt.show()

def printInterseccion(operation, conjunto_a, conjunto_b, response):
     # Crea un diagrama de Venn
    venn_diagram = venn2(subsets=(conjunto_a.totalData(), conjunto_b.totalData(), response.totalData()),
        set_labels=('Conjunto A', 'Conjunto B'))

    # Agrega etiquetas para los elementos de cada conjunto
    venn_diagram.get_label_by_id('10').set_text('\n'.join(map(str, conjunto_a.diferencia(conjunto_b))))
    venn_diagram.get_label_by_id('01').set_text('\n'.join(map(str, conjunto_b.diferencia(conjunto_a))))
    venn_diagram.get_label_by_id('11').set_text('\n'.join(map(str, response.elementos)))

    title = 'Diagrama de Venn' + '\n' + 'Interseccion'
    plt.title(title)
    plt.show()

def printDiferencia(operation, conjunto_a, conjunto_b, response):

    venn_diagram = venn2(subsets=(conjunto_a.totalData(), conjunto_b.totalData(), 0),
        set_labels=('Conjunto A', 'Conjunto B'))

    # Agrega etiquetas para los elementos de cada conjunto
    venn_diagram.get_label_by_id('10').set_text('\n'.join(map(str, conjunto_a.diferencia(conjunto_b))))
    venn_diagram.get_label_by_id('01').set_text('\n'.join(map(str, conjunto_b.diferencia(conjunto_a))))

    # Muestra el diagrama de Venn
    plt.title('Diagrama de Venn (Diferencia de A con B)')
    plt.show()


def printComplemento(response):

    # Crea un diagrama de Venn
    venn_diagram = venn2(subsets=(response.totalData(), 0, 0),
        set_labels=('Complemento'))

    venn_diagram.get_label_by_id('10').set_text('\n'.join(map(str, response.elementos)))

    title = 'Diagrama de Venn' + '\n' + 'Complemento'
    plt.title(title)
    plt.show()




