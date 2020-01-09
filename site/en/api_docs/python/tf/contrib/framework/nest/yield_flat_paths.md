page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.nest.yield_flat_paths


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/util/nest.py#L1240-L1277">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Yields paths for some nested structure.

``` python
tf.contrib.framework.nest.yield_flat_paths(
    nest,
    expand_composites=False
)
```



<!-- Placeholder for "Used in" -->

Paths are lists of objects which can be str-converted, which may include
integers or other types which are used as indices in a dict.

The flat list will be in the corresponding order as if you called
`snt.nest.flatten` on the structure. This is handy for naming Tensors such
the TF scope structure matches the tuple structure.

E.g. if we have a tuple `value = Foo(a=3, b=Bar(c=23, d=42))`

```shell
>>> nest.flatten(value)
[3, 23, 42]
>>> list(nest.yield_flat_paths(value))
[('a',), ('b', 'c'), ('b', 'd')]
```

```shell
>>> list(nest.yield_flat_paths({'a': [3]}))
[('a', 0)]
>>> list(nest.yield_flat_paths({'a': 3}))
[('a',)]
```

#### Args:


* <b>`nest`</b>: the value to produce a flattened paths list for.
* <b>`expand_composites`</b>: If true, then composite tensors such as tf.SparseTensor
   and tf.RaggedTensor are expanded into their component tensors.


#### Yields:

Tuples containing index or key values which form the path to a specific
  leaf value in the nested structure.
