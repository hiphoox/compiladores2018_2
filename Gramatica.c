#include <stdio.h>
#include <stdlib.h>

typedef struct nPRODUCTO{ //nodo de la lista de producciones
    int v_simbolo;
    int v_noTerminal;       //banderas para saber qué tipo de simbolo es
    
    char *simbolo;      
    struct nPRODUCTO *noTerminal;   //apuntador a la lista de produccion del no terminal
    
    struct nPRODUCTO *next;
}nPRODUCTO;


void imprimeProducciones(nPRODUCTO *p){
    do{
        if (p->v_simbolo)
            printf("\t%s\n",p->simbolo);
        else
            printf("\t*Elemento no terminal\n");
            
        p = p->next;
    }while(p != NULL);
};


int main(){
    
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
    cursor->simbolo = "Colon";
    
    
    printf("Lista de producción de STATEMENT:\n");
    imprimeProducciones(pStatement);
    
    //************************************************************  EXPRESION
    
    cursor = pExpresion;
    cursor->v_simbolo = 1;
    cursor->simbolo = "integer";
    
    

    return 0;
}
