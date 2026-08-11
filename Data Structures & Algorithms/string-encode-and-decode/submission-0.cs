public class Solution {

    public string Encode(IList<string> strs) {
        string encodedString = "";
        foreach (string str in strs) {
            encodedString += $"{str.Length.ToString()}${str}";
        }

        return encodedString;
    }

    public List<string> Decode(string s) {
        List<string> retVal = new();
        while (s.Length > 0) {
            string lenStr = s.Substring(0, s.IndexOf("$"));
            s = s.Substring(s.IndexOf("$") + 1);
            int len = int.Parse(lenStr);
            if (s.Length > len) {
                retVal.Add(s.Substring(0, len));
            } else {
                retVal.Add(s);
            }
            s = s.Substring(len);
        }

        return retVal;
    }
}
