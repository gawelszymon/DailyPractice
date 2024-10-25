class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        ArrayList<Integer> l = new ArrayList<>();
        int a = 0, b = 0;
        
        while(a < m && b < n) {
            if (nums1[a] <= nums2[b]) {
                if (nums1[a] == 0) {
                    a++;
                    continue;
                } else {
                    l.add(nums1[a]);
                    a++;
                }
            } else {
                if (nums2[b] == 0) {
                    b++;
                    continue;
                } else {
                    l.add(nums2[b]);
                    b++;
                }
            }
        }
        
        while (a < m) {
                if (nums1[a] == 0) {
                    a++;
                    continue;
                } else {
                    l.add(nums1[a]);
                    a++;
                }            
        }
        
        while (b < n) {
                if (nums2[b] == 0) {
                    b++;
                    continue;
                } else {
                    l.add(nums2[b]);
                    b++;
                }            
        }
        
        for (int i = 0; i < nums1.length; i++) {
            nums1[i] = 0;
        }        
        
        for (int i = 0; i < l.size(); i++) {
            nums1[i] = l.get(i);
        }
        
        Arrays.sort(nums1);
        
    }
}