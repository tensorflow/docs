


<!-- DO NOT EDIT! Automatically generated file. -->
# Module: tf.test

### Module `tf.test`

Testing. See the [Testing](../../../api_guides/python/test) guide.


## Members

[`class Benchmark`](../tf/test/Benchmark): Abstract class that provides helpers for TensorFlow benchmarks.

[`class TestCase`](../tf/test/TestCase): Base class for tests that need to test TensorFlow.

[`assert_equal_graph_def(...)`](../tf/test/assert_equal_graph_def): Asserts that two `GraphDef`s are (mostly) the same.

[`compute_gradient(...)`](../tf/test/compute_gradient): Computes and returns the theoretical and numerical Jacobian.

[`compute_gradient_error(...)`](../tf/test/compute_gradient_error): Computes the gradient error.

[`get_temp_dir(...)`](../tf/test/get_temp_dir): Returns a temporary directory for use during tests.

[`gpu_device_name(...)`](../tf/test/gpu_device_name): Returns the name of a GPU device if available or the empty string.

[`is_built_with_cuda(...)`](../tf/test/is_built_with_cuda): Returns whether TensorFlow was built with CUDA (GPU) support.

[`is_gpu_available(...)`](../tf/test/is_gpu_available): Returns whether TensorFlow can access a GPU.

[`main(...)`](../tf/test/main): Runs all unit tests.

[`mock`](../tf/test/mock) module

[`test_src_dir_path(...)`](../tf/test/test_src_dir_path): Creates an absolute test srcdir path given a relative path.

Defined in [`tensorflow/python/platform/test.py`](https://www.tensorflow.org/code/tensorflow/python/platform/test.py).

