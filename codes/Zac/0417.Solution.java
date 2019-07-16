// dfs
class DFS_Solution {
    int R, C;
    int[][] dir = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0 || grid[0] == null || grid[0].length == 0) {
            return 0;
        }
        R = grid.length;
        C = grid[0].length;
        int count = 0;
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                if (grid[r][c] == '1') {
                    count++;
                    dfs(grid, r, c);
                }
            }
        }
        return count;
    }

    private void dfs(char[][] grid, int r0, int c0) {
        grid[r0][c0] = '0';
        for (int[] d : dir) {
            int r = r0 + d[0], c = c0 + d[1];
            if (r >= 0 && r < R && c >= 0 && c < C && grid[r][c] == '1') {
                dfs(grid, r, c);
            }
        }
    }
}

// bfs
class BFS_Solution {
    public List<int[]> pacificAtlantic(int[][] matrix) {
        List<int[]> ans = new ArrayList();
        if (matrix == null || matrix.length == 0 || matrix[0] == null || matrix[0].length == 0) {
            return ans;
        }
        int R = matrix.length, C = matrix[0].length;
        int[][] dir = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        int[][] ocean = new int[R][C];
        boolean[][] visited = new boolean[R][C];
        Queue<Integer> queue = new LinkedList();
        // pacific
        for (int r = 0, c = 0; r < R; r++) {
            visited[r][c] = true;
            queue.offer(r * C + c);
        }
        for (int r = 0, c = 1; c < C; c++) {
            visited[r][c] = true;
            queue.offer(r * C + c);
        }
        while (!queue.isEmpty()) {
            int pos = queue.poll();
            int r = pos / C, c = pos % C;
            ocean[r][c]++;
            for (int[] d : dir) {
                int x = r + d[0], y = c + d[1];
                if (x >= 0 && x < R && y >= 0 && y < C
                        && !visited[x][y] && matrix[x][y] >= matrix[r][c]) {
                    visited[x][y] = true;
                    queue.offer(x * C + y);
                }
            }
        }
        // atlantic
        visited = new boolean[R][C];
        for (int r = 0, c = C - 1; r < R; r++) {
            visited[r][c] = true;
            queue.offer(r * C + c);
        }
        for (int r = R - 1, c = 0; c < C - 1; c++) {
            visited[r][c] = true;
            queue.offer((R - 1) * C + c);
        }
        while (!queue.isEmpty()) {
            int pos = queue.poll();
            int r = pos / C, c = pos % C;
            ocean[r][c]++;
            for (int[] d : dir) {
                int x = r + d[0], y = c + d[1];
                if (x >= 0 && x < R && y >= 0 && y < C
                        && !visited[x][y] && matrix[x][y] >= matrix[r][c]) {
                    visited[x][y] = true;
                    queue.offer(x * C + y);
                }
            }
        }
        // collect the result
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                if (ocean[r][c] == 2) {
                    ans.add(new int[]{r, c});
                }
            }
        }
        return ans;
    }
}