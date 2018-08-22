public class Operador {
    public static boolean isoperador(String cadena){
        boolean result = false;
        switch(cadena){
            case "+":
                result=true;
                break;
        }
        return result;
    }
}
