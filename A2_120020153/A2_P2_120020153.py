def find_max_treasure(n, depths):
    stack = []
    max_treasure = 0
    
    for i in range(n):
        while stack and depths[i] < depths[stack[-1]]:
            height = depths[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_treasure = max(max_treasure, height * width)
        
        stack.append(i)
    
    while stack:
        height = depths[stack.pop()]
        width = n if not stack else n - stack[-1] - 1
        max_treasure = max(max_treasure, height * width)
    
    return max_treasure


T = int(input())

queries = []
for _ in range(T):
    n = int(input())
    depths = list(map(int, input().split()))
    queries.append((n, depths))

for query in queries:
    n, depths = query
    result = find_max_treasure(n, depths)
    print(result)
