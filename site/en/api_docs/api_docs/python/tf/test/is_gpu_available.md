

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.test.is_gpu_available

``` python
is_gpu_available(cuda_only=False)
```



Defined in [`tensorflow/python/platform/test.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/python/platform/test.py).

See the guide: [Testing > Utilities](../../../../api_guides/python/test#Utilities)

Returns whether TensorFlow can access a GPU.

#### Args:

* <b>`cuda_only`</b>: limit the search to CUDA gpus.


#### Returns:

  True iff a gpu device of the requested kind is available.