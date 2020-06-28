# 获取到中间元素
# 如果比中间值小，就在从小到中间值的中间值寻找
# 如果比中间值大，就在从小到中间值的中间值寻找


li = [2,3,5,10,15,16,18,22,26,30,32,35,41,42,43,55,56,66,67,69,72,76,82,83,88]


# 非递归
def two(l, n):
    low, high = 0, len(l)-1
    while low <= high:
        mid = (high+low)//2
        if l[mid] == n:
            return mid
        elif l[mid] > n:
            high = mid-1
        elif l[mid] < n:
            low = mid+1
    return 'none'


# 递归
def find(l, aim, start=0, end=None):
    end = len(l) if end is None else end
    mid_index = (end + start) // 2
    if start <= end:
        if l[mid_index] < aim:
            return find(l, aim, start=mid_index+1, end=end)
        elif l[mid_index] > aim:
            return find(l, aim, start=start, end=mid_index-1)
        else:
            return mid_index
    else:
        return '找不到这个值...'


print(find(li, 66))
print(two(li, 66))





