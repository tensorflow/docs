page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.strings.to_hash_bucket

Converts each string in the input Tensor to its hash mod by a number of buckets.

### Aliases:

* `tf.compat.v1.string_to_hash_bucket`
* `tf.compat.v1.strings.to_hash_bucket`
* `tf.string_to_hash_bucket`
* `tf.strings.to_hash_bucket`

``` python
tf.strings.to_hash_bucket(
    string_tensor=None,
    num_buckets=None,
    name=None,
    input=None
)
```



Defined in [`python/ops/string_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/string_ops.py).

<!-- Placeholder for "Used in" -->

The hash function is deterministic on the content of the string within the
process.

Note that the hash function may change from time to time.
This functionality will be deprecated and it's recommended to use
<a href="../../tf/strings/to_hash_bucket_fast"><code>tf.string_to_hash_bucket_fast()</code></a> or <a href="../../tf/strings/to_hash_bucket_strong"><code>tf.string_to_hash_bucket_strong()</code></a>.

#### Args:


* <b>`string_tensor`</b>: A `Tensor` of type `string`.
* <b>`num_buckets`</b>: An `int` that is `>= 1`. The number of buckets.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `int64`.
