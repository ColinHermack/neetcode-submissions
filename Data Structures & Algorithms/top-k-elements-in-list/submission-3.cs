public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        Dictionary<int, int> occurrences = new();
        foreach (int num in nums) {
            if (occurrences.ContainsKey(num)) {
                occurrences[num]++;
            } else {
                occurrences[num] = 1;
            }
        }

        Queue<int>[] buckets = new Queue<int>[nums.Length + 1];
        for (int i = 0; i < nums.Length + 1; i++) {
            buckets[i] = new Queue<int>();
        }

        foreach (var pair in occurrences) {
            buckets[pair.Value].Enqueue(pair.Key);
        }

        int[] retVal = new int[k];
        int bucketIndex = nums.Length;

        for (int i = 0; i < k; i++) {
            while (buckets[bucketIndex].Count == 0) {
                bucketIndex--;
            }
            retVal[i] = buckets[bucketIndex].Dequeue();
        }

        return retVal;
    }
}
