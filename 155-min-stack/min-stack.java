class MinStack {

    private ArrayDeque<Integer> stack1;
    private ArrayDeque<Integer> stack2;

    public MinStack() {
        stack1 = new ArrayDeque<>();
        stack2 = new ArrayDeque<>();
    }

    public void push(int val) {

        stack1.push(val);

        if (stack2.isEmpty() || stack2.peek() >= val) {
            stack2.push(val);
        }
    }

    public void pop() {

        int x = stack1.pop();

        if (x == stack2.peek()) {
            stack2.pop();
        }
    }

    public int top() {
        return stack1.peek();
    }

    public int getMin() {
        return stack2.peek();
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