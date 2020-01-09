page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.lookup.StrongHashSpec


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/lookup_ops.py#L800-L820">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `StrongHashSpec`

A structure to specify a key of the strong keyed hash spec.

Inherits From: [`HasherSpec`](../../../tf/contrib/lookup/HasherSpec)

<!-- Placeholder for "Used in" -->

The strong hash requires a `key`, which is a list of 2 unsigned integer
numbers. These should be non-zero; random numbers generated from random.org
would be a fine choice.

#### Fields:


* <b>`key`</b>: The key to be used by the keyed hashing function.

<h2 id="__new__"><code>__new__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/lookup_ops.py#L812-L820">View source</a>

``` python
@staticmethod
__new__(
    cls,
    key
)
```

Create new instance of HasherSpec(hasher, key)




## Properties

<h3 id="hasher"><code>hasher</code></h3>




<h3 id="key"><code>key</code></h3>
