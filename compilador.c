//Autor: Alejandro Rivera Nagano
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct TOKEN{
    char *name;
    char *value;
    struct TOKEN *next;
};

struct LISTA_TOKENS{
    struct TOKEN *head;
    struct TOKEN *tail;
};

void agregaToken(struct LISTA_TOKENS *lista, char *value){
   if(lista->head != NULL){
       lista->tail->next = (struct TOKEN *)calloc(1,sizeof(struct TOKEN));
       lista->tail = lista->tail->next;
       lista->tail->next = NULL;
       lista->tail->value = value;
    }
    else{
        lista->head = (struct TOKEN *)calloc(1,sizeof(struct TOKEN));
        lista->tail = lista->head;
        lista->tail->next = NULL;
        lista->head->value = value;
    }
}


void imprimeTokens(struct LISTA_TOKENS *lista){
    struct TOKEN *token = (struct TOKEN *)calloc(1,sizeof(struct TOKEN));
    token = lista->head;
    while(token != NULL){
        printf("%s\n",token->value);
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
 /****************************************************** PARTE 2: tokenizer   */


    struct LISTA_TOKENS *lista;
    lista = (struct LISTA_TOKENS *)calloc(1,sizeof(struct LISTA_TOKENS));
    
    lista->head = NULL;
    lista->tail= NULL;
    char *delimitadores = " ();[]{}\n";
    int j, limite;
    char *resto, *valor;
    resto = bufer;

    /****************************************************** todo este while se puede optimizar aun   */
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
                    agregaToken(lista, valor);
                }   
                resto  = resto + limite + 1;
            break;
                
            case '\n':                                      //enters- mismo caso que espacios
                if(limite > 0){
                    for(j=0;j<limite;j++){                  
                        valor[j] = resto[j];
                    }
                   agregaToken(lista, valor);
                }   
                resto  = resto + limite + 1;
            break;
              
            
            
            
            
            
            /*----------------------------              single tokens: delimitadores que no ignoramos */
            case '(':                                   //dos casos posibles
                if(limite > 0){                         // a) ya ibamos a medio token
                    for(j=0;j<limite;j++){                  //lo terminamos y lo guardamos
                        valor[j] = resto[j];
                    }
                    agregaToken(lista, valor);
                    resto = resto + limite ;
                }
                valor = "(";                            //no tenemos token a medias:
                agregaToken(lista, valor);                  //agregamos token sencillo
                resto ++;
            break;
                
            case ')':
                if(limite > 0){
                    for(j=0;j<limite;j++){             //mismo caso (single token)
                        valor[j] = resto[j];
                    }
                   agregaToken(lista, valor);
                    resto = resto + limite ;
                }
                valor = ")";
                agregaToken(lista, valor);
                resto ++;
            break;
                
            case '[':
                if(limite > 0){
                    for(j=0;j<limite;j++){                  //single token
                        valor[j] = resto[j];
                    }
                    agregaToken(lista, valor);
                    resto = resto + limite ;
                }
                valor = "[";
               agregaToken(lista, valor);
                resto ++;
            break;
                
            case ']':
                if(limite > 0){
                    for(j=0;j<limite;j++){                  //single token
                        valor[j] = resto[j];
                    }
                    agregaToken(lista, valor);;
                    resto = resto + limite ;
                }
                valor = "]";
                agregaToken(lista, valor);
                resto ++;
            break;
                
            
            case '{':
                if(limite > 0){
                    for(j=0;j<limite;j++){                  //single token
                        valor[j] = resto[j];
                    }
                    agregaToken(lista, valor);
                    resto = resto + limite ;
                }
                valor = "{";
                agregaToken(lista, valor);
                resto ++;
            break;
                
            case '}':
                if(limite > 0){
                    for(j=0;j<limite;j++){                  //hsingle token
                        valor[j] = resto[j];
                    }
                    agregaToken(lista, valor);
                    resto = resto + limite ;
                }
                valor = "}";
                agregaToken(lista, valor);
                resto ++;
            break;
            
            case ';':
                 if(limite > 0){
                    for(j=0;j<limite;j++){                  //single token
                        valor[j] = resto[j];
                    }
                    agregaToken(lista, valor);
                    resto = resto + limite ;
                }
                valor = ";";
                agregaToken(lista, valor);
                resto ++;
            break;               
            
            default:
            break;
                
        
        }
        
       
    };

   
    
    
    imprimeTokens(lista);
/******************************************************************************************************************/    
/******************************************************************************************************************/
/****************************************************** PARTE 3: parser   */
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    return 1;
}
