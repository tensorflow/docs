# Optimize TensorFlow GPU Performance with the TensorFlow Profiler

## Overview

Use the optimizations in this guide to ensure you get the maximum performance
out of your GPUs. Using the TensorFlow Profiler as the main tool to gain insight
into performance, this guide will help you debug when one or more of your GPUs
are underutilized.

Read the
[Profiler tutorial](https://www.tensorflow.org/tensorboard/tensorboard_profiling_keras)
to learn more about how to get started with using the Profiler. Also, read the
[Profiler guide](https://www.tensorflow.org/guide/profiler#profiler_tools) to
learn more about the various profiling tools available and the various methods
available to optimize TensorFlow performance on the host (CPU).

Keep in mind that offloading computations to GPU might not always be beneficial,
particularly for small models. There are overheads due to data transfer between
host (CPU) and device (GPU), as well as overheads due to the latency involved
when the host launches GPU kernels. Good performance is achieved when the host
successfully keeps the GPU occupied by offloading enough work.

### Performance Optimization Workflow

This guide outlines how to debug performance issues starting with a single GPU,
then moving to a single host with multiple GPUs. It is recommended to debug
performance issues in this order. For example, if you are using a TensorFlow
distribution strategy to train a model on a single host with multiple GPUs and
notice suboptimal GPU utilization, you should first optimize and debug
performance for 1 GPU, before debugging the multi-GPU system. The recommended
order is as follows:

1.  Optimize and debug performance on 1 GPU
    1.  Check if input pipeline is a bottleneck
    2.  Debug performance of 1 GPU
    3.  Enable fp16 and optionally enable XLA
2.  Optimize and debug performance on multi-GPU single host

As a baseline for getting performant code on GPU, this guide assumes you are
already using `tf.function`. The Keras compile/fit API will utilize
`tf.function` automatically under the hood. When writing a custom training loop,
refer to [this guide](https://www.tensorflow.org/guide/function) on how to
enable `tf.function`.

The next sections discuss suggested approaches for each of the scenarios above
to help identify and fix performance bottlenecks.

## Optimize Performance on 1 GPU

In an ideal case, your program should have high GPU utilization, minimal CPU
(host) to GPU (device) communication, and no overhead from the input pipeline.
The first step in analyzing performance is to get a profile for a model running
with one GPU.

The [Overview Page](https://www.tensorflow.org/guide/profiler#overview_page) of
the TensorFlow Profiler provides an idea of how far away your program is from
the ideal scenario.

![TensorFlow Profiler Overview Page](images/gpu_perf_analysis/overview_page.png "The overview page of the TensorFlow Profiler")

The key numbers to look for on the overview page are:

1.  How much of the step time is from actual device execution
2.  The percentage of ops placed on device vs host
3.  How many kernels use fp16

Achieving optimal performance means maximizing these numbers in all three cases.
To get an in-depth understanding of your program, you will need to be familiar
with the TensorFlow Profiler
[trace viewer](https://www.tensorflow.org/guide/profiler#trace_viewer). The
sections below show some common trace viewer patterns that you should look for
when diagnosing performance bottlenecks.

Below is an image of a model trace view running on 1 GPU. From the _Tensorflow
Name Scope_ and _Tensorflow Ops_ sections, you can identify different parts of
the model, like the forward pass, the loss function, backward pass/gradient
calculation, and the optimizer weight update. You can also see ops running on
the GPU next to each _Stream_, which refer to CUDA streams. Each stream is used
for specific tasks. In this trace, _Stream#118_ is used to launch compute
kernels and device to device copies. _Stream#119_ is used for host to device
copy and *Stream#120* for device to host copy.

The trace below shows common characteristics of a performant model.

![image](images/gpu_perf_analysis/traceview_ideal.png "An example TensorFlow Profiler trace view")

For example, the GPU compute timeline (_Stream#118_) looks busy with very few
gaps. There are minimal copies from host to device (_Stream #119_) and from
device to host (_Stream #120_), as well as minimal gaps between steps. When you
run the TensorFlow Profiler for your program, you might not see these ideal
characteristics in your trace view. The rest of this guide covers common
scenarios and how to fix them.

### Debug Input Pipeline

The first step in GPU performance debugging is to determine if your program is
input-bound. The easiest way to figure this out is to use the TensorFlow
Profiler’s
[Input-Pipeline Analyzer](https://www.tensorflow.org/guide/profiler#input_pipeline_analyzer),
which gives an overview of time spent in the input pipeline.

![image](images/gpu_perf_analysis/input_pipeline_analyzer.png "TensorFlow Profiler Input-Analyzer")

The following are potential actions you can take if your input-pipeline
contributes significantly to step time:

*   Refer to the `tf.data` specific
    [guide](https://www.tensorflow.org/guide/data_performance_analysis) to learn
    how to debug your input pipeline.
*   Another quick way to check if the input pipeline is the bottleneck is to use
    randomly generated input data that does not need any pre-processing.
    [Here is an example](https://github.com/tensorflow/models/blob/4a5770827edf1c3974274ba3e4169d0e5ba7478a/official/vision/image_classification/resnet/resnet_runnable.py#L50-L57)
    of using this technique for a ResNet model. If the input pipeline is optimal
    you should see similar performance with real data and with generated
    random/synthetic data. The only overhead in the synthetic data case will be
    due to input data copy which again can be prefetched and optimized.

Also see the guidance
[here](https://www.tensorflow.org/guide/profiler#optimize_the_input_data_pipeline).

### Debug Performance of 1 GPU

There are several factors that can contribute to low GPU utilization. Below are
some scenarios commonly observed when looking at the trace viewer and potential
solutions.

#### Analyze Gaps Between Steps

A common observation when your program is not running optimally is gaps between
training steps. In the image below, there is a large gap between steps 8 and 9,
meaning that the GPU is idle during that time.

![image](images/gpu_perf_analysis/traceview_step_gaps.png "TensorFlow Profile trace view showing gaps between steps")

If your trace viewer shows large gaps between steps, this could be an indication
that your program is input bound. In that case you should refer to the previous
section on debugging your input pipeline if you have not already done so.
However, even with an optimized input pipeline, you can still see gaps between
the end of one step and the start of another due to CPU thread contention.
`tf.data` makes use of background threads to parallelize pipeline processing.
These threads may interfere with GPU host-side activity that happens at the
beginning of each step, such as copying data or scheduling GPU operations.

If you see large gaps on the host side, which schedules these ops on the GPU,
you can set the environment variable `TF_GPU_THREAD_MODE=gpu_private`. This
ensures that GPU kernels are launched from their own dedicated threads, and
don't get queued behind `tf.data` work.

Gaps between steps can also be caused by metric calculations, Keras callbacks,
or ops outside of `tf.function` that run on the host. These ops don’t have as
good performance as the ops inside a TensorFlow graph. Additionally, some of
these ops run on the CPU and copy tensors back and forth from the GPU.

If after optimizing your input pipeline you still notice gaps between steps in
the trace viewer, you should look at the model code between steps, and see if
disabling callbacks/metrics improves performance. Some details of these ops are
also on the trace viewer (both device and host side).The recommendation in this
scenario is to amortize the overhead of these ops by executing them after a
fixed number of steps instead of every step. When using the `compile` method in
the `tf.keras` API, setting the `experimental_steps_per_execution` flag does
this automatically. For custom training loops, use `tf.while_loop`.

#### Achieve Higher Device Utilization

##### Small GPU Kernels and Host Kernel Launch Delays

The host enqueues kernels to be run on the GPU, but there is a latency (around
20-40 μs) involved before kernels are actually executed on the GPU. In an ideal
case, the host enqueues enough kernels on the GPU such that the GPU spends most
of its time executing, rather than waiting on the host to enqueue more kernels.

The TensorFlow Profiler's
[Overview Page](https://www.tensorflow.org/guide/profiler#overview_page) shows
how much time the GPU was idle due to waiting on the host to launch kernels. In
the image below, the GPU is idle for about 10% of the step time waiting on
kernels to be launched.

![image](images/gpu_perf_analysis/performance_summary.png "Summary of performance from TensorFlow Profile")

The trace viewer for this same program shows small gaps between kernels where
the host is busy launching kernels on the GPU.

![image](images/gpu_perf_analysis/traceview_kernel_gaps.png "TensorFlow Profile trace view demonstrating gaps between kernels")

By launching a lot of small ops on the GPU (like a scalar add for example), the
host might not keep up with the GPU. The
[Tensorflow Stats](https://www.tensorflow.org/guide/profiler#tensorflow_stats)
page for the same TensorFlow Profile shows 126,224 Mul operations taking 2.77
seconds. Thus, each kernel is about 21.9 μs, which is very small (around the
same time as launch latency) and can potentially result in host kernel launch
delays.

![image](images/gpu_perf_analysis/tensorflow_stats_page.png "TensorFlow Profile stats page")

If your trace viewer shows many small gaps between ops on the GPU like the image
above, you can:

*   Concatenate small tensors and use vectorized ops or use a larger batch size
    to make each launched kernel do more work, which will keep the GPU busy for
    longer.
*   Make sure you are using `tf.function` to create TF graphs and not running
    ops in a pure eager mode. Using `tf.keras.Model.compile` automatically does
    this.
*   Fuse kernels using XLA. For more details, see the
    [section](#enable_mixed_precision_and_xla) below on how to enable XLA to get
    higher performance. This is an experimental feature, but leads to high
    device utilization.

##### Tensorflow Op Placement

The TensorFlow Profiler
[Overview Page](https://www.tensorflow.org/guide/profiler#overview_page) tells
you the percentage of ops placed on the host vs device (you can also verify the
placement of specific ops by looking at the trace viewer). Like in the image
below, you want the percentage of ops on the host to be very small compared to
the device.

![image](images/gpu_perf_analysis/opp_placement.png "TF Op Placement")

Ideally most of the compute intensive ops should be placed on the GPU. To find
out which devices the operations and tensors in your model are assigned to, set
`tf.debugging.set_log_device_placement(True)` as the first statement of your
program. Note that in some cases, even if you specify an op to be placed on a
particular device, its implementation might override this condition
(example:`tf.unique`). Even for single GPU training, specifying a distribution
strategy, such as `tf.distribute.OneDeviceStrategy`, can result in more
deterministic placement of ops on your device.

One reason for having the majority of ops placed on the GPU is to prevent
excessive memory copies between host and device (memory copies for model
input/output data between host and device are expected). An example of excessive
copying can be seen in the trace view below on GPU streams _#167_, _#168_, and
_#169_.

![image](images/gpu_perf_analysis/traceview_excessive_copy.png "TensorFlow Profile trace view demonstrating excessive H2D/D2H copies")

These copies can sometimes hurt performance if they block GPU kernels from
executing. Memory copy operations in the trace viewer have more information
about the ops that are the source of these copied tensors, but it might not
always be easy to associate a memCopy with an op. In these cases, it is helpful
to look at the ops nearby to see if the memory copy happens at the same location
in every step.

#### More Efficient Kernels on GPUs

Once your program's GPU utilization is acceptable, the next step is to look into
increasing the efficiency of the GPU kernels by utilizing Tensor Cores or fusing
ops.

##### Utilize Tensor Cores

Modern GPUs have specialized tensor cores that can significantly improve the
performance of kernels that are eligible. The
[GPU kernel stats page](https://www.tensorflow.org/guide/profiler#gpu_kernel_stats)
indicates which GPU kernels are Tensor Core eligible, and which kernels are
using the Tensor Core. Enabling `fp16` (see Enabling Mixed Precision section
below) is one way to make your program’s General Matrix Multiply (GEMM) kernels
(matmul ops) utilize the Tensor Core. GPU kernels use the Tensor Cores
efficiently when the precision is fp16 and input/output tensor dimensions are
divisible by 8 or 16 (for `int8`).

Note: With cuDNN v7.6.3 and later, convolution dimensions will automatically be
padded where necessary to leverage Tensor Cores.

For other detailed recommendations on how to make kernels efficient for GPUs,
refer to the
[NVIDIA Deep Learning Performance](https://docs.nvidia.com/deeplearning/performance/index.html#perf-guidelines)
guide.

##### Fuse ops

Use `tf.xla.experimental_compile` to fuse smaller ops to form bigger kernels
leading to significant performance gains.

### Enable mixed precision and XLA

After following the above steps, enabling mixed precision and XLA are two
optional steps you can take to improve performance further. The suggested
approach is to enable them one by one and verify that the performance benefits
are as expected.

#### Enable Mixed Precision

The TensorFlow
[Mixed Precision](https://www.tensorflow.org/guide/keras/mixed_precision) guide
shows how to enable `fp16` precision on GPUs. Enable
[AMP](https://developer.nvidia.com/automatic-mixed-precision) on NVIDIA® GPUs to
use Tensor Cores and realize up to 3x overall speedups when compared to using
just `fp32` precision on Volta and newer GPU architectures.

Ensure that matrix/tensor dimensions satisfy requirements for calling kernels
that use Tensor Cores. GPU kernels use the Tensor Cores efficiently when the
precision is fp16 and input/output dimensions are divisible by 8 or 16 (for
int8). Note that with cuDNN v7.6.3 and later, convolution dimensions will
automatically be padded where necessary to leverage Tensor Cores.

Follow the best practices below to maximize the performance benefits of `fp16`
precision.

##### Use optimal fp16 Kernels

With `fp16` enabled, your program’s matrix multiplications (GEMM) kernels,
should use the corresponding `fp16` version that utilizes the Tensor Cores.
However, in some cases, this does not happen and you do not see the expected
speedup from enabling `fp16`, as your program falls back to the inefficient
implementation instead.

![image](images/gpu_perf_analysis/gpu_kernels.png "TensorFlow Profile GPU Kernel Stats page")

The [GPU kernel](https://www.tensorflow.org/guide/profiler#gpu_kernel_stats)
stats page shows which ops are Tensor Core eligible and which kernels are
actually using the efficient Tensor Core. The
[NVIDIA guide on deep learning performance](https://docs.nvidia.com/deeplearning/performance/mixed-precision-training/index.html#opt-tensor-cores)
contains additional suggestions on how to leverage Tensor Cores. Additionally,
the benefits of using `fp16` will also show in kernels that were previously
memory bound, as now the ops will take half the time.

##### Dynamic vs Static Loss Scaling

Loss scaling is necessary when using `fp16` to prevent underflow due to low
precision. There are two types of loss scaling, dynamic and static, both of
which are explained in greater detail in the
[Mixed Precision guide](https://www.tensorflow.org/guide/keras/mixed_precision).
You can use the `mixed_float16` policy to automatically enable loss scaling
within the Keras optimizer.

Note: The Keras mixed precision API defaults to evaluating standalone softmax
ops (ops not part of a Keras loss function) as `fp16` which can lead to
numerical issues and poor convergence. Cast such ops to `fp32` for optimal
performance.

When trying to optimize performance, it is important to remember that dynamic
loss scaling can introduce additional conditional ops that run on the host, and
lead to gaps that will be visible between steps in the trace viewer. On the
other hand, static loss scaling does not have such overheads and can be a better
option in terms of performance with the catch that you need to specify the
correct static-loss scale value.

#### Enable XLA

As a final step in getting the best performance with a single GPU, you can
experiment with enabling XLA, which will fuse ops and lead to better device
utilization and a lower memory footprint. For details on how to enable XLA in
your program, refer to the [guide](https://www.tensorflow.org/xla).

You can set the global JIT level to `-1` (off), `1`, or `2`. A higher level is
more aggressive and may reduce parallelism and use more memory. Set the value to
`1` if you have memory restrictions. Note that XLA does not perform well for
models with variable input tensor shapes as the XLA compiler would have to keep
compiling kernels whenever it encounters new shapes.

## Optimize Performance on Multi-GPU Single Host

The `tf.distribute.MirroredStrategy` API can be used to scale model training
from 1 GPU to multiple GPUs on a single host. To learn more about how to do
distributed training with Tensorflow, please refer to the
[Distributed training with Keras](https://www.tensorflow.org/tutorials/distribute/keras)
guide. Although the transition from one GPU to multiple GPUs should ideally be
scalable out of the box, you can sometimes encounter performance issues.

When going from training with a single GPU to multiple GPUs on the same host,
ideally you should see performance scaling with only the additional overhead of
gradient communication and increased host thread utilization. Because of this
overhead, you will not see an exact 2x speedup if you move from 1 to 2 GPUs for
example. The trace view below shows an example of the extra communication
overhead when training on multiple GPUs. There is some overhead to concatenate
the gradients, communicate them across replicas, and split them before doing the
weight update.

![image](images/gpu_perf_analysis/traceview_multi_gpu.png "TensorFlow Profile trace view for single host multi GPU scenario")

The following checklist will help you to achieve better performance when
optimizing performance in the multi-GPU scenario:

1.  Try to maximize the batch size, which will lead to higher device utilization
    and amortize the costs of communication across multiple GPUs. Using the
    [memory profiler](https://www.tensorflow.org/guide/profiler#memory_profile_summary)
    helps get a sense of how close your program is to peak memory utilization.
    Note that while a higher batch size can affect convergence, this is usually
    outweighed by the performance benefits.
2.  When moving from a single GPU to multiple GPUs, the same host now has to
    process much more input data. So after (1) it is recommended to re-check the
    input pipeline performance and make sure it is not a bottleneck.
3.  Check the GPU timeline in your program's trace view to see if there are
    unnecessary AllReduce calls, as this results in a synchronization across all
    devices. In the trace view shown above, the AllReduce is done via the NCCL
    kernel, and there is only one NCCL call on each GPU for the gradients on
    each step.
4.  Check for unnecessary D2H, H2D and D2D copy operations and see if they can
    be minimized.
5.  Check the step time to make sure each replica is doing the same work. It can
    happen that one GPU (typically GPU0) is oversubscribed because the host
    mistakenly ends up putting more work on it.
6.  Lastly, check the training step across all GPUs in your trace view for any
    ops that are executing sequentially. This usually happens when your program
    includes control dependencies from one GPU to another. Debugging performance
    in this situation has been solved on a case-by-case basis in the past. If
    you observe this behavior in your program,
    [file a Github issue](https://github.com/tensorflow/tensorflow/issues/new/choose)
    with images of your trace view.

#### Optimize Gradient AllReduce

When training with a synchronous strategy, each device receives a portion of the
input data. After computing the forward and backwards passes through the model,
the gradients calculated on each device need to be aggregated and reduced. This
gradient AllReduce happens after the gradient calculation on each device, and
before the optimizer updates the model weights. Each GPU first concatenates the
gradients across the model layers, communicates them across GPUs using
`tf.distribute.CrossDeviceOps` (`tf.distribute.NcclAllReduce` is the default),
and then returns the gradients after reduction per layer. The optimizer will use
these reduced gradients to update the weights of your model. Ideally, this
process should happen at the same time on all GPUs to prevent any overheads. The
time to AllReduce should be approximately the same as:

```
(number of parameters * 4bytes)/ (communication bandwidth)
```

This calculation is useful as a quick check to understand whether the
performance you see when running a distributed training job is as expected, or
if you need to do further performance debugging. You can get the number of
parameters in your model from `tf.keras.Model.summary`.

Note that each model parameter is 4 bytes since Tensorflow uses fp32 to
communicate gradients. Even when you have enabled fp16, NCCL AllReduce utilizes
fp32 parameters. In the future, Tensorflow will support AllReduce operations
using fp16, as well as pipelining the gradient AllReduce so it overlaps with the
gradient computation.

To see benefits of scaling, the step-time needs to be much higher compared to
these overheads. One way to achieve this is to use a higher batch size as batch
size affects step time, but does not impact the communication overhead.

#### GPU Host Thread Contention

When running multiple GPUs, the CPU’s job is to keep all of the devices busy by
efficiently launching GPU kernels across the devices. However, when there are a
lot of independent operations that the CPU can schedule on one GPU, the CPU can
decide to use a lot of its host threads to keep one GPU busy, and then launch
kernels on another GPU in a non-deterministic order. This can cause a skew or
negative scaling, which can hurt performance.

The trace viewer below shows the overhead when the CPU staggers GPU kernel
launches inefficiently, as GPU1 is idle and then starts running ops after GPU2
has started.

![image](images/gpu_perf_analysis/traceview_gpu_idle.png "TensorFlow Profile device trace view demonstrating inefficient kernel launch")

The trace view for the host shows that the host is launching kernels on GPU2
before launching them on GPU1 (note that the below tf_Compute* ops are not
indicative of CPU threads).

![image](images/gpu_perf_analysis/traceview_host_contention.png "TensorFlow Profile host trace view demonstrating inefficient kernel launch")

If you see this staggering of GPU kernels in your program’s trace view, the
recommended action is to:

*   Set the TensorFlow environment variable `TF_GPU_THREAD_MODE` to
    `gpu_private`. This environment variable will tell the host to keep threads
    for a GPU private.
*   By default,`TF_GPU_THREAD_MODE=gpu_private` sets the number of threads to 2,
    which is sufficient in most cases. However, that number can be changed by
    setting the TensorFlow environment variable `TF_GPU_THREAD_COUNT` to the
    desired number of threads.
