// How to return int array
// https://www.homeandlearn.co.uk/java/java_methods.html
// https://stackoverflow.com/questions/1938101/how-to-initialize-an-array-in-java


public class passIntArray {


    public static void main(String args[])
    {
        int[] res = total();
        for(int str : res)
            System.out.println(str);
    }                                 

    public static int[] total() {

         int[] xs = new int[] {1,2,3,4};
         int[] ret = new int[4];
         return xs;

    }

}
