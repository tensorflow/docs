


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.FIFOQueue.from_list

### `tf.FIFOQueue.from_list`

```
tf.FIFOQueue.from_list(index, queues)
```

### `tf.PaddingFIFOQueue.from_list`

```
tf.PaddingFIFOQueue.from_list(index, queues)
```

### `tf.PriorityQueue.from_list`

```
tf.PriorityQueue.from_list(index, queues)
```

### `tf.QueueBase.from_list`

```
tf.QueueBase.from_list(index, queues)
```

### `tf.RandomShuffleQueue.from_list`

```
tf.RandomShuffleQueue.from_list(index, queues)
```


Create a queue using the queue reference from `queues[index]`.

#### Args:

* <b>`index`</b>: An integer scalar tensor that determines the input that gets
    selected.
* <b>`queues`</b>: A list of `QueueBase` objects.


#### Returns:

  A `QueueBase` object.


#### Raises:

* <b>`TypeError`</b>: When `queues` is not a list of `QueueBase` objects,
    or when the data types of `queues` are not all the same.

Defined in [`tensorflow/python/ops/data_flow_ops.py`](https://www.tensorflow.org/code/tensorflow/python/ops/data_flow_ops.py).

