class Solution {
    public String addBinary(String a, String b) {
        String res = "";
        int c = 0;

        int len = Math.max(a.length(), b.length());

        for(int i = 0; i < len; i++) {
            int x = (i < a.length()) ? a.charAt(a.length() - 1 - i) - '0' : 0;
            int y = (i < b.length()) ? b.charAt(b.length() - 1 - i) - '0' : 0;

            int sum = x + y + c;
            int n = sum % 2;
            res = n + res;
            c = sum / 2;
        }

        if (c == 1) {
            return "1" + res;
        }

        return res;
    }
}