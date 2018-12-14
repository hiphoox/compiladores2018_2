struct ARBOL{
    struct PROGRAMA *hijo;
};

struct PROGRAMA{
    struct FUNCION *hijo;
};

struct FUNCION{
    struct EXPRESION *hijo;
    char *id;
};


struct STATEMENT{
    struct EXPRESION *hijo;
};

struct EXPRESION{
    int integer;
};



