import java.util.*;

public class LRUCache {
    public static void main(String[] args) {
        int capacity = 3;

        LinkedHashMap<Integer, Integer> cache =
            new LinkedHashMap<>(capacity, 0.75f, true) {
                protected boolean removeEldestEntry(Map.Entry<Integer, Integer> eldest) {
                    return size() > capacity;
                }
            };

        cache.put(1, 10);
        cache.put(2, 20);
        cache.put(3, 30);
        cache.get(1);
        cache.put(4, 40);

        System.out.println(cache);
    }
}
