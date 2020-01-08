page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.lookup.StrongHashSpec

## Class `StrongHashSpec`

Inherits From: [`HasherSpec`](../../../tf/contrib/lookup/HasherSpec)



Defined in [`tensorflow/python/ops/lookup_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/ops/lookup_ops.py).

A structure to specify a key of the strong keyed hash spec.

The strong hash requires a `key`, which is a list of 2 unsigned integer
numbers. These should be non-zero; random numbers generated from random.org
would be a fine choice.

#### Fields:

* <b>`key`</b>: The key to be used by the keyed hashing function.

<h2 id="__new__"><code>__new__</code></h2>

``` python
@staticmethod
__new__(
    cls,
    key
)
```





## Properties

<h3 id="hasher"><code>hasher</code></h3>



<h3 id="key"><code>key</code></h3>





