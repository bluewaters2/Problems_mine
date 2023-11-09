# Quickselect TC:O(N^2) in worst case and O(N) in avg case, SC:O(N)
def partition(arr, l, r):
    pivot = arr[r]
    i = l
    for j in range(l, r):
        if (arr[j]<=pivot):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i

def kthsmallest(arr, low, high, k):
    pos = partition(arr, low, high)
    if pos-low == k-1:
        return arr[pos]
    if (pos-low>k-1):
        return kthsmallest(arr, low, pos-1, k)
    return kthsmallest(arr, pos+1, high, k-(pos-low+1))
    
def main():
    st = input()
    arr = [int(x) for x in st.split(",")]
    n = len(arr)
    k = int(input())
    ans = kthsmallest(arr, 0, n-1, k)
    return ans

if __name__ == "__main__":
    print(main())
