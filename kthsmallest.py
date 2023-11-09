# Using counting sort: TC: O(N+max_ele), SC:O(max_ele)
def kthsmallest(arr, n, k):
    cnt = 0
    # Find the max element
    m = max(arr)
    # create a dict of length max+1 to count and store the ele in the array
    counter = {}
    for nu in arr:
        counter[nu] = 1+counter.get(nu, 0)
    for i in range(m+1):
        if i in counter:
            cnt += counter[i]
            if cnt>=k:
                return i
    return -1
def main():
    st = input()
    arr = [int(x) for x in st.split(",")]
    n = len(arr)
    k = int(input())
    ans = kthsmallest(arr, n, k)
    return ans

if __name__ == "__main__":
    print(main())
