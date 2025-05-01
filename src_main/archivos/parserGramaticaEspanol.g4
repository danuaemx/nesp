parser grammar parserGramaticaEspanol;

options {
    // Asegúrate de que 'gramaticaEspanol' es el nombre de tu archivo lexer (.g4)
    tokenVocab = gramaticaEspanol;
}

// ------------------------
// Reglas Principales
// ------------------------

// Programa principal: una secuencia de una o más instrucciones
programa
    : instruccion+ EOF
    ;

// Instrucciones: Las diferentes sentencias que componen el programa
instruccion
    : declaracion PUNTO          // Una declaración debe terminar en punto
    | asignacion PUNTO           // Una asignación debe terminar en punto
    | sentencia_if             // if/entonces/fin (no lleva punto explícito aquí)
    | sentencia_while          // mientras/entonces/fin (no lleva punto explícito aquí)
    | definicion_funcion       // funcion/fin (no lleva punto explícito aquí)
    | retorno PUNTO              // devuelve/punto
    | llamada_funcion PUNTO    // Permitir llamadas a función como instrucción (ej: limpiarPantalla().)
    | expresion PUNTO            // Permitir una expresión sola como instrucción (raro, pero posible, ej: 5.)
    ;

// ------------------------
// Declaraciones
// ------------------------

declaracion
    : ID ES_UN TIPO_DATO                                // Variable simple: variable es un entero
    | ID ES_UN ARREGLO_DE TIPO_DATO DE dimension        // Arreglo: miArreglo es un arreglo de real de 5 por 10
    ;

// Dimensiones de arreglos (1D, 2D, 3D, etc.)
dimension
    : NUMERO                                            // Una sola dimensión: 10
    | NUMERO (POR NUMERO)+                              // Múltiples dimensiones: 5 por 10 por 2
    ;

// ------------------------
// Asignaciones
// ------------------------

// Regla de asignación: permite asignar a variables simples y elementos de arreglo
asignacion
    : designador ASIGNA expresion                       // variable asigna 5. O miVector[2] asigna x + 1.
    | ID ASIGNA condicion                             // activo asigna x es mayor que 5. (Asumiendo asignación booleana solo a ID)
    ;

// NUEVA REGLA: Designador (Lo que puede ir a la izquierda de 'asigna')
// Representa una ubicación de memoria donde se puede guardar un valor.
designador
    : ID                                                // Variable simple: contador
    | ID CORCHETE_IZQ lista_indices CORCHETE_DER        // Elemento de arreglo: miVector[indice] o matriz[fila, col]
    ;

// ------------------------
// Estructuras de Control
// ------------------------

sentencia_if
    : SI condicion ENTONCES bloque FIN
    ;

sentencia_while
    : MIENTRAS condicion ENTONCES bloque FIN
    ;

// ------------------------
// Funciones
// ------------------------

definicion_funcion
    : FUNCION ID PARENTESIS_IZQ parametros? PARENTESIS_DER DOS_PUNTOS bloque FIN
    ;

parametros
    : ID (COMA ID)*                                     // Lista de identificadores de parámetros
    ;

retorno
    : DEVUELVE expresion                                // Sentencia de retorno de función
    ;

// Bloque de código: una secuencia de instrucciones (usado en if, while, funciones)
bloque
    : instruccion+
    ;

// ------------------------
// Condiciones (Lógica Booleana)
// ------------------------

condicion
    : expresion operador_relacional expresion           // Comparación: a es igual que b
    | expresion                                         // Una expresión puede ser una condición (ej: variable booleana 'activo')
    | condicion Y condicion                             // Lógica AND
    | condicion O condicion                             // Lógica OR
    | NO condicion                                      // Lógica NOT
    | PARENTESIS_IZQ condicion PARENTESIS_DER           // Agrupación con paréntesis
    ;

operador_relacional
    : ES_IGUAL_QUE
    | ES_DISTINTO_DE
    | ES_MAYOR_QUE
    | ES_MENOR_QUE
    | ES_MAYOR_O_IGUAL_QUE
    | ES_MENOR_O_IGUAL_QUE
    ;

// ------------------------
// Expresiones (Cálculos y Valores)
// ------------------------

// Expresión: define la precedencia y asociatividad de operadores
expresion
    : termino                                           // Base de la expresión
    | expresion (MAS | MENOS) expresion                 // Suma, Resta (menor precedencia)
    | expresion (POR | ENTRE) expresion                 // Multiplicación, División
    | expresion A_LA expresion                          // Potencia (ajustar precedencia si es necesario)
    | PARENTESIS_IZQ expresion PARENTESIS_DER           // Agrupación para alterar precedencia
    | llamada_funcion                                   // Una llamada a función que devuelve un valor es una expresión
    // Añadimos el acceso a arreglo aquí también explícitamente para lectura
    | ID CORCHETE_IZQ lista_indices CORCHETE_DER        // Leer valor de un arreglo: miVector[3]
    ;

// Término: los elementos básicos que componen una expresión
termino
    : ID                                                // Identificador (variable)
    | NUMERO                                            // Literal numérico: 5, 3.14
    | CADENA                                            // Literal de texto: "hola"
    // NOTA: La llamada a función y el acceso a arreglo ahora están directamente en 'expresion'
    // para manejar mejor la recursividad y precedencia. Si ANTLR se queja de recursividad izquierda,
    // podríamos necesitar refactorizar 'expresion' usando precedencia explícita.
    ;


// Lista de índices para acceso a arreglos (dentro de [])
lista_indices
    : expresion (COMA expresion)*                       // Uno o más índices separados por comas: 3 o 1, 2 o x, y+1
    ;

// Llamada a función
llamada_funcion
    : ID PARENTESIS_IZQ argumentos? PARENTESIS_DER
    ;

// Argumentos de una llamada a función
argumentos
    : expresion (COMA expresion)*                       // Cero o más expresiones separadas por comas
    ;