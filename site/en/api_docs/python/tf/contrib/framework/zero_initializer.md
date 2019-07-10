page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.zero_initializer

Initialize 'ref' with all zeros, ref tensor should be uninitialized.

``` python
tf.contrib.framework.zero_initializer(
    ref,
    use_locking=True,
    name='zero_initializer'
)
```



Defined in [`contrib/framework/python/ops/variables.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/framework/python/ops/variables.py).

<!-- Placeholder for "Used in" -->

If already initialized, you will get ValueError. This op is intended to
save memory during initialization.
Args:
  ref: ref of the tensor need to be zero initialized.
  name: optional name for this operation.

#### Returns:

ref that initialized.


#### Raises:


* <b>`ValueError`</b>: If ref tensor is initialized.