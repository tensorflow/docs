page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.autograph.StackTraceMapper


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/autograph/impl/api.py#L120-L149">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `StackTraceMapper`

Remaps generated code to code it originated from.



<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/autograph/impl/api.py#L123-L124">View source</a>

``` python
__init__(converted_fn)
```

Initialize self.  See help(type(self)) for accurate signature.




## Methods

<h3 id="__enter__"><code>__enter__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/util/tf_stack.py#L61-L77">View source</a>

``` python
__enter__()
```




<h3 id="__exit__"><code>__exit__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/util/tf_stack.py#L79-L81">View source</a>

``` python
__exit__(
    unused_type,
    unused_value,
    unused_traceback
)
```




<h3 id="get_effective_source_map"><code>get_effective_source_map</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/autograph/impl/api.py#L126-L149">View source</a>

``` python
get_effective_source_map()
```

Returns a map (filename, lineno) -> (filename, lineno, function_name).


<h3 id="reset"><code>reset</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/util/tf_stack.py#L91-L92">View source</a>

``` python
reset()
```
