


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.input_pipeline.obtain_next

### `tf.contrib.input_pipeline.obtain_next`

```
tf.contrib.input_pipeline.obtain_next(string_list_tensor, counter)
```


Basic wrapper for the ObtainNextOp.

#### Args:

* <b>`string_list_tensor`</b>: A tensor that is a list of strings
* <b>`counter`</b>: an int64 ref tensor to keep track of which element is returned.


#### Returns:

  An op that produces the element at counter + 1 in the list, round
  robin style.

Defined in [`tensorflow/contrib/input_pipeline/python/ops/input_pipeline_ops.py`](https://www.tensorflow.org/code/tensorflow/contrib/input_pipeline/python/ops/input_pipeline_ops.py).

