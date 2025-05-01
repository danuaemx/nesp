lexer grammar gramaticaEspanol;

// Palabras reservadas

FUNCION : 'funcion';
SI : 'si';
ENTONCES : 'entonces:';
FIN : 'fin';
MIENTRAS : 'mientras';
ASIGNA : 'asigna';
A_LA : 'a la';
DEVUELVE : 'devuelve';
ES_UN : 'es un';
ARREGLO_DE : 'arreglo de';
DE : 'de';

// Operadores relacionales

ES_DISTINTO_DE : 'es distinto de';
ES_IGUAL_QUE : 'es igual que';
ES_MAYOR_QUE : 'es mayor que';
ES_MENOR_QUE : 'es menor que';
ES_MAYOR_O_IGUAL_QUE : 'es mayor o igual que';
ES_MENOR_O_IGUAL_QUE : 'es menor o igual que';

// Operadores aritméticos

MAS : 'mas';
MENOS : 'menos';
POR : 'por';
ENTRE : 'entre';

// Operadores lógicos

Y : 'y';
O : 'o';
NO : 'no';

// Tipos de datos

TIPO_DATO : 'entero' | 'real' | 'texto' | 'bit';

// Identificadores

ID : [a-zA-ZáéíóúÁÉÍÓÚñÑ][a-zA-Z0-9_áéíóúÁÉÍÓÚñÑ]*;

// Números

NUMERO : [0-9]+ ('.' [0-9]+)?;

// Cadenas

CADENA : '"' (~["\r\n])* '"';

// Comentarios

COMENTARIO : 'Nota:' .*? '/' -> skip;

// Delimitadores

PARENTESIS_IZQ : '(';
PARENTESIS_DER : ')';
CORCHETE_IZQ   : '[';
CORCHETE_DER   : ']';
DOS_PUNTOS : ':';
PUNTO : '.';
COMA : ',';

// Espacios en blanco y saltos de línea

WS : [ \t\r\n]+ -> skip;

// Capturar cualquier otro carácter como error

ERROR : .;
