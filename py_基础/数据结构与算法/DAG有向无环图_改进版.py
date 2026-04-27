# -*- coding: utf-8 -*-
# @Time    : 2024/6/17 17:00
# @Author  : 高菲
# @File    : DAG有向无环图_改进版.py
"""
DAG（Directed Acyclic Graph）有向无环图是一种特殊的图结构，其中的边具有方向，并且不存在任何环路。
这种结构在许多领域都有广泛的应用，例如任务调度、数据处理流程、版本控制等。
在这个改进版本的实现中，我们使用了 `defaultdict` 来简化图的表示和入度的计算。`defaultdict` 是 Python 的一个字典子类，它允许我们为不存在的键提供默认值，这样我们就不需要在添加边时手动检查键是否存在。
以下是改进版的 DAG 实现：
"""
from collections import defaultdict, deque


class DAG:
    def __init__(self):
        # defaultdict:访问不存在的键时不会引发 KeyError，而是返回一个默认值，这里默认值是一个空列表。
        self.graph = defaultdict(list)  # 邻接表
        # defaultdict:访问不存在的键时不会引发 KeyError，而是返回一个默认值，这里默认值是0。
        self.in_degree = defaultdict(int)  # 记录入度

        self.nodes = set()  # 节点集

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

    def node_setoff(self, node):
        return [node, 0, 0]  # 节点,水平偏移,垂直偏移

    def topological_sort(self):
        """执行拓扑排序"""
        # 1. 找到所有入度为 0 的节点，并将它们转换为包含节点信息的列表，加入队列。
        #    水平偏移 所有的节点在同一水平线上，水平偏移初始化为0。
        #    垂直偏移 所有的源点（入度为0的节点）在同一水平线上，垂直偏移为0。
        queue = deque(
            [self.node_setoff(node) for node in self.nodes if self.in_degree[node] == 0]
        )
        result = []

        while queue:
            node_w = queue.popleft()
            result.append(node_w)

            # 2. 处理邻居，减少入度
            for neighbor in self.graph[node_w[0]]:
                self.in_degree[neighbor] -= 1
                # 3. 如果入度变为 0，加入队列
                if self.in_degree[neighbor] == 0:
                    queue.append(
                        [neighbor, 0, node_w[2] + 1]
                    )  # 水平偏移初始化为0，垂直偏移加1

        # 4. 检查是否有环
        if len(result) != len(self.nodes):
            return None  # 存在环，无法排序
        else:
            cur_v_offset = 0
            cur_h_offset = 0
            for node_w in result:
                # 如果当前节点的垂直偏移不等于当前的垂直偏移，则说明进入了下一层，重置水平偏移，并更新当前的垂直偏移。
                if node_w[2] != cur_v_offset:
                    cur_v_offset = node_w[2]
                    cur_h_offset = 0

                # 更新当前节点的水平偏移，并将水平偏移加1，为下一个节点准备。
                node_w[1] = cur_h_offset
                cur_h_offset += 1

            return result


def main():
    dag = DAG()
    dag.add_edge("A", "B")
    dag.add_edge("A", "C")
    dag.add_edge("B", "D")
    dag.add_edge("C", "D")
    # dag.add_edge("D", "A")  # 添加一个环

    sorted_nodes = dag.topological_sort()
    if sorted_nodes is not None:
        print("拓扑排序结果:", sorted_nodes)
    else:
        print("图中存在环，无法进行拓扑排序。")


if __name__ == "__main__":
    main()
