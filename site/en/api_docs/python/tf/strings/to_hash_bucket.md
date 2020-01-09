page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.strings.to_hash_bucket


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/string_ops.py#L459-L481">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Converts each string in the input Tensor to its hash mod by a number of buckets.

### Aliases:

* `tf.compat.v2.strings.to_hash_bucket`


``` python
tf.strings.to_hash_bucket(
    input,
    num_buckets,
    name=None
)
```



<!-- Placeholder for "Used in" -->

The hash function is deterministic on the content of the string within the
process.

Note that the hash function may change from time to time.
This functionality will be deprecated and it's recommended to use
<a href="../../tf/strings/to_hash_bucket_fast"><code>tf.strings.to_hash_bucket_fast()</code></a> or <a href="../../tf/strings/to_hash_bucket_strong"><code>tf.strings.to_hash_bucket_strong()</code></a>.

#### Args:


* <b>`input`</b>: A `Tensor` of type `string`.
* <b>`num_buckets`</b>: An `int` that is `>= 1`. The number of buckets.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `int64`.
