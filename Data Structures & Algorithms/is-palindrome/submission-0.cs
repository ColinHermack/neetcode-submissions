public class Solution {
    public bool IsPalindrome(string s) {
        string alphanumeric = new string(s.Where(char.IsLetterOrDigit).ToArray()).ToLower();
        int p1 = 0;
        int p2 = alphanumeric.Length - 1;

        while (p2 >= p1) {
            if (alphanumeric[p1] != alphanumeric[p2]) {
                return false;
            }
            p1++;
            p2--;
        }
        return true;
    }
}
