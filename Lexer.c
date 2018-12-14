#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

typedef struct TOKEN{
    char *type;
    char *value;
    struct TOKEN *next;
}TOKEN;

typedef struct LISTA_TOKENS{
    struct TOKEN *head;
    struct TOKEN *tail;
}LISTA_TOKENS;

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


void identificaTokens(struct TOKEN *tok){
    int i = 0;
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
};


void lexea(char* bufer, struct LISTA_TOKENS* lista){
    //printf("Lista de tokens creada. (Vacia)\n");
    char *delimitadores = " ();[]{}\n";
    int j, limite;
    char *resto, *valor;
    resto = bufer;
    
    
    struct TOKEN *tok = lista->head;    //tok es un cursor que usaremos para identificar los tokens
    identificaTokens(tok);

    
    
    
    while(*resto){                                           //mientras queden caracteres por escanear
        limite = strcspn(resto, delimitadores);                        //calculamos cuanto mide el sig. token

        if(limite == 0){                                    //si tenemos que hacer single token ()[]{};* etc
            valor = (char *)calloc(1,sizeof(char));
        }
        else{
           valor = (char *)calloc(limite, sizeof(char));    //si el token es mas largo que un caracter(id, keyword...)

        }   
      
        switch(resto[limite]){                              //segun el caracter leido, decidimos dónde termina el token
            /*-------------------------------               para espacios y enters */
            case ' ':
                if(limite > 0){                             //si estábamos a mitad de un token, lo terminamos
                    for(j=0;j<limite;j++){                  
                        valor[j] = resto[j];                //lo agregamos a la lista
                    }
                    agregaToken(lista, valor,NULL);
                }                                           //Si no estábamos a medio token, simplemente lo ignoramos
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
                agregaToken(lista, valor,"leftPar");                  //agregamos token sencillo
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
                agregaToken(lista, valor,"rightPar");
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
                agregaToken(lista, valor,"leftKey");
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
                agregaToken(lista, valor,"rightKey");
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
                agregaToken(lista, valor,"colon");
                resto ++;
            break;               
            
            default:
            break;
        }
    };  
    
};

void imprimeTokens(struct LISTA_TOKENS *lista){
    struct TOKEN *token = (struct TOKEN *)calloc(1,sizeof(struct TOKEN));
    token = lista->head;
    printf("\n\n\nPrograma lexeado. Lista de tokens:\n");
    while(token != NULL){
        printf("\t%s, %s\n",token->value, token->type);
        token = token->next;
    }
}
