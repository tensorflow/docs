page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.experimental.MapVectorizationOptions


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/data/experimental/MapVectorizationOptions">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/data/experimental/ops/optimization_options.py#L25-L53">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `MapVectorizationOptions`

Represents options for the MapVectorization optimization.



### Aliases:

* Class <a href="/api_docs/python/tf/data/experimental/MapVectorizationOptions"><code>tf.compat.v1.data.experimental.MapVectorizationOptions</code></a>
* Class <a href="/api_docs/python/tf/data/experimental/MapVectorizationOptions"><code>tf.compat.v2.data.experimental.MapVectorizationOptions</code></a>


<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/data/util/options.py#L33-L35">View source</a>

``` python
__init__()
```

Initialize self.  See help(type(self)) for accurate signature.




## Properties

<h3 id="enabled"><code>enabled</code></h3>

Whether to vectorize map transformations. If None, defaults to False.


<h3 id="use_choose_fastest"><code>use_choose_fastest</code></h3>

Whether to use ChooseFastestBranchDataset with this transformation. If True, the pipeline picks between the vectorized and original segment at runtime based on their iterations speed. If None, defaults to False.




## Methods

<h3 id="__eq__"><code>__eq__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/data/util/options.py#L37-L43">View source</a>

``` python
__eq__(other)
```

Return self==value.


<h3 id="__ne__"><code>__ne__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/data/util/options.py#L45-L49">View source</a>

``` python
__ne__(other)
```

Return self!=value.
