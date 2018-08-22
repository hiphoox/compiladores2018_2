import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Identificador {
    public static boolean isidentificador(String cadena){
        Pattern exp = Pattern.compile("[a-zA-Z0-9_]\\w");
        Matcher reg = exp.matcher(cadena);
        if(reg.find()){
            return true;
        }else{
            return false;
        }
    }
}
