class Solution {
    // Heap: how much water a cell can hold depends on the shortest cell around it
    // TC: O(MNlog(M+N))
    // SC: O(MN)
    public int trapRainWater(int[][] heightMap) {
        if (heightMap == null
                || heightMap.length == 0
                || heightMap[0] == null
                || heightMap[0].length == 0) {
            return 0;
        }
        int water = 0;
        int R = heightMap.length, C = heightMap[0].length;
        boolean[][] visited = new boolean[R][C];
        PriorityQueue<Integer> minHeap = new PriorityQueue<Integer>(
                (a, b) -> heightMap[a / C][a % C] - heightMap[b / C][b % C]
        );
        // init heap (corner cells is useless)
        visited[0][0] = visited[0][C - 1] = visited[R - 1][0] = visited[R - 1][C - 1] = true;
        for (int c = 1; c < C - 1; c++) {
            visited[0][c] = true;
            visited[R - 1][c] = true;
            minHeap.offer(c);
            minHeap.offer((R - 1) * C  + c);
        }
        for (int r = 1; r < R - 1; r++) {
            visited[r][0] = true;
            visited[r][C - 1] = true;
            minHeap.offer(r * C);
            minHeap.offer(r * C + C - 1);
        }
        int[][] dir = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        while (!minHeap.isEmpty()) {
            int pos = minHeap.poll();
            int row = pos / C, col = pos % C;
            int limit = heightMap[row][col];
            for (int[] d : dir) {
                int r = row + d[0], c = col + d[1];
                if (r >= 0 && r < R && c >= 0 && c < C && !visited[r][c]) {
                    visited[r][c] = true;
                    if (heightMap[r][c] < limit) {
                        water += limit - heightMap[r][c];
                        heightMap[r][c] = limit;
                    }
                    minHeap.offer(r * C + c);
                }
            }
        }
        return water;
    }
}