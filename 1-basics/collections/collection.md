## Counter

```python
from collections import 
a = "aaaabbbccc"
my_counter = Counter(a)
print(my_counter.items()) # key value pairs
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(1)[0])
print(list(my_counter.elements())))

```

## namedtuple

```python
from collection import namedtuple
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt)


```

## OrderedDict

```python
from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['c'] = 2
ordered_dict['d'] = 3
ordered_dict['a']= 1
pirnt(oredered_dict)

```


## defaultdict

```python
from collections import defaultdict
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['a'])


```
