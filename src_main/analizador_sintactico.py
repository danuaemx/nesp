#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import datetime
from antlr4 import *
from antlr4.tree.Trees import Trees
# Importar Lexer y Parser generados por ANTLR
from archivos.gramaticaEspanol import gramaticaEspanol as gramaticaEspanolLexer
from archivos.parserGramaticaEspanol import parserGramaticaEspanol
from archivos.parserGramaticaEspanolListener import parserGramaticaEspanolListener

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


# --- Listener para construir Tabla de Símbolos ---
class TablaSimbolosListener(parserGramaticaEspanolListener):
    def __init__(self):
        self.tabla_simbolos = []
        self.ambito_actual = "global"

    def enterDeclaracion(self, ctx):
        """Procesa declaraciones de variables y arreglos"""
        try:
            # Obtener el identificador de la variable
            nombre = ctx.ID().getText()

            # Determinar si es un arreglo o una variable simple
            es_arreglo = ctx.ARREGLO_DE() is not None

            if es_arreglo:
                tipo = f"arreglo de {ctx.TIPO_DATO().getText()}"
                # Extraer dimensiones del arreglo
                dimensiones = []
                dimension_ctx = ctx.dimension()
                if dimension_ctx:
                    dimensiones = [num.getText() for num in dimension_ctx.NUMERO()]

                valor = f"[{' x '.join(dimensiones)}]"
            else:
                tipo = ctx.TIPO_DATO().getText()
                valor = "no inicializado"

            self.tabla_simbolos.append({
                'nombre': nombre,
                'tipo': tipo,
                'valor': valor,
                'ambito': self.ambito_actual,
                'linea': ctx.start.line,
                'columna': ctx.start.column + 1
            })
        except Exception as e:
            print(f"Error al procesar declaración: {e}")

    def enterAsignacion(self, ctx):
        """Procesa asignaciones a variables"""
        try:
            # Para asignaciones a variables o elementos de arreglo
            if ctx.designador():
                # Si es una asignación a un elemento de arreglo
                designador = ctx.designador()
                if designador.ID() and designador.CORCHETE_IZQ():
                    nombre_base = designador.ID().getText()
                    indices = []

                    # Extraer los índices del arreglo si están disponibles
                    lista_indices = designador.lista_indices()
                    if lista_indices and lista_indices.expresion():
                        # Puede ser una lista de expresiones para matrices multidimensionales
                        for expr in lista_indices.expresion():
                            indices.append(expr.getText())

                    posicion = f"[{', '.join(indices)}]"
                    nombre = f"{nombre_base}{posicion}"
                    valor = ctx.expresion().getText() if ctx.expresion() else "expresión compleja"

                    # Añadir a la tabla de símbolos
                    self.tabla_simbolos.append({
                        'nombre': nombre,
                        'tipo': 'elemento_arreglo',
                        'valor': valor,
                        'ambito': self.ambito_actual,
                        'linea': ctx.start.line,
                        'columna': ctx.start.column + 1
                    })

                # Si es una asignación simple a una variable
                elif designador.ID():
                    nombre = designador.ID().getText()

                    # Intentar obtener el valor de la expresión
                    valor = ctx.expresion().getText() if ctx.expresion() else "expresión compleja"

                    # Buscar si la variable ya está en la tabla
                    encontrado = False
                    for simbolo in self.tabla_simbolos:
                        if simbolo['nombre'] == nombre and simbolo['ambito'] == self.ambito_actual:
                            simbolo['valor'] = valor  # Actualizar el valor
                            encontrado = True
                            break

                    # Si es una nueva variable (asignación implícita)
                    if not encontrado:
                        self.tabla_simbolos.append({
                            'nombre': nombre,
                            'tipo': "inferido",
                            'valor': valor,
                            'ambito': self.ambito_actual,
                            'linea': ctx.start.line,
                            'columna': ctx.start.column + 1
                        })

            # Para asignaciones con condiciones booleanas
            elif ctx.ID() and ctx.condicion():
                nombre = ctx.ID().getText()
                valor = ctx.condicion().getText()

                # Lógica similar a la anterior para actualizar o agregar a la tabla
                encontrado = False
                for simbolo in self.tabla_simbolos:
                    if simbolo['nombre'] == nombre and simbolo['ambito'] == self.ambito_actual:
                        simbolo['valor'] = valor
                        encontrado = True
                        break

                if not encontrado:
                    self.tabla_simbolos.append({
                        'nombre': nombre,
                        'tipo': "booleano",
                        'valor': valor,
                        'ambito': self.ambito_actual,
                        'linea': ctx.start.line,
                        'columna': ctx.start.column + 1
                    })
        except Exception as e:
            print(f"Error al procesar asignación: {e}")

    def enterDefinicion_funcion(self, ctx):
        """Procesa definiciones de funciones"""
        try:
            nombre = ctx.ID().getText()
            self.ambito_anterior = self.ambito_actual
            self.ambito_actual = nombre

            # Recopilar información de parámetros
            parametros = []
            if ctx.parametros():
                parametros = [param.getText() for param in ctx.parametros().ID()]

            # Añadir la función a la tabla de símbolos
            self.tabla_simbolos.append({
                'nombre': nombre,
                'tipo': 'funcion',
                'valor': f"({', '.join(parametros)})",
                'ambito': self.ambito_anterior,
                'linea': ctx.start.line,
                'columna': ctx.start.column + 1
            })

            # Añadir los parámetros a la tabla de símbolos
            for parametro in parametros:
                self.tabla_simbolos.append({
                    'nombre': parametro,
                    'tipo': 'parametro',
                    'valor': 'no inicializado',
                    'ambito': nombre,
                    'linea': ctx.start.line,
                    'columna': ctx.start.column + 1
                })

        except Exception as e:
            print(f"Error al procesar definición de función: {e}")

    def exitDefinicion_funcion(self, ctx):
        """Restaura ámbito al salir de la definición de función"""
        if hasattr(self, 'ambito_anterior'):
            self.ambito_actual = self.ambito_anterior

    def enterSentencia_if(self, ctx):
        """Registra estructuras condicionales para análisis"""
        try:
            condicion = ctx.condicion().getText()
            self.tabla_simbolos.append({
                'nombre': f"if_{ctx.start.line}_{ctx.start.column}",
                'tipo': 'estructura_control',
                'valor': f"si {condicion} entonces",
                'ambito': self.ambito_actual,
                'linea': ctx.start.line,
                'columna': ctx.start.column + 1
            })
        except Exception as e:
            print(f"Error al procesar sentencia if: {e}")

    def enterSentencia_while(self, ctx):
        """Registra estructuras de bucle para análisis"""
        try:
            condicion = ctx.condicion().getText()
            self.tabla_simbolos.append({
                'nombre': f"while_{ctx.start.line}_{ctx.start.column}",
                'tipo': 'estructura_control',
                'valor': f"mientras {condicion} entonces",
                'ambito': self.ambito_actual,
                'linea': ctx.start.line,
                'columna': ctx.start.column + 1
            })
        except Exception as e:
            print(f"Error al procesar sentencia while: {e}")

    def enterRetorno(self, ctx):
        """Registra instrucciones de retorno"""
        try:
            valor_retorno = ctx.expresion().getText()
            self.tabla_simbolos.append({
                'nombre': f"retorno_{ctx.start.line}_{ctx.start.column}",
                'tipo': 'instruccion',
                'valor': f"devuelve {valor_retorno}",
                'ambito': self.ambito_actual,
                'linea': ctx.start.line,
                'columna': ctx.start.column + 1
            })
        except Exception as e:
            print(f"Error al procesar retorno: {e}")

    def enterExpresion(self, ctx):
        """Procesa expresiones con acceso a elementos de arreglo"""
        try:
            # Detectar acceso a arreglo en una expresión (para lectura)
            if ctx.ID() and ctx.CORCHETE_IZQ():
                nombre_base = ctx.ID().getText()
                indices = []

                # Extraer los índices
                lista_indices = ctx.lista_indices()
                if lista_indices and lista_indices.expresion():
                    for expr in lista_indices.expresion():
                        indices.append(expr.getText())

                posicion = f"[{', '.join(indices)}]"
                nombre_completo = f"{nombre_base}{posicion}"

                # Comprobar si ya existe en la tabla
                existe = False
                for simbolo in self.tabla_simbolos:
                    if simbolo['nombre'] == nombre_completo:
                        existe = True
                        break

                # Registrar el acceso al elemento si no existe
                if not existe:
                    self.tabla_simbolos.append({
                        'nombre': nombre_completo,
                        'tipo': 'elemento_arreglo_acceso',
                        'valor': f"acceso en {', '.join(indices)}",
                        'ambito': self.ambito_actual,
                        'linea': ctx.start.line,
                        'columna': ctx.start.column + 1
                    })
        except Exception as e:
            # Ignorar errores aquí, ya que es una detección auxiliar
            pass


