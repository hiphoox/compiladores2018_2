//Autor: Alejandro Rivera Nagano
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

struct TOKEN{
    char *type;
    char *value;
    struct TOKEN *next;
};

struct PRODUCTO{
    char *type;
    int terminal;
    struct PRODUCTO *next;
};

struct LISTA_PRODUCTOS{
    struct PRODUCTO *head;
    struct PRODUCTO *tail;
};

struct PROGRAMA{
    struct FUNCION *hijo;
    struct ARBOL *padre;
};

struct EXPRESION{
    struct FUNCION *padre;
    struct LISTA_PRODUCTOS *produccion;
};


struct FUNCION{
    struct LISTA_PRODUCTOS *produccion;
    struct EXPRESION *hijo;
    struct PROGRAMA *padre;
    struct LISTA_TOKENS *contenido;
    
};

struct ARBOL{
    struct PROGRAMA *hijo;
};

struct LISTA_TOKENS{
    struct TOKEN *head;
    struct TOKEN *tail;
};

struct ARBOL * iniciaArbol(){
    
};

void agregaToken(struct LISTA_TOKENS *lista, char *value, char *type){
   if(lista->head != NULL){
       lista->tail->next = (struct TOKEN *)calloc(1,sizeof(struct TOKEN));
       lista->tail = lista->tail->next;
       lista->tail->next = NULL;
       lista->tail->value = value;
       lista->tail->type = type;
       
    }
    else{
        lista->head = (struct TOKEN *)calloc(1,sizeof(struct TOKEN));
        lista->tail = lista->head;
        lista->tail->next = NULL;
        lista->head->value = value;
        lista->tail->type = type;
    }
}


void imprimeTokens(struct LISTA_TOKENS *lista){
    struct TOKEN *token = (struct TOKEN *)calloc(1,sizeof(struct TOKEN));
    token = lista->head;
    while(token != NULL){
        printf("%s, %s\n",token->value, token->type);
        token = token->next;
    }
}


