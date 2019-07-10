page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.test.is_gpu_available

Returns whether TensorFlow can access a GPU.

### Aliases:

* `tf.compat.v1.test.is_gpu_available`
* `tf.compat.v2.test.is_gpu_available`
* `tf.test.is_gpu_available`

``` python
tf.test.is_gpu_available(
    cuda_only=False,
    min_cuda_compute_capability=None
)
```



Defined in [`python/framework/test_util.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/framework/test_util.py).

<!-- Placeholder for "Used in" -->

Warning: if a non-GPU version of the package is installed, the function would
also return False. Use <a href="../../tf/test/is_built_with_cuda"><code>tf.test.is_built_with_cuda</code></a> to validate if TensorFlow
was build with CUDA support.

#### Args:


* <b>`cuda_only`</b>: limit the search to CUDA GPUs.
* <b>`min_cuda_compute_capability`</b>: a (major,minor) pair that indicates the minimum
  CUDA compute capability required, or None if no requirement.


#### Returns:

True if a GPU device of the requested kind is available.
