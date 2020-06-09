"""
自定义一个类 
    1、对这个类创建的对象，进行属性限制，对象只能设置这个三个属性：  title    money   data
    2、通过相关机制对设置的属性类型进行限制，title只能设置字符串类型数据    
    money设置为int类型数据  data可以设置为任意类型
    3、通过相关机制实现，data 属性不能进行删除
    4、当money设置的值少于0时，确保查询出来的值为0，
"""


class AttrTest:
    __slots__ = ['title', 'money', 'data']

    def __init__(self, title, money, data):
        self.title = title
        self.money = money
        self.data = data

    def __setattr__(self, key, value):
        if key == "title":
            if isinstance(value, str):
                super().__setattr__(key, value)
            else:
                raise AttributeError("title只能为str类型")
        elif key == "money":
            if isinstance(value, int):
                super().__setattr__(key, value)
            else:
                raise AttributeError("money只能为int类型")

    def __delattr__(self, item):
        if item == "data":
            raise AttributeError("data不能删除")

    def __getattribute__(self, item):
        if item == "money":
            return super().__getattribute__("money") if super().__getattribute__("money") >= 0 else 0


from copy import deepcopy


def new_num():
    list1 = [i for i in range(1, 41)]
    list2 = deepcopy(list1)
    list3 = []
    start = 0

    while len(list3) < 20:
        if start + 8 < len(list2):
            list3.append(list2[start + 8])
            new_start = list2.index(list2[start + 8])
            list2.pop(start + 8)
            start = new_start
        else:

            list3.append(list2[start + 8 - len(list2)])
            new_start = list2.index(list2[start + 8 - len(list2)])
            list2.pop(start + 8 - len(list2))
            start = new_start
    return list3


"""
有一艘船上有40个人，由于触礁出现了漏水，现在船上最多只能载20个人，需要20个人下船。
于是这40个人排成一队，根据站位，每个人领取了一个编号，从1开始到40。
然后从1开始到9进行循环报数，报数为9的人出列下船，一直循环，直到船上只剩下20人。
示例：1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19....40
第一次报到9下船的人，编号为9（1,2,3,...编号为9的人报9）
第二次下船的，编号为18，（10的人报1....18的人报9）
第三次下船的，编号为27  （19的人报1....27的人报9）
第四次下船，编号为36  （28的人报1....36的人报9）
第五次下船，编号为5 （37的人报1，38报2,39报3,40报4....5的人报9）
第六次下船，编号为15
.....

请问最后那些编号的人下船了？
"""

if __name__ == '__main__':
    print("--------第一题--------")
    try:
        obj = AttrTest(123, -1, 34)
        print(obj.money)
    except AttributeError as e:
        print(e)
    try:
        obj = AttrTest("python", "123", "34")
        print(obj.money)
    except AttributeError as e:
        print(e)
    try:
        obj = AttrTest("python", "123", "34")
        print(obj.money)
    except AttributeError as e:
        print(e)
    # del obj.data
    obj = AttrTest("python", -1, 34)
    print("money小于0时查询结果：", obj.money)

    print("--------第二题--------")
    print(new_num())
    print("--------第三题没有做--------")
