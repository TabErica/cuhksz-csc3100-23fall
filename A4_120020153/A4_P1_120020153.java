import java.util.*;

class Node implements Comparable<Node> {
    int x;
    int y;
    int cost;

    public Node(int x, int y, int cost) {
        this.x = x;
        this.y = y;
        this.cost = cost;
    }

    @Override
    public int compareTo(Node other) {
        return Integer.compare(this.cost, other.cost);
    }
}

public class A4_P1_120020153 {
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, -1, 0, 1};
    static char[] directions = {'w', 'a', 's', 'd'};

    public static int dijkstra(char[][] grid, int[] start, int[] end) {
        int m = grid.length;
        int n = grid[0].length;

        int[][] cost = new int[m][n];
        for (int i = 0; i < m; i++) {
            Arrays.fill(cost[i], Integer.MAX_VALUE);
        }

        cost[start[0]][start[1]] = 0;
        PriorityQueue<Node> queue = new PriorityQueue<>();
        queue.add(new Node(start[0], start[1], 0));

        while (!queue.isEmpty()) {
            Node current = queue.poll();
            int x = current.x;
            int y = current.y;
            int currCost = current.cost;

            if (x == end[0] && y == end[1]) {
                return currCost;
            }

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx >= 0 && nx < m && ny >= 0 && ny < n) {
                    int weight = (x == start[0] && y == start[1]) ? 0 : (grid[x][y] == directions[i] ? 0 : 1);
                    int alt = currCost + weight;

                    if (alt < cost[nx][ny]) {
                        cost[nx][ny] = alt;
                        queue.add(new Node(nx, ny, alt));
                    }
                }
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int m = scanner.nextInt();
        int n = scanner.nextInt();
        scanner.nextLine();  // Consume the newline character

        char[][] grid = new char[m][n];
        int[] start = new int[2];
        int[] end = new int[2];

        for (int i = 0; i < m; i++) {
            String row = scanner.nextLine();
            grid[i] = row.toCharArray();

            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 'i') {
                    start[0] = i;
                    start[1] = j;
                } else if (grid[i][j] == 'j') {
                    end[0] = i;
                    end[1] = j;
                }
            }
        }

        int changesNeeded = dijkstra(grid, start, end);
        System.out.println(changesNeeded);
    }
}
