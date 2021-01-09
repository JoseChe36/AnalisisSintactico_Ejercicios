/**
 * @(#)DocApoyo.java
 *
 *
 * @author JoseChe
 * @version 1.00 2021/1/8
 */
public class DocApoyo {
        
    /**
     * Creates a new instance of <code>DocApoyo</code>.
     */
    public DocApoyo() {
    }
    
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        double suma; int i; int cont = 0;	
    	
    	do
    		{
    			double num1 = Math.random() * 10; double num2 = Math.random() * 10;
    			suma = num1 + num2;
    			
    			System.out.println("la suma es: " + suma);
    				if(suma > 9)
    		{
    			System.out.println("El n�mero alcanza la decena.");
    			System.out.println();
    		}else{ System.out.println("El n�mero solo alcanza la unidad.");
    		System.out.println();}
    		
    			cont = cont + 1;	
    		}while (cont < 5);
    }
}
