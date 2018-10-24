

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.input_pipeline.obtain_next

``` python
tf.contrib.input_pipeline.obtain_next(
    string_list_tensor,
    counter
)
```



Defined in [`tensorflow/contrib/input_pipeline/python/ops/input_pipeline_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/input_pipeline/python/ops/input_pipeline_ops.py).

Basic wrapper for the ObtainNextOp.

#### Args:

* <b>`string_list_tensor`</b>: A tensor that is a list of strings
* <b>`counter`</b>: an int64 ref tensor to keep track of which element is returned.


#### Returns:

An op that produces the element at counter + 1 in the list, round
robin style.