public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        var groups = new Dictionary<string, List<string>>();
        foreach (string str in strs) {
            var keyArr = new int[26];
            foreach (char c in str) {
                keyArr[(int)c - 97]++;
            }
            string keyStr = string.Join("", keyArr.Select(n => n.ToString("X")));
            if (groups.ContainsKey(keyStr)) {
                groups[keyStr].Add(str);
            } else {
                groups[keyStr] = new List<string>();
                groups[keyStr].Add(str);
            }
        }
        List<List<string>> retVal = new();
        foreach (string key in groups.Keys) {
            retVal.Add(groups[key]);
        }
        return retVal;
    }
}
