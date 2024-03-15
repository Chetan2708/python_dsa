class Solution {
    public int[] productExceptSelf(int[] nums) {
        int pro=1;
        int isZero=0;
        for(int i=0;i<nums.length;i++)
        {
            if(nums[i]!=0) pro*=nums[i];    
            else{
                isZero+=1;
            }
        }
        int[] ans=new int[nums.length];
        for(int i=0;i<ans.length;i++)
        {
            if(nums[i]!=0)
            {
                if(isZero>0) ans[i]=0;
                else ans[i]=pro/nums[i];
            } else {
                if(isZero==1) ans[i]=pro;
                else ans[i]=0;
            }
        }
        return ans;
    }
}