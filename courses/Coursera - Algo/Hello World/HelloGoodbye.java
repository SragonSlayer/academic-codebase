import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

public class HelloGoodbye {
    public static void main(String[] args){
        String input1 = args[0];
        String input2 = args[1];
        StdOut.println("Hello " + input1 + " and " + input2 + ".");
        StdOut.println("Goodbye " + input2 + " and " + input1 + ".");
    }
}