public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        int product = 1;
        int numZeroes = 0;
        foreach (int num in nums) {
            if (num != 0) {
                product *= num;
            } else {
                numZeroes++;
            }
        }
        
        if (numZeroes > 1) {
            return nums.Select(n => 0).ToArray();
        }

        if (numZeroes == 1) {
            return nums.Select(n => {
                if (n == 0) {
                    return product;
                }
                return 0;
            }).ToArray();
        }

        return nums.Select(n => product / n).ToArray();
    }
}