# --- Clase para formateo y visualización del árbol sintáctico ---
class ArbolSintactico:
    @staticmethod
    def formatear_arbol(arbol, parser):
        """Formatea el árbol sintáctico para visualización."""
        # Convertir el árbol a texto usando la utilidad Trees de ANTLR
        arbol_texto = Trees.toStringTree(arbol, None, parser)

        # Aplicar formato para mejor visualización
        nivel = 0
        resultado = []
        en_cadena = False

        i = 0
        while i < len(arbol_texto):
            c = arbol_texto[i]

            # Manejar paréntesis de apertura
            if c == '(' and not en_cadena:
                resultado.append(c)
                nivel += 1
                resultado.append('\n' + '  ' * nivel)

            # Manejar paréntesis de cierre
            elif c == ')' and not en_cadena:
                nivel -= 1
                resultado.append('\n' + '  ' * nivel)
                resultado.append(c)

            # Manejar comillas (para no formatear dentro de cadenas)
            elif c == '"':
                resultado.append(c)
                en_cadena = not en_cadena

            # Caracteres normales
            else:
                resultado.append(c)

            i += 1

        return ''.join(resultado)

    @staticmethod
    def arbol_a_html(arbol_texto, tokens, tabla_simbolos):
        """Convierte el árbol formatado a HTML para visualización más rica."""
        # CSS para el formato
        html = '<!DOCTYPE html>\n<html>\n<head>\n'
        html += '<meta charset="UTF-8">\n'
        html += '<style>\n'
        html += 'body { font-family: "Segoe UI", Arial, sans-serif; margin: 20px; background-color: #f5f5f5; }\n'
        html += '.container { display: flex; flex-wrap: wrap; gap: 20px; }\n'
        html += '.section { background-color: white; border-radius: 8px; padding: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }\n'
        html += '.tree { white-space: pre; font-family: monospace; font-size: 14px; overflow: auto; max-height: 800px; }\n'
        html += '.tree-container { flex: 2; min-width: 500px; }\n'
        html += '.tokens-container, .symbols-container { flex: 1; min-width: 400px; }\n'
        html += 'table { border-collapse: collapse; width: 100%; margin-top: 10px; }\n'
        html += 'th, td { border: 1px solid #ddd; padding: 8px; text-align: left; font-size: 14px; }\n'
        html += 'th { background-color: #f2f2f2; position: sticky; top: 0; }\n'
        html += 'tr:nth-child(even) { background-color: #f9f9f9; }\n'
        html += 'h2 { color: #333; margin-top: 0; }\n'
        html += '.table-container { max-height: 600px; overflow: auto; }\n'
        html += '.keyword { color: #0000FF; font-weight: bold; }\n'
        html += '.identifier { color: #008800; }\n'
        html += '.number { color: #FF0000; }\n'
        html += '.string { color: #A31515; }\n'
        html += '.operator { color: #0000FF; }\n'
        html += '</style>\n</head>\n<body>\n'

        # Título principal
        html += '<h1>Análisis Sintáctico NESP</h1>\n'
        html += '<div class="container">\n'

        # Sección del árbol sintáctico
        html += '<div class="section tree-container">\n'
        html += '<h2>Árbol Sintáctico</h2>\n'
        html += '<div class="tree">\n'

        # Aplicar coloreado al árbol
        colorized_tree = arbol_texto
        # Reemplazar palabras clave y otros elementos con etiquetas de span coloreadas
        keywords = ['programa', 'instruccion', 'declaracion', 'asignacion', 'sentencia_if',
                    'sentencia_while', 'definicion_funcion', 'retorno', 'bloque', 'condicion',
                    'expresion', 'termino', 'designador', 'parametros', 'argumentos',
                    'operador_relacional', 'lista_indices']
        for keyword in keywords:
            colorized_tree = colorized_tree.replace(keyword, f'<span class="keyword">{keyword}</span>')

        html += colorized_tree.replace('<', '&lt;').replace('>', '&gt;').replace('\n', '<br>')
        html += '\n</div>\n</div>\n'

        # Sección de tokens
        html += '<div class="section tokens-container">\n'
        html += '<h2>Tokens Léxicos</h2>\n'
        html += '<div class="table-container">\n'
        html += '<table>\n'
        html += '<tr><th>Tipo</th><th>Texto</th><th>Línea</th><th>Columna</th></tr>\n'

        for token in tokens:
            tipo_class = "keyword"
            if token['tipo'] == 'ID':
                tipo_class = "identifier"
            elif token['tipo'] == 'NUMERO':
                tipo_class = "number"
            elif token['tipo'] == 'CADENA':
                tipo_class = "string"

            html += f'<tr><td>{token["tipo"]}</td><td class="{tipo_class}">{token["texto"]}</td>'
            html += f'<td>{token["linea"]}</td><td>{token["columna"]}</td></tr>\n'

        html += '</table>\n</div>\n</div>\n'

        # Sección de la tabla de símbolos
        html += '<div class="section symbols-container">\n'
        html += '<h2>Tabla de Símbolos</h2>\n'
        html += '<div class="table-container">\n'
        html += '<table>\n'
        html += '<tr><th>Nombre</th><th>Tipo</th><th>Valor</th><th>Ámbito</th><th>Línea</th><th>Columna</th></tr>\n'

        for simbolo in tabla_simbolos:
            nombre_class = "identifier" if simbolo['tipo'] not in ['funcion', 'estructura_control',
                                                                   'instruccion'] else "keyword"
            tipo_class = "keyword"
            valor_class = "string" if simbolo['valor'].startswith('"') else "number" if simbolo[
                'valor'].isdigit() else "operator"

            html += f'<tr>'
            html += f'<td class="{nombre_class}">{simbolo["nombre"]}</td>'
            html += f'<td class="{tipo_class}">{simbolo["tipo"]}</td>'
            html += f'<td class="{valor_class}">{simbolo["valor"]}</td>'
            html += f'<td>{simbolo["ambito"]}</td>'
            html += f'<td>{simbolo["linea"]}</td>'
            html += f'<td>{simbolo["columna"]}</td>'
            html += f'</tr>\n'

        html += '</table>\n</div>\n</div>\n'

        # Cierre del documento
        html += '</div>\n</body>\n</html>'

        return html

    @staticmethod
    def arbol_a_dot(arbol, parser):
        """Convierte el árbol sintáctico a formato DOT para Graphviz."""
        dot = ['digraph {']
        dot.append('  node [shape=box, style=filled, fillcolor=lightgray, fontname="Arial", fontsize=10];')
        dot.append('  edge [fontname="Arial", fontsize=9];')

        # Función recursiva para recorrer el árbol y generar nodos DOT
        nodo_id = 0
        nodo_mapa = {}  # Para mapear nodos del árbol a IDs en el grafo DOT

        def recorrer_arbol(nodo, padre_id=None):
            nonlocal nodo_id

            # Asignar un ID único a este nodo
            mi_id = nodo_id
            nodo_id += 1
            nodo_mapa[nodo] = mi_id

            # Obtener el texto de este nodo
            texto = "nodo"  # Default value
            if parser is not None and hasattr(nodo, 'getText'):
                try:
                    # Intentar obtener el texto del nodo
                    texto_raw = nodo.getText()
                    # Escapar caracteres problemáticos para DOT
                    texto = texto_raw.replace('"', '\\"').replace('\\', '\\\\').replace('\n', '\\n').replace('\t',
                                                                                                             '\\t')
                    # Limitar longitud del texto
                    if len(texto) > 30:
                        texto = texto[:27] + "..."
                except Exception as e:
                    # Si falla, usar la clase del nodo
                    texto = nodo.__class__.__name__.replace('"', '\\"')

            # Si hay un nombre de regla, usarlo en lugar del texto
            if hasattr(nodo, 'getRuleIndex'):
                try:
                    rule_index = nodo.getRuleIndex()
                    rule_names = parser.ruleNames
                    if rule_index >= 0 and rule_index < len(rule_names):
                        rule_name = rule_names[rule_index]
                        # Si el nodo tiene texto específico, incluirlo como texto alternativo
                        if hasattr(nodo, 'getText') and nodo.getText() != rule_name:
                            texto_nodo = nodo.getText()
                            # Escapar caracteres especiales
                            texto_nodo = texto_nodo.replace('"', '\\"').replace('\\', '\\\\').replace('\n', '\\n')
                            # Limitar longitud
                            if len(texto_nodo) > 20:
                                texto_nodo = texto_nodo[:17] + "..."
                            texto = f"{rule_name}\\n'{texto_nodo}'"
                        else:
                            texto = rule_name
                except Exception as e:
                    pass

            # Para nodos terminales (tokens)
            if hasattr(nodo, 'symbol'):
                try:
                    token = nodo.symbol
                    token_text = str(token.text).replace('"', '\\"').replace('\\', '\\\\').replace('\n', '\\n')
                    # Limitar longitud
                    if len(token_text) > 20:
                        token_text = token_text[:17] + "..."
                    token_type = parser.symbolicNames[token.type] if token.type < len(parser.symbolicNames) else str(
                        token.type)
                    texto = f"{token_type}\\n'{token_text}'"
                except Exception as e:
                    pass

            # Añadir este nodo al grafo DOT, con doble comilla para el label
            dot.append(f'  node{mi_id} [label="{texto}"];')

            # Si hay un padre, conectarlo con este nodo
            if padre_id is not None:
                dot.append(f'  node{padre_id} -> node{mi_id};')

            # Recorrer recursivamente los hijos
            if hasattr(nodo, 'getChildCount'):
                for i in range(nodo.getChildCount()):
                    hijo = nodo.getChild(i)
                    recorrer_arbol(hijo, mi_id)

        # Comenzar el recorrido desde la raíz del árbol
        recorrer_arbol(arbol)

        dot.append('}')
        return '\n'.join(dot)


