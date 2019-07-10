page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.experimental.ThreadingOptions

## Class `ThreadingOptions`





Defined in [`tensorflow/python/data/experimental/ops/threading_options.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/data/experimental/ops/threading_options.py).

Represents options for dataset threading.

You can set the threading options of a dataset through the
`experimental_threading` property of <a href="../../../tf/data/Options"><code>tf.data.Options</code></a>; the property is
an instance of <a href="../../../tf/data/experimental/ThreadingOptions"><code>tf.data.experimental.ThreadingOptions</code></a>.

```python
options = tf.data.Options()
options.experimental_threading.private_threadpool_size = 10
dataset = dataset.with_options(options)
```

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__()
```

Initialize self.  See help(type(self)) for accurate signature.



## Properties

<h3 id="max_intra_op_parallelism"><code>max_intra_op_parallelism</code></h3>

If set, it overrides the maximum degree of intra-op parallelism.

<h3 id="private_threadpool_size"><code>private_threadpool_size</code></h3>

If set, the dataset will use a private threadpool of the given size.



## Methods

<h3 id="__eq__"><code>__eq__</code></h3>

``` python
__eq__(other)
```

Return self==value.

<h3 id="__ne__"><code>__ne__</code></h3>

``` python
__ne__(other)
```

Return self!=value.

<h3 id="__setattr__"><code>__setattr__</code></h3>

``` python
__setattr__(
    name,
    value
)
```

Implement setattr(self, name, value).



