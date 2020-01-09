page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.test.is_gpu_available


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/framework/test_util.py#L1385-L1447">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns whether TensorFlow can access a GPU.

### Aliases:

* `tf.compat.v1.test.is_gpu_available`
* `tf.compat.v2.test.is_gpu_available`


``` python
tf.test.is_gpu_available(
    cuda_only=False,
    min_cuda_compute_capability=None
)
```



<!-- Placeholder for "Used in" -->

Warning: if a non-GPU version of the package is installed, the function would
also return False. Use <a href="../../tf/test/is_built_with_cuda"><code>tf.test.is_built_with_cuda</code></a> to validate if TensorFlow
was build with CUDA support.

#### Args:


* <b>`cuda_only`</b>: limit the search to CUDA GPUs.
* <b>`min_cuda_compute_capability`</b>: a (major,minor) pair that indicates the minimum
  CUDA compute capability required, or None if no requirement.

Note that the keyword arg name "cuda_only" is misleading (since routine will
return true when a GPU device is available irrespective of whether TF was
built with CUDA support or ROCm support. However no changes here because

++ Changing the name "cuda_only" to something more generic would break
   backward compatibility

++ Adding an equivalent "rocm_only" would require the implementation check
   the build type. This in turn would require doing the same for CUDA and thus
   potentially break backward compatibility

++ Adding a new "cuda_or_rocm_only" would not break backward compatibility,
   but would require most (if not all) callers to update the call to use
   "cuda_or_rocm_only" instead of "cuda_only"

#### Returns:

True if a GPU device of the requested kind is available.
