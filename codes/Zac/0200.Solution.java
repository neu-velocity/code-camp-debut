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

// union find
class UF_Solution {
    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0 || grid[0] == null || grid[0].length == 0) {
            return 0;
        }
        int R = grid.length, C = grid[0].length;
        int[][] dir = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        DSU dsu = new DSU(R * C);
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                if (grid[r][c] == '1') {
                    int p = dsu.find(r * C + c);
                    for (int[] d : dir) {
                        int x = r + d[0], y = c + d[1];
                        if (x >= 0 && x < R && y >= 0 && y < C && grid[x][y] == '1') {
                            dsu.union(p, x * C + y);
                        }
                    }
                }
            }
        }
        return dsu.count;
    }

    class DSU {
        int count;
        int[] parents;

        DSU(int size) {
            this.count = 0;
            this.parents = new int[size];
            Arrays.fill(parents, -1);
        }

        int find(int x) {
            if (parents[x] == -1) {
                count++;
                parents[x] = x;;
            }
            while (x != parents[x]) {
                x = parents[x];
            }
            return x;
        }

        void union(int x, int y) {
            int p_x = find(x);
            int p_y = find(y);
            if (p_x != p_y) {
                count--;
                parents[p_x] = p_y;
            }
        }
    }
}