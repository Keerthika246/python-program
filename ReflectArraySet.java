import java.lang.reflect.Array;  
import java.util.Arrays;  

public class ReflectArraySet  {  
     public static void main(String[] argv) throws Exception {  
   	 int[] arr = { 1, 2, 3 };   
     	Object obj = Array.get(arr, 2);  
   		 System.out.println("obj:"+obj);  
    	Array.set(arr, 2, 1);  
    		System.out.println("Array :: " +Arrays.toString(arr));  
  }  
}  