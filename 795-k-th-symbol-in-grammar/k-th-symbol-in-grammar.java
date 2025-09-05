class Solution {
    public int kthGrammar(int n, int k) {
        // Base case
        if (n == 1 && k == 1) return 0;

        // Total length of row n is 2^(n-1)
        int length = (int)Math.pow(2, n - 1);
        int mid = length / 2;

        if (k > mid) {
            // if k is in the second half, it's the flipped value of (n-1, k-mid)
            return 1 - kthGrammar(n - 1, k - mid);
        } else {
            // if k is in the first half
            return kthGrammar(n - 1, k);
        }
    }
}
