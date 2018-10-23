

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.kfac.layer_collection.LayerParametersDict

## Class `LayerParametersDict`





Defined in [`tensorflow/contrib/kfac/python/ops/layer_collection.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/contrib/kfac/python/ops/layer_collection.py).

An OrderedDict where keys are Tensors or tuples of Tensors.

Ensures that no Tensor is associated with two different keys.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    *args,
    **kwargs
)
```



<h3 id="__contains__"><code>__contains__</code></h3>

``` python
__contains__(key)
```



<h3 id="__delitem__"><code>__delitem__</code></h3>

``` python
__delitem__(key)
```



<h3 id="__eq__"><code>__eq__</code></h3>

``` python
__eq__(other)
```

od.__eq__(y) <==> od==y.  Comparison to another OD is order-sensitive
while comparison to a regular mapping is order-insensitive.

<h3 id="__getitem__"><code>__getitem__</code></h3>

``` python
__getitem__(key)
```



<h3 id="__iter__"><code>__iter__</code></h3>

``` python
__iter__()
```

od.__iter__() <==> iter(od)

<h3 id="__ne__"><code>__ne__</code></h3>

``` python
__ne__(other)
```

od.__ne__(y) <==> od!=y

<h3 id="__reduce__"><code>__reduce__</code></h3>

``` python
__reduce__()
```

Return state information for pickling

<h3 id="__repr__"><code>__repr__</code></h3>

``` python
__repr__(_repr_running={})
```

od.__repr__() <==> repr(od)

<h3 id="__reversed__"><code>__reversed__</code></h3>

``` python
__reversed__()
```

od.__reversed__() <==> reversed(od)

<h3 id="__setitem__"><code>__setitem__</code></h3>

``` python
__setitem__(
    key,
    value
)
```



<h3 id="clear"><code>clear</code></h3>

``` python
clear()
```

od.clear() -> None.  Remove all items from od.

<h3 id="copy"><code>copy</code></h3>

``` python
copy()
```

od.copy() -> a shallow copy of od

<h3 id="fromkeys"><code>fromkeys</code></h3>

``` python
fromkeys(
    cls,
    iterable,
    value=None
)
```

OD.fromkeys(S[, v]) -> New ordered dictionary with keys from S.
If not specified, the value defaults to None.

<h3 id="items"><code>items</code></h3>

``` python
items()
```

od.items() -> list of (key, value) pairs in od

<h3 id="iteritems"><code>iteritems</code></h3>

``` python
iteritems()
```

od.iteritems -> an iterator over the (key, value) pairs in od

<h3 id="iterkeys"><code>iterkeys</code></h3>

``` python
iterkeys()
```

od.iterkeys() -> an iterator over the keys in od

<h3 id="itervalues"><code>itervalues</code></h3>

``` python
itervalues()
```

od.itervalues -> an iterator over the values in od

<h3 id="keys"><code>keys</code></h3>

``` python
keys()
```

od.keys() -> list of keys in od

<h3 id="pop"><code>pop</code></h3>

``` python
pop(
    key,
    default=__marker
)
```

od.pop(k[,d]) -> v, remove specified key and return the corresponding
value.  If key is not found, d is returned if given, otherwise KeyError
is raised.

<h3 id="popitem"><code>popitem</code></h3>

``` python
popitem(last=True)
```

od.popitem() -> (k, v), return and remove a (key, value) pair.
Pairs are returned in LIFO order if last is true or FIFO order if false.

<h3 id="setdefault"><code>setdefault</code></h3>

``` python
setdefault(
    key,
    default=None
)
```

od.setdefault(k[,d]) -> od.get(k,d), also set od[k]=d if k not in od

<h3 id="update"><code>update</code></h3>

``` python
update(
    *args,
    **kwds
)
```

D.update([E, ]**F) -> None.  Update D from mapping/iterable E and F.
If E present and has a .keys() method, does:     for k in E: D[k] = E[k]
If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
In either case, this is followed by: for k, v in F.items(): D[k] = v

<h3 id="values"><code>values</code></h3>

``` python
values()
```

od.values() -> list of values in od

<h3 id="viewitems"><code>viewitems</code></h3>

``` python
viewitems()
```

od.viewitems() -> a set-like object providing a view on od's items

<h3 id="viewkeys"><code>viewkeys</code></h3>

``` python
viewkeys()
```

od.viewkeys() -> a set-like object providing a view on od's keys

<h3 id="viewvalues"><code>viewvalues</code></h3>

``` python
viewvalues()
```

od.viewvalues() -> an object providing a view on od's values



## Class Members

<h3 id="__hash__"><code>__hash__</code></h3>

