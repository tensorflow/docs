page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.test


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>



Testing.

<!-- Placeholder for "Used in" -->

See the [Testing](https://tensorflow.org/api_docs/python/tf/test) guide.

Note: `tf.compat.v1.test.mock` is an alias to the python `mock` or
`unittest.mock` depending on the python version.

## Classes

[`class Benchmark`](../tf/test/Benchmark): Abstract class that provides helpers for TensorFlow benchmarks.

[`class TestCase`](../tf/test/TestCase): Base class for tests that need to test TensorFlow.

## Functions

[`assert_equal_graph_def(...)`](../tf/test/assert_equal_graph_def): Asserts that two `GraphDef`s are (mostly) the same.

[`benchmark_config(...)`](../tf/test/benchmark_config): Returns a tf.compat.v1.ConfigProto for disabling the dependency optimizer.

[`compute_gradient(...)`](../tf/test/compute_gradient): Computes the theoretical and numeric Jacobian of `f`.

[`create_local_cluster(...)`](../tf/test/create_local_cluster): Create and start local servers and return the associated `Server` objects.

[`gpu_device_name(...)`](../tf/test/gpu_device_name): Returns the name of a GPU device if available or the empty string.

[`is_built_with_cuda(...)`](../tf/test/is_built_with_cuda): Returns whether TensorFlow was built with CUDA (GPU) support.

[`is_built_with_gpu_support(...)`](../tf/test/is_built_with_gpu_support): Returns whether TensorFlow was built with GPU (i.e. CUDA or ROCm) support.

[`is_built_with_rocm(...)`](../tf/test/is_built_with_rocm): Returns whether TensorFlow was built with ROCm (GPU) support.

[`is_gpu_available(...)`](../tf/test/is_gpu_available): Returns whether TensorFlow can access a GPU.

[`main(...)`](../tf/test/main): Runs all unit tests.
