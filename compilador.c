//Autor: Alejandro Rivera Nagano
#include "Lexer.c"
#include "Parser.c"


int main(){
/**********************************************************************************************************************/
/******************************************************* PARTE 0: abrir archivo y guardar el contenido en una cadena */
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
    struct LISTA_TOKENS *lista;
    lista = (struct LISTA_TOKENS *)calloc(1,sizeof(struct LISTA_TOKENS));
    lista->head = NULL;
    lista->tail= NULL;
    
    lexea(bufer, lista);
    
    struct TOKEN *tok = lista->head;    //tok es un cursor que usaremos para identificar los tokens
    identificaTokens(tok);

    imprimeTokens(lista);
    
    
/******************************************************************************************************************/    
/****************************************************** 
 *
 * 
 * PARTE 2: parser   */
    


   
    return 1;
}
