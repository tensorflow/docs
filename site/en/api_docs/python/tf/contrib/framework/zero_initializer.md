


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.framework.zero_initializer

### `tf.contrib.framework.zero_initializer`

```
tf.contrib.framework.zero_initializer(ref, use_locking=True, name='zero_initializer')
```


See the guide: [Framework (contrib) > Variables](../../../../../api_guides/python/contrib.framework#Variables)

Initialize 'ref' with all zeros, ref tensor should be uninitialized.
If already initialized, you will get ValueError. This op is intended to
save memory during initialization.
Args:
  ref: ref of the tensor need to be zero initialized.
  name: optional name for this operation.
Returns:
  ref that initialized.
Raises:
  ValueError: If ref tensor is initialized.

Defined in [`tensorflow/contrib/framework/python/ops/variables.py`](https://www.tensorflow.org/code/tensorflow/contrib/framework/python/ops/variables.py).

