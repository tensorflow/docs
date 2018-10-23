

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.lookup.HasherSpec

## Class `HasherSpec`





Defined in [`tensorflow/python/ops/lookup_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/python/ops/lookup_ops.py).

A structure for the spec of the hashing function to use for hash buckets.

`hasher` is the name of the hashing function to use (eg. "fasthash",
"stronghash").
`key` is optional and specify the key to use for the hash function if
supported, currently only used by a strong hash.

#### Fields:

* <b>`hasher`</b>: The hasher name to use.
* <b>`key`</b>: The key to be used by the hashing function, if required.

## Properties

<h3 id="hasher"><code>hasher</code></h3>

Alias for field number 0

<h3 id="key"><code>key</code></h3>

Alias for field number 1



## Methods

<h3 id="__new__"><code>__new__</code></h3>

``` python
__new__(
    _cls,
    hasher,
    key
)
```

Create new instance of HasherSpec(hasher, key)



