import java.util.*;

public class CharacterFrequency {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String text = sc.nextLine();

        HashMap<Character, Integer> freq = new HashMap<>();

        for (char ch : text.toCharArray()) {
            if (ch != ' ') {
                freq.put(ch, freq.getOrDefault(ch, 0) + 1);
            }
        }

        for (Map.Entry<Character, Integer> entry : freq.entrySet()) {
            System.out.println(entry.getKey() + " : " + entry.getValue());
        }
    }
}
