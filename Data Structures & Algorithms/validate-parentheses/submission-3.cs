public class Solution {
    public bool IsValid(string s) {
        

        Stack<char> charStack = new();

        foreach(char c in s) {
            if (c == '(' || c == '{' || c == '[') {
                charStack.Push(c);
            } else {
                char corr;
                try {
                    corr = charStack.Pop();
                } catch (InvalidOperationException) {
                    return false;
                }
                if (c == ')') {
                    if (corr != '(') return false;
                } else if (c == '}') {
                    if (corr != '{') return false;
                } else if (c == ']') {
                    if (corr != '[') return false;
                }
            }
        }

        if (charStack.Count == 0) return true;

        return false;
    }
}
