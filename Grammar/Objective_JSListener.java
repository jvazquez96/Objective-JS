// Generated from Objective_JS.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link Objective_JSParser}.
 */
public interface Objective_JSListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#inicio}.
	 * @param ctx the parse tree
	 */
	void enterInicio(Objective_JSParser.InicioContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#inicio}.
	 * @param ctx the parse tree
	 */
	void exitInicio(Objective_JSParser.InicioContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#main}.
	 * @param ctx the parse tree
	 */
	void enterMain(Objective_JSParser.MainContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#main}.
	 * @param ctx the parse tree
	 */
	void exitMain(Objective_JSParser.MainContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#clase}.
	 * @param ctx the parse tree
	 */
	void enterClase(Objective_JSParser.ClaseContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#clase}.
	 * @param ctx the parse tree
	 */
	void exitClase(Objective_JSParser.ClaseContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#imports}.
	 * @param ctx the parse tree
	 */
	void enterImports(Objective_JSParser.ImportsContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#imports}.
	 * @param ctx the parse tree
	 */
	void exitImports(Objective_JSParser.ImportsContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#class_declaration}.
	 * @param ctx the parse tree
	 */
	void enterClass_declaration(Objective_JSParser.Class_declarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#class_declaration}.
	 * @param ctx the parse tree
	 */
	void exitClass_declaration(Objective_JSParser.Class_declarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#bloque}.
	 * @param ctx the parse tree
	 */
	void enterBloque(Objective_JSParser.BloqueContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#bloque}.
	 * @param ctx the parse tree
	 */
	void exitBloque(Objective_JSParser.BloqueContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#preEstatuto}.
	 * @param ctx the parse tree
	 */
	void enterPreEstatuto(Objective_JSParser.PreEstatutoContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#preEstatuto}.
	 * @param ctx the parse tree
	 */
	void exitPreEstatuto(Objective_JSParser.PreEstatutoContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#claseAux}.
	 * @param ctx the parse tree
	 */
	void enterClaseAux(Objective_JSParser.ClaseAuxContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#claseAux}.
	 * @param ctx the parse tree
	 */
	void exitClaseAux(Objective_JSParser.ClaseAuxContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#bloqueClase}.
	 * @param ctx the parse tree
	 */
	void enterBloqueClase(Objective_JSParser.BloqueClaseContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#bloqueClase}.
	 * @param ctx the parse tree
	 */
	void exitBloqueClase(Objective_JSParser.BloqueClaseContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#constructor}.
	 * @param ctx the parse tree
	 */
	void enterConstructor(Objective_JSParser.ConstructorContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#constructor}.
	 * @param ctx the parse tree
	 */
	void exitConstructor(Objective_JSParser.ConstructorContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#constructorAux}.
	 * @param ctx the parse tree
	 */
	void enterConstructorAux(Objective_JSParser.ConstructorAuxContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#constructorAux}.
	 * @param ctx the parse tree
	 */
	void exitConstructorAux(Objective_JSParser.ConstructorAuxContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#constructorAux2}.
	 * @param ctx the parse tree
	 */
	void enterConstructorAux2(Objective_JSParser.ConstructorAux2Context ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#constructorAux2}.
	 * @param ctx the parse tree
	 */
	void exitConstructorAux2(Objective_JSParser.ConstructorAux2Context ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#atributos}.
	 * @param ctx the parse tree
	 */
	void enterAtributos(Objective_JSParser.AtributosContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#atributos}.
	 * @param ctx the parse tree
	 */
	void exitAtributos(Objective_JSParser.AtributosContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#atributosPublic}.
	 * @param ctx the parse tree
	 */
	void enterAtributosPublic(Objective_JSParser.AtributosPublicContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#atributosPublic}.
	 * @param ctx the parse tree
	 */
	void exitAtributosPublic(Objective_JSParser.AtributosPublicContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#atributosPublicAux}.
	 * @param ctx the parse tree
	 */
	void enterAtributosPublicAux(Objective_JSParser.AtributosPublicAuxContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#atributosPublicAux}.
	 * @param ctx the parse tree
	 */
	void exitAtributosPublicAux(Objective_JSParser.AtributosPublicAuxContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#atributosPrivate}.
	 * @param ctx the parse tree
	 */
	void enterAtributosPrivate(Objective_JSParser.AtributosPrivateContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#atributosPrivate}.
	 * @param ctx the parse tree
	 */
	void exitAtributosPrivate(Objective_JSParser.AtributosPrivateContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#atributosPrivateAux}.
	 * @param ctx the parse tree
	 */
	void enterAtributosPrivateAux(Objective_JSParser.AtributosPrivateAuxContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#atributosPrivateAux}.
	 * @param ctx the parse tree
	 */
	void exitAtributosPrivateAux(Objective_JSParser.AtributosPrivateAuxContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#atributosProtected}.
	 * @param ctx the parse tree
	 */
	void enterAtributosProtected(Objective_JSParser.AtributosProtectedContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#atributosProtected}.
	 * @param ctx the parse tree
	 */
	void exitAtributosProtected(Objective_JSParser.AtributosProtectedContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#metodos}.
	 * @param ctx the parse tree
	 */
	void enterMetodos(Objective_JSParser.MetodosContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#metodos}.
	 * @param ctx the parse tree
	 */
	void exitMetodos(Objective_JSParser.MetodosContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#metodosPublicos}.
	 * @param ctx the parse tree
	 */
	void enterMetodosPublicos(Objective_JSParser.MetodosPublicosContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#metodosPublicos}.
	 * @param ctx the parse tree
	 */
	void exitMetodosPublicos(Objective_JSParser.MetodosPublicosContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#metodosPublicosAux}.
	 * @param ctx the parse tree
	 */
	void enterMetodosPublicosAux(Objective_JSParser.MetodosPublicosAuxContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#metodosPublicosAux}.
	 * @param ctx the parse tree
	 */
	void exitMetodosPublicosAux(Objective_JSParser.MetodosPublicosAuxContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#metodosPrivados}.
	 * @param ctx the parse tree
	 */
	void enterMetodosPrivados(Objective_JSParser.MetodosPrivadosContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#metodosPrivados}.
	 * @param ctx the parse tree
	 */
	void exitMetodosPrivados(Objective_JSParser.MetodosPrivadosContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#metodosPrivadosAux}.
	 * @param ctx the parse tree
	 */
	void enterMetodosPrivadosAux(Objective_JSParser.MetodosPrivadosAuxContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#metodosPrivadosAux}.
	 * @param ctx the parse tree
	 */
	void exitMetodosPrivadosAux(Objective_JSParser.MetodosPrivadosAuxContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#func}.
	 * @param ctx the parse tree
	 */
	void enterFunc(Objective_JSParser.FuncContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#func}.
	 * @param ctx the parse tree
	 */
	void exitFunc(Objective_JSParser.FuncContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#funcAux}.
	 * @param ctx the parse tree
	 */
	void enterFuncAux(Objective_JSParser.FuncAuxContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#funcAux}.
	 * @param ctx the parse tree
	 */
	void exitFuncAux(Objective_JSParser.FuncAuxContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#impConstructores}.
	 * @param ctx the parse tree
	 */
	void enterImpConstructores(Objective_JSParser.ImpConstructoresContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#impConstructores}.
	 * @param ctx the parse tree
	 */
	void exitImpConstructores(Objective_JSParser.ImpConstructoresContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#impConstructoresMultiples}.
	 * @param ctx the parse tree
	 */
	void enterImpConstructoresMultiples(Objective_JSParser.ImpConstructoresMultiplesContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#impConstructoresMultiples}.
	 * @param ctx the parse tree
	 */
	void exitImpConstructoresMultiples(Objective_JSParser.ImpConstructoresMultiplesContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#impConstructor}.
	 * @param ctx the parse tree
	 */
	void enterImpConstructor(Objective_JSParser.ImpConstructorContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#impConstructor}.
	 * @param ctx the parse tree
	 */
	void exitImpConstructor(Objective_JSParser.ImpConstructorContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#impFunc}.
	 * @param ctx the parse tree
	 */
	void enterImpFunc(Objective_JSParser.ImpFuncContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#impFunc}.
	 * @param ctx the parse tree
	 */
	void exitImpFunc(Objective_JSParser.ImpFuncContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#impFuncAux2}.
	 * @param ctx the parse tree
	 */
	void enterImpFuncAux2(Objective_JSParser.ImpFuncAux2Context ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#impFuncAux2}.
	 * @param ctx the parse tree
	 */
	void exitImpFuncAux2(Objective_JSParser.ImpFuncAux2Context ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#argumentos}.
	 * @param ctx the parse tree
	 */
	void enterArgumentos(Objective_JSParser.ArgumentosContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#argumentos}.
	 * @param ctx the parse tree
	 */
	void exitArgumentos(Objective_JSParser.ArgumentosContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#argumentosAux}.
	 * @param ctx the parse tree
	 */
	void enterArgumentosAux(Objective_JSParser.ArgumentosAuxContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#argumentosAux}.
	 * @param ctx the parse tree
	 */
	void exitArgumentosAux(Objective_JSParser.ArgumentosAuxContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#bloqueConstructor}.
	 * @param ctx the parse tree
	 */
	void enterBloqueConstructor(Objective_JSParser.BloqueConstructorContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#bloqueConstructor}.
	 * @param ctx the parse tree
	 */
	void exitBloqueConstructor(Objective_JSParser.BloqueConstructorContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#bloqueFunc}.
	 * @param ctx the parse tree
	 */
	void enterBloqueFunc(Objective_JSParser.BloqueFuncContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#bloqueFunc}.
	 * @param ctx the parse tree
	 */
	void exitBloqueFunc(Objective_JSParser.BloqueFuncContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#bloqueFuncAux}.
	 * @param ctx the parse tree
	 */
	void enterBloqueFuncAux(Objective_JSParser.BloqueFuncAuxContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#bloqueFuncAux}.
	 * @param ctx the parse tree
	 */
	void exitBloqueFuncAux(Objective_JSParser.BloqueFuncAuxContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#bloqueFuncAux2}.
	 * @param ctx the parse tree
	 */
	void enterBloqueFuncAux2(Objective_JSParser.BloqueFuncAux2Context ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#bloqueFuncAux2}.
	 * @param ctx the parse tree
	 */
	void exitBloqueFuncAux2(Objective_JSParser.BloqueFuncAux2Context ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#preVars}.
	 * @param ctx the parse tree
	 */
	void enterPreVars(Objective_JSParser.PreVarsContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#preVars}.
	 * @param ctx the parse tree
	 */
	void exitPreVars(Objective_JSParser.PreVarsContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#vars_}.
	 * @param ctx the parse tree
	 */
	void enterVars_(Objective_JSParser.Vars_Context ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#vars_}.
	 * @param ctx the parse tree
	 */
	void exitVars_(Objective_JSParser.Vars_Context ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#varsAux}.
	 * @param ctx the parse tree
	 */
	void enterVarsAux(Objective_JSParser.VarsAuxContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#varsAux}.
	 * @param ctx the parse tree
	 */
	void exitVarsAux(Objective_JSParser.VarsAuxContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#varsRepeated}.
	 * @param ctx the parse tree
	 */
	void enterVarsRepeated(Objective_JSParser.VarsRepeatedContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#varsRepeated}.
	 * @param ctx the parse tree
	 */
	void exitVarsRepeated(Objective_JSParser.VarsRepeatedContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#tipo_dato}.
	 * @param ctx the parse tree
	 */
	void enterTipo_dato(Objective_JSParser.Tipo_datoContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#tipo_dato}.
	 * @param ctx the parse tree
	 */
	void exitTipo_dato(Objective_JSParser.Tipo_datoContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#tipo_dato_list}.
	 * @param ctx the parse tree
	 */
	void enterTipo_dato_list(Objective_JSParser.Tipo_dato_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#tipo_dato_list}.
	 * @param ctx the parse tree
	 */
	void exitTipo_dato_list(Objective_JSParser.Tipo_dato_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#dim}.
	 * @param ctx the parse tree
	 */
	void enterDim(Objective_JSParser.DimContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#dim}.
	 * @param ctx the parse tree
	 */
	void exitDim(Objective_JSParser.DimContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#dimMatrix}.
	 * @param ctx the parse tree
	 */
	void enterDimMatrix(Objective_JSParser.DimMatrixContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#dimMatrix}.
	 * @param ctx the parse tree
	 */
	void exitDimMatrix(Objective_JSParser.DimMatrixContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#tipo_dato_no_list}.
	 * @param ctx the parse tree
	 */
	void enterTipo_dato_no_list(Objective_JSParser.Tipo_dato_no_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#tipo_dato_no_list}.
	 * @param ctx the parse tree
	 */
	void exitTipo_dato_no_list(Objective_JSParser.Tipo_dato_no_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#tipo}.
	 * @param ctx the parse tree
	 */
	void enterTipo(Objective_JSParser.TipoContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#tipo}.
	 * @param ctx the parse tree
	 */
	void exitTipo(Objective_JSParser.TipoContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#estatuto}.
	 * @param ctx the parse tree
	 */
	void enterEstatuto(Objective_JSParser.EstatutoContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#estatuto}.
	 * @param ctx the parse tree
	 */
	void exitEstatuto(Objective_JSParser.EstatutoContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#asignacion}.
	 * @param ctx the parse tree
	 */
	void enterAsignacion(Objective_JSParser.AsignacionContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#asignacion}.
	 * @param ctx the parse tree
	 */
	void exitAsignacion(Objective_JSParser.AsignacionContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#condicion}.
	 * @param ctx the parse tree
	 */
	void enterCondicion(Objective_JSParser.CondicionContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#condicion}.
	 * @param ctx the parse tree
	 */
	void exitCondicion(Objective_JSParser.CondicionContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#condicionAux}.
	 * @param ctx the parse tree
	 */
	void enterCondicionAux(Objective_JSParser.CondicionAuxContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#condicionAux}.
	 * @param ctx the parse tree
	 */
	void exitCondicionAux(Objective_JSParser.CondicionAuxContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#condicionChoice}.
	 * @param ctx the parse tree
	 */
	void enterCondicionChoice(Objective_JSParser.CondicionChoiceContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#condicionChoice}.
	 * @param ctx the parse tree
	 */
	void exitCondicionChoice(Objective_JSParser.CondicionChoiceContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#escritura}.
	 * @param ctx the parse tree
	 */
	void enterEscritura(Objective_JSParser.EscrituraContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#escritura}.
	 * @param ctx the parse tree
	 */
	void exitEscritura(Objective_JSParser.EscrituraContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#escrituraAux}.
	 * @param ctx the parse tree
	 */
	void enterEscrituraAux(Objective_JSParser.EscrituraAuxContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#escrituraAux}.
	 * @param ctx the parse tree
	 */
	void exitEscrituraAux(Objective_JSParser.EscrituraAuxContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#ciclos}.
	 * @param ctx the parse tree
	 */
	void enterCiclos(Objective_JSParser.CiclosContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#ciclos}.
	 * @param ctx the parse tree
	 */
	void exitCiclos(Objective_JSParser.CiclosContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#doAux}.
	 * @param ctx the parse tree
	 */
	void enterDoAux(Objective_JSParser.DoAuxContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#doAux}.
	 * @param ctx the parse tree
	 */
	void exitDoAux(Objective_JSParser.DoAuxContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#llamadaFunc}.
	 * @param ctx the parse tree
	 */
	void enterLlamadaFunc(Objective_JSParser.LlamadaFuncContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#llamadaFunc}.
	 * @param ctx the parse tree
	 */
	void exitLlamadaFunc(Objective_JSParser.LlamadaFuncContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#argumentosLlamada}.
	 * @param ctx the parse tree
	 */
	void enterArgumentosLlamada(Objective_JSParser.ArgumentosLlamadaContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#argumentosLlamada}.
	 * @param ctx the parse tree
	 */
	void exitArgumentosLlamada(Objective_JSParser.ArgumentosLlamadaContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#argumentosLlamadaAux}.
	 * @param ctx the parse tree
	 */
	void enterArgumentosLlamadaAux(Objective_JSParser.ArgumentosLlamadaAuxContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#argumentosLlamadaAux}.
	 * @param ctx the parse tree
	 */
	void exitArgumentosLlamadaAux(Objective_JSParser.ArgumentosLlamadaAuxContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#lectura}.
	 * @param ctx the parse tree
	 */
	void enterLectura(Objective_JSParser.LecturaContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#lectura}.
	 * @param ctx the parse tree
	 */
	void exitLectura(Objective_JSParser.LecturaContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#lecturaAux}.
	 * @param ctx the parse tree
	 */
	void enterLecturaAux(Objective_JSParser.LecturaAuxContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#lecturaAux}.
	 * @param ctx the parse tree
	 */
	void exitLecturaAux(Objective_JSParser.LecturaAuxContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#objeto}.
	 * @param ctx the parse tree
	 */
	void enterObjeto(Objective_JSParser.ObjetoContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#objeto}.
	 * @param ctx the parse tree
	 */
	void exitObjeto(Objective_JSParser.ObjetoContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#objetoAux}.
	 * @param ctx the parse tree
	 */
	void enterObjetoAux(Objective_JSParser.ObjetoAuxContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#objetoAux}.
	 * @param ctx the parse tree
	 */
	void exitObjetoAux(Objective_JSParser.ObjetoAuxContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#megaExpresion}.
	 * @param ctx the parse tree
	 */
	void enterMegaExpresion(Objective_JSParser.MegaExpresionContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#megaExpresion}.
	 * @param ctx the parse tree
	 */
	void exitMegaExpresion(Objective_JSParser.MegaExpresionContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#megaExpresionAux}.
	 * @param ctx the parse tree
	 */
	void enterMegaExpresionAux(Objective_JSParser.MegaExpresionAuxContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#megaExpresionAux}.
	 * @param ctx the parse tree
	 */
	void exitMegaExpresionAux(Objective_JSParser.MegaExpresionAuxContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#superExpresion}.
	 * @param ctx the parse tree
	 */
	void enterSuperExpresion(Objective_JSParser.SuperExpresionContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#superExpresion}.
	 * @param ctx the parse tree
	 */
	void exitSuperExpresion(Objective_JSParser.SuperExpresionContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#superExpresionOperadores}.
	 * @param ctx the parse tree
	 */
	void enterSuperExpresionOperadores(Objective_JSParser.SuperExpresionOperadoresContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#superExpresionOperadores}.
	 * @param ctx the parse tree
	 */
	void exitSuperExpresionOperadores(Objective_JSParser.SuperExpresionOperadoresContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterExpresion(Objective_JSParser.ExpresionContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitExpresion(Objective_JSParser.ExpresionContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#expresionOperadores}.
	 * @param ctx the parse tree
	 */
	void enterExpresionOperadores(Objective_JSParser.ExpresionOperadoresContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#expresionOperadores}.
	 * @param ctx the parse tree
	 */
	void exitExpresionOperadores(Objective_JSParser.ExpresionOperadoresContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#termino}.
	 * @param ctx the parse tree
	 */
	void enterTermino(Objective_JSParser.TerminoContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#termino}.
	 * @param ctx the parse tree
	 */
	void exitTermino(Objective_JSParser.TerminoContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#terminoOperadores}.
	 * @param ctx the parse tree
	 */
	void enterTerminoOperadores(Objective_JSParser.TerminoOperadoresContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#terminoOperadores}.
	 * @param ctx the parse tree
	 */
	void exitTerminoOperadores(Objective_JSParser.TerminoOperadoresContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFactor(Objective_JSParser.FactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFactor(Objective_JSParser.FactorContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#factorParentesis}.
	 * @param ctx the parse tree
	 */
	void enterFactorParentesis(Objective_JSParser.FactorParentesisContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#factorParentesis}.
	 * @param ctx the parse tree
	 */
	void exitFactorParentesis(Objective_JSParser.FactorParentesisContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#varCte}.
	 * @param ctx the parse tree
	 */
	void enterVarCte(Objective_JSParser.VarCteContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#varCte}.
	 * @param ctx the parse tree
	 */
	void exitVarCte(Objective_JSParser.VarCteContext ctx);
	/**
	 * Enter a parse tree produced by {@link Objective_JSParser#matrix}.
	 * @param ctx the parse tree
	 */
	void enterMatrix(Objective_JSParser.MatrixContext ctx);
	/**
	 * Exit a parse tree produced by {@link Objective_JSParser#matrix}.
	 * @param ctx the parse tree
	 */
	void exitMatrix(Objective_JSParser.MatrixContext ctx);
}