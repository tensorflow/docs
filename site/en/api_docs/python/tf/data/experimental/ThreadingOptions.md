page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.experimental.ThreadingOptions


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/data/experimental/ops/threading_options.py#L26-L50">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `ThreadingOptions`

Represents options for dataset threading.



### Aliases:

* Class `tf.compat.v1.data.experimental.ThreadingOptions`
* Class `tf.compat.v2.data.experimental.ThreadingOptions`


<!-- Placeholder for "Used in" -->

You can set the threading options of a dataset through the
`experimental_threading` property of <a href="../../../tf/data/Options"><code>tf.data.Options</code></a>; the property is
an instance of <a href="../../../tf/data/experimental/ThreadingOptions"><code>tf.data.experimental.ThreadingOptions</code></a>.

```python
options = tf.data.Options()
options.experimental_threading.private_threadpool_size = 10
dataset = dataset.with_options(options)
```

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/data/util/options.py#L33-L35">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/data/util/options.py#L37-L43">View source</a>

``` python
__eq__(other)
```

Return self==value.


<h3 id="__ne__"><code>__ne__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/data/util/options.py#L45-L49">View source</a>

``` python
__ne__(other)
```

Return self!=value.
