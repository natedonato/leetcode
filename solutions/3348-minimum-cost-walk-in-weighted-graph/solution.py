class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        sections = {}
        costs = {}
        nodes = {}
        section_index = 0

        # make graph
        for edge in edges:
            node1 = edge[0]
            node2 = edge[1]
            weight = edge[2]

            if node1 not in nodes:
                nodes[node1] = {
                    "val": node1,
                    "edges": []
                }
            if node2 not in nodes:
                nodes[node2] = {
                    "val": node2,
                    "edges": []
                }
  

            nodes[node1]['edges'].append((node2, weight))
            nodes[node2]['edges'].append((node1, weight))

        visited = set()

        for node in nodes.values():

            if(node["val"] in visited):
                continue
            else:
                q = deque()
                q.append(node)
                total_weight = -1
                while(q):
                    current = q.popleft()
                    if current["val"] in visited:
                        continue

                    current["section"] = section_index

                    visited.add(current["val"])
                    for edge in current['edges']:
                        q.append(nodes[edge[0]])
                        total_weight &= edge[1]

                sections[section_index] = total_weight
                section_index += 1

        answers = []
        for query in queries:
            if(query[0] not in nodes or query[1] not in nodes):
                answers.append(-1)
            elif nodes[query[0]]["section"] != nodes[query[1]][
                "section"
            ]:
                answers.append(-1)
            else:
                answers.append(sections[nodes[query[0]]["section"]])
        
        return answers
