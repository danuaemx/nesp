#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from antlr4 import *
from src.gramaticaEspanol import gramaticaEspanol as gramaticaEspanolLexer
from antlr4.error.ErrorListener import ErrorListener

class MiErrorListener(ErrorListener):
    def __init__(self):
        super(MiErrorListener, self).__init__()
        self.errores = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errores.append(f"Error en línea {line}:{column} - {msg}")
        
    def getErrores(self):
        return self.errores

def ejecutar_analisis_lexico(codigo_fuente):
    """
    Ejecuta únicamente el análisis léxico del código fuente.
    """

    # Crear el stream de caracteres desde el código fuente
    input_stream = InputStream(codigo_fuente)
    
    # Crear el lexer
    lexer = gramaticaEspanolLexer(input_stream)
    
    # Desactivar la salida de errores por consola
    lexer.removeErrorListeners()
    error_listener = MiErrorListener()
    lexer.addErrorListener(error_listener)
    
    # Obtener todos los tokens
    tokens = lexer.getAllTokens()
    
    # Preparar el resultado
    resultado = []
    for token in tokens:
        token_type = lexer.symbolicNames[token.type]
        token_text = token.text
        token_line = token.line
        token_column = token.column
        
        # Si es un ERROR, no lo añadimos a la lista de tokens válidos
        if token_type != 'ERROR':
            resultado.append({
                'tipo': token_type,
                'texto': token_text,
                'linea': token_line,
                'columna': token_column
            })
        
    # Reiniciar el lexer para posible análisis sintáctico posterior
    lexer.reset()
    
    return resultado, error_listener.getErrores()

def imprimir_tokens(tokens):
    """
    Imprime los tokens de manera formateada.
    """
    print("\n=== ANÁLISIS LÉXICO ===")
    print("{:<20} {:<30} {:<10} {:<10}".format("TIPO", "TEXTO", "LÍNEA", "COLUMNA"))
    print("-" * 70)
    
    for token in tokens:
        print("{:<20} {:<30} {:<10} {:<10}".format(
            token['tipo'],
            token['texto'],
            token['linea'],
            token['columna']
        ))

def imprimir_errores(errores):
    """
    Imprime los errores encontrados.
    """
    if errores:
        print("\n=== ERRORES ENCONTRADOS ===")
        for error in errores:
            print(f"- {error}")
    else:
        print("\n=== NO SE ENCONTRARON ERRORES ===")

def procesar_archivo(nombre_archivo):
    """
    Procesa un archivo de código fuente.
    """
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            codigo_fuente = archivo.read()
        
        # Análisis léxico
        tokens, errores_lexicos = ejecutar_analisis_lexico(codigo_fuente)
        imprimir_tokens(tokens)
        imprimir_errores(errores_lexicos)

            
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}'")
    except Exception as e:
        print(f"Error inesperado: {e}")

def procesar_texto(codigo_fuente):
    """
    Procesa un texto de código fuente proporcionado directamente.
    """
    try:
        # Análisis léxico
        tokens, errores_lexicos = ejecutar_analisis_lexico(codigo_fuente)
        imprimir_tokens(tokens)
        imprimir_errores(errores_lexicos)

            
    except Exception as e:
        print(f"Error inesperado: {e}")

def main():
    """
    Función principal.
    """
    if len(sys.argv) < 2:
        print("Uso:")
        print("  python analizador_lexico.py archivo.txt")
        print("  python analizador_lexico.py -c \"codigo fuente\"")
        return
    
    if sys.argv[1] == '-c' and len(sys.argv) >= 3:
        # Procesar texto directo desde la línea de comandos
        codigo_fuente = sys.argv[2]
        procesar_texto(codigo_fuente)
    else:
        # Procesar archivo
        nombre_archivo = sys.argv[1]
        procesar_archivo(nombre_archivo)

if __name__ == "__main__":
    main()
