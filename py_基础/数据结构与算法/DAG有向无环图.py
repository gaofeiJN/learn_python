from collections import defaultdict, deque


class DAG:
    def __init__(self):
        # defaultdict:访问不存在的键时不会引发 KeyError，而是返回一个默认值，这里默认值是一个空列表。
        self.graph = defaultdict(list)  # 邻接表
        # defaultdict:访问不存在的键时不会引发 KeyError，而是返回一个默认值，这里默认值是0。
        self.in_degree = defaultdict(int)  # 记录入度
        self.nodes = set()

    def add_edge(self, u, v):
        """添加边 u -> v"""
        # 向u的邻居列表中添加v
        self.graph[u].append(v)

        # 向节点集合中添加u和v，重复的元素会被自动去除。
        # set.update() 方法用于将一个可迭代对象中的元素添加到集合中，重复的元素会被自动去除。
        self.nodes.update([u, v])

        # 更新u,v的入度，v的入度加1，u的入度保持不变。
        self.in_degree[v] += 1
        if u not in self.in_degree:
            self.in_degree[u] = 0

    def topological_sort(self):
        """执行拓扑排序"""
        # 1. 找到所有入度为 0 的节点
        queue = deque([node for node in self.nodes if self.in_degree[node] == 0])
        result = []

        while queue:
            node = queue.popleft()
            result.append(node)

            # 2. 处理邻居，减少入度
            for neighbor in self.graph[node]:
                self.in_degree[neighbor] -= 1
                # 3. 如果入度变为 0，加入队列
                if self.in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # 4. 检查是否有环
        if len(result) != len(self.nodes):
            return None  # 存在环，无法排序
        return result


def main():
    dag = DAG()
    dag.add_edge("A", "B")
    dag.add_edge("A", "C")
    dag.add_edge("B", "D")
    dag.add_edge("C", "D")
    dag.add_edge("D", "A")  # 添加一个环

    sorted_nodes = dag.topological_sort()
    if sorted_nodes is not None:
        print("拓扑排序结果:", sorted_nodes)
    else:
        print("图中存在环，无法进行拓扑排序。")


if __name__ == "__main__":
    main()
