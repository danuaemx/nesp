parser grammar parserGramaticaEspanol;

options {
    tokenVocab = gramaticaEspanol;
}

// Programa principal
programa
    : instruccion+ EOF
    ;

// Instrucciones
instruccion
    : declaracion PUNTO
    | asignacion PUNTO
    | sentencia_if
    | sentencia_while
    | definicion_funcion
    | retorno PUNTO
    | expresion PUNTO
    ;

// Declaraciones
declaracion
    : ID ES_UN TIPO_DATO                                           // DeclaracionSimple
    | ID ES_UN ARREGLO_DE TIPO_DATO DE dimension                   // DeclaracionArreglo
    ;

// Dimensiones de arreglos (1D, 2D, 3D, etc.)
dimension
    : NUMERO                                                       // Dimension1D
    | NUMERO POR NUMERO                                            // Dimension2D
    | NUMERO POR NUMERO POR NUMERO                                 // Dimension3D
    ;

// Asignaciones
asignacion
    : ID ASIGNA expresion
    ;

// Estructuras de control
sentencia_if
    : SI condicion ENTONCES bloque FIN
    ;

sentencia_while
    : MIENTRAS condicion ENTONCES bloque FIN
    ;

// Definición de funciones
definicion_funcion
    : FUNCION ID PARENTESIS_IZQ parametros? PARENTESIS_DER DOS_PUNTOS bloque FIN
    ;

parametros
    : ID (COMA ID)*
    ;

// Retorno
retorno
    : DEVUELVE expresion
    ;

// Bloque de código
bloque
    : instruccion+
    ;

// Condiciones
condicion
    : expresion operador_relacional expresion                      // CondicionRelacional
    | expresion                                                    // CondicionExpresion
    | condicion Y condicion                                        // CondicionAnd
    | condicion O condicion                                        // CondicionOr
    | NO condicion                                                 // CondicionNot
    | PARENTESIS_IZQ condicion PARENTESIS_DER                      // CondicionParentesis
    ;

operador_relacional
    : ES_IGUAL_QUE
    | ES_DISTINTO_DE
    | ES_MAYOR_QUE
    | ES_MENOR_QUE
    | ES_MAYOR_O_IGUAL_QUE
    | ES_MENOR_O_IGUAL_QUE
    ;

// Expresiones
expresion
    : termino                                                      // ExpresionTermino
    | expresion MAS expresion                                      // ExpresionSuma
    | expresion MENOS expresion                                    // ExpresionResta
    | expresion POR expresion                                      // ExpresionMultiplicacion
    | expresion ENTRE expresion                                    // ExpresionDivision
    | expresion A_LA expresion                                     // ExpresionPotencia
    | PARENTESIS_IZQ expresion PARENTESIS_DER                      // ExpresionParentesis
    | llamada_funcion                                              // ExpresionLlamadaFuncion
    ;

// Término
termino
    : ID                                                           // TerminoID
    | NUMERO                                                       // TerminoNumero
    | CADENA                                                       // TerminoCadena
    ;

// Llamada a función
llamada_funcion
    : ID PARENTESIS_IZQ argumentos? PARENTESIS_DER
    ;

argumentos
    : expresion (COMA expresion)*
    ;
