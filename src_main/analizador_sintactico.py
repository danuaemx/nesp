#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from antlr4 import *
# Importar Lexer y Parser generados por ANTLR
from gramaticaEspanol import gramaticaEspanol as gramaticaEspanolLexer
from parserGramaticaEspanol import parserGramaticaEspanol

from antlr4.error.ErrorListener import ErrorListener

# --- Listener de Errores (Reutilizable para Lexer y Parser) ---
class MiErrorListener(ErrorListener):
    def __init__(self):
        super(MiErrorListener, self).__init__()
        self.errores = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Añade 1 a la columna para que sea 1-based como usualmente se espera
        tipo_error = "Sintáctico"

        self.errores.append(f"Error {tipo_error} en línea {line}:{column + 1} - {msg}")

    def getErrores(self):
        return self.errores

    def limpiarErrores(self):
        self.errores = []

# --- Funciones de Análisis ---

def ejecutar_analisis(codigo_fuente):
    """
    Ejecuta el análisis léxico y sintáctico del código fuente.
    """
    input_stream = InputStream(codigo_fuente)

    # 1. Análisis Léxico
    lexer = gramaticaEspanolLexer(input_stream)
    lexer.removeErrorListeners() # Quitar listener por defecto
    error_listener_lexico = MiErrorListener()
    lexer.addErrorListener(error_listener_lexico)

    stream = CommonTokenStream(lexer)
    stream.fill() # Cargar todos los tokens para verificar errores léxicos primero

    tokens_lexico = stream.tokens # Obtener la lista de tokens (puede ser útil)
    errores_lexicos = error_listener_lexico.getErrores()

    resultado_lexico = []
    for token in tokens_lexico:
        if token.type != Token.EOF: # No incluir EOF en la lista visual
            token_type = lexer.symbolicNames[token.type]
            if token_type != 'ERROR': # Solo incluir tokens válidos en el resultado
                 resultado_lexico.append({
                    'tipo': token_type,
                    'texto': token.text,
                    'linea': token.line,
                    'columna': token.column + 1
                })
            # Nota: Los tokens ERROR ya se capturan como errores léxicos.

    # Si hay errores léxicos, no continuar con el análisis sintáctico
    if errores_lexicos:
        return resultado_lexico, errores_lexicos, [] # Devolver tokens, errores léxicos, sin errores sintácticos

    # 2. Análisis Sintáctico (solo si no hay errores léxicos)
    # Necesitamos reiniciar el stream para que el parser lo lea desde el principio
    stream.seek(0)
    parser = parserGramaticaEspanol(stream)
    parser.removeErrorListeners() # Quitar listener por defecto
    error_listener_sintactico = MiErrorListener()
    parser.addErrorListener(error_listener_sintactico)

    # Ejecutar el parser comenzando desde la regla 'programa'
    try:
        parser.programa() # Llamada a la regla inicial de la gramática del parser
    except Exception as e:
        # Capturar otras posibles excepciones durante el parseo
        # Aunque los errores de sintaxis deberían ser capturados por el listener
        print(f"Excepción inesperada durante el análisis sintáctico: {e}")
        import traceback
        traceback.print_exc()


    errores_sintacticos = error_listener_sintactico.getErrores()

    return resultado_lexico, errores_lexicos, errores_sintacticos

# --- Funciones de Impresión ---

def imprimir_tokens(tokens):
    """Imprime los tokens léxicos válidos."""
    print("\n=== ANÁLISIS LÉXICO (Tokens Válidos) ===")
    if not tokens:
        print("No se generaron tokens válidos.")
        return
    print("{:<25} {:<30} {:<10} {:<10}".format("TIPO", "TEXTO", "LÍNEA", "COLUMNA"))
    print("-" * 75)
    for token in tokens:
        print("{:<25} {:<30} {:<10} {:<10}".format(
            token['tipo'],
            f"'{token['texto']}'",
            token['linea'],
            token['columna']
        ))

def imprimir_errores(titulo, errores):
    """Imprime una lista de errores."""
    if errores:
        print(f"\n=== {titulo.upper()} ===")
        for error in errores:
            print(f"- {error}")
    # else: # Opcional: imprimir mensaje si no hay errores
    #    print(f"\n=== NO SE ENCONTRARON {titulo.upper()} ===")


# --- Funciones de Procesamiento ---

def procesar_archivo(nombre_archivo):
    """Procesa un archivo de código fuente."""
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            codigo_fuente = archivo.read()

        tokens, errores_lexicos, errores_sintacticos = ejecutar_analisis(codigo_fuente)

        imprimir_tokens(tokens)
        imprimir_errores("Errores Léxicos Encontrados", errores_lexicos)

        # Solo mostrar resultado sintáctico si no hubo errores léxicos
        if not errores_lexicos:
            imprimir_errores("Errores Sintácticos Encontrados", errores_sintacticos)
            if not errores_sintacticos:
                print("\n=== ANÁLISIS SINTÁCTICO EXITOSO ===")
        else:
             print("\n--- Análisis sintáctico omitido debido a errores léxicos ---")


    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}'")
    except ImportError as e:
        print(f"Error: No se pudieron importar los módulos generados por ANTLR: {e}")
        print(f"Asegúrate de haber generado el lexer y parser para Python con:")
        print(f"  antlr4 -Dlanguage=Python3 gramaticaEspanol.g4")
        print(f"  antlr4 -Dlanguage=Python3 parserGramaticaEspanol.g4")
        print(f"Y que los archivos .py resultantes estén en el mismo directorio o en el PYTHONPATH.")
    except Exception as e:
        print(f"Error inesperado: {e}")
        import traceback
        traceback.print_exc()

def procesar_texto(codigo_fuente):
    """Procesa un texto de código fuente proporcionado directamente."""
    try:
        tokens, errores_lexicos, errores_sintacticos = ejecutar_analisis(codigo_fuente)

        imprimir_tokens(tokens)
        imprimir_errores("Errores Léxicos Encontrados", errores_lexicos)

        if not errores_lexicos:
            imprimir_errores("Errores Sintácticos Encontrados", errores_sintacticos)
            if not errores_sintacticos:
                print("\n=== ANÁLISIS SINTÁCTICO EXITOSO ===")
        else:
             print("\n--- Análisis sintáctico omitido debido a errores léxicos ---")

    except ImportError as e:
        print(f"Error: No se pudieron importar los módulos generados por ANTLR: {e}")
        # ... (mismo mensaje de error que en procesar_archivo) ...
    except Exception as e:
        print(f"Error inesperado: {e}")
        import traceback
        traceback.print_exc()

# --- Función Principal ---
def main():
    """Función principal."""
    if len(sys.argv) < 2:
        print("Uso:")
        print(f"  python {sys.argv[0]} archivo_entrada.nesp")
        print(f"  python {sys.argv[0]} -c \"codigo fuente en una cadena\"")
        return

    if sys.argv[1] == '-c':
        if len(sys.argv) >= 3:
            codigo_fuente = " ".join(sys.argv[2:])
            procesar_texto(codigo_fuente)
        else:
            print("Error: Falta el código fuente después de la opción -c.")
            print(f"Ejemplo: python {sys.argv[0]} -c \"variable asigna 5.\"")
    else:
        nombre_archivo = sys.argv[1]
        procesar_archivo(nombre_archivo)

if __name__ == "__main__":
    main()