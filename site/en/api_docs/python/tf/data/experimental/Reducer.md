page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.experimental.Reducer

## Class `Reducer`

A reducer is used for reducing a set of elements.



### Aliases:

* Class `tf.compat.v1.data.experimental.Reducer`
* Class `tf.compat.v2.data.experimental.Reducer`
* Class `tf.data.experimental.Reducer`



Defined in [`python/data/experimental/ops/grouping.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/data/experimental/ops/grouping.py).

<!-- Placeholder for "Used in" -->

A reducer is represented as a tuple of the three functions:
  1) initialization function: key => initial state
  2) reduce function: (old state, input) => new state
  3) finalization function: state => result

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    init_func,
    reduce_func,
    finalize_func
)
```






## Properties

<h3 id="finalize_func"><code>finalize_func</code></h3>




<h3 id="init_func"><code>init_func</code></h3>




<h3 id="reduce_func"><code>reduce_func</code></h3>






