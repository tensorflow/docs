page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.dense_to_sparse

Converts a dense tensor into a sparse tensor.

``` python
tf.contrib.layers.dense_to_sparse(
    tensor,
    eos_token=0,
    outputs_collections=None,
    scope=None
)
```



Defined in [`contrib/layers/python/layers/layers.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/layers/python/layers/layers.py).

<!-- Placeholder for "Used in" -->

An example use would be to convert dense labels to sparse ones
so that they can be fed to the ctc_loss.

#### Args:


* <b>`tensor`</b>: An `int` `Tensor` to be converted to a `Sparse`.
* <b>`eos_token`</b>: An integer. It is part of the target label that signifies the
  end of a sentence.
* <b>`outputs_collections`</b>: Collection to add the outputs.
* <b>`scope`</b>: Optional scope for name_scope.