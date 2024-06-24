import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class A3_P1_120020153 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input
        int n = scanner.nextInt();
        int[] colors = new int[n];
        for (int i = 0; i < n; i++) {
            colors[i] = scanner.nextInt();
        }

        List<int[]> edges = new ArrayList<>();

        for (int i = 0; i < n - 1; i++) {
            int u = scanner.nextInt();
            int w = scanner.nextInt();
            edges.add(new int[]{u, w});
        }

        // Output
        long result = calculateDistances(n, colors, edges);
        System.out.println(result);
        scanner.close();
    }

    private static void dfs(int u, int parent, long[] dis, long[] count, Map<Integer, List<int[]>> graph, int[] colors) {
        for (int[] edge : graph.get(u)) {
            int v = edge[0];
            int w = edge[1];

            if (v == parent) {
                continue;
            }

            if (colors[v - 1] == 0) {
                dfs(v, u, dis, count, graph, colors);
                count[u] += count[v];
                dis[u] += dis[v] + count[v] * w;
            } else if (colors[v - 1] == 1) {
                count[v] += 1;
                dfs(v, u, dis, count, graph, colors);
                count[u] += count[v];
                dis[u] += dis[v] + (count[v]) * w;
            }
        }
    }

    private static void dfs2(int u, int parent, long[] dis, long[] count, Map<Integer, List<int[]>> graph, long[] ans, int black) {
        for (int[] edge : graph.get(u)) {
            int v = edge[0];
            int w = edge[1];

            if (v == parent) {
                continue;
            }

            ans[v] = ans[u] - count[v] * w + (black - count[v]) * w;
            dfs2(v, u, dis, count, graph, ans, black);
        }
    }

    private static long calculateDistances(int n, int[] colors, List<int[]> edges) {
        Map<Integer, List<int[]>> graph = new HashMap<>();

        for (int i = 1; i <= n; i++) {
            graph.put(i, new ArrayList<>());
        }

        for (int idx = 0; idx < edges.size(); idx++) {
            int[] edge = edges.get(idx);
            int u = edge[0];
            int w = edge[1];
            int v = idx + 2;
            graph.get(u).add(new int[]{v, w});
            graph.get(v).add(new int[]{u, w});
        }

        long[] dis = new long[n + 1];
        long[] count = new long[n + 1];
        long[] ans = new long[n + 1];
        int black = 0;
        for (int color : colors) {
            if (color == 1) {
                black++;
            }
        }

        dfs(1, 0, dis, count, graph, colors);
        ans[1] = dis[1];
        dfs2(1, 0, dis, count, graph, ans, black);
        long result = 0;

        for (int i = 0; i < colors.length; i++) {
            result += (colors[i] * ans[i + 1]);
        }
        result = result/2;
        return result;
    }
}
