# Generated from src/parserGramaticaEspanol.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .parserGramaticaEspanol import parserGramaticaEspanol
else:
    from parserGramaticaEspanol import parserGramaticaEspanol

# This class defines a complete generic visitor for a parse tree produced by parserGramaticaEspanol.

class parserGramaticaEspanolVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by parserGramaticaEspanol#programa.
    def visitPrograma(self, ctx:parserGramaticaEspanol.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by parserGramaticaEspanol#instruccion.
    def visitInstruccion(self, ctx:parserGramaticaEspanol.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by parserGramaticaEspanol#declaracion.
    def visitDeclaracion(self, ctx:parserGramaticaEspanol.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by parserGramaticaEspanol#dimension.
    def visitDimension(self, ctx:parserGramaticaEspanol.DimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by parserGramaticaEspanol#asignacion.
    def visitAsignacion(self, ctx:parserGramaticaEspanol.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by parserGramaticaEspanol#sentencia_if.
    def visitSentencia_if(self, ctx:parserGramaticaEspanol.Sentencia_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by parserGramaticaEspanol#sentencia_while.
    def visitSentencia_while(self, ctx:parserGramaticaEspanol.Sentencia_whileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by parserGramaticaEspanol#definicion_funcion.
    def visitDefinicion_funcion(self, ctx:parserGramaticaEspanol.Definicion_funcionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by parserGramaticaEspanol#parametros.
    def visitParametros(self, ctx:parserGramaticaEspanol.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by parserGramaticaEspanol#retorno.
    def visitRetorno(self, ctx:parserGramaticaEspanol.RetornoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by parserGramaticaEspanol#bloque.
    def visitBloque(self, ctx:parserGramaticaEspanol.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by parserGramaticaEspanol#condicion.
    def visitCondicion(self, ctx:parserGramaticaEspanol.CondicionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by parserGramaticaEspanol#operador_relacional.
    def visitOperador_relacional(self, ctx:parserGramaticaEspanol.Operador_relacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by parserGramaticaEspanol#expresion.
    def visitExpresion(self, ctx:parserGramaticaEspanol.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by parserGramaticaEspanol#termino.
    def visitTermino(self, ctx:parserGramaticaEspanol.TerminoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by parserGramaticaEspanol#llamada_funcion.
    def visitLlamada_funcion(self, ctx:parserGramaticaEspanol.Llamada_funcionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by parserGramaticaEspanol#argumentos.
    def visitArgumentos(self, ctx:parserGramaticaEspanol.ArgumentosContext):
        return self.visitChildren(ctx)



del parserGramaticaEspanol