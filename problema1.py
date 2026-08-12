import sys

from file_utils import leer_lineas
from shunting_yard import convertir_a_postfix
from tree_builder import construir_arbol
from tree_renderer import dibujar_arbol
from thompson import construir_afn
from afn_renderer import dibujar_afn
from simulador import simular


def main():
    if len(sys.argv) < 3:
        print("Uso: python problema1.py <archivo_expresiones> <archivo_cadenas>")
        return

    expresiones = leer_lineas(sys.argv[1])
    cadenas = leer_lineas(sys.argv[2])

    if len(expresiones) != len(cadenas):
        print("El archivo de cadenas debe tener una linea por cada expresion.")
        return

    for numero, (expresion, cadena) in enumerate(zip(expresiones, cadenas), start=1):
        print(f"\nExpresion {numero}: {expresion}")
        print(f"  Cadena w: {cadena!r}")

        postfix, pasos_postfix = convertir_a_postfix(expresion)
        print("  Conversion a postfix:")
        for paso in pasos_postfix:
            print(f"    {paso}")
        print(f"  Postfix: {' '.join(postfix)}")

        raiz, pasos_arbol = construir_arbol(postfix)
        print("  Construccion del arbol:")
        for paso in pasos_arbol:
            print(f"    {paso}")

        ruta_arbol = dibujar_arbol(raiz, f"salida/expresion_{numero}")
        print(f"  Arbol guardado en: {ruta_arbol}")

        afn = construir_afn(raiz)
        ruta_afn = dibujar_afn(afn, f"salida/afn_{numero}")
        print(f"  AFN guardado en: {ruta_afn} ({afn.num_estados} estados, {len(afn.transiciones)} transiciones)")

        aceptada = simular(afn, cadena)
        print(f"  w pertenece a L(r): {'si' if aceptada else 'no'}")


if __name__ == "__main__":
    main()