# --- Funciones para Manejo de Archivos ---

def crear_directorio_salida(nombre_base):
    """Crea un directorio para guardar los archivos de salida con timestamp."""
    # Obtener timestamp actual
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    # Crear nombre del directorio
    nombre_dir = f"{nombre_base}_{timestamp}"

    # Crear el directorio si no existe
    try:
        if not os.path.exists(nombre_dir):
            os.makedirs(nombre_dir)
        return nombre_dir
    except Exception as e:
        print(f"Error al crear directorio de salida: {e}")
        return "."  # Directorio actual como fallback


# --- Funciones de Análisis ---

def ejecutar_analisis(codigo_fuente):
    """
    Ejecuta el análisis léxico y sintáctico del código fuente.
    """
    input_stream = InputStream(codigo_fuente)

    # 1. Análisis Léxico
    lexer = gramaticaEspanolLexer(input_stream)
    lexer.removeErrorListeners()  # Quitar listener por defecto
    error_listener_lexico = MiErrorListener()
    lexer.addErrorListener(error_listener_lexico)

    stream = CommonTokenStream(lexer)
    stream.fill()  # Cargar todos los tokens para verificar errores léxicos primero

    tokens_lexico = stream.tokens  # Obtener la lista de tokens
    errores_lexicos = error_listener_lexico.getErrores()

    resultado_lexico = []
    for token in tokens_lexico:
        if token.type != Token.EOF:  # No incluir EOF en la lista visual
            token_type = lexer.symbolicNames[token.type]
            if token_type != 'ERROR':  # Solo incluir tokens válidos en el resultado
                resultado_lexico.append({
                    'tipo': token_type,
                    'texto': token.text,
                    'linea': token.line,
                    'columna': token.column + 1
                })

    # Si hay errores léxicos, no continuar con el análisis sintáctico
    if errores_lexicos:
        return resultado_lexico, errores_lexicos, [], None, []

    # 2. Análisis Sintáctico (solo si no hay errores léxicos)
    stream.seek(0)
    parser = parserGramaticaEspanol(stream)
    parser.removeErrorListeners()
    error_listener_sintactico = MiErrorListener()
    parser.addErrorListener(error_listener_sintactico)

    # Ejecutar el parser comenzando desde la regla 'programa'
    try:
        # Capturar el árbol sintáctico
        arbol = parser.programa()

        # Construir tabla de símbolos
        tabla_simbolos_listener = TablaSimbolosListener()
        walker = ParseTreeWalker()
        walker.walk(tabla_simbolos_listener, arbol)

        # Formatear árbol para visualización
        arbol_formateado = ArbolSintactico.formatear_arbol(arbol, parser)

    except Exception as e:
        print(f"Excepción inesperada durante el análisis sintáctico: {e}")
        import traceback
        traceback.print_exc()
        arbol_formateado = None
        tabla_simbolos = []
    else:
        tabla_simbolos = tabla_simbolos_listener.tabla_simbolos

    errores_sintacticos = error_listener_sintactico.getErrores()

    return resultado_lexico, errores_lexicos, errores_sintacticos, arbol_formateado, tabla_simbolos


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


