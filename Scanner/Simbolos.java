public class Simbolos {
    public static String issimbolos(String cadena){
        String result = "";
        switch(cadena){
            case "{":
                result="{ Open Brace";
                break;
            case "}":
                result="{ Close Brace";
                break;
            case "(":
                result="{ Open Parenthesis";
                break;
            case ")":
                result="{ Close Parenthesis";
                break;
            case ";":
                result="; Close Semicolon";
                break;
        }
        return result;
    }
}
