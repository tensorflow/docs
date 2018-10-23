

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.utils.SequenceEnqueuer

## Class `SequenceEnqueuer`





Defined in [`tensorflow/python/keras/_impl/keras/utils/data_utils.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/python/keras/_impl/keras/utils/data_utils.py).

Base class to enqueue inputs.

The task of an Enqueuer is to use parallelism to speed up preprocessing.
This is done with processes or threads.

Examples:

```python
    enqueuer = SequenceEnqueuer(...)
    enqueuer.start()
    datas = enqueuer.get()
    for data in datas:
        # Use the inputs; training, evaluating, predicting.
        # ... stop sometime.
    enqueuer.close()
```

The `enqueuer.get()` should be an infinite stream of datas.

## Methods

<h3 id="get"><code>get</code></h3>

``` python
get()
```

Creates a generator to extract data from the queue.

Skip the data if it is `None`.

#### Returns:

Generator yielding tuples `(inputs, targets)`
    or `(inputs, targets, sample_weights)`.

<h3 id="is_running"><code>is_running</code></h3>

``` python
is_running()
```



<h3 id="start"><code>start</code></h3>

``` python
start(
    workers=1,
    max_queue_size=10
)
```

Starts the handler's workers.

#### Arguments:

* <b>`workers`</b>: number of worker threads
* <b>`max_queue_size`</b>: queue size
        (when full, threads could block on `put()`).

<h3 id="stop"><code>stop</code></h3>

``` python
stop(timeout=None)
```

Stop running threads and wait for them to exit, if necessary.

Should be called by the same thread which called start().

#### Arguments:

* <b>`timeout`</b>: maximum time to wait on thread.join()



