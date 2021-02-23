from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)

x = isinstance(p, Point)
print('x=', x)

# 圆
Circle = namedtuple('Circle', ['x', 'y', 'r'])

# -------------------------
# deque
from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)
q.pop()
print(q)
q.popleft()
print(q)

# ------------------------
# defaultdict
# 使用dict时，如果不存在，就会抛出Error。如果希望key不存在时，返回一个默认值，就可以使用defaultdict
from collections import defaultdict

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

# ------------------------
from collections import OrderedDict

d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
od = OrderedDict([('a', 1), ('d', 4), ('b', 2), ('c', 3)])
print(od.keys())


# OrderDict可以实现一个FIFO的dict,当容量超出限制时，先删除最早添加的Key
class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0  # 这个写法没有见过
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
            OrderedDict.__setitem__(self, key, value)


# ------------------------
# ChainMap
# ChainMap可以把一组dict串联成一个逻辑上的dict.ChainMap本身也是一个dict,但是查找的时候，会按照顺序在内部的dict依次查找。
# 应用程序都需要传入参数，命令行参数 --> 环境变量 --> 默认参数
from collections import ChainMap
import os, argparse

# 构造缺省参数:
defaults = {
    'color': 'red',
    'user': 'guest'
}
# 构造命令行参数
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = {k: v for k, v in vars(namespace).items() if v}
# 组成ChainMap:
combined = ChainMap(command_line_args, os.environ, defaults)

# 打印参数
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])
# ------------------------
# Counter
from collections import Counter

c = Counter()
for ch in 'programing':
    c[ch] = c[ch] + 1

print(c)  # 统计字符出现的次数
# Counter({'r': 2, 'g': 2, 'p': 1, 'o': 1, 'a': 1, 'm': 1, 'i': 1, 'n': 1})




# ------------------------
