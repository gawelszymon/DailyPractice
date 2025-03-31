class Solution {
    public boolean increasingTriplet(int[] nums) {
        int n1 = Integer.MAX_VALUE;
        int n2 = Integer.MAX_VALUE;
        int n3 = Integer.MAX_VALUE;

        for (int n : nums) {
            if (n <= n1) {
                n1 = n;
            } else if (n <= n2 && n > n1) {
                n2 = n;
            } else if (n <= n3 && n > n2) {
                return true;
            }
        }
        return false;
    }
}