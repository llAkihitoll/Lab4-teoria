import sys

from file_utils import leer_lineas
from shunting_yard import convertir_a_postfix
from tree_builder import construir_arbol
from tree_renderer import dibujar_arbol


def main():
    if len(sys.argv) < 2:
        print("Uso: python problema1.py <archivo>")
        return

    ruta = sys.argv[1]
    expresiones = leer_lineas(ruta)

    for numero, expresion in enumerate(expresiones, start=1):
        print(f"\nExpresion {numero}: {expresion}")

        postfix, pasos_postfix = convertir_a_postfix(expresion)
        print("  Conversion a postfix:")
        for paso in pasos_postfix:
            print(f"    {paso}")
        print(f"  Postfix: {' '.join(postfix)}")

        raiz, pasos_arbol = construir_arbol(postfix)
        print("  Construccion del arbol:")
        for paso in pasos_arbol:
            print(f"    {paso}")

        ruta_imagen = dibujar_arbol(raiz, f"salida/expresion_{numero}")
        print(f"  Arbol guardado en: {ruta_imagen}")


if __name__ == "__main__":
    main()