def imprimir_arbol_sintactico(arbol):
    """Imprime el árbol de análisis sintáctico."""
    if arbol:
        print("\n=== ÁRBOL DE ANÁLISIS SINTÁCTICO ===")
        print(arbol)
    else:
        print("\n=== NO SE PUDO GENERAR EL ÁRBOL SINTÁCTICO ===")


def imprimir_tabla_simbolos(tabla):
    """Imprime la tabla de símbolos."""
    print("\n=== TABLA DE SÍMBOLOS ===")
    if not tabla:
        print("No se generaron entradas en la tabla de símbolos.")
        return

    print("{:<20} {:<15} {:<25} {:<15} {:<8} {:<8}".format(
        "NOMBRE", "TIPO", "VALOR", "ÁMBITO", "LÍNEA", "COLUMNA"))
    print("-" * 95)

    for simbolo in tabla:
        valor_mostrar = str(simbolo['valor'])
        if len(valor_mostrar) > 23:
            valor_mostrar = valor_mostrar[:20] + "..."

        print("{:<20} {:<15} {:<25} {:<15} {:<8} {:<8}".format(
            simbolo['nombre'],
            simbolo['tipo'],
            valor_mostrar,
            simbolo['ambito'],
            simbolo['linea'],
            simbolo['columna']
        ))


