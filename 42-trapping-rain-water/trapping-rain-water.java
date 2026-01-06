class Solution {
    // public int trap(int[] height) {
    //     int n = height.length;
    //     int[] maxLeftArray = new int[n];
    //     int[] maxRightArray = new int[n];
    //     maxLeftArray[0] = height[0];
    //     for (int i = 1 ; i < n ; i++){
    //         maxLeftArray[i] = Math.max(height[i] , maxLeftArray[i-1]);
    //     }
    //     maxRightArray[n-1] = height[n-1];
    //     for (int i = n-2; i >= 0 ; i--){
    //         maxRightArray[i] = Math.max(height[i] , maxRightArray[i + 1]);
    //     }

    //     int water = 0;
    //     for (int i = 0; i < n; i++) {
    //         water += Math.min(maxLeftArray[i], maxRightArray[i]) - height[i];
    //     }

    //     return water;
    // }

    public int trap(int[] height) {
        int n = height.length;
        int left = 0 ;
        int right = n-1;

        int maxL = 0;
        int maxR = 0;

        int water = 0; 

        while (left <= right){
            if(height[left] <= height[right]){
                if (height[left] >= maxL){
                    maxL = height[left];
                }
                else{
                    water+= maxL - height[left];
                }
                left++;
            }
            else {
                if (height[right] >= maxR){
                    maxR = height[right];
                }
                else{
                    water+= maxR - height[right];
                }
                right--;
            }
        }
        return water;
    }
}
