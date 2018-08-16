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
                Arrays.stream(tmp.split("#")).filter(item -> !item.isEmpty()).collect(Collectors.toList()).forEach(s1 -> System.out.println(s1));
            });
        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}