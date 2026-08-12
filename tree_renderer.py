from graphviz import Digraph


def dibujar_arbol(raiz, ruta_salida):
    """Dibuja el arbol sintactico con Graphviz y lo guarda como PNG.

    ruta_salida es la ruta del archivo sin extension (ej. "salida/expresion_1").
    Devuelve la ruta del PNG generado.
    """
    grafo = Digraph()
    contador = [0]

    def agregar_nodo(nodo):
        id_nodo = str(contador[0])
        contador[0] += 1
        grafo.node(id_nodo, nodo.valor)

        if nodo.izquierdo:
            id_izquierdo = agregar_nodo(nodo.izquierdo)
            grafo.edge(id_nodo, id_izquierdo)
        if nodo.derecho:
            id_derecho = agregar_nodo(nodo.derecho)
            grafo.edge(id_nodo, id_derecho)

        return id_nodo

    agregar_nodo(raiz)

    return grafo.render(ruta_salida, format="png", cleanup=True)
