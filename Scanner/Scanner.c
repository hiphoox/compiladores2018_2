#include<stdio.h>
#include <stdlib.h>
#include <string.h>
#define LIMITE 50

void obtenerTokens(char cadena[]);
void guardarToken(char cadena[]);

int postok=1;
char auxcadena[200] = "";
char c1[50];
char c2[50];
char c3[50];
char c4[50];
char c5[50];
char c6[50];
char c7[50];
char c8[50];
char c9[50];

int main(){
	
	//char Tokens[]={"","","","","","","","",""};
    
    FILE *archivo;
    char dato[200];
    char *cadena;
    
    archivo = fopen("archivo.txt","r");
    
    if(archivo != NULL){
    	while(!feof(archivo)){
    		fgets(dato,100,archivo);
    		cadena = dato;
    		
    		while(*cadena != '\0'){			
	    		
	    		switch(*cadena){
	    			case '0': strcat(auxcadena,"0"); obtenerTokens(auxcadena); break;
	    			case '1': strcat(auxcadena,"1"); obtenerTokens(auxcadena); break;
	    			case '2': strcat(auxcadena,"2"); obtenerTokens(auxcadena); break;
	    			case '3': strcat(auxcadena,"3"); obtenerTokens(auxcadena); break;
	    			case '4': strcat(auxcadena,"4"); obtenerTokens(auxcadena); break;
	    			case '5': strcat(auxcadena,"5"); obtenerTokens(auxcadena); break;
	    			case '6': strcat(auxcadena,"6"); obtenerTokens(auxcadena); break;
	    			case '7': strcat(auxcadena,"7"); obtenerTokens(auxcadena); break;
	    			case '8': strcat(auxcadena,"8"); obtenerTokens(auxcadena); break;
	    			case '9': strcat(auxcadena,"9"); obtenerTokens(auxcadena); break;
	    			case 'a': strcat(auxcadena,"a"); obtenerTokens(auxcadena); break;
	    			case 'b': strcat(auxcadena,"b"); obtenerTokens(auxcadena); break;
	    			case 'c': strcat(auxcadena,"c"); obtenerTokens(auxcadena); break;
	    			case 'd': strcat(auxcadena,"d"); obtenerTokens(auxcadena); break;
	    			case 'e': strcat(auxcadena,"e"); obtenerTokens(auxcadena); break;
	    			case 'f': strcat(auxcadena,"f"); obtenerTokens(auxcadena); break;
	    			case 'g': strcat(auxcadena,"g"); obtenerTokens(auxcadena); break;
	    			case 'h': strcat(auxcadena,"h"); obtenerTokens(auxcadena); break;
	    			case 'i': strcat(auxcadena,"i"); obtenerTokens(auxcadena); break;
	    			case 'j': strcat(auxcadena,"j"); obtenerTokens(auxcadena); break;
	    			case 'k': strcat(auxcadena,"k"); obtenerTokens(auxcadena); break;
	    			case 'l': strcat(auxcadena,"l"); obtenerTokens(auxcadena); break;
	    			case 'm': strcat(auxcadena,"m"); obtenerTokens(auxcadena); break;
	    			case 'n': strcat(auxcadena,"n"); obtenerTokens(auxcadena); break;
	    			case 'o': strcat(auxcadena,"o"); obtenerTokens(auxcadena); break;
	    			case 'p': strcat(auxcadena,"p"); obtenerTokens(auxcadena); break;
	    			case 'q': strcat(auxcadena,"q"); obtenerTokens(auxcadena); break;
	    			case 'r': strcat(auxcadena,"r"); obtenerTokens(auxcadena); break;
	    			case 's': strcat(auxcadena,"s"); obtenerTokens(auxcadena); break;
	    			case 't': strcat(auxcadena,"t"); obtenerTokens(auxcadena); break;
	    			case 'u': strcat(auxcadena,"u"); obtenerTokens(auxcadena); break;
	    			case 'v': strcat(auxcadena,"v"); obtenerTokens(auxcadena); break;
	    			case 'w': strcat(auxcadena,"w"); obtenerTokens(auxcadena); break;
	    			case 'x': strcat(auxcadena,"x"); obtenerTokens(auxcadena); break;
	    			case 'y': strcat(auxcadena,"y"); obtenerTokens(auxcadena); break;
	    			case 'z': strcat(auxcadena,"z"); obtenerTokens(auxcadena); break;
	    			case '(': postok++; guardarToken("("); break;
	    			case ')': postok++; guardarToken(")");break;
	    			case '{': postok++; guardarToken("{");break;
	    			case '}': postok++; guardarToken("}");break;
	    			case ';': guardarToken(auxcadena); postok++; guardarToken(";");break;
	    			//default : strcat(auxcadena, cadena); puts(auxcadena);
				}
				*cadena++;
			}
			
    		//puts(dato);
    		//puts(cadena);
		}
	}
	
	fclose(archivo);
	
	return 0;
}

void obtenerTokens(char cadena[]){
	if((strcmp(cadena,"int"))== 0){
		//puts("int");
		postok++;
		guardarToken(cadena);
		memset(auxcadena,'\0',200);
	};
	
	if((strcmp(cadena,"main"))== 0){
		//puts("main");	
		postok++;
		guardarToken(cadena);
		memset(auxcadena,'\0',200);
	};
	
	if((strcmp(cadena,"return"))== 0){
		//puts("return");
		postok++;
		guardarToken(cadena);
		memset(auxcadena,'\0',200);
	};
}

void guardarToken(char cadena[]){
	switch(postok){
		case 1: strcpy(c1,cadena); puts(c1); break;
		case 2: strcpy(c2,cadena); puts(c2); break;
		case 3: strcpy(c3,cadena); puts(c3); break;
		case 4: strcpy(c4,cadena); puts(c4); break;
		case 5: strcpy(c5,cadena); puts(c5); break;
		case 6: strcpy(c6,cadena); puts(c6); break;
		case 7: strcpy(c7,cadena); puts(c7); break;
		case 8: strcpy(c8,cadena); puts(c8); break;
		case 9: strcpy(c9,cadena); puts(c9); break;
	}
}
