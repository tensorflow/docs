

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.train.sdca_fprint

``` python
sdca_fprint(
    input,
    name=None
)
```



Defined in `tensorflow/python/ops/gen_sdca_ops.py`.

Computes fingerprints of the input strings.

#### Args:

* <b>`input`</b>: A `Tensor` of type `string`.
    vector of strings to compute fingerprints on.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `int64`.
a (N,2) shaped matrix where N is the number of elements in the input
vector. Each row contains the low and high parts of the fingerprint.