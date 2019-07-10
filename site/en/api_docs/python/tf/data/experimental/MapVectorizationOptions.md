page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.experimental.MapVectorizationOptions

## Class `MapVectorizationOptions`

Represents options for the MapVectorization optimization.



### Aliases:

* Class `tf.compat.v1.data.experimental.MapVectorizationOptions`
* Class `tf.compat.v2.data.experimental.MapVectorizationOptions`
* Class `tf.data.experimental.MapVectorizationOptions`



Defined in [`python/data/experimental/ops/optimization_options.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/data/experimental/ops/optimization_options.py).

<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__()
```






## Properties

<h3 id="enabled"><code>enabled</code></h3>

Whether to vectorize map transformations. If None, defaults to False.


<h3 id="use_choose_fastest"><code>use_choose_fastest</code></h3>

Whether to use ChooseFastestBranchDataset with this transformation. If True, the pipeline picks between the vectorized and original segment at runtime based on their iterations speed. If None, defaults to False.




## Methods

<h3 id="__eq__"><code>__eq__</code></h3>

``` python
__eq__(other)
```




<h3 id="__ne__"><code>__ne__</code></h3>

``` python
__ne__(other)
```