def guardar_arbol_html(arbol, tokens, tabla_simbolos, directorio_salida, nombre_archivo):
    """Guarda el árbol sintáctico y las tablas en formato HTML."""
    if arbol:
        html = ArbolSintactico.arbol_a_html(arbol, tokens, tabla_simbolos)
        ruta_completa = os.path.join(directorio_salida, f"{nombre_archivo}_analisis.html")

        try:
            with open(ruta_completa, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"\nAnálisis completo guardado como HTML en: {ruta_completa}")
        except Exception as e:
            print(f"Error al guardar el análisis como HTML: {e}")


def generar_dot_arbol(arbol, parser, directorio_salida, nombre_archivo):
    """Genera solo el archivo DOT del árbol sintáctico."""
    try:
        # Generar código DOT personalizado para el árbol
        dot_str = ArbolSintactico.arbol_a_dot(arbol, parser)

        # Guardar en el directorio de salida
        ruta_completa = os.path.join(directorio_salida, f"{nombre_archivo}.dot")
        with open(ruta_completa, 'w', encoding='utf-8') as f:
            f.write(dot_str)

        print(f"\nArchivo DOT del árbol sintáctico guardado en: {ruta_completa}")
        return ruta_completa

    except Exception as e:
        print(f"Error al generar archivo DOT: {e}")
        return None


