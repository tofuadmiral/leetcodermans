import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the twoStrings function below.
    static String twoStrings(String s1, String s2) {
        // begin to code here
        
        // create a dictionary/hashmap in java, prep for amazon interview
        
        HashMap<Character, Integer> s1letters = new HashMap <Character, Integer>();

        // determine if s1 and s2 share a common substring
        for(int i=0; i<s1.length(); i++){
            // iterate through s1 and add to a dictionary of strings
            s1letters.put(s1.charAt(i), 1);
        }

        // now we have a dictionary of strings to iterate through
        boolean nosub = true;
        int counter=0;
        while(nosub==true && counter<s2.length()){
            if (s1letters.containsKey(s2.charAt(counter))) nosub=false;
            counter++;
        }
        if(nosub){return "YES";}
        return "NO";

    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int q = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int qItr = 0; qItr < q; qItr++) {
            String s1 = scanner.nextLine();

            String s2 = scanner.nextLine();

            String result = twoStrings(s1, s2);

            bufferedWriter.write(result);
            bufferedWriter.newLine();
        }

        bufferedWriter.close();

        scanner.close();
    }
}
