page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.lookup.StaticVocabularyTable


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/lookup/StaticVocabularyTable">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/lookup_ops.py#L1211-L1218">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `StaticVocabularyTable`

String to Id table wrapper that assigns out-of-vocabulary keys to buckets.

Inherits From: [`StaticVocabularyTable`](../../tf/compat/v2/lookup/StaticVocabularyTable)

### Aliases:

* Class <a href="/api_docs/python/tf/lookup/StaticVocabularyTable"><code>tf.compat.v1.lookup.StaticVocabularyTable</code></a>


<!-- Placeholder for "Used in" -->

For example, if an instance of `StaticVocabularyTable` is initialized with a
string-to-id initializer that maps:

* `emerson -> 0`
* `lake -> 1`
* `palmer -> 2`

The `Vocabulary` object will performs the following mapping:

* `emerson -> 0`
* `lake -> 1`
* `palmer -> 2`
* `<other term> -> bucket_id`, where bucket_id will be between `3` and
`3 + num_oov_buckets - 1`, calculated by:
`hash(<term>) % num_oov_buckets + vocab_size`

If input_tensor is `["emerson", "lake", "palmer", "king", "crimson"]`,
the lookup result is `[0, 1, 2, 4, 7]`.

If `initializer` is None, only out-of-vocabulary buckets are used.

#### Example usage:



```python
num_oov_buckets = 3
input_tensor = tf.constant(["emerson", "lake", "palmer", "king", "crimnson"])
table = tf.lookup.StaticVocabularyTable(
    tf.TextFileIdTableInitializer(filename), num_oov_buckets)
out = table.lookup(input_tensor).
table.init.run()
print(out.eval())
```

The hash function used for generating out-of-vocabulary buckets ID is
Fingerprint64.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/lookup_ops.py#L1077-L1136">View source</a>

``` python
__init__(
    initializer,
    num_oov_buckets,
    lookup_key_dtype=None,
    name=None
)
```

Construct a `StaticVocabularyTable` object.


#### Args:


* <b>`initializer`</b>: A TableInitializerBase object that contains the data used to
  initialize the table. If None, then we only use out-of-vocab buckets.
* <b>`num_oov_buckets`</b>: Number of buckets to use for out-of-vocabulary keys. Must
  be greater than zero.
* <b>`lookup_key_dtype`</b>: Data type of keys passed to `lookup`. Defaults to
  `initializer.key_dtype` if `initializer` is specified, otherwise
  <a href="../../tf#string"><code>tf.string</code></a>. Must be string or integer, and must be castable to
  `initializer.key_dtype`.
* <b>`name`</b>: A name for the operation (optional).


#### Raises:


* <b>`ValueError`</b>: when `num_oov_buckets` is not positive.
* <b>`TypeError`</b>: when lookup_key_dtype or initializer.key_dtype are not
  integer or string. Also when initializer.value_dtype != int64.



## Properties

<h3 id="initializer"><code>initializer</code></h3>




<h3 id="key_dtype"><code>key_dtype</code></h3>

The table key dtype.


<h3 id="name"><code>name</code></h3>

The name of the table.


<h3 id="resource_handle"><code>resource_handle</code></h3>

Returns the resource handle associated with this Resource.


<h3 id="value_dtype"><code>value_dtype</code></h3>

The table value dtype.




## Methods

<h3 id="lookup"><code>lookup</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/lookup_ops.py#L1168-L1207">View source</a>

``` python
lookup(
    keys,
    name=None
)
```

Looks up `keys` in the table, outputs the corresponding values.

It assigns out-of-vocabulary keys to buckets based in their hashes.

#### Args:


* <b>`keys`</b>: Keys to look up. May be either a `SparseTensor` or dense `Tensor`.
* <b>`name`</b>: Optional name for the op.


#### Returns:

A `SparseTensor` if keys are sparse, otherwise a dense `Tensor`.



#### Raises:


* <b>`TypeError`</b>: when `keys` doesn't match the table key data type.

<h3 id="size"><code>size</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/lookup_ops.py#L1159-L1166">View source</a>

``` python
size(name=None)
```

Compute the number of elements in this table.
