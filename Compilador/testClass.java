import java.util.*;

public class testClass
{

	
	public static List<String> Tokenizer(String cProgram)
	{

        List<String> tokens = new ArrayList<String>();

		cProgram=cProgram.trim();
		String separatedChars[] = cProgram.split(" ");
		Boolean bandera=false;
		for (String caracter : separatedChars)
				{
					for(char  simbolo : caracter.toCharArray())
					{
						if(Character.toString(simbolo).equals("("))
						{
							braceType openB = new braceType();
							tokens.add(openB.openBrace);
							bandera= true;
						}
						else if(Character.toString(simbolo).equals(")"))
						{
							braceType openB = new braceType();
							tokens.add(openB.closeBrace);
							bandera= true;
						}
					}
				if(!bandera)
					tokens.add(caracter);	
				bandera=false;
				}
		return tokens;
	}

	public static void main(String[] args)
	{
		String cProgram= "           int main () { return 0 ; }  ";
		List<String>  Tokens=Tokenizer(cProgram);
		for(String token : Tokens)
		{
			System.out.println(token);
		}
	}
	
}
class braceType
{
	public String openBrace="(";
	public String closeBrace=")";
	public String openCurlyBrace="{";
	public String closeCurlyBrace="}";

}

class keyWord
{
	private String cadena;

	public  keyWord(String cadena)
	{
		this.cadena= cadena;
	}
	public void printKeyWord()
	{
		System.out.println(this.cadena);
	}
}