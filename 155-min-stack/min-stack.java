class MinStack {

    private ArrayDeque<int[]> stack;

    public MinStack() {
        stack = new ArrayDeque<>();
    }

    public void push(int val) {
        if( stack.isEmpty() ) stack.push( new int[]{val,val});
        else {
            int currentMin = stack.peek()[1];
            int newMin = Math.min(currentMin , val);

            stack.push(new int[]{val, newMin});
        }
    }

    public void pop() {
        stack.pop();
    }

    public int top() {
        return stack.peek()[0];
    }

    public int getMin() {
        return stack.peek()[1];
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */