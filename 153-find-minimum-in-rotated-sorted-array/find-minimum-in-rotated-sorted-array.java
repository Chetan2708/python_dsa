class Solution {
    public int findMin(int[] arr) {
        //go for the sorted part first, 
        // pick the lowest from there 
        // and you get the minimum 
        // then find in the rotated part
     int low= 0 , high = arr.length - 1;
     while (low < high){
         int mid = low + (high - low) / 2;
    if(arr[mid] > arr[high]){
        low = mid + 1; // Minimum is in the right half
     }
    else {
        high = mid; // Minimum is in the left half or at mid
     }

    }
        return arr[low]; // The minimum element is at index low
    }
}