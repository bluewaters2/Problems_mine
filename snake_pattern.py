def snake_pattern(mat, n):
    ans = []
    for i in range(n):
        if i%2==0:
            for j in range(n):
                ans.append(mat[i][j])
        else:
            for j in range(n-1,-1,-1):
                ans.append(mat[i][j])
    return ans

def main():
    n = int(input())
    mat = []
    for i in range(n):
        rows = input()
        r = [int(x) for x in rows.split()]
        mat.append(r)
    res = []
    res = snake_pattern(mat, n)
    print(res)
    return res
    
if __name__ == "__main__":
    main()
