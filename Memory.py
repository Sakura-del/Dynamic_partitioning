import sys


class Memory():
    def __init__(self, start, size):
        # 初始化，以元组存储起始地址和长度
        # 把空闲区和进程的元组装载在两个不同的列表中
        # 空闲区存储起始地址和长度，进程存储起始地址，长度和ID
        self.start = start
        tup = (self.start, size)
        # 起始地址 长度
        self.used = []
        self.unused = [tup]

    def FF(self, size, id):
        # 最先适应算法
        for item in self.used:
            # 判断该进程是否在内存中
            if id == item[2]:
                print('该进程已存在,请重新输入')
                return False
        if len(self.unused) == 0:
            print('内存已满，无法装入进程')
            return False
        for index, item in enumerate(self.unused):
            # 遍历列表找到合适大小的空闲区
            if item[1] == size:
                # 内存相等时直接删除该空闲区并将该空闲区装入used列表
                tup = (item[0], size, id)
                self.used.append(tup)
                del self.unused[index]
                self.unused = sorted(self.unused, key=lambda x: x[0])
                print('成功装入内存')
                # 将空闲区按起始地址排序
                return True
            elif item[1] > size:
                # 大于时将空闲区分成两部分
                tup1 = (item[0], size, id)
                tup2 = (item[0] + size, item[1] - size)
                del self.unused[index]
                self.unused.append(tup2)
                self.unused = sorted(self.unused, key=lambda x: x[0])
                # 将空闲区按起始地址排序
                self.used.append(tup1)
                self.used = sorted(self.used, key=lambda x: x[0])
                print('成功装入内存')
                return True
        print('没有合适大小的空闲区！！！\n请重新输入\n')
        return False

    def REFF(self, id):
        # 最先适应算法的回收算法
        for index, item in enumerate(self.used):
            # 遍历列表找到id匹配的进程
            if item[2] == id:
                tup = (item[0], item[1])
                # 将进程整个加入到空闲区列表
                self.unused.append(tup)
                del self.used[index]
                # 删除该进程
                self.unused = sorted(self.unused, key=lambda x: x[0])
                self.used = sorted(self.used, key=lambda x: x[0])

                for i, tpl in enumerate(self.unused):
                    # 删除无用的空闲区
                    if tpl[1] == 0:
                        del self.unused[i]

                for i, tpl in enumerate(self.unused):
                    # 将连续的空闲区合并为一个
                    if (i + 1 < len(self.unused)) and self.unused[i + 1] == (
                            tpl[0] + tpl[1]):
                        tpl1 = (tpl[0], tpl[1] + self.unused[i + 1][1])
                        del self.unused[i]
                        del self.unused[i + 1]
                        self.unused.append(tpl1)
                        self.unused = sorted(self.unused, key=lambda x: x[0])
                return True
        return False
        ''' 
        三种算法极其类似，除了对空闲区的排序方式不一样，其余都可以复用，故不多赘述
        '''

    def REBF(self, id):
        # 最先适应算法的回收算法
        for index, item in enumerate(self.used):
            if item[2] == id:
                tup = (item[0], item[1])
                self.unused.append(tup)
                del self.used[index]
                self.unused = sorted(self.unused, key=lambda x: x[0])

                for i, tpl in enumerate(self.unused):
                    if tpl[1] == 0:
                        del self.unused[i]

                for i, tpl in enumerate(self.unused):
                    if (i + 1 < len(self.unused)) and self.unused[i + 1] == (
                            tpl[0] + tpl[1]):
                        tpl1 = (tpl[0], tpl[1] + self.unused[i + 1][1])
                        del self.unused[i]
                        del self.unused[i + 1]
                        self.unused.append(tpl1)
                        self.unused = sorted(self.unused, key=lambda x: x[1])
                return True
        return False

    def REWF(self, id):
        # 最先适应算法的回收算法
        for index, item in enumerate(self.used):
            if item[2] == id:
                tup = (item[0], item[1])
                self.unused.append(tup)
                del self.used[index]
                self.unused = sorted(self.unused,
                                     key=lambda x: x[0],
                                     reverse=True)

                for i, tpl in enumerate(self.unused):
                    if tpl[1] == 0:
                        del self.unused[i]

                for i, tpl in enumerate(self.unused):
                    if (i + 1 < len(self.unused)) and self.unused[i + 1] == (
                            tpl[0] + tpl[1]):
                        tpl1 = (tpl[0], tpl[1] + self.unused[i + 1][1])
                        del self.unused[i]
                        del self.unused[i + 1]
                        self.unused.append(tpl1)
                        self.unused = sorted(self.unused,
                                             key=lambda x: x[1],
                                             reverse=True)
                return True
        return False

    def BF(self, size, id):
        # 最优适应算法
        for item in self.used:
            if id == item[2]:
                print('该进程已存在,请重新输入')
                return False
        if len(self.unused) == 0:
            print('内存已满，无法装入进程')
            return False
        for index, item in enumerate(self.unused):
            if item[1] == size:
                tup = (item[0], size, id)
                self.used.append(tup)
                del self.unused[index]
                self.unused = sorted(self.unused, key=lambda x: x[1])
                # 将空闲区按大小顺序排序
                print('成功装入内存')
                return True
            elif item[1] > size:
                tup1 = (item[0], size, id)
                tup2 = (item[0] + size, item[1] - size)
                del self.unused[index]
                self.unused.append(tup2)
                self.unused = sorted(self.unused, key=lambda x: x[1])
                self.used.append(tup1)
                self.used = sorted(self.used, key=lambda x: x[1])
                print('成功装入内存')
                return True
        print('没有合适大小的空闲区！！！\n请重新输入\n')
        return False

    def WF(self, size, id):
        # 最坏适应算法
        for item in self.used:
            if id == item[2]:
                print('该进程已存在,请重新输入')
                return False
        if len(self.unused) == 0:
            print('内存已满，无法装入进程')
            return False
        for index, item in enumerate(self.unused):
            if item[1] == size:
                tup = (item[0], size, id)
                self.used.append(tup)
                del self.unused[index]
                self.unused.sort(key=lambda x: x[1], reverse=True)
                # 将空闲区逆序排序
                print('成功装入内存')
                return True
            elif item[1] > size:
                tup1 = (item[0], size, id)
                tup2 = (item[0] + size, item[1] - size)
                del self.unused[index]
                self.unused.append(tup2)
                self.unused.sort(key=lambda x: x[1], reverse=True)
                self.used.append(tup1)
                self.used = sorted(self.used, key=lambda x: x[1], reverse=True)
                print('成功装入内存')
                return True
        print('没有合适大小的空闲区！！！\n请重新输入\n')
        return False

    def show(self):
        used = sorted(self.used, key=lambda x: x[0])
        unused = sorted(self.unused, key=lambda x: x[0])
        # 将列表中的元素按地址排序以便展示
        if len(self.used) == 0:
            print('内存中无进程')
        else:
            print('已使用的内存空间:')
            print('ID' + '\t' + '起始地址' + '\t' + '终止地址' + '\t' + '分区大小' + '\n')
            for index, item in enumerate(used):
                print('{}'.format(item[2]) + '\t' + '{}'.format(item[0]) +
                      '\t\t'
                      '{}'.format(item[0] + item[1] - 1) + '\t\t' +
                      '{}'.format(item[1]))
        if len(self.used) == 0:
            print('内存中无进程')
        else:
            print('未使用的内存空间:')
            print('编号' + '\t' + '起始地址' + '\t' + '终止地址' + '\t' + '分区大小' + '\n')
            for index, item in enumerate(unused):
                print('{}'.format(index) + '\t' + '{}'.format((item[0])) +
                      '\t\t' + '{}'.format(item[1] + item[0] - 1) + '\t\t' +
                      '{}'.format((item[1])) + '\n')


if __name__ == "__main__":
    length = eval(input('请输入内存大小：'))
    my = Memory(0, length)
    print('请选择优先算法：')
    print('1.最先适应算法\n')
    print('2.最优适应算法\n')
    print('3.最坏适应算法\n')
    s = eval(input())
    while True:
        if s in [1, 2, 3]:
            break
        else:
            print('您的输入有误，请重新输入')

    while (True):
        select = eval(input('分配还是回收？(1-分配，2-回收)'))
        if select == 1:
            ID = input('请输入要分配的进程ID：')
            size = eval(input('请输入待分配的内存大小：'))
            if s == 1:
                if my.FF(size, ID) is False:
                    continue
            elif s == 2:
                if my.BF(size, ID) is False:
                    continue
            else:
                if my.WF(size, ID) is False:
                    continue
        elif select == 2:
            id = input('请输入待回收的进程ID：')
            if s == 1:
                if my.REFF(id) is False:
                    continue
            elif s == 2:
                if my.REBF(id) is False:
                    continue
            else:
                if my.REWF(id) is False:
                    continue
        my.show()
        char = input('还要继续吗？y/n')
        if char == 'n':
            break
    print('感谢您的使用!')
    sys.exit(0)
