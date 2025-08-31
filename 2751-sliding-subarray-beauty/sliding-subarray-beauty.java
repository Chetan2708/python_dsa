class Solution {
    public int[] getSubarrayBeauty(int[] nums, int k, int x) {
        int i = 0 ;
        int j = 0 ;
        int n = nums.length;
        int[] freq = new int[51];
        int[] res = new int [n - k + 1];

        while (j < n){
            if (nums[j] < 0) freq[nums[j] + 50]++;

            if (j-i+1 == k){  
                int count = 0 ;
                int beauty = 0;
                for(int val= 0; val < 50; val++){
                    count += freq[val];
                    if(count >=x ){
                        beauty = val-50;
                        break;
                    } 
                }
                res[j - k + 1] = beauty;
                if (nums[i] < 0) freq[nums[i] + 50]--;
                i++;
            }
            j++; 
        }
        return res;
    }
}