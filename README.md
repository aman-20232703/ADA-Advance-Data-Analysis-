# ADA Practical Algorithms

Collection of Python implementations for common algorithms studied in Algorithm Design and Analysis, grouped by topic for quick reference and experimentation.

## Getting Started

- Requires Python 3.9 or newer (no external packages needed).
- Clone or download the repository, then run scripts directly from the repo root using `python <script_name>.py`.
- Each script contains a runnable example that prints results to the console.

## Repository Layout

- `binary_search.py`, `linear_search.py`, `sbset_sum.py` – Searching and backtracking examples, including binary search, linear search, and the subset sum decision problem.
- `graph/` – Graph-oriented algorithms: breadth-first search, depth-first search, adjacency matrix helpers, bipartite graph check, maximum subarray (Kadane), and Strassen matrix multiplication.
- `greedy_algorithim/` – Greedy and dynamic programming hybrids such as fractional and 0/1 knapsack, minimum coin change, Kruskal minimum spanning tree, and Prim minimum spanning tree.
- `sorting/` – Classic sorting routines: bubble, counting, heap, insertion, merge, quick, radix, selection, and topological ordering for DAGs.
- `sort.txt` – Notes on best, average, and worst case analysis plus divide-and-conquer basics.

## Highlights by Category

- **Searching**: Iterative binary search (`binary_search.py`) and linear scan (`linear_search.py`) with example arrays and console output.
- **Dynamic Programming**: Subset sum recursion (`sbset_sum.py`) and two 0/1 knapsack tabulations (`greedy_algorithim/integer_knapsack.py`).
- **Greedy Strategies**: Fractional knapsack ratio sorting, coin change minimization, and MST construction via Kruskal and Prim implementations.
- **Graph Utilities**: BFS and DFS traversals, adjacency matrix helpers, bipartite validation, and Kadane maximum subarray detection (`graph/maxsub_arryay.py`).
- **Matrix Operations**: Strassen 2x2 matrix multiplication and a traditional matrix multiply reference implementation (`graph/strassen's_algorithim.py`).
- **Sorting Algorithms**: Comprehensive implementations covering comparison-based and digit-based methods in `sorting/`.

## Running Examples

1. Open a terminal in the repository root.
2. Execute a script, for example:
   - `python sorting/merge_sort.py`
   - `python greedy_algorithim/kruskals.py`
   - `python graph/dfs.py`
3. Observe printed output illustrating the algorithm's behavior.

## Extending the Repository

- Add new algorithms alongside existing categories to keep the structure consistent.
- Provide a short docstring explaining the algorithm's purpose, time complexity, and usage pattern.
- Include a small test harness or sample input within each script for quick manual validation.
