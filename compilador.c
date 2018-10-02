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
    struct FUNCION *funcion;
};

struct BODY{
    struct LISTA_PRODUCTOS *produccion;
};


struct FUNCION{
    struct LISTA_PRODUCTOS *produccion;
    struct BODY *body;
    
};

struct ARBOL{
    struct PROGRAMA *programa;
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

   
    
    struct TOKEN *iterador = lista->head;               //Identificamos los tokens
    while (iterador != NULL){
       if (!(iterador->type))
            if (strcmp(iterador->value, "int")==0)
                iterador->type = "keyword";
            else
                if (strcmp(iterador->value, "return")==0)
                    iterador->type = "keyword";
                else
                    if(isdigit(iterador->value[0]))
                        iterador->type="integer";
                    else
                        iterador->type ="identifier";
        
        iterador = iterador->next;
    }

  //  imprimeTokens(lista);
    
    
/******************************************************************************************************************/    
/****************************************************** 
 *
 * 
 * PARTE 3: parser   */
    


    struct ARBOL *ast = (struct ARBOL *)calloc(1,sizeof(struct ARBOL));
    ast->programa = (struct PROGRAMA *)calloc(1,sizeof(struct PROGRAMA));
    ast->programa->funcion = (struct FUNCION *)calloc(1,sizeof(struct FUNCION));
    ast->programa->funcion->produccion = (struct LISTA_PRODUCTOS *)calloc(1,sizeof(struct LISTA_PRODUCTOS));
    ast->programa->funcion->produccion->head = (struct PRODUCTO *)calloc(1,sizeof(struct PRODUCTO));
    struct PRODUCTO *indicador = ast->programa->funcion->produccion->head;
    
    indicador->type = "keyword";                //int
    indicador->terminal = 1;
    indicador->next = (struct PRODUCTO *)calloc(1,sizeof(struct PRODUCTO));
    indicador = indicador->next;
    
    indicador->type = "identifier";                //main
    indicador->terminal = 1;
    indicador->next = (struct PRODUCTO *)calloc(1,sizeof(struct PRODUCTO));
    indicador = indicador->next;
    
    indicador->type = "LeftPar";                //(
    indicador->terminal = 1;
    indicador->next = (struct PRODUCTO *)calloc(1,sizeof(struct PRODUCTO));
    indicador = indicador->next;
    
    indicador->type = "RightPar";                //)
    indicador->terminal = 1;
    indicador->next = (struct PRODUCTO *)calloc(1,sizeof(struct PRODUCTO));
    indicador = indicador->next;
    
    indicador->type = "LeftKey";                //{
    indicador->terminal = 1;
    indicador->next = (struct PRODUCTO *)calloc(1,sizeof(struct PRODUCTO));
    indicador = indicador->next;

    
    indicador->type = "keyword";                //return
    indicador->terminal = 1;
    indicador->next = (struct PRODUCTO *)calloc(1,sizeof(struct PRODUCTO));
    indicador = indicador->next;
    
    indicador->type = "integer";                //2
    indicador->terminal = 1;
    indicador->next = (struct PRODUCTO *)calloc(1,sizeof(struct PRODUCTO));
    indicador = indicador->next;
    
    
    indicador->type = "Colon";                //;
    indicador->terminal = 1;
    indicador->next = (struct PRODUCTO *)calloc(1,sizeof(struct PRODUCTO));
    indicador = indicador->next;
    
    indicador->type = "RightKey";                //}
    indicador->terminal = 1;
    indicador->next = NULL;
    
    
    //regresamos indicador al inicio
    iterador = lista->head;                                   //LISTA DE TOKENS
    indicador = ast->programa->funcion->produccion->head;      //PRODUCCIONES DE FUNCION
    
    int k = 0;
    while (iterador!=NULL){
        //printf("Evaluando %s contra %s",iterador->type, indicador->type );
        if (strcmp(iterador->type, indicador->type)==0){
            k +=1;
        }
        
        iterador = iterador->next;
        indicador = indicador->next;
    }
    
//     if (k=9)
//         printf("parseo exitoso\n");
    
    
/*    
    indicador = ast->programa->funcion->produccion->head;
    while (indicador){
        printf("%s\n",indicador->type);
        indicador = indicador->next;
    }
    */
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    return 1;
}
