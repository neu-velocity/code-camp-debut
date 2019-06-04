class Solution {
    // Intuition: the largest rectangle which consecutive bars can build depends on the shortest one among them.
    //
    // For each bar i in heights, we find the largest rectangle (let's say: rec[i]) it can build (of which height is heights[i]).
    // Then the largest one of these rectangles is our answer: Max{rec[i]}, 0 <= i < heights.length
    //
    // How to calculate rec[i]?
    // The bars in rec[i] cannot be shorter than the i-th bar (if so, the height of rec[i] won't be heights[i])
    // -> We find the first shorter bar in the left(j) and the first shorter bar in the right(k)
    // -> In other words, all the bars between j and k are eaqul or higher than i
    // -> Then we get the area: rec[i] = heights[i] * (j - k - 1)
    //
    // How to find the first shorter bar in the left/right?
    // -> To find the first less/greater element: a monotonous stack can help.
    //
    // To summarize, 3 steps:
    // For each bar in histogram:
    // 1: find the first shorter bar in its left
    // 2: find the first shorter bar in its right
    // 3: find the largest rectangle it can build
    // Among these rectangles, choose the largest one.
    //
    // T: O(n)
    // S: O(n)
    public int largestRectangleArea(int[] heights) {
        if (heights == null || heights.length == 0) {
            return 0;
        }
        Stack<Integer> stack = new Stack();
        int[] left = new int[heights.length], right = new int[heights.length];
        for (int i = 0; i < heights.length; i++) {
            while (!stack.isEmpty() && heights[stack.peek()] >= heights[i]) {
                stack.pop();
            }
            if (stack.isEmpty()) {
                left[i] = -1;
            } else {
                left[i] = stack.peek();
            }
            stack.push(i);
        }
        stack.clear();
        for (int i = heights.length - 1; i >= 0; i--) {
            while (!stack.isEmpty() && heights[stack.peek()] >= heights[i]) {
                stack.pop();
            }
            if (stack.isEmpty()) {
                right[i] = heights.length;
            } else {
                right[i] = stack.peek();
            }
            stack.push(i);
        }
        int maxArea = 0;
        for (int i = 0; i < heights.length; i++) {
            maxArea = Math.max(maxArea, heights[i] * (right[i] - left[i] - 1));
        }
        return maxArea;
    }
}