def generar_imagen_arbol(arbol, parser, directorio_salida, nombre_archivo):
    """Genera tanto el archivo DOT como la imagen PNG del árbol sintáctico."""
    # Primero generar el DOT
    ruta_dot = generar_dot_arbol(arbol, parser, directorio_salida, nombre_archivo)

    if not ruta_dot:
        return

    try:
        # Importar graphviz y generar la imagen
        import graphviz

        # Extraer solo el contenido del archivo DOT
        with open(ruta_dot, 'r', encoding='utf-8') as f:
            dot_str = f.read()

        # Crear el gráfico
        graph = graphviz.Source(dot_str)

        # Guardar como imagen
        ruta_base = os.path.join(directorio_salida, f"{nombre_archivo}")
        graph.render(ruta_base, format="png", cleanup=True)
        print(f"\nImagen del árbol sintáctico guardada como: {ruta_base}.png")

    except ImportError:
        print("\nNota: Para generar imágenes del árbol sintáctico, instale graphviz:")
        print("pip install graphviz")
        print("Y asegúrese de tener el software Graphviz instalado en su sistema.")
    except Exception as e:
        print(f"Error al generar imagen del árbol: {e}")
        print("Intente revisar el archivo DOT archivos para identificar posibles problemas.")


# --- Funciones de Procesamiento ---

