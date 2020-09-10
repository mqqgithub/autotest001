
# 生成器是可以迭代的，但只可以读取它一次。因为用的时候才生成
# yield就是 return 返回一个值，并且记住这个返回的位置，下次迭代就从这个位置后(下一行)开始


def read_in_blocks(file_obj, block_size=5):
    """
    逐件读取文件
    默认块大小：2KB
    """
    while True:
        data = file_obj.read(block_size)  # 每次读取指定的长度
        if not data:
            break
        yield data


with open('..\common\data1.txt', 'r', encoding='utf-8') as f:
    for chuck in read_in_blocks(f, 5):
        print(chuck)
        list1 = chuck.split(r'\n')
        print(list1)
