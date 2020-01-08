

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.kfac.utils.SubGraph

## Class `SubGraph`





Defined in [`tensorflow/contrib/kfac/python/ops/utils.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/kfac/python/ops/utils.py).

Defines a subgraph given by all the dependencies of a given set of outputs.
  

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(outputs)
```



<h3 id="filter_list"><code>filter_list</code></h3>

``` python
filter_list(node_list)
```

Filters 'node_list' to nodes in this subgraph.

<h3 id="is_member"><code>is_member</code></h3>

``` python
is_member(node)
```

Check if 'node' is in this subgraph.

<h3 id="variable_uses"><code>variable_uses</code></h3>

``` python
variable_uses(var)
```

Computes number of times a variable is used.

#### Args:

* <b>`var`</b>: Variable or ResourceVariable instance.


#### Returns:

Number of times a variable is used within this subgraph.


#### Raises:

* <b>`ValueError`</b>: If 'var' is not a variable type.



