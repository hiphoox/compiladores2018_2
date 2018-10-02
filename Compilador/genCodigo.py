import os

def x(programa):
    if (len(programa) != 0):                    # Si el ast recibido no esta vacio siginifica que el parser logro revisar correctamente la sintaxis 
        cadInicio = '.globl _main\n_main:\n'    # Estructura inicial del codigo ensamblador
        for i in programa:                      # Recorremos nuestra lista de funciones en el programa
            for j in i:                         # Verificamos los elementos encontrados en cada funcion
                if "INT" in j:                  # En cuanto encontremos el valor de retorno asignamos ese valor en una variable auxiliar
                    valorRet = j[4:-1]
                    break;
        
        cadInicio = cadInicio + "\tmovl $" + str(valorRet) + ", %eax\n\tret\n" # Completamos la estructura del ensamblador con el valor de retorno encontrado
        
        ar = open("assembly.s", 'w+')       # Abrimos el archivo donde escribiremos nuestro codigo ensamblador
        ar.write(cadInicio)                 # Lo escribimos en el archivo
        
        ar.close()                          # Cerramos el archivo

        os.system("as assembly.s -o out")   # Lo mandamos a compilar con el comando correspondiente

        os.remove("assembly.s")             # Ya compilado borramos el archivo 'assembly.s'
        print("COMPILACION EXITOSA") 

    else:
        print("COMPILACION NO EXITOSA")     # Si el ast esta vacio significa que hubo un error en sintaxis por lo que no se compila nada

    return
