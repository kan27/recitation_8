# CMPS 2200 Recitation 08 Answers

**Name:**_Srikanya Garuda________________________
**Name:**_________________________


Place all written answers from `recitation-10.md` here for easier grading.



- **2) (2 pts)** What is the work of `reachable`, assuming $n$ nodes and $m$ edges?
W(n) = O(n + m)

- **4) (1 pt)** What is the worst case number of times we need to call `reachable` to determine if a graph is connected?
Once, the connected function uses reachable only once.

- **5) (2 pts)** What is the work of `connected`, assuming $n$ nodes and $m$ edges?
W(n) = O(n + m), work also determined by reachable function

- **7) (1 pt)** What if we switched the graph representation to an adjacency matrix? Would the work of `reachable` change? If so, what would it be? If not, why not?
O(n^2), need to check a node's relation to each node and look for if an edge exists, so n*n
