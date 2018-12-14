//***************************************GRAMATICA

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

//*************************************PARSER

typedef struct ARBOL{
    struct PROGRAMA *hijo;
}ARBOL;

typedef struct PROGRAMA{
    struct FUNCION *hijo;
}PROGRAMA;

typedef struct FUNCION{
    struct EXPRESION *hijo;
    char *id;
}FUNCION;


typedef struct STATEMENT{
    struct EXPRESION *hijo;
}STATEMENT;

typedef struct EXPRESION{
    int integer;
}EXPRESION;


union pARBOL{
    ARBOL *pa;
    PROGRAMA *pp;
    FUNCION *pf;
    STATEMENT *ps;
    EXPRESION *pe;
};


int parsea(TOKEN *tok, nPRODUCTO *producto, union pARBOL *p, int a){
    switch (a){
        case 0:
            printf("p apunta a FUNCION\n");
            break;
            
        case 1:
            printf("p apunta a STATEMENT\n");
            break;
            
        case 2:
            printf("p apunta a EXPRESION\n");
            break;
            
        default:
            printf("ERROOOR\n");
            break;
    }
    
    
    do{
        printf("token actual: %s\n",tok->value);
        if(producto->v_noTerminal){
            parsea(tok, producto->noTerminal, p, a + 1);
        }
        else{
            if ((strcmp(producto->simbolo, tok->type)==0)){
                
            }
            else{
                printf("ERROR DE PARSEO, SE ESPERABA %s en lugar de %s\n", producto->simbolo, tok->type);
                return 1;
            }
        }
        tok = tok->next;
        producto = producto->next;
    }while(producto != NULL);
    
    
    return 0;
};