int main(){
/**********************************************************************************************************************/
/******************************************************* PARTE 1: abrir archivo y guardar el contenido en una cadena */
    FILE *archivo = fopen("return2.c","r");
    int numbytes;
    char *bufer;
    

    if (archivo == NULL){                               //intenta abrir el archivo
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
 
/**********************************************************************************************************************/
 /****************************************************** PARTE 2: lexer   */


    struct LISTA_TOKENS *lista;
    lista = (struct LISTA_TOKENS *)calloc(1,sizeof(struct LISTA_TOKENS));
    
    lista->head = NULL;
    lista->tail= NULL;
    printf("EXITO\n");
    char *delimitadores = " ();[]{}\n";
    int j, limite;
    char *resto, *valor;
    resto = bufer;

    /************************************************************************************************   */
    while(*resto){                                           //mientras queden caracteres por escanear
        limite = strcspn(resto, delimitadores);                        //calculamos cuanto mide el sig. token

        if(limite == 0){                                    //si tenemos que hacer single token ()[]{};* etc
            valor = (char *)calloc(1,sizeof(char));
        }
        else{
           valor = (char *)calloc(limite, sizeof(char));    //si el token es mas largo que un caracter(id, keyword...)

        }   
      
        switch(resto[limite]){                              //segun el caracter leido:
            /*-------------------------------               ignoramos espacios y enters */
            case ' ':
                if(limite > 0){                             //solo si ya ibamos a medio token, lo terminamos
                    for(j=0;j<limite;j++){                  
                        valor[j] = resto[j];                //lo agregamos a la lista
                    }
                    agregaToken(lista, valor,NULL);
                }   
                resto  = resto + limite + 1;
            break;
                
            case '\n':                                      //enters- mismo caso que espacios
                if(limite > 0){
                    for(j=0;j<limite;j++){                  
                        valor[j] = resto[j];
                    }
                   agregaToken(lista, valor, NULL);
                }   
                resto  = resto + limite + 1;
            break;
              
            /*----------------------------              single tokens: delimitadores que no ignoramos */
            case '(':                                   //dos casos posibles
                if(limite > 0){                         // a) ya ibamos a medio token
                    for(j=0;j<limite;j++){                  //lo terminamos y lo guardamos
                        valor[j] = resto[j];
                    }
                    agregaToken(lista, valor,NULL);
                    resto = resto + limite ;
                }
                valor = "(";                            //no tenemos token a medias:
                agregaToken(lista, valor,"LeftPar");                  //agregamos token sencillo
                resto ++;
            break;
                
            case ')':
                if(limite > 0){
                    for(j=0;j<limite;j++){             //mismo caso (single token)
                        valor[j] = resto[j];
                    }
                   agregaToken(lista, valor,NULL);
                    resto = resto + limite ;
                }
                valor = ")";
                agregaToken(lista, valor,"RightPar");
                resto ++;
            break;
            
            
            case '{':
                if(limite > 0){
                    for(j=0;j<limite;j++){                  //single token
                        valor[j] = resto[j];
                    }
                    agregaToken(lista, valor,NULL);
                    resto = resto + limite ;
                }
                valor = "{";
                agregaToken(lista, valor,"LeftKey");
                resto ++;
            break;
                
            case '}':
                if(limite > 0){
                    for(j=0;j<limite;j++){                  //hsingle token
                        valor[j] = resto[j];
                    }
                    agregaToken(lista, valor,NULL);
                    resto = resto + limite ;
                }
                valor = "}";
                agregaToken(lista, valor,"RightKey");
                resto ++;
            break;
            
            case ';':
                 if(limite > 0){
                    for(j=0;j<limite;j++){                  //single token
                        valor[j] = resto[j];
                    }
                    agregaToken(lista, valor,NULL);
                    resto = resto + limite ;
                }
                valor = ";";
                agregaToken(lista, valor,"Colon");
                resto ++;
            break;               
            
            default:
            break;
        }
    };

   
    
    struct TOKEN *tok = lista->head;               //Identificamos los tokens
    while (tok != NULL){
       if (!(tok->type))
            if (strcmp(tok->value, "int")==0)
                tok->type = "keyword";
            else
                if (strcmp(tok->value, "return")==0)
                    tok->type = "keyword";
                else
                    if(isdigit(tok->value[0]))
                        tok->type="integer";
                    else                                //falta rechazar caracteres prohibidos
                        tok->type ="identifier";
        
        tok = tok->next;
    }

    printf("Tokens:\n");
    imprimeTokens(lista);
    
    
/******************************************************************************************************************/    
/****************************************************** 
 *
 * 
 * PARTE 3: parser   */
    


    struct ARBOL *ast = (struct ARBOL *)calloc(1,sizeof(struct ARBOL));
    ast->hijo = (struct PROGRAMA *)calloc(1,sizeof(struct PROGRAMA));
    ast->hijo->padre = ast; //el padre de PROGRAMA es ARBOL
    
    ast->hijo->hijo = (struct FUNCION *)calloc(1,sizeof(struct FUNCION));
    ast->hijo->hijo->padre = ast->hijo; //el padre de FUNCION es PROGRAMA
    
    ast->hijo->hijo->produccion = (struct LISTA_PRODUCTOS *)calloc(1,sizeof(struct LISTA_PRODUCTOS));
    ast->hijo->hijo->produccion->head = (struct PRODUCTO *)calloc(1,sizeof(struct PRODUCTO));
    
    struct PRODUCTO *prod = ast->hijo->hijo->produccion->head;     //variable que nos permitira asignarle las reglas de produccion  a FUNCION
    
    prod->type = "keyword";                //int
    prod->terminal = 1;
    prod->next = (struct PRODUCTO *)calloc(1,sizeof(struct PRODUCTO));
    prod = prod->next;
    
    prod->type = "identifier";                //main
    prod->terminal = 1;
    prod->next = (struct PRODUCTO *)calloc(1,sizeof(struct PRODUCTO));
    prod = prod->next;
    
    prod->type = "LeftPar";                //(
    prod->terminal = 1;
    prod->next = (struct PRODUCTO *)calloc(1,sizeof(struct PRODUCTO));
    prod = prod->next;
    
    prod->type = "RightPar";                //)
    prod->terminal = 1;
    prod->next = (struct PRODUCTO *)calloc(1,sizeof(struct PRODUCTO));
    prod = prod->next;
    
    prod->type = "LeftKey";                //{
    prod->terminal = 1;
    prod->next = (struct PRODUCTO *)calloc(1,sizeof(struct PRODUCTO));
    prod = prod->next;

    prod->type = "EXPRESION";                //return 2;
    prod->terminal = 0;
    prod->next = (struct PRODUCTO *)calloc(1,sizeof(struct PRODUCTO));
    prod = prod->next;
    
    prod->type = "RightKey";                //}
    prod->terminal = 1;
    prod->next = NULL;
    
    
    
    
    
    ast->hijo->hijo->hijo=(struct EXPRESION *)calloc(1,sizeof(struct EXPRESION));                 //creamos EXPRESION y su lista de produccion
    ast->hijo->hijo->hijo->padre = ast->hijo->hijo;
    
    ast->hijo->hijo->hijo->produccion = (struct LISTA_PRODUCTOS *)calloc(1,sizeof(struct LISTA_PRODUCTOS));
    ast->hijo->hijo->hijo->produccion->head = (struct PRODUCTO *)calloc(1,sizeof(struct PRODUCTO));
    
    prod = ast->hijo->hijo->hijo->produccion->head; 
    prod->type = "keyword";                //int
    prod->terminal = 1;
    prod->next = (struct PRODUCTO *)calloc(1,sizeof(struct PRODUCTO));
    prod = prod->next;
    
    prod->type = "integer";                //main
    prod->terminal = 1;
    prod->next = (struct PRODUCTO *)calloc(1,sizeof(struct PRODUCTO));
    prod = prod->next;
    
    prod->type = "Colon";                //(
    prod->terminal = 1;
    prod->next = (struct PRODUCTO *)calloc(1,sizeof(struct PRODUCTO));
    prod = prod->next;
    
    
    //AHORA comparemos nuestra lista de tokens con las reglas de produccion de FUNCION:
    //regresamos prod al inicio
    tok = lista->head;                                   //LISTA DE TOKENS
    prod = ast->hijo->hijo->produccion->head;      //PRODUCCIONES DE FUNCION
    
    int i, k = 0;
    while (tok!=lista->tail){
        printf("Evaluando %s contra %s: ",tok->type, prod->type );
        if (strcmp(tok->type, prod->type)==0){
            //agregaToken(ast->hijo->hijo->contenido,tok->value,tok->type);
            printf("coinciden\n");
        }
        else{
            if (!prod->terminal){
                printf("no coinciden, creando hijo\n");
                prod = ast->hijo->hijo->hijo->produccion->head;
                if (strcmp(tok->type, prod->type)!=0){    //
                    printf("ERROR DE PARSEO\n");
                    exit(0);
                }
                else{
                    printf("coinciden\n");
                }
            }
            

        }
                  
        tok = tok->next;
        prod = prod->next;
      
    }

    
   
    return 1;
}
