import java.util.Iterator;
import java.util.LinkedList;

/**
 * BFS (Breadth-First Search) 너비우선탐색
 * 루트 노드(혹은 임의의 노드)에서 시작해서 인접한 노드를 먼저 탐색하는 방법
 * 특징: 최단경로, 재귀호출x, 큐(선입선출)
 * Prim, Dijkstra 알고리즘과 유사
 * 
 */

// 의사코드
/*
 * class pseudocode {
 * 
 * void search(Node root) {
 * Queue<E> queue = new Queue();
 * root.marked = true //mark node as 'visited'
 * queue.enqueue(root); //1. add this node at the end of the queue
 * 
 * //3. Run queue until it's empty
 * while(!queue.isEmpty()){
 * Node r = queue.dequeue(); //pop node
 * visit(r); //2. visit node
 * 
 * //2. visit nodes that adjacent with main node
 * foreach(Node n in r.adjacent){
 * if(n.marked == false){
 * n.marked = true; //mark node as 'visited'
 * queue.enqueue(n); //add this node at the end of the queue
 * }
 * }
 * }
 * }
 * }
 */

// BFS 구현
class Graph {
    private int nodeCnt; // 노드개수
    private LinkedList<Integer> adj[]; // 인접 노드리스트

    Graph(int ndCnt) {
        nodeCnt = ndCnt;
        adj = new LinkedList[ndCnt];

        for (int i = 0; i < ndCnt; ++i) { // 인접 노드리스트 초기화
            adj[i] = new LinkedList();
        }
    }

    void addEdge(int n, int w) { // 노드연결
        adj[n].add(w);
    }

    void BFS(int startNode) {//
        boolean visited[] = new boolean[nodeCnt]; // 노드의 방문여부 판단 (초기값: false)
        LinkedList<Integer> queue = new LinkedList<>(); // BFS를 위한 큐 생성

        // 현재노드를 방문한것으로 표시하고 큐에 삽입
        visited[startNode] = true;
        queue.add(startNode);

        // 큐가 빌때까지 반복
        while (queue.size() != 0) {
            // 큐에서 노드 추출
            int curNode = queue.poll();

            // 방문한 노드와 인접한 노드 리스트 추출
            Iterator<Integer> it = adj[curNode].listIterator();
            while (it.hasNext()) {
                int next = it.next();

                // 방문하지 않은 노드면 방문으로 표시 후 큐에 삽입(enqueue)
                if (!visited[next]) {
                    visited[next] = true; // 현재 노드 방문표시
                    queue.add(next); // 큐에 삽입
                }
            }
        }
        System.out.print(visited);
    }

    // 사용방법
    public static void main(String args[]) {
        Graph g = new Graph(4);
        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 2);
        g.addEdge(2, 0);
        g.addEdge(2, 3);
        g.addEdge(3, 3);

        g.BFS(2);

    }

}
