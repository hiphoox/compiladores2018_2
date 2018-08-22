import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Constante {
    public static String isconstante(String cadena){
        String result = "";
        Pattern exp = Pattern.compile("[0-9]");
        Matcher reg = exp.matcher(cadena);
        if(reg.find()){
            result = "INT <"+cadena+">";
        }else{
            Pattern exp1 = Pattern.compile("\\d+\\.\\d+");
            reg = exp1.matcher(cadena);
            if(reg.find()){
                result = "FLOAT <"+cadena+">";
            }
        }
        return result;
    }
}
