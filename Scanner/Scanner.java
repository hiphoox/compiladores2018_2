import java.io.IOException;
        import java.nio.file.Files;
        import java.nio.file.Paths;
        import java.util.Arrays;
        import java.util.stream.Collectors;
        import java.util.stream.Stream;

public class Scanner {
    public static void main(String args[]) {
        String nombreArchivo = "return_2.c";
        try (Stream<String> stream = Files.lines(Paths.get(nombreArchivo))) {
            stream.forEach(s -> {
                String tmp = s.replace(" ","#").replace("(","#(").replace(")","#)")
                        .replace("{","#{").replace("}","#}").replace(";","#;").replace("\t","");
                Arrays.stream(tmp.split("#")).filter(item -> !item.isEmpty()).collect(Collectors.toList()).forEach(s1 -> {
                    if(Keyword.iskeyword(s1)){
                        System.out.println(s1 + " Keyword");
                    }else if(Operador.isoperador(s1)){
                        System.out.println(s1 + " Operator");
                    }else if(Identificador.isidentificador(s1)){
                        System.out.println(s1 + " ID");
                    }else if(!Constante.isconstante(s1).isEmpty()) {
                        System.out.println(Constante.isconstante(s1));
                    }else if(!Simbolos.issimbolos(s1).isEmpty()) {
                        System.out.println(Simbolos.issimbolos(s1));
                    }else{
                        System.out.println(s1);
                    }
                });
            });
        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}