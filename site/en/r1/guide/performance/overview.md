# Performance

Better TensorFlow performance comes out-of-the-box by using the high-level APIs.
The sections below detail the high-level APIs to use as well a few tips for
debugging, a little history, and a few instances where manual tuning is
beneficial. It covers best practices that are relevant to a variety of hardware
and models.

### Input pipeline

The input pipeline extracts data from a location, transforms it, and loads it
onto an accelerator for processing. As accelerators become faster, it is
important that the input pipeline keeps up with the demand. The `tf.data` API is
designed with flexibility, ease of use, and performance in mind. For using and
maximizing performance with the `tf.data` API, see the
[data input pipeline](datasets.md) guide.

Reading large numbers of small files significantly impacts I/O performance.
One approach to get maximum I/O throughput is to preprocess input data into
larger (~100MB) `TFRecord` files. For smaller data sets (200MB-1GB), the best
approach is often to load the entire data set into memory. The document
[Downloading and converting to TFRecord format](https://github.com/tensorflow/models/tree/master/research/slim#downloading-and-converting-to-tfrecord-format)
includes information and scripts for creating `TFRecord`s, and this
[script](https://github.com/tensorflow/models/tree/master/research/tutorials/image/cifar10_estimator/generate_cifar10_tfrecords.py)
converts the CIFAR-10 dataset into `TFRecord`s.

While feeding data using a `feed_dict` offers a high level of flexibility, in
general, `feed_dict` does not provide a scalable solution. Avoid using `feed_dict`
for all but trivial examples.

```python
# feed_dict often results in suboptimal performance.
sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
```

### RNN Performance

There are many ways to specify an RNN computation in TensorFlow and they have
trade-offs with respect to model flexibility and performance. The
`tf.nn.rnn_cell.BasicLSTMCell` should be considered a reference implementation
and used only as a last resort when no other options will work.

When using one of the cells, rather than the fully fused RNN layers, you have a
choice of whether to use `tf.nn.static_rnn` or `tf.nn.dynamic_rnn`. There
shouldn't generally be a performance difference at runtime, but large unroll
amounts can increase the graph size of the `tf.nn.static_rnn` and cause long
compile times. An additional advantage of `tf.nn.dynamic_rnn` is that it can
optionally swap memory from the GPU to the CPU to enable training of very long
sequences. Depending on the model and hardware configuration, this can come at
a performance cost. It is also possible to run multiple iterations of
`tf.nn.dynamic_rnn` and the underlying `tf.while_loop` construct in parallel,
although this is rarely useful with RNN models as they are inherently
sequential.

On NVIDIA GPUs, the use of `tf.contrib.cudnn_rnn` should always be preferred
unless you want layer normalization, which it doesn't support. It is often at
least an order of magnitude faster than `tf.contrib.rnn.BasicLSTMCell` and
`tf.contrib.rnn.LSTMBlockCell` and uses 3-4x less memory than
`tf.contrib.rnn.BasicLSTMCell`.

If you need to run one step of the RNN at a time, as might be the case in
reinforcement learning with a recurrent policy, then you should use the
`tf.contrib.rnn.LSTMBlockCell` with your own environment interaction loop
inside a `tf.while_loop` construct. Running one step of the RNN at a time and
returning to Python is possible, but it will be slower.

On CPUs, mobile devices, and if `tf.contrib.cudnn_rnn` is not available on
your GPU, the fastest and most memory efficient option is
`tf.contrib.rnn.LSTMBlockFusedCell`.

For all of the less common cell types like `tf.contrib.rnn.NASCell`,
`tf.contrib.rnn.PhasedLSTMCell`, `tf.contrib.rnn.UGRNNCell`,
`tf.contrib.rnn.GLSTMCell`, `tf.contrib.rnn.Conv1DLSTMCell`,
`tf.contrib.rnn.Conv2DLSTMCell`, `tf.contrib.rnn.LayerNormBasicLSTMCell`,
etc., be aware that they are implemented in the graph like
`tf.contrib.rnn.BasicLSTMCell` and will suffer from the same poor
performance and high memory usage. Consider whether or not those
trade-offs are worth it before using these cells. For example, while layer
normalization can speed up convergence, because cuDNN is 20x faster, the fastest
wall clock time to convergence is usually obtained without it.


## Manual tuning

### Optimizing for CPU

CPUs, which includes Intel® Xeon Phi™, achieve optimal performance when
TensorFlow is [built from source](../../install/source.md) with all of the
instructions supported by the target CPU.

Beyond using the latest instruction sets, Intel® has added support for the
Intel® Math Kernel Library for Deep Neural Networks (Intel® MKL-DNN) to
TensorFlow. While the name is not completely accurate, these optimizations are
often simply referred to as *MKL* or *TensorFlow with MKL*.
[TensorFlow with Intel® MKL-DNN](#tensorflow-with-intel-mkl-dnn) contains details
about the MKL optimizations.

The two configurations listed below are used to optimize CPU performance by
adjusting the thread pools.

* `intra_op_parallelism_threads`: Nodes that can use multiple threads to
  parallelize their execution will schedule the individual pieces into this pool.
* `inter_op_parallelism_threads`: All ready nodes are scheduled in this pool.

These configurations are set using the `tf.ConfigProto` and passed to `tf.Session`
in the `config` attribute as shown in the snippet below. For both configuration
options, if they are unset or set to 0, will default to the number of logical
CPU cores. Testing has shown that the default is effective for systems ranging
from one CPU with 4 cores to multiple CPUs with 70+ combined logical cores.
A common alternative optimization is to set the number of threads in both pools
equal to the number of physical cores rather than logical cores.

```python
config = tf.ConfigProto()
config.intra_op_parallelism_threads = 44
config.inter_op_parallelism_threads = 44
tf.Session(config=config)
```

### TensorFlow with Intel® MKL DNN

Intel® has added optimizations to TensorFlow for Intel® Xeon® and Intel® Xeon
Phi™ through the use of the Intel® Math Kernel Library for Deep Neural Networks
(Intel® MKL-DNN) optimized primitives. The optimizations also provide speedups
for the consumer line of processors, e.g. i5 and i7 Intel processors. The Intel
published paper
[TensorFlow* Optimizations on Modern Intel® Architecture](https://software.intel.com/en-us/articles/tensorflow-optimizations-on-modern-intel-architecture)
contains additional details on the implementation.

Note: MKL was added as of TensorFlow 1.2 and currently only works on Linux. It
also does not work when also using `--config=cuda`.

In addition to providing significant performance improvements for training CNN
based models, compiling with the MKL creates a binary that is optimized for AVX
and AVX2. The result is a single binary that is optimized and compatible with
most modern (post-2011) processors.

TensorFlow can be compiled with the MKL optimizations using the following
commands that depend on the version of the TensorFlow source used.

For TensorFlow source versions after 1.3.0:

```bash
./configure
# Pick the desired options
bazel build --config=mkl --config=opt //tensorflow/tools/pip_package:build_pip_package
```

For TensorFlow versions 1.2.0 through 1.3.0:

```bash
./configure
Do you wish to build TensorFlow with MKL support? [y/N] Y
Do you wish to download MKL LIB from the web? [Y/n] Y
# Select the defaults for the rest of the options.

bazel build --config=mkl --copt="-DEIGEN_USE_VML" -c opt //tensorflow/tools/pip_package:build_pip_package
```

### Tuning MKL for the best performance

This section details the different configurations and environment variables that
can be used to tune the MKL to get optimal performance. Before tweaking various
environment variables make sure the model is using the `NCHW` (`channels_first`)
[data format](#data-formats). The MKL is optimized for `NCHW` and Intel is
working to get near performance parity when using `NHWC`.

MKL uses the following environment variables to tune performance:

* `KMP_BLOCKTIME` - Sets the time, in milliseconds, that a thread should wait,
  after completing the execution of a parallel region, before sleeping.
* `KMP_AFFINITY` - Enables the run-time library to bind threads to physical
  processing units.
* `KMP_SETTINGS` - Enables (true) or disables (false) the printing of OpenMP*
  run-time library environment variables during program execution.
* `OMP_NUM_THREADS` - Specifies the number of threads to use.

More details on the KMP variables are on
[Intel's](https://software.intel.com/en-us/node/522775) site and the OMP
variables on
[gnu.org](https://gcc.gnu.org/onlinedocs/libgomp/Environment-Variables.html)

While there can be substantial gains from adjusting the environment variables,
which is discussed below, the simplified advice is to set the
`inter_op_parallelism_threads` equal to the number of physical CPUs and to set
the following environment variables:

* `KMP_BLOCKTIME=0`
* `KMP_AFFINITY=granularity=fine,verbose,compact,1,0`

Example setting MKL variables with command-line arguments:

```bash
KMP_BLOCKTIME=0 KMP_AFFINITY=granularity=fine,verbose,compact,1,0 \
KMP_SETTINGS=1 python your_python_script.py
```

Example setting MKL variables with python `os.environ`:

```python
os.environ["KMP_BLOCKTIME"] = str(FLAGS.kmp_blocktime)
os.environ["KMP_SETTINGS"] = str(FLAGS.kmp_settings)
os.environ["KMP_AFFINITY"]= FLAGS.kmp_affinity
if FLAGS.num_intra_threads > 0:
  os.environ["OMP_NUM_THREADS"]= str(FLAGS.num_intra_threads)
```

There are models and hardware platforms that benefit from different settings.
Each variable that impacts performance is discussed below.

* `KMP_BLOCKTIME`: The MKL default is 200ms, which was not optimal in our
  testing. 0 (0ms) was a good default for CNN based models that were tested.
  The best performance for AlexNet was achieved at 30ms and both GoogleNet and
  VGG11 performed best set at 1ms.
* `KMP_AFFINITY`: The recommended setting is `granularity=fine,verbose,compact,1,0`.
* `OMP_NUM_THREADS`: This defaults to the number of physical cores.
  Adjusting this parameter beyond matching the number of cores can have an
  impact when using Intel® Xeon Phi™ (Knights Landing) for some models. See
  [TensorFlow* Optimizations on Modern Intel® Architecture](https://software.intel.com/en-us/articles/tensorflow-optimizations-on-modern-intel-architecture)
  for optimal settings.
* `intra_op_parallelism_threads`: Setting this equal to the number of
  physical cores is recommended. Setting the value to 0, which is the default,
  results in the value being set to the number of logical cores - this is an
  alternate option to try for some architectures. This value and `OMP_NUM_THREADS`
  should be equal.
* `inter_op_parallelism_threads`: Setting this equal to the number of
  sockets is recommended. Setting the value to 0, which is the default,
  results in the value being set to the number of logical cores.


## Building and installing from source

The default TensorFlow binaries target the broadest range of hardware to make
TensorFlow accessible to everyone. If using CPUs for training or inference, it
is recommended to compile TensorFlow with all of the optimizations available for
the CPU in use.

To install the most optimized version of TensorFlow, build and install
[from source](../../install/source.md). If there is a need to build TensorFlow
on a platform that has different hardware than the target, then cross-compile
with the highest optimizations for the target platform. The following command is
an example of using `bazel` to compile for a specific platform:

```python
# This command optimizes for Intel’s Broadwell processor
bazel build -c opt --copt=-march="broadwell" --config=cuda //tensorflow/tools/pip_package:build_pip_package

```

### Environment, build, and install tips

* `./configure` asks which compute capability to include in the build. This
  does not impact overall performance but does impact initial startup. After
  running TensorFlow once, the compiled kernels are cached by CUDA. If using
  a docker container, the data is not cached and the penalty is paid each time
  TensorFlow starts. The best practice is to include the
  [compute capabilities](http://developer.nvidia.com/cuda-gpus)
  of the GPUs that will be used, e.g. P100: 6.0, Titan X (Pascal): 6.1,
  Titan X (Maxwell): 5.2, and K80: 3.7.
* Use a version of `gcc` that supports all of the optimizations of the target
  CPU. The recommended minimum gcc version is 4.8.3. On macOS, upgrade to the
  latest Xcode version and use the version of clang that comes with Xcode.
* Install the latest stable CUDA platform and cuDNN libraries supported by
  TensorFlow.


## History

### Data formats

Data formats refers to the structure of the Tensor passed to a given *op*. The
discussion below is specifically about 4D Tensors representing images. In
TensorFlow the parts of the 4D tensor are often referred to by the following
letters:

* N refers to the number of images in a batch.
* H refers to the number of pixels in the vertical (height) dimension.
* W refers to the number of pixels in the horizontal (width) dimension.
* C refers to the channels. For example, 1 for black and white or grayscale
  and 3 for RGB.

Within TensorFlow there are two naming conventions representing the two most
common data formats:

* `NCHW` or `channels_first`
* `NHWC` or `channels_last`

`NHWC` is the TensorFlow default and `NCHW` is the optimal format to use when
training on NVIDIA GPUs using [cuDNN](https://developer.nvidia.com/cudnn).

The best practice is to build models that work with both data formats. This
simplifies training on GPUs and then running inference on CPUs. If TensorFlow is
compiled with the [Intel MKL](#tensorflow-with-intel-mkl-dnn) optimizations,
many operations, especially those related to CNN based models, will be optimized
and support `NCHW`. If not using the MKL, some operations are not supported on
CPU when using `NCHW`.

The brief history of these two formats is that TensorFlow started by using
`NHWC` because it was a little faster on CPUs. In the long term, we are working
on tools to auto rewrite graphs to make switching between the formats
transparent and take advantages of micro optimizations where a GPU op may be
faster using `NHWC` than the normally most efficient `NCHW`.


## Debugging

### Debug input pipeline optimization

Typical models retrieve data from disk and preprocess it before sending the data
through the network. For example, models that process JPEG images will follow
this flow: load image from disk, decode JPEG into a tensor, crop and pad,
possibly flip and distort, and then batch. This flow is referred to as the input
pipeline. As GPUs and other hardware accelerators get faster, preprocessing of
data can be a bottleneck.

Determining if the input pipeline is the bottleneck can be complicated. One of
the most straightforward methods is to reduce the model to a single operation
(trivial model) after the input pipeline and measure the examples per second. If
the difference in examples per second for the full model and the trivial model
is minimal then the input pipeline is likely a bottleneck. Below are some other
approaches to identifying issues:

* Check if a GPU is underutilized by running `nvidia-smi -l 2`. If GPU
  utilization is not approaching 80-100%, then the input pipeline may be the
  bottleneck.
* Generate a timeline and look for large blocks of white space (waiting). An
  example of generating a timeline exists as part of the
  [XLA jit tutorial](../../extend/xla/jit.md).
* Check CPU usage. It is possible to have an optimized input pipeline and lack
  the CPU cycles to process the pipeline.
* Estimate the throughput needed and verify the disk used is capable of that
  level of throughput. Some cloud solutions have network attached disks that
  start as low as 50 MB/sec, which is slower than spinning disks (150 MB/sec),
  SATA SSDs (500 MB/sec), and PCIe SSDs (2,000+ MB/sec).

### Preprocessing on the CPU

Placing input pipeline operations on the CPU can significantly improve
performance. Utilizing the CPU for the input pipeline frees the GPU to focus on
training. To ensure preprocessing is on the CPU, wrap the preprocessing
operations as shown below:

```python
with tf.device('/cpu:0'):
  # function to get and process images or data.
  distorted_inputs = load_and_distort_images()
```

If using `tf.estimator.Estimator` the input function is automatically placed on
the CPU.
