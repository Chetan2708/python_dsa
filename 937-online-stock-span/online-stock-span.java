class StockSpanner {

    // pair class to hold {price, span}
    private static class Node {
        int price;
        int span;

        Node(int price, int span) {
            this.price = price;
            this.span = span;
        }
    }

    private ArrayDeque<Node> stack;

    public StockSpanner() {
        stack = new ArrayDeque<>();
    }

    public int next(int price) {
        int span = 1;

        // pop all smaller or equal prices
        while (!stack.isEmpty() && stack.peek().price <= price) {
            span += stack.pop().span;
        }

        // push current price with its computed span
        stack.push(new Node(price, span));

        return span;
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner obj = new StockSpanner();
 * int param_1 = obj.next(price);
 */