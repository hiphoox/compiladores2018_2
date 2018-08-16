import java.util.Scanner;
import java.io.*;
public class Token 
{
    public static void main(String[] args) throws FileNotFoundException {
        String Ruta = "C:\\Users\\Zen\\Desktop\\return_2.c";
        Scanner scan = new Scanner( new File(Ruta));
        while(scan.hasNext())
        {
            System.out.println(scan.next());
        }
    }   
}