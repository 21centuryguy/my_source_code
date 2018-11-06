
// How to return sting array
// https://stackoverflow.com/questions/15360170/returning-string-array-to-the-method-and-print-returned-array


public class passStringArray {

    public static void main(String args[])
    {
        String[] res = demo();
        for(String str : res)
            System.out.println(str);
    }                                 


    public static String[] demo()
    {
         String[] xs = new String[] {"a","b","c","d"};
         String[] ret = new String[4];
         ret[0]=xs[0];
         ret[1]=xs[1];
         ret[2]=xs[2];
         ret[3]=xs[3];
         return ret;
     }

}
