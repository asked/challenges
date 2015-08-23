
public class CheckWord
{
    
        
        /*A handful of words have their letters in alphabetical order, that is nowhere in the word do you change direction in the word if you were to scan along the English alphabet. An example is the word "almost", which has its letters in alphabetical order.
    
         Your challenge today is to write a program that can determine if the letters in a word are in alphabetical order. */
        
  private String[] words ={
							"biopsy",
							"chinos",
							"defaced",
							"chintz",
							"sponged",
							"bijoux",
							"abhors",
							"begins",
							"chimps",
							"wronged"
    						  
		
							};
    
    public char[] array=
    {'a','b','c','d', 'e', 'f', 'g',
    'h','i','j','k','l', 'm','n',
    'o','p','q','r','s','t','u','v',
    'w','x','y','z'};
    
    // our constructor; print out the String array here
    public CheckWord()
    {
        String str;
        
        for (int i=0; i<words.length; i++)
        {
            str = words[i];
            int strsize = str.length();
            int l = 0, k =0 ,Match = 0 ;
             
            while ((k < strsize) && (l <= array.length)){
                if (str.charAt(k) == array[l]){
                    k++;
					
					if ( l == array.length)
						break;
                   	else
					 	l++;
					Match++;
				    if (Match == strsize){
        	     		System.out.println(str+"  In Order");
				 		break;
             		}
     
                }else{
					if (l == 25){
						System.out.println(str+"  NOT in Order");	
                   		 break;
					}
					else		
						 l++;
                }
 
            }

        }
    }

    public static void main(String[] args)
    {
        new CheckWord();
    }
}