def procesar_archivo(nombre_archivo):
    """Procesa un archivo de código fuente."""
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            codigo_fuente = archivo.read()

        tokens, errores_lexicos, errores_sintacticos, arbol, tabla_simbolos = ejecutar_analisis(codigo_fuente)

        imprimir_tokens(tokens)
        imprimir_errores("Errores Léxicos Encontrados", errores_lexicos)

        # Solo mostrar resultado sintáctico si no hubo errores léxicos
        if not errores_lexicos:
            imprimir_errores("Errores Sintácticos Encontrados", errores_sintacticos)
            if not errores_sintacticos:
                print("\n=== ANÁLISIS SINTÁCTICO EXITOSO ===")
                imprimir_arbol_sintactico(arbol)
                imprimir_tabla_simbolos(tabla_simbolos)

                # Crear directorio para resultados
                nombre_base = os.path.splitext(os.path.basename(nombre_archivo))[0]
                dir_salida = crear_directorio_salida(nombre_base)

                # Guardar visualizaciones
                guardar_arbol_html(arbol, tokens, tabla_simbolos, dir_salida, nombre_base)

                # Intentar generar solo el DOT del árbol
                try:
                    stream = CommonTokenStream(gramaticaEspanolLexer(InputStream(codigo_fuente)))
                    parser = parserGramaticaEspanol(stream)
                    tree = parser.programa()
                    generar_dot_arbol(tree, parser, dir_salida, nombre_base)
                except Exception as e:
                    print(f"No se pudo generar el archivo DOT del árbol: {e}")

        else:
            print("\n--- Análisis sintáctico omitido debido a errores léxicos ---")

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}'")
    except ImportError as e:
        print(f"Error: No se pudieron importar los módulos generados por ANTLR: {e}")
        print(f"Asegúrate de haber archivos el lexer y parser para Python con:")
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
        tokens, errores_lexicos, errores_sintacticos, arbol, tabla_simbolos = ejecutar_analisis(codigo_fuente)

        imprimir_tokens(tokens)
        imprimir_errores("Errores Léxicos Encontrados", errores_lexicos)

        if not errores_lexicos:
            imprimir_errores("Errores Sintácticos Encontrados", errores_sintacticos)
            if not errores_sintacticos:
                print("\n=== ANÁLISIS SINTÁCTICO EXITOSO ===")
                imprimir_arbol_sintactico(arbol)
                imprimir_tabla_simbolos(tabla_simbolos)

                # Crear directorio para resultados
                dir_salida = crear_directorio_salida("analisis_texto")

                # Guardar visualizaciones
                guardar_arbol_html(arbol, tokens, tabla_simbolos, dir_salida, "analisis")

                # Intentar generar imagen completa del árbol para modo -c
                try:
                    stream = CommonTokenStream(gramaticaEspanolLexer(InputStream(codigo_fuente)))
                    parser = parserGramaticaEspanol(stream)
                    tree = parser.programa()
                    generar_imagen_arbol(tree, parser, dir_salida, "arbol")
                except Exception as e:
                    print(f"No se pudo generar la imagen del árbol: {e}")
        else:
            print("\n--- Análisis sintáctico omitido debido a errores léxicos ---")

    except ImportError as e:
        print(f"Error: No se pudieron importar los módulos generados por ANTLR: {e}")
        print(f"Asegúrate de haber archivos el lexer y parser para Python con:")
        print(f"  antlr4 -Dlanguage=Python3 gramaticaEspanol.g4")
        print(f"  antlr4 -Dlanguage=Python3 parserGramaticaEspanol.g4")
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
            print(f"Ejemplo: python {sys.argv[0]} -c \"variable es un entero.\"")
    else:
        nombre_archivo = sys.argv[1]
        procesar_archivo(nombre_archivo)


if __name__ == "__main__":
    main()