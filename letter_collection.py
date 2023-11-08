def letter_collect(n, m, mat, q, queries):
    ans = []
    for k in range(q):
        s = 0
        hop = queries[k][0]
        x = queries[k][1]
        y = queries[k][2]
        for i in range(x-hop, x+hop+1):
            if i>=0 and i<n:
                if y-hop>=0:
                    s+=mat[i][y-hop]
                if y+hop<m:
                    s+=mat[i][y+hop]
        for i in range(y-hop+1, y+hop):
            if i>=0 and i<n:
                if x-hop>=0:
                    s+=mat[x-hop][i]
                if x+hop<n:
                    s+=mat[x+hop][i]
        ans.append(s)
    return ans

def main():
    mat = []
    n = int(input())
    m = int(input())
    for i in range(n):
        row = input()
        row_values = [int(x) for x in row.split()]
        mat.append(row_values)
    q = int(input())
    queries = []
    for i in range(q):
        l = input()
        vals = [int(x) for x in l.split()]
        queries.append(vals)
    res = []
    res = letter_collect(n, m, mat, q, queries)
    print(res)
    return res

if __name__ == "__main__":
    main()
