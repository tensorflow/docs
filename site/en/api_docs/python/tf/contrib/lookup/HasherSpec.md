page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.lookup.HasherSpec

## Class `HasherSpec`

A structure for the spec of the hashing function to use for hash buckets.





Defined in [`python/ops/lookup_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/lookup_ops.py).

<!-- Placeholder for "Used in" -->

`hasher` is the name of the hashing function to use (eg. "fasthash",
"stronghash").
`key` is optional and specify the key to use for the hash function if
supported, currently only used by a strong hash.

#### Fields:


* <b>`hasher`</b>: The hasher name to use.
* <b>`key`</b>: The key to be used by the hashing function, if required.

## Properties

<h3 id="hasher"><code>hasher</code></h3>




<h3 id="key"><code>key</code></h3>






