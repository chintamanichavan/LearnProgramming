# # PreOrder

# # Recursive Implementation

# marked = [False] * G.size()
# def dfs (G,v):
#     visit(v)
#     marked[v] = True
#     for w in G.neighbors(v):
#         if not marked[w]:
#             dfs(G,w)

# # Iterative Implementation

# marked = [False] * G.size()
# def dfs_iter(G,v):
#     stack = [v]
#     while len(stack) > 0:
#         v = stack.pop()
#         if not marked[v]:
#             visit[v]
#             marked[v] = True
#             for w in G.neighbors(v):
#                 if not marked[w]:
#                     stack.append(w)


# # PostOrder

# Recursive Implementation

# marked = [False] * G.size()
# def dfs_post(G,v):
#     marked[v] = True
#     for w in G.neighbors(v):
#         if not marked[w]:
#             dfs_post(G,w)
#     visit(v)

# Iterative Implmentation



