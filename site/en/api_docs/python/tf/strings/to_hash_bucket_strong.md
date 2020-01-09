page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.strings.to_hash_bucket_strong


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/strings/to_hash_bucket_strong">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_string_ops.py`



Converts each string in the input Tensor to its hash mod by a number of buckets.

### Aliases:

* <a href="/api_docs/python/tf/strings/to_hash_bucket_strong"><code>tf.compat.v1.string_to_hash_bucket_strong</code></a>
* <a href="/api_docs/python/tf/strings/to_hash_bucket_strong"><code>tf.compat.v1.strings.to_hash_bucket_strong</code></a>
* <a href="/api_docs/python/tf/strings/to_hash_bucket_strong"><code>tf.compat.v2.strings.to_hash_bucket_strong</code></a>
* <a href="/api_docs/python/tf/strings/to_hash_bucket_strong"><code>tf.string_to_hash_bucket_strong</code></a>


``` python
tf.strings.to_hash_bucket_strong(
    input,
    num_buckets,
    key,
    name=None
)
```



<!-- Placeholder for "Used in" -->

The hash function is deterministic on the content of the string within the
process. The hash function is a keyed hash function, where attribute `key`
defines the key of the hash function. `key` is an array of 2 elements.

A strong hash is important when inputs may be malicious, e.g. URLs with
additional components. Adversaries could try to make their inputs hash to the
same bucket for a denial-of-service attack or to skew the results. A strong
hash can be used to make it difficult to find inputs with a skewed hash value
distribution over buckets. This requires that the hash function is
seeded by a high-entropy (random) "key" unknown to the adversary.

The additional robustness comes at a cost of roughly 4x higher compute
time than <a href="../../tf/strings/to_hash_bucket_fast"><code>tf.string_to_hash_bucket_fast</code></a>.

#### Args:


* <b>`input`</b>: A `Tensor` of type `string`. The strings to assign a hash bucket.
* <b>`num_buckets`</b>: An `int` that is `>= 1`. The number of buckets.
* <b>`key`</b>: A list of `ints`.
  The key used to seed the hash function, passed as a list of two uint64
  elements.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `int64`.
