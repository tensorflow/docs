# Performance

Performance is an important consideration when training machine learning
models. Performance speeds up and scales research while
also providing end users with near instant predictions. This section provides
details on the high level APIs to use along with best practices to build
and train high performance models, and quantize models for the least latency
and highest throughput for inference.

* [Performance Guide](../performance/performance_guide.md) contains a collection of best
  practices for optimizing your TensorFlow code.
* [Data input pipeline guide](../performance/datasets_performance.md) describes the tf.data
  API for building efficient data input pipelines for TensorFlow.
* [Benchmarks](../performance/benchmarks.md) contains a collection of
  benchmark results for a variety of hardware configurations.
* For optimizing inference on GPUs, refer to
  [NVIDIA TensorRT™ integration with TensorFlow.](https://medium.com/tensorflow/speed-up-tensorflow-inference-on-gpus-with-tensorrt-13b49f3db3fa)

[TensorFlow Lite](../lite) has
[optimization techniques](../lite/performance/best_practices) for mobile and
embedded devices.
