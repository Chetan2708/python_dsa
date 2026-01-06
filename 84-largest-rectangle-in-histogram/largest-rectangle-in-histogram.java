class Solution {
    public int largestRectangleArea(int[] heights) {
        int n = heights.length;
        int[] prevSmaller = new int[n];
        int[] nextSmaller = new int[n];
        int maxArea = 0;
        ArrayDeque<Integer> stack = new ArrayDeque<>();

        // NSR ( next smaller )
        for(int i = n-1; i >= 0 ; i--){
            while(!stack.isEmpty() && heights[stack.peek()] >= heights[i]){
                stack.pop();
            }
            nextSmaller[i] = stack.isEmpty() ? n : stack.peek();
            stack.push(i);    
        }
        // REUSE
        stack.clear();
        // NSL ( previous smaller )
        for(int i = 0; i < n ; i++){
            while(!stack.isEmpty() && heights[stack.peek()] >= heights[i]){
                stack.pop();
            }
            prevSmaller[i] = stack.isEmpty() ? -1 : stack.peek();
            stack.push(i);    
        }
        
        for (int i = 0; i < n; i++) {
            int width = nextSmaller[i] - prevSmaller[i] - 1;  // r - l - 1
            int area = heights[i] * width;

            maxArea = Math.max(maxArea, area);
        }

        return maxArea;
    }
}