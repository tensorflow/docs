

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.assert_global_step

``` python
tf.train.assert_global_step(global_step_tensor)
```



Defined in [`tensorflow/python/training/training_util.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/training/training_util.py).

See the guides: [Framework (contrib) > Variables](../../../../api_guides/python/contrib.framework#Variables), [Training > Training Utilities](../../../../api_guides/python/train#Training_Utilities)

Asserts `global_step_tensor` is a scalar int `Variable` or `Tensor`.

#### Args:

* <b>`global_step_tensor`</b>: `Tensor` to test.