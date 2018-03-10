# Generated from Objective_JS.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .Objective_JSParser import Objective_JSParser
else:
    from Objective_JSParser import Objective_JSParser

# This class defines a complete generic visitor for a parse tree produced by Objective_JSParser.

class Objective_JSVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by Objective_JSParser#inicio.
    def visitInicio(self, ctx:Objective_JSParser.InicioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#main.
    def visitMain(self, ctx:Objective_JSParser.MainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#clase.
    def visitClase(self, ctx:Objective_JSParser.ClaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#imports.
    def visitImports(self, ctx:Objective_JSParser.ImportsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#class_declaration.
    def visitClass_declaration(self, ctx:Objective_JSParser.Class_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#bloque.
    def visitBloque(self, ctx:Objective_JSParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#preEstatuto.
    def visitPreEstatuto(self, ctx:Objective_JSParser.PreEstatutoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#claseAux.
    def visitClaseAux(self, ctx:Objective_JSParser.ClaseAuxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#bloqueClase.
    def visitBloqueClase(self, ctx:Objective_JSParser.BloqueClaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#constructor.
    def visitConstructor(self, ctx:Objective_JSParser.ConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#constructorAux.
    def visitConstructorAux(self, ctx:Objective_JSParser.ConstructorAuxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#constructorAux2.
    def visitConstructorAux2(self, ctx:Objective_JSParser.ConstructorAux2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#atributos.
    def visitAtributos(self, ctx:Objective_JSParser.AtributosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#atributosPublic.
    def visitAtributosPublic(self, ctx:Objective_JSParser.AtributosPublicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#atributosPublicAux.
    def visitAtributosPublicAux(self, ctx:Objective_JSParser.AtributosPublicAuxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#atributosPrivate.
    def visitAtributosPrivate(self, ctx:Objective_JSParser.AtributosPrivateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#atributosPrivateAux.
    def visitAtributosPrivateAux(self, ctx:Objective_JSParser.AtributosPrivateAuxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#atributosProtected.
    def visitAtributosProtected(self, ctx:Objective_JSParser.AtributosProtectedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#metodos.
    def visitMetodos(self, ctx:Objective_JSParser.MetodosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#metodosPublicos.
    def visitMetodosPublicos(self, ctx:Objective_JSParser.MetodosPublicosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#metodosPublicosAux.
    def visitMetodosPublicosAux(self, ctx:Objective_JSParser.MetodosPublicosAuxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#metodosPrivados.
    def visitMetodosPrivados(self, ctx:Objective_JSParser.MetodosPrivadosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#metodosPrivadosAux.
    def visitMetodosPrivadosAux(self, ctx:Objective_JSParser.MetodosPrivadosAuxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#func.
    def visitFunc(self, ctx:Objective_JSParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#funcAux.
    def visitFuncAux(self, ctx:Objective_JSParser.FuncAuxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#impConstructores.
    def visitImpConstructores(self, ctx:Objective_JSParser.ImpConstructoresContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#impConstructoresMultiples.
    def visitImpConstructoresMultiples(self, ctx:Objective_JSParser.ImpConstructoresMultiplesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#impConstructor.
    def visitImpConstructor(self, ctx:Objective_JSParser.ImpConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#impFunc.
    def visitImpFunc(self, ctx:Objective_JSParser.ImpFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#impFuncAux2.
    def visitImpFuncAux2(self, ctx:Objective_JSParser.ImpFuncAux2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#argumentos.
    def visitArgumentos(self, ctx:Objective_JSParser.ArgumentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#argumentosAux.
    def visitArgumentosAux(self, ctx:Objective_JSParser.ArgumentosAuxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#bloqueConstructor.
    def visitBloqueConstructor(self, ctx:Objective_JSParser.BloqueConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#bloqueConstructorAux.
    def visitBloqueConstructorAux(self, ctx:Objective_JSParser.BloqueConstructorAuxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#bloqueFunc.
    def visitBloqueFunc(self, ctx:Objective_JSParser.BloqueFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#bloqueFuncAux.
    def visitBloqueFuncAux(self, ctx:Objective_JSParser.BloqueFuncAuxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#bloqueFuncAux2.
    def visitBloqueFuncAux2(self, ctx:Objective_JSParser.BloqueFuncAux2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#preVars.
    def visitPreVars(self, ctx:Objective_JSParser.PreVarsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#vars_.
    def visitVars_(self, ctx:Objective_JSParser.Vars_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#varsAux.
    def visitVarsAux(self, ctx:Objective_JSParser.VarsAuxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#varsRepeated.
    def visitVarsRepeated(self, ctx:Objective_JSParser.VarsRepeatedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#tipo_dato.
    def visitTipo_dato(self, ctx:Objective_JSParser.Tipo_datoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#tipo_dato_list.
    def visitTipo_dato_list(self, ctx:Objective_JSParser.Tipo_dato_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#dim.
    def visitDim(self, ctx:Objective_JSParser.DimContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#dimMatrix.
    def visitDimMatrix(self, ctx:Objective_JSParser.DimMatrixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#tipo_dato_no_list.
    def visitTipo_dato_no_list(self, ctx:Objective_JSParser.Tipo_dato_no_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#tipo.
    def visitTipo(self, ctx:Objective_JSParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#estatuto.
    def visitEstatuto(self, ctx:Objective_JSParser.EstatutoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#asignacion.
    def visitAsignacion(self, ctx:Objective_JSParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#condicion.
    def visitCondicion(self, ctx:Objective_JSParser.CondicionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#condicionAux.
    def visitCondicionAux(self, ctx:Objective_JSParser.CondicionAuxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#condicionChoice.
    def visitCondicionChoice(self, ctx:Objective_JSParser.CondicionChoiceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#escritura.
    def visitEscritura(self, ctx:Objective_JSParser.EscrituraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#escrituraAux.
    def visitEscrituraAux(self, ctx:Objective_JSParser.EscrituraAuxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#ciclos.
    def visitCiclos(self, ctx:Objective_JSParser.CiclosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#doAux.
    def visitDoAux(self, ctx:Objective_JSParser.DoAuxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#llamadaFunc.
    def visitLlamadaFunc(self, ctx:Objective_JSParser.LlamadaFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#argumentosLlamada.
    def visitArgumentosLlamada(self, ctx:Objective_JSParser.ArgumentosLlamadaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#argumentosLlamadaAux.
    def visitArgumentosLlamadaAux(self, ctx:Objective_JSParser.ArgumentosLlamadaAuxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#lectura.
    def visitLectura(self, ctx:Objective_JSParser.LecturaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#lecturaAux.
    def visitLecturaAux(self, ctx:Objective_JSParser.LecturaAuxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#decInc.
    def visitDecInc(self, ctx:Objective_JSParser.DecIncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#decIncAux.
    def visitDecIncAux(self, ctx:Objective_JSParser.DecIncAuxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#objeto.
    def visitObjeto(self, ctx:Objective_JSParser.ObjetoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#objetoAux.
    def visitObjetoAux(self, ctx:Objective_JSParser.ObjetoAuxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#megaExpresion.
    def visitMegaExpresion(self, ctx:Objective_JSParser.MegaExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#megaExpresionAux.
    def visitMegaExpresionAux(self, ctx:Objective_JSParser.MegaExpresionAuxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#superExpresion.
    def visitSuperExpresion(self, ctx:Objective_JSParser.SuperExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#superExpresionOperadores.
    def visitSuperExpresionOperadores(self, ctx:Objective_JSParser.SuperExpresionOperadoresContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#expresion.
    def visitExpresion(self, ctx:Objective_JSParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#expresionOperadores.
    def visitExpresionOperadores(self, ctx:Objective_JSParser.ExpresionOperadoresContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#termino.
    def visitTermino(self, ctx:Objective_JSParser.TerminoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#terminoOperadores.
    def visitTerminoOperadores(self, ctx:Objective_JSParser.TerminoOperadoresContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#factor.
    def visitFactor(self, ctx:Objective_JSParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#factorParentesis.
    def visitFactorParentesis(self, ctx:Objective_JSParser.FactorParentesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#varCte.
    def visitVarCte(self, ctx:Objective_JSParser.VarCteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Objective_JSParser#matrix.
    def visitMatrix(self, ctx:Objective_JSParser.MatrixContext):
        return self.visitChildren(ctx)



del Objective_JSParser