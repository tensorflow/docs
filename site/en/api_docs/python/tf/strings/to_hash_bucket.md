page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.strings.to_hash_bucket


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/strings/to_hash_bucket">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/string_ops.py#L484-L492">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Converts each string in the input Tensor to its hash mod by a number of buckets.

### Aliases:

* <a href="/api_docs/python/tf/strings/to_hash_bucket"><code>tf.compat.v1.string_to_hash_bucket</code></a>
* <a href="/api_docs/python/tf/strings/to_hash_bucket"><code>tf.compat.v1.strings.to_hash_bucket</code></a>
* <a href="/api_docs/python/tf/strings/to_hash_bucket"><code>tf.string_to_hash_bucket</code></a>


``` python
tf.strings.to_hash_bucket(
    string_tensor=None,
    num_buckets=None,
    name=None,
    input=None
)
```



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
