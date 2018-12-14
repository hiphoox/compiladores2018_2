//Autor: Alejandro Rivera Nagano
#include "Lexer.c"
#include "Parser.c"




int main(){
 //******************************************************PARTE 0: Definir gramática   
    
    //************************************************************  FUNCION
    nPRODUCTO *pFuncion = (nPRODUCTO *)calloc(1,sizeof(nPRODUCTO));
    nPRODUCTO *cursor = pFuncion;

    pFuncion->v_simbolo = 1;
    pFuncion->simbolo = "keyword";
    
    
    cursor->next = (nPRODUCTO *)calloc(1,sizeof(nPRODUCTO));
    cursor = cursor->next;
    cursor->v_simbolo = 1;
    cursor->simbolo = "identifier";
    
    
    cursor->next = (nPRODUCTO *)calloc(1,sizeof(nPRODUCTO));
    cursor = cursor->next;
    cursor->v_simbolo = 1;
    cursor->simbolo = "leftPar";
    
    cursor->next = (nPRODUCTO *)calloc(1,sizeof(nPRODUCTO));
    cursor = cursor->next;
    cursor->v_simbolo = 1;
    cursor->simbolo = "rightPar";
    
    
    cursor->next = (nPRODUCTO *)calloc(1,sizeof(nPRODUCTO));
    cursor = cursor->next;
    cursor->v_simbolo = 1;
    cursor->simbolo = "leftKey";
    
    
    cursor->next = (nPRODUCTO *)calloc(1,sizeof(nPRODUCTO));
    cursor = cursor->next;
    cursor->v_noTerminal = 1;
    cursor->noTerminal = (nPRODUCTO *)calloc(1,sizeof(nPRODUCTO));
    nPRODUCTO *pStatement = cursor->noTerminal;
    
    
    cursor->next = (nPRODUCTO *)calloc(1,sizeof(nPRODUCTO));
    cursor = cursor->next;
    cursor->v_simbolo = 1;
    cursor->simbolo = "rightKey";
    
        
    printf("Lista de producción de FUNCION:\n");
    imprimeProducciones(pFuncion);
    
    //************************************************************  STATEMENT
    cursor = pStatement;
    cursor->v_simbolo = 1;
    cursor->simbolo = "keyword";
    
    cursor->next = (nPRODUCTO *)calloc(1,sizeof(nPRODUCTO));
    cursor = cursor->next;
    cursor->v_noTerminal = 1;
    cursor->noTerminal = (nPRODUCTO *)calloc(1,sizeof(nPRODUCTO));
    nPRODUCTO *pExpresion = cursor->noTerminal;
    
    cursor->next = (nPRODUCTO *)calloc(1,sizeof(nPRODUCTO));
    cursor = cursor->next;
    cursor->v_simbolo = 1;
    cursor->simbolo = "colon";
    
    
    printf("Lista de producción de STATEMENT:\n");
    imprimeProducciones(pStatement);
    
    //************************************************************  EXPRESION
    
    cursor = pExpresion;
    cursor->v_simbolo = 1;
    cursor->simbolo = "integer";
    
    printf("Lista de producción de EXPRESION:\n");
    imprimeProducciones(pExpresion);
    
    
    
    
    
    

    
/**********************************************************************************************************************/
/******************************************************* PARTE 0.5: abrir archivo y guardar el contenido en una cadena */
    FILE *archivo = fopen("return2.c","r");
    int numbytes;
    char *bufer;
    

    if (archivo == NULL){
        printf("No se encontró archivo\n");
        return 0;
    }
    fseek(archivo, 0, SEEK_END);                        
    numbytes = ftell(archivo);                          //obtiene el numero de caracteres del archivo
    fseek(archivo, 0, SEEK_SET);                        //regresa el file pointer al principio del archivo
    bufer = (char *)calloc(numbytes, sizeof(char));     //reserva espacio para guardar todo el archivo en una cadena
    if (bufer == NULL){
        printf("No se reservó espacio correctamente\n");
        return 0;
    }
    fread(bufer, sizeof(char), numbytes, archivo);      //guarda el archivo en una cadena
    fclose(archivo);
 

    
    
    
    
    
 /****************************************************** PARTE 1: lexer   */
    LISTA_TOKENS *lista;
    lista = (LISTA_TOKENS *)calloc(1,sizeof(LISTA_TOKENS));
    lista->head = NULL;
    lista->tail= NULL;
    
    lexea(bufer, lista);
        
    identificaTokens(lista->head);

    imprimeTokens(lista);
    
    
    
    
/******************************************************************************************************************/    
/****************************************************** 
 *
 * 
 * PARTE 2: parser   */
    
    ARBOL* ast = (ARBOL *)calloc(1,sizeof(ARBOL));
    union pARBOL *p = (union pARBOL*)calloc(1,sizeof(union pARBOL));
    
    p->pa = ast;
    p->pp = p->pa->hijo = (PROGRAMA*)calloc(1,sizeof(PROGRAMA));

    p->pf = p->pp->hijo = (FUNCION*)calloc(1,sizeof(FUNCION));
    
    
    
    int a = 0;
    imprimeTokens(lista);
    parsea(lista->head, pFuncion, p, a);
    
    
   
    return 1;
}
