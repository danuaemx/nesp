# Generated from src/parserGramaticaEspanol.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
#else:
	#from typing.io import TextIO

def serializedATN():
    return [
        4,1,36,197,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,4,0,36,8,0,11,0,12,0,37,1,0,1,
        0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,
        1,57,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,68,8,2,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,79,8,3,1,4,1,4,1,4,1,4,1,5,1,5,1,
        5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,3,7,101,8,
        7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,5,8,111,8,8,10,8,12,8,114,9,8,
        1,9,1,9,1,9,1,10,4,10,120,8,10,11,10,12,10,121,1,11,1,11,1,11,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,136,8,11,1,11,1,
        11,1,11,1,11,1,11,1,11,5,11,144,8,11,10,11,12,11,147,9,11,1,12,1,
        12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,158,8,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,5,
        13,175,8,13,10,13,12,13,178,9,13,1,14,1,14,1,15,1,15,1,15,3,15,185,
        8,15,1,15,1,15,1,16,1,16,1,16,5,16,192,8,16,10,16,12,16,195,9,16,
        1,16,0,2,22,26,17,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,
        0,2,1,0,12,17,1,0,26,28,206,0,35,1,0,0,0,2,56,1,0,0,0,4,67,1,0,0,
        0,6,78,1,0,0,0,8,80,1,0,0,0,10,84,1,0,0,0,12,90,1,0,0,0,14,96,1,
        0,0,0,16,107,1,0,0,0,18,115,1,0,0,0,20,119,1,0,0,0,22,135,1,0,0,
        0,24,148,1,0,0,0,26,157,1,0,0,0,28,179,1,0,0,0,30,181,1,0,0,0,32,
        188,1,0,0,0,34,36,3,2,1,0,35,34,1,0,0,0,36,37,1,0,0,0,37,35,1,0,
        0,0,37,38,1,0,0,0,38,39,1,0,0,0,39,40,5,0,0,1,40,1,1,0,0,0,41,42,
        3,4,2,0,42,43,5,33,0,0,43,57,1,0,0,0,44,45,3,8,4,0,45,46,5,33,0,
        0,46,57,1,0,0,0,47,57,3,10,5,0,48,57,3,12,6,0,49,57,3,14,7,0,50,
        51,3,18,9,0,51,52,5,33,0,0,52,57,1,0,0,0,53,54,3,26,13,0,54,55,5,
        33,0,0,55,57,1,0,0,0,56,41,1,0,0,0,56,44,1,0,0,0,56,47,1,0,0,0,56,
        48,1,0,0,0,56,49,1,0,0,0,56,50,1,0,0,0,56,53,1,0,0,0,57,3,1,0,0,
        0,58,59,5,26,0,0,59,60,5,9,0,0,60,68,5,25,0,0,61,62,5,26,0,0,62,
        63,5,9,0,0,63,64,5,10,0,0,64,65,5,25,0,0,65,66,5,11,0,0,66,68,3,
        6,3,0,67,58,1,0,0,0,67,61,1,0,0,0,68,5,1,0,0,0,69,79,5,27,0,0,70,
        71,5,27,0,0,71,72,5,20,0,0,72,79,5,27,0,0,73,74,5,27,0,0,74,75,5,
        20,0,0,75,76,5,27,0,0,76,77,5,20,0,0,77,79,5,27,0,0,78,69,1,0,0,
        0,78,70,1,0,0,0,78,73,1,0,0,0,79,7,1,0,0,0,80,81,5,26,0,0,81,82,
        5,6,0,0,82,83,3,26,13,0,83,9,1,0,0,0,84,85,5,2,0,0,85,86,3,22,11,
        0,86,87,5,3,0,0,87,88,3,20,10,0,88,89,5,4,0,0,89,11,1,0,0,0,90,91,
        5,5,0,0,91,92,3,22,11,0,92,93,5,3,0,0,93,94,3,20,10,0,94,95,5,4,
        0,0,95,13,1,0,0,0,96,97,5,1,0,0,97,98,5,26,0,0,98,100,5,30,0,0,99,
        101,3,16,8,0,100,99,1,0,0,0,100,101,1,0,0,0,101,102,1,0,0,0,102,
        103,5,31,0,0,103,104,5,32,0,0,104,105,3,20,10,0,105,106,5,4,0,0,
        106,15,1,0,0,0,107,112,5,26,0,0,108,109,5,34,0,0,109,111,5,26,0,
        0,110,108,1,0,0,0,111,114,1,0,0,0,112,110,1,0,0,0,112,113,1,0,0,
        0,113,17,1,0,0,0,114,112,1,0,0,0,115,116,5,8,0,0,116,117,3,26,13,
        0,117,19,1,0,0,0,118,120,3,2,1,0,119,118,1,0,0,0,120,121,1,0,0,0,
        121,119,1,0,0,0,121,122,1,0,0,0,122,21,1,0,0,0,123,124,6,11,-1,0,
        124,125,3,26,13,0,125,126,3,24,12,0,126,127,3,26,13,0,127,136,1,
        0,0,0,128,136,3,26,13,0,129,130,5,24,0,0,130,136,3,22,11,2,131,132,
        5,30,0,0,132,133,3,22,11,0,133,134,5,31,0,0,134,136,1,0,0,0,135,
        123,1,0,0,0,135,128,1,0,0,0,135,129,1,0,0,0,135,131,1,0,0,0,136,
        145,1,0,0,0,137,138,10,4,0,0,138,139,5,22,0,0,139,144,3,22,11,5,
        140,141,10,3,0,0,141,142,5,23,0,0,142,144,3,22,11,4,143,137,1,0,
        0,0,143,140,1,0,0,0,144,147,1,0,0,0,145,143,1,0,0,0,145,146,1,0,
        0,0,146,23,1,0,0,0,147,145,1,0,0,0,148,149,7,0,0,0,149,25,1,0,0,
        0,150,151,6,13,-1,0,151,158,3,28,14,0,152,153,5,30,0,0,153,154,3,
        26,13,0,154,155,5,31,0,0,155,158,1,0,0,0,156,158,3,30,15,0,157,150,
        1,0,0,0,157,152,1,0,0,0,157,156,1,0,0,0,158,176,1,0,0,0,159,160,
        10,7,0,0,160,161,5,18,0,0,161,175,3,26,13,8,162,163,10,6,0,0,163,
        164,5,19,0,0,164,175,3,26,13,7,165,166,10,5,0,0,166,167,5,20,0,0,
        167,175,3,26,13,6,168,169,10,4,0,0,169,170,5,21,0,0,170,175,3,26,
        13,5,171,172,10,3,0,0,172,173,5,7,0,0,173,175,3,26,13,4,174,159,
        1,0,0,0,174,162,1,0,0,0,174,165,1,0,0,0,174,168,1,0,0,0,174,171,
        1,0,0,0,175,178,1,0,0,0,176,174,1,0,0,0,176,177,1,0,0,0,177,27,1,
        0,0,0,178,176,1,0,0,0,179,180,7,1,0,0,180,29,1,0,0,0,181,182,5,26,
        0,0,182,184,5,30,0,0,183,185,3,32,16,0,184,183,1,0,0,0,184,185,1,
        0,0,0,185,186,1,0,0,0,186,187,5,31,0,0,187,31,1,0,0,0,188,193,3,
        26,13,0,189,190,5,34,0,0,190,192,3,26,13,0,191,189,1,0,0,0,192,195,
        1,0,0,0,193,191,1,0,0,0,193,194,1,0,0,0,194,33,1,0,0,0,195,193,1,
        0,0,0,15,37,56,67,78,100,112,121,135,143,145,157,174,176,184,193
    ]

class parserGramaticaEspanol ( Parser ):

    grammarFileName = "parserGramaticaEspanol.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'funcion'", "'si'", "'entonces:'", "'fin'", 
                     "'mientras'", "'asigna'", "'a la'", "'devuelve'", "'es un'", 
                     "'arreglo de'", "'de'", "'es distinto de'", "'es igual que'", 
                     "'es mayor que'", "'es menor que'", "'es mayor o igual que'", 
                     "'es menor o igual que'", "'mas'", "'menos'", "'por'", 
                     "'entre'", "'y'", "'o'", "'no'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "':'", "'.'", "','" ]

    symbolicNames = [ "<INVALID>", "FUNCION", "SI", "ENTONCES", "FIN", "MIENTRAS", 
                      "ASIGNA", "A_LA", "DEVUELVE", "ES_UN", "ARREGLO_DE", 
                      "DE", "ES_DISTINTO_DE", "ES_IGUAL_QUE", "ES_MAYOR_QUE", 
                      "ES_MENOR_QUE", "ES_MAYOR_O_IGUAL_QUE", "ES_MENOR_O_IGUAL_QUE", 
                      "MAS", "MENOS", "POR", "ENTRE", "Y", "O", "NO", "TIPO_DATO", 
                      "ID", "NUMERO", "CADENA", "COMENTARIO", "PARENTESIS_IZQ", 
                      "PARENTESIS_DER", "DOS_PUNTOS", "PUNTO", "COMA", "WS", 
                      "ERROR" ]

    RULE_programa = 0
    RULE_instruccion = 1
    RULE_declaracion = 2
    RULE_dimension = 3
    RULE_asignacion = 4
    RULE_sentencia_if = 5
    RULE_sentencia_while = 6
    RULE_definicion_funcion = 7
    RULE_parametros = 8
    RULE_retorno = 9
    RULE_bloque = 10
    RULE_condicion = 11
    RULE_operador_relacional = 12
    RULE_expresion = 13
    RULE_termino = 14
    RULE_llamada_funcion = 15
    RULE_argumentos = 16

    ruleNames =  [ "programa", "instruccion", "declaracion", "dimension", 
                   "asignacion", "sentencia_if", "sentencia_while", "definicion_funcion", 
                   "parametros", "retorno", "bloque", "condicion", "operador_relacional", 
                   "expresion", "termino", "llamada_funcion", "argumentos" ]

    EOF = Token.EOF
    FUNCION=1
    SI=2
    ENTONCES=3
    FIN=4
    MIENTRAS=5
    ASIGNA=6
    A_LA=7
    DEVUELVE=8
    ES_UN=9
    ARREGLO_DE=10
    DE=11
    ES_DISTINTO_DE=12
    ES_IGUAL_QUE=13
    ES_MAYOR_QUE=14
    ES_MENOR_QUE=15
    ES_MAYOR_O_IGUAL_QUE=16
    ES_MENOR_O_IGUAL_QUE=17
    MAS=18
    MENOS=19
    POR=20
    ENTRE=21
    Y=22
    O=23
    NO=24
    TIPO_DATO=25
    ID=26
    NUMERO=27
    CADENA=28
    COMENTARIO=29
    PARENTESIS_IZQ=30
    PARENTESIS_DER=31
    DOS_PUNTOS=32
    PUNTO=33
    COMA=34
    WS=35
    ERROR=36

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(parserGramaticaEspanol.EOF, 0)

        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(parserGramaticaEspanol.InstruccionContext)
            else:
                return self.getTypedRuleContext(parserGramaticaEspanol.InstruccionContext,i)


        def getRuleIndex(self):
            return parserGramaticaEspanol.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = parserGramaticaEspanol.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 34
                self.instruccion()
                self.state = 37 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1543504166) != 0)):
                    break

            self.state = 39
            self.match(parserGramaticaEspanol.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracion(self):
            return self.getTypedRuleContext(parserGramaticaEspanol.DeclaracionContext,0)


        def PUNTO(self):
            return self.getToken(parserGramaticaEspanol.PUNTO, 0)

        def asignacion(self):
            return self.getTypedRuleContext(parserGramaticaEspanol.AsignacionContext,0)


        def sentencia_if(self):
            return self.getTypedRuleContext(parserGramaticaEspanol.Sentencia_ifContext,0)


        def sentencia_while(self):
            return self.getTypedRuleContext(parserGramaticaEspanol.Sentencia_whileContext,0)


        def definicion_funcion(self):
            return self.getTypedRuleContext(parserGramaticaEspanol.Definicion_funcionContext,0)


        def retorno(self):
            return self.getTypedRuleContext(parserGramaticaEspanol.RetornoContext,0)


        def expresion(self):
            return self.getTypedRuleContext(parserGramaticaEspanol.ExpresionContext,0)


        def getRuleIndex(self):
            return parserGramaticaEspanol.RULE_instruccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccion" ):
                listener.enterInstruccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccion" ):
                listener.exitInstruccion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccion" ):
                return visitor.visitInstruccion(self)
            else:
                return visitor.visitChildren(self)




    def instruccion(self):

        localctx = parserGramaticaEspanol.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instruccion)
        try:
            self.state = 56
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.declaracion()
                self.state = 42
                self.match(parserGramaticaEspanol.PUNTO)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.asignacion()
                self.state = 45
                self.match(parserGramaticaEspanol.PUNTO)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 47
                self.sentencia_if()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 48
                self.sentencia_while()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 49
                self.definicion_funcion()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 50
                self.retorno()
                self.state = 51
                self.match(parserGramaticaEspanol.PUNTO)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 53
                self.expresion(0)
                self.state = 54
                self.match(parserGramaticaEspanol.PUNTO)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(parserGramaticaEspanol.ID, 0)

        def ES_UN(self):
            return self.getToken(parserGramaticaEspanol.ES_UN, 0)

        def TIPO_DATO(self):
            return self.getToken(parserGramaticaEspanol.TIPO_DATO, 0)

        def ARREGLO_DE(self):
            return self.getToken(parserGramaticaEspanol.ARREGLO_DE, 0)

        def DE(self):
            return self.getToken(parserGramaticaEspanol.DE, 0)

        def dimension(self):
            return self.getTypedRuleContext(parserGramaticaEspanol.DimensionContext,0)


        def getRuleIndex(self):
            return parserGramaticaEspanol.RULE_declaracion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion" ):
                return visitor.visitDeclaracion(self)
            else:
                return visitor.visitChildren(self)




    def declaracion(self):

        localctx = parserGramaticaEspanol.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaracion)
        try:
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.match(parserGramaticaEspanol.ID)
                self.state = 59
                self.match(parserGramaticaEspanol.ES_UN)
                self.state = 60
                self.match(parserGramaticaEspanol.TIPO_DATO)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.match(parserGramaticaEspanol.ID)
                self.state = 62
                self.match(parserGramaticaEspanol.ES_UN)
                self.state = 63
                self.match(parserGramaticaEspanol.ARREGLO_DE)
                self.state = 64
                self.match(parserGramaticaEspanol.TIPO_DATO)
                self.state = 65
                self.match(parserGramaticaEspanol.DE)
                self.state = 66
                self.dimension()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERO(self, i:int=None):
            if i is None:
                return self.getTokens(parserGramaticaEspanol.NUMERO)
            else:
                return self.getToken(parserGramaticaEspanol.NUMERO, i)

        def POR(self, i:int=None):
            if i is None:
                return self.getTokens(parserGramaticaEspanol.POR)
            else:
                return self.getToken(parserGramaticaEspanol.POR, i)

        def getRuleIndex(self):
            return parserGramaticaEspanol.RULE_dimension

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDimension" ):
                listener.enterDimension(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDimension" ):
                listener.exitDimension(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimension" ):
                return visitor.visitDimension(self)
            else:
                return visitor.visitChildren(self)




    def dimension(self):

        localctx = parserGramaticaEspanol.DimensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_dimension)
        try:
            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.match(parserGramaticaEspanol.NUMERO)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.match(parserGramaticaEspanol.NUMERO)
                self.state = 71
                self.match(parserGramaticaEspanol.POR)
                self.state = 72
                self.match(parserGramaticaEspanol.NUMERO)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 73
                self.match(parserGramaticaEspanol.NUMERO)
                self.state = 74
                self.match(parserGramaticaEspanol.POR)
                self.state = 75
                self.match(parserGramaticaEspanol.NUMERO)
                self.state = 76
                self.match(parserGramaticaEspanol.POR)
                self.state = 77
                self.match(parserGramaticaEspanol.NUMERO)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(parserGramaticaEspanol.ID, 0)

        def ASIGNA(self):
            return self.getToken(parserGramaticaEspanol.ASIGNA, 0)

        def expresion(self):
            return self.getTypedRuleContext(parserGramaticaEspanol.ExpresionContext,0)


        def getRuleIndex(self):
            return parserGramaticaEspanol.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = parserGramaticaEspanol.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(parserGramaticaEspanol.ID)
            self.state = 81
            self.match(parserGramaticaEspanol.ASIGNA)
            self.state = 82
            self.expresion(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sentencia_ifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SI(self):
            return self.getToken(parserGramaticaEspanol.SI, 0)

        def condicion(self):
            return self.getTypedRuleContext(parserGramaticaEspanol.CondicionContext,0)


        def ENTONCES(self):
            return self.getToken(parserGramaticaEspanol.ENTONCES, 0)

        def bloque(self):
            return self.getTypedRuleContext(parserGramaticaEspanol.BloqueContext,0)


        def FIN(self):
            return self.getToken(parserGramaticaEspanol.FIN, 0)

        def getRuleIndex(self):
            return parserGramaticaEspanol.RULE_sentencia_if

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia_if" ):
                listener.enterSentencia_if(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia_if" ):
                listener.exitSentencia_if(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia_if" ):
                return visitor.visitSentencia_if(self)
            else:
                return visitor.visitChildren(self)




    def sentencia_if(self):

        localctx = parserGramaticaEspanol.Sentencia_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_sentencia_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(parserGramaticaEspanol.SI)
            self.state = 85
            self.condicion(0)
            self.state = 86
            self.match(parserGramaticaEspanol.ENTONCES)
            self.state = 87
            self.bloque()
            self.state = 88
            self.match(parserGramaticaEspanol.FIN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sentencia_whileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MIENTRAS(self):
            return self.getToken(parserGramaticaEspanol.MIENTRAS, 0)

        def condicion(self):
            return self.getTypedRuleContext(parserGramaticaEspanol.CondicionContext,0)


        def ENTONCES(self):
            return self.getToken(parserGramaticaEspanol.ENTONCES, 0)

        def bloque(self):
            return self.getTypedRuleContext(parserGramaticaEspanol.BloqueContext,0)


        def FIN(self):
            return self.getToken(parserGramaticaEspanol.FIN, 0)

        def getRuleIndex(self):
            return parserGramaticaEspanol.RULE_sentencia_while

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia_while" ):
                listener.enterSentencia_while(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia_while" ):
                listener.exitSentencia_while(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia_while" ):
                return visitor.visitSentencia_while(self)
            else:
                return visitor.visitChildren(self)




    def sentencia_while(self):

        localctx = parserGramaticaEspanol.Sentencia_whileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_sentencia_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(parserGramaticaEspanol.MIENTRAS)
            self.state = 91
            self.condicion(0)
            self.state = 92
            self.match(parserGramaticaEspanol.ENTONCES)
            self.state = 93
            self.bloque()
            self.state = 94
            self.match(parserGramaticaEspanol.FIN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Definicion_funcionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCION(self):
            return self.getToken(parserGramaticaEspanol.FUNCION, 0)

        def ID(self):
            return self.getToken(parserGramaticaEspanol.ID, 0)

        def PARENTESIS_IZQ(self):
            return self.getToken(parserGramaticaEspanol.PARENTESIS_IZQ, 0)

        def PARENTESIS_DER(self):
            return self.getToken(parserGramaticaEspanol.PARENTESIS_DER, 0)

        def DOS_PUNTOS(self):
            return self.getToken(parserGramaticaEspanol.DOS_PUNTOS, 0)

        def bloque(self):
            return self.getTypedRuleContext(parserGramaticaEspanol.BloqueContext,0)


        def FIN(self):
            return self.getToken(parserGramaticaEspanol.FIN, 0)

        def parametros(self):
            return self.getTypedRuleContext(parserGramaticaEspanol.ParametrosContext,0)


        def getRuleIndex(self):
            return parserGramaticaEspanol.RULE_definicion_funcion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefinicion_funcion" ):
                listener.enterDefinicion_funcion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefinicion_funcion" ):
                listener.exitDefinicion_funcion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinicion_funcion" ):
                return visitor.visitDefinicion_funcion(self)
            else:
                return visitor.visitChildren(self)




    def definicion_funcion(self):

        localctx = parserGramaticaEspanol.Definicion_funcionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_definicion_funcion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(parserGramaticaEspanol.FUNCION)
            self.state = 97
            self.match(parserGramaticaEspanol.ID)
            self.state = 98
            self.match(parserGramaticaEspanol.PARENTESIS_IZQ)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 99
                self.parametros()


            self.state = 102
            self.match(parserGramaticaEspanol.PARENTESIS_DER)
            self.state = 103
            self.match(parserGramaticaEspanol.DOS_PUNTOS)
            self.state = 104
            self.bloque()
            self.state = 105
            self.match(parserGramaticaEspanol.FIN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(parserGramaticaEspanol.ID)
            else:
                return self.getToken(parserGramaticaEspanol.ID, i)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(parserGramaticaEspanol.COMA)
            else:
                return self.getToken(parserGramaticaEspanol.COMA, i)

        def getRuleIndex(self):
            return parserGramaticaEspanol.RULE_parametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametros" ):
                listener.enterParametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametros" ):
                listener.exitParametros(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametros" ):
                return visitor.visitParametros(self)
            else:
                return visitor.visitChildren(self)




    def parametros(self):

        localctx = parserGramaticaEspanol.ParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_parametros)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(parserGramaticaEspanol.ID)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 108
                self.match(parserGramaticaEspanol.COMA)
                self.state = 109
                self.match(parserGramaticaEspanol.ID)
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RetornoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEVUELVE(self):
            return self.getToken(parserGramaticaEspanol.DEVUELVE, 0)

        def expresion(self):
            return self.getTypedRuleContext(parserGramaticaEspanol.ExpresionContext,0)


        def getRuleIndex(self):
            return parserGramaticaEspanol.RULE_retorno

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRetorno" ):
                listener.enterRetorno(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRetorno" ):
                listener.exitRetorno(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRetorno" ):
                return visitor.visitRetorno(self)
            else:
                return visitor.visitChildren(self)




    def retorno(self):

        localctx = parserGramaticaEspanol.RetornoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_retorno)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(parserGramaticaEspanol.DEVUELVE)
            self.state = 116
            self.expresion(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(parserGramaticaEspanol.InstruccionContext)
            else:
                return self.getTypedRuleContext(parserGramaticaEspanol.InstruccionContext,i)


        def getRuleIndex(self):
            return parserGramaticaEspanol.RULE_bloque

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque" ):
                listener.enterBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque" ):
                listener.exitBloque(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = parserGramaticaEspanol.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_bloque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 118
                self.instruccion()
                self.state = 121 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1543504166) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(parserGramaticaEspanol.ExpresionContext)
            else:
                return self.getTypedRuleContext(parserGramaticaEspanol.ExpresionContext,i)


        def operador_relacional(self):
            return self.getTypedRuleContext(parserGramaticaEspanol.Operador_relacionalContext,0)


        def NO(self):
            return self.getToken(parserGramaticaEspanol.NO, 0)

        def condicion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(parserGramaticaEspanol.CondicionContext)
            else:
                return self.getTypedRuleContext(parserGramaticaEspanol.CondicionContext,i)


        def PARENTESIS_IZQ(self):
            return self.getToken(parserGramaticaEspanol.PARENTESIS_IZQ, 0)

        def PARENTESIS_DER(self):
            return self.getToken(parserGramaticaEspanol.PARENTESIS_DER, 0)

        def Y(self):
            return self.getToken(parserGramaticaEspanol.Y, 0)

        def O(self):
            return self.getToken(parserGramaticaEspanol.O, 0)

        def getRuleIndex(self):
            return parserGramaticaEspanol.RULE_condicion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicion" ):
                listener.enterCondicion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicion" ):
                listener.exitCondicion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicion" ):
                return visitor.visitCondicion(self)
            else:
                return visitor.visitChildren(self)



    def condicion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = parserGramaticaEspanol.CondicionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_condicion, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 124
                self.expresion(0)
                self.state = 125
                self.operador_relacional()
                self.state = 126
                self.expresion(0)
                pass

            elif la_ == 2:
                self.state = 128
                self.expresion(0)
                pass

            elif la_ == 3:
                self.state = 129
                self.match(parserGramaticaEspanol.NO)
                self.state = 130
                self.condicion(2)
                pass

            elif la_ == 4:
                self.state = 131
                self.match(parserGramaticaEspanol.PARENTESIS_IZQ)
                self.state = 132
                self.condicion(0)
                self.state = 133
                self.match(parserGramaticaEspanol.PARENTESIS_DER)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 145
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 143
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = parserGramaticaEspanol.CondicionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_condicion)
                        self.state = 137
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 138
                        self.match(parserGramaticaEspanol.Y)
                        self.state = 139
                        self.condicion(5)
                        pass

                    elif la_ == 2:
                        localctx = parserGramaticaEspanol.CondicionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_condicion)
                        self.state = 140
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 141
                        self.match(parserGramaticaEspanol.O)
                        self.state = 142
                        self.condicion(4)
                        pass

             
                self.state = 147
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Operador_relacionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ES_IGUAL_QUE(self):
            return self.getToken(parserGramaticaEspanol.ES_IGUAL_QUE, 0)

        def ES_DISTINTO_DE(self):
            return self.getToken(parserGramaticaEspanol.ES_DISTINTO_DE, 0)

        def ES_MAYOR_QUE(self):
            return self.getToken(parserGramaticaEspanol.ES_MAYOR_QUE, 0)

        def ES_MENOR_QUE(self):
            return self.getToken(parserGramaticaEspanol.ES_MENOR_QUE, 0)

        def ES_MAYOR_O_IGUAL_QUE(self):
            return self.getToken(parserGramaticaEspanol.ES_MAYOR_O_IGUAL_QUE, 0)

        def ES_MENOR_O_IGUAL_QUE(self):
            return self.getToken(parserGramaticaEspanol.ES_MENOR_O_IGUAL_QUE, 0)

        def getRuleIndex(self):
            return parserGramaticaEspanol.RULE_operador_relacional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperador_relacional" ):
                listener.enterOperador_relacional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperador_relacional" ):
                listener.exitOperador_relacional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperador_relacional" ):
                return visitor.visitOperador_relacional(self)
            else:
                return visitor.visitChildren(self)




    def operador_relacional(self):

        localctx = parserGramaticaEspanol.Operador_relacionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_operador_relacional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 258048) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termino(self):
            return self.getTypedRuleContext(parserGramaticaEspanol.TerminoContext,0)


        def PARENTESIS_IZQ(self):
            return self.getToken(parserGramaticaEspanol.PARENTESIS_IZQ, 0)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(parserGramaticaEspanol.ExpresionContext)
            else:
                return self.getTypedRuleContext(parserGramaticaEspanol.ExpresionContext,i)


        def PARENTESIS_DER(self):
            return self.getToken(parserGramaticaEspanol.PARENTESIS_DER, 0)

        def llamada_funcion(self):
            return self.getTypedRuleContext(parserGramaticaEspanol.Llamada_funcionContext,0)


        def MAS(self):
            return self.getToken(parserGramaticaEspanol.MAS, 0)

        def MENOS(self):
            return self.getToken(parserGramaticaEspanol.MENOS, 0)

        def POR(self):
            return self.getToken(parserGramaticaEspanol.POR, 0)

        def ENTRE(self):
            return self.getToken(parserGramaticaEspanol.ENTRE, 0)

        def A_LA(self):
            return self.getToken(parserGramaticaEspanol.A_LA, 0)

        def getRuleIndex(self):
            return parserGramaticaEspanol.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresion" ):
                return visitor.visitExpresion(self)
            else:
                return visitor.visitChildren(self)



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = parserGramaticaEspanol.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expresion, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 151
                self.termino()
                pass

            elif la_ == 2:
                self.state = 152
                self.match(parserGramaticaEspanol.PARENTESIS_IZQ)
                self.state = 153
                self.expresion(0)
                self.state = 154
                self.match(parserGramaticaEspanol.PARENTESIS_DER)
                pass

            elif la_ == 3:
                self.state = 156
                self.llamada_funcion()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 176
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 174
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = parserGramaticaEspanol.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 159
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 160
                        self.match(parserGramaticaEspanol.MAS)
                        self.state = 161
                        self.expresion(8)
                        pass

                    elif la_ == 2:
                        localctx = parserGramaticaEspanol.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 162
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 163
                        self.match(parserGramaticaEspanol.MENOS)
                        self.state = 164
                        self.expresion(7)
                        pass

                    elif la_ == 3:
                        localctx = parserGramaticaEspanol.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 165
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 166
                        self.match(parserGramaticaEspanol.POR)
                        self.state = 167
                        self.expresion(6)
                        pass

                    elif la_ == 4:
                        localctx = parserGramaticaEspanol.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 168
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 169
                        self.match(parserGramaticaEspanol.ENTRE)
                        self.state = 170
                        self.expresion(5)
                        pass

                    elif la_ == 5:
                        localctx = parserGramaticaEspanol.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 171
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 172
                        self.match(parserGramaticaEspanol.A_LA)
                        self.state = 173
                        self.expresion(4)
                        pass

             
                self.state = 178
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TerminoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(parserGramaticaEspanol.ID, 0)

        def NUMERO(self):
            return self.getToken(parserGramaticaEspanol.NUMERO, 0)

        def CADENA(self):
            return self.getToken(parserGramaticaEspanol.CADENA, 0)

        def getRuleIndex(self):
            return parserGramaticaEspanol.RULE_termino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermino" ):
                listener.enterTermino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermino" ):
                listener.exitTermino(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermino" ):
                return visitor.visitTermino(self)
            else:
                return visitor.visitChildren(self)




    def termino(self):

        localctx = parserGramaticaEspanol.TerminoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_termino)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 469762048) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Llamada_funcionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(parserGramaticaEspanol.ID, 0)

        def PARENTESIS_IZQ(self):
            return self.getToken(parserGramaticaEspanol.PARENTESIS_IZQ, 0)

        def PARENTESIS_DER(self):
            return self.getToken(parserGramaticaEspanol.PARENTESIS_DER, 0)

        def argumentos(self):
            return self.getTypedRuleContext(parserGramaticaEspanol.ArgumentosContext,0)


        def getRuleIndex(self):
            return parserGramaticaEspanol.RULE_llamada_funcion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlamada_funcion" ):
                listener.enterLlamada_funcion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlamada_funcion" ):
                listener.exitLlamada_funcion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlamada_funcion" ):
                return visitor.visitLlamada_funcion(self)
            else:
                return visitor.visitChildren(self)




    def llamada_funcion(self):

        localctx = parserGramaticaEspanol.Llamada_funcionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_llamada_funcion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(parserGramaticaEspanol.ID)
            self.state = 182
            self.match(parserGramaticaEspanol.PARENTESIS_IZQ)
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1543503872) != 0):
                self.state = 183
                self.argumentos()


            self.state = 186
            self.match(parserGramaticaEspanol.PARENTESIS_DER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(parserGramaticaEspanol.ExpresionContext)
            else:
                return self.getTypedRuleContext(parserGramaticaEspanol.ExpresionContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(parserGramaticaEspanol.COMA)
            else:
                return self.getToken(parserGramaticaEspanol.COMA, i)

        def getRuleIndex(self):
            return parserGramaticaEspanol.RULE_argumentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentos" ):
                listener.enterArgumentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentos" ):
                listener.exitArgumentos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentos" ):
                return visitor.visitArgumentos(self)
            else:
                return visitor.visitChildren(self)




    def argumentos(self):

        localctx = parserGramaticaEspanol.ArgumentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_argumentos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.expresion(0)
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 189
                self.match(parserGramaticaEspanol.COMA)
                self.state = 190
                self.expresion(0)
                self.state = 195
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[11] = self.condicion_sempred
        self._predicates[13] = self.expresion_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def condicion_sempred(self, localctx:CondicionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         




