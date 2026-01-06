class MinStack {

    private ArrayDeque<Long> stack;
    private long minElement;

    public MinStack() {
        stack = new ArrayDeque<>();
        minElement = 0;
    }

    public void push(int x) {

        if (stack.isEmpty()) {
            stack.push((long) x);
            minElement = x;
            return;
        }

        if (x >= minElement) {
            stack.push((long) x);
        } else {
            long encoded = 2L * x - minElement;
            stack.push(encoded);
            minElement = x;
        }
    }

    public int pop() {

        long top = stack.pop();

        if (top >= minElement) {
            return (int) top;
        } else {
            long originalMin = minElement;
            minElement = 2L * minElement - top;
            return (int) originalMin;
        }
    }

    public int top() {

        long top = stack.peek();

        if (top >= minElement) {
            return (int) top;
        } else {
            return (int) minElement;
        }
    }

    public int getMin() {
        return (int) minElement;
    }
}
