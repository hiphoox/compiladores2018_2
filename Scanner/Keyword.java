public class Keyword {
    public static boolean iskeyword(String cadena){
        boolean result = false;
        switch(cadena){
            case "auto":
                result=true;
                break;
            case "break":
                result=true;
                break;
            case "case":
                result=true;
                break;
            case "const":
                result=true;
                break;
            case "char":
                result=true;
                break;
            case "continue":
                result=true;
                break;
            case "default":
                result=true;
                break;
            case "do":
                result=true;
                break;
            case "double":
                result=true;
                break;
            case "else":
                result=true;
                break;
            case "enum":
                result=true;
                break;
            case "extern":
                result=true;
                break;
            case "float":
                result=true;
                break;
            case "for":
                result=true;
                break;
            case "goto":
                result=true;
                break;
            case "if":
                result=true;
                break;
            case "int":
                result=true;
                break;
            case "long":
                result=true;
                break;
            case "register":
                result=true;
                break;
            case "return":
                result=true;
                break;
            case "short":
                result=true;
                break;
            case "signed":
                result=true;
                break;
            case "sizeof":
                result=true;
                break;
            case "static":
                result=true;
                break;
            case "struct":
                result=true;
                break;
            case "switch":
                result=true;
                break;
            case "typedef":
                result=true;
                break;
            case "union":
                result=true;
                break;
            case "unsigned":
                result=true;
                break;
            case "volatile":
                result=true;
                break;
            case "void":
                result=true;
                break;
            case "while":
                result=true;
                break;
        }
        return result;
    }
}
