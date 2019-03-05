# Using GPUs

## Supported devices

TensorFlow supports running computations on a variety of types of devices,
including `CPU` and `GPU`. They are represented with `strings`, for example:

*   `"/cpu:0"`: The CPU of your machine.
*   `"/device:GPU:0"`: The first GPU of your machine that is visible to
TensorFlow
*   `"/device:GPU:1"`: The second GPU of your machine that is visible to
TensorFlow, etc.

If a TensorFlow operation has both CPU and GPU implementations, by default the
GPU devices will be given priority when the operation is assigned to a device.
For example, `matmul` has both CPU and GPU kernels. On a system with devices
`cpu:0` and `gpu:0`, `gpu:0` will be selected to run `matmul` unless you
explicitly request running it on another device.


## Logging device placement

To find out which devices your operations and tensors are assigned to, put
`tf.debugging.set_log_device_placement(True)` as the first statement of your
program.

```python
tf.debugging.set_log_device_placement(True)

# Creates some tensors
a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
c = tf.matmul(a, b)
print(c)
```

You should see the following output:

```
Executing op MatMul in device /job:localhost/replica:0/task:0/device:CPU:0
tf.Tensor(
[[22. 28.]
 [49. 64.]], shape=(2, 2), dtype=float32)
```

## Manual device placement

If you would like a particular operation to run on a device of your choice
instead of what's automatically selected for you, you can use `with tf.device`
to create a device context, and all the operations within that context will
run on the same designated device.

```python
tf.debugging.set_log_device_placement(True)

# Place tensors on the CPU
with tf.device('/cpu:0'):
  a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
  b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
c = tf.matmul(a, b)
print(c)
```

You will see that now `a` and `b` are assigned to `cpu:0`. Since a device was
not explicitly specified for the `MatMul` operation, the TensorFlow runtime will
choose one based on the operation and available devices (`cpu:0` in this
example) and automatically copy tensors between devices if required.

```
Executing op MatMul in device /job:localhost/replica:0/task:0/device:CPU:0
tf.Tensor(
[[22. 28.]
 [49. 64.]], shape=(2, 2), dtype=float32)
```

## Allowing GPU memory growth

By default, TensorFlow maps nearly all of the GPU memory of all GPUs (subject to
[`CUDA_VISIBLE_DEVICES`](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#env-vars))
visible to the process. This is done to more efficiently use the relatively
precious GPU memory resources on the devices by reducing [memory
fragmentation](https://en.wikipedia.org/wiki/Fragmentation_\(computing\)).

In some cases it is desirable for the process to only allocate a subset of the
available memory, or to only grow the memory usage as is needed by the process.
TensorFlow provides two methods to control this.

The first option is to turn on memory growth by calling
`tf.config.gpu.set_per_process_memory_growth()` method, which attempts to
allocate only as much GPU memory in needed for the runtime allocations: it
starts out allocating very little memory, and as the program gets run and more
GPU memory is needed, we extend the GPU memory region allocated to the
TensorFlow process. Note that we do not release memory, since that can lead to
even worse memory fragmentation. To turn process memory growth on, put this as
the first statement of your program:

```python
tf.config.gpu.set_per_process_memory_growth()
```

The second method is `tf.gpu.set_per_process_memory_fraction()`, which
determines the fraction of the overall amount of memory that each visible GPU
should be allocated. For example, you can tell TensorFlow to only allocate 40%
of the total memory of each GPU by:

```python
tf.config.gpu.set_per_process_memory_fraction(0.4)
```

This is useful if you want to truly bound the amount of GPU memory available to
the TensorFlow process.

## Using a single GPU on a multi-GPU system

If you have more than one GPU in your system, the GPU with the lowest ID will be
selected by default. If you would like to run on a different GPU, you will need
to specify the preference explicitly:

```python
tf.debugging.set_log_device_placement(True)

# Specify a device
with tf.device('/device:GPU:2'):
  a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
  b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
  c = tf.matmul(a, b)

print(c)
```

If the device you have specified does not exist, you will get
`RuntimeError`:

```
RuntimeError: Error copying tensor to device: /job:localhost/replica:0/task:0/device:GPU:2. /job:localhost/replica:0/task:0/device:GPU:2 unknown device.
```

If you would like TensorFlow to automatically choose an existing and supported
device to run the operations in case the specified one doesn't exist, you can
call `tf.config.set_soft_device_placement(True)`.

```python
tf.config.set_soft_device_placement(True)
tf.debugging.set_log_device_placement(True)

# Creates some tensors
with tf.device('/device:GPU:2'):
  a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
  b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
  c = tf.matmul(a, b)

print(c)
```

## Using multiple GPUs

#### With `tf.distribute.Strategy`

The best practice for using multiple GPUs is to use `tf.distribute.Strategy`.
Here is a simple example:

```python
strategy = tf.distribute.MirroredStrategy()

with strategy.scope():
  inputs = tf.keras.layers.Input(shape=(1,))
  predictions = tf.keras.layers.Dense(1)(inputs)
  model = tf.keras.models.Model(inputs=inputs, outputs=predictions)
  model.compile(loss='mse',
                optimizer=tf.train.GradientDescentOptimizer(learning_rate=0.2))
```

This program will run a copy of your model on each GPU, splitting the input data
between them, also known as "[data parallelism](https://en.wikipedia.org/wiki/Data_parallelism)".

For more information about distribution strategies, check out the guide
[here](./distribute_strategy.ipynb).


#### Without `tf.distribute.Strategy`

`tf.distribute.Strategy` works under the hood by replicating computation across
devices. You can manually implement replication by constructing your model on
each GPU. For example:


``` python
tf.debugging.set_log_device_placement(True)

# Replicate your computation on multiple GPUs
c = []
for d in ['/device:GPU:2', '/device:GPU:3']:
  with tf.device(d):
    a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3])
    b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2])
    c.append(tf.matmul(a, b))
with tf.device('/cpu:0'):
  sum = tf.add_n(c)

print(sum)
```

You will see the following output.

```
Executing op MatMul in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op MatMul in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op AddN in device /job:localhost/replica:0/task:0/device:CPU:0
tf.Tensor(
[[ 44.  56.]
 [ 98. 128.]], shape=(2, 2), dtype=float32)
```
