page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.experimental.Reducer


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/data/experimental/ops/grouping.py#L443-L467">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `Reducer`

A reducer is used for reducing a set of elements.



### Aliases:

* Class `tf.compat.v1.data.experimental.Reducer`
* Class `tf.compat.v2.data.experimental.Reducer`


<!-- Placeholder for "Used in" -->

A reducer is represented as a tuple of the three functions:
  1) initialization function: key => initial state
  2) reduce function: (old state, input) => new state
  3) finalization function: state => result

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/data/experimental/ops/grouping.py#L452-L455">View source</a>

``` python
__init__(
    init_func,
    reduce_func,
    finalize_func
)
```

Initialize self.  See help(type(self)) for accurate signature.




## Properties

<h3 id="finalize_func"><code>finalize_func</code></h3>




<h3 id="init_func"><code>init_func</code></h3>




<h3 id="reduce_func"><code>reduce_func</code></h3>
