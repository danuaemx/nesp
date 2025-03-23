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
    : ID ES_UN TIPO_DATO                                           
    | ID ES_UN ARREGLO_DE TIPO_DATO DE dimension                   
    ;

// Dimensiones de arreglos (1D, 2D, 3D, etc.)
dimension
    : NUMERO                                                       
    | NUMERO (POR NUMERO)+
    ;

// Asignaciones
asignacion
    : ID ASIGNA expresion
    | ID ASIGNA condicion
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
    : expresion operador_relacional expresion                     
    | expresion                                                    
    | condicion Y condicion                                       
    | condicion O condicion                                        
    | NO condicion                                                
    | PARENTESIS_IZQ condicion PARENTESIS_DER                     
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
    : termino                                                      
    | expresion MAS expresion                                     
    | expresion MENOS expresion                                   
    | expresion POR expresion                                      
    | expresion ENTRE expresion                                    
    | expresion A_LA expresion                                     
    | PARENTESIS_IZQ expresion PARENTESIS_DER                      
    | llamada_funcion                                              
    ;

// Término
termino
    : ID                                                           
    | NUMERO                                                       
    | CADENA                                                       
    ;

// Llamada a función
llamada_funcion
    : ID PARENTESIS_IZQ argumentos? PARENTESIS_DER
    ;

argumentos
    : expresion (COMA expresion)*
    ;
