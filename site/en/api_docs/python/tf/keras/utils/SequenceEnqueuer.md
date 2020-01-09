page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.utils.SequenceEnqueuer


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/utils/data_utils.py#L575-L696">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `SequenceEnqueuer`

Base class to enqueue inputs.



### Aliases:

* Class `tf.compat.v1.keras.utils.SequenceEnqueuer`
* Class `tf.compat.v2.keras.utils.SequenceEnqueuer`


<!-- Placeholder for "Used in" -->

The task of an Enqueuer is to use parallelism to speed up preprocessing.
This is done with processes or threads.

#### Example:



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

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/utils/data_utils.py#L596-L624">View source</a>

``` python
__init__(
    sequence,
    use_multiprocessing=False
)
```

Initialize self.  See help(type(self)) for accurate signature.




## Methods

<h3 id="get"><code>get</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/utils/data_utils.py#L687-L696">View source</a>

``` python
get()
```

Creates a generator to extract data from the queue.

Skip the data if it is `None`.
# Returns
    Generator yielding tuples `(inputs, targets)`
        or `(inputs, targets, sample_weights)`.

<h3 id="is_running"><code>is_running</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/utils/data_utils.py#L626-L627">View source</a>

``` python
is_running()
```




<h3 id="start"><code>start</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/utils/data_utils.py#L629-L647">View source</a>

``` python
start(
    workers=1,
    max_queue_size=10
)
```

Starts the handler's workers.


#### Arguments:


* <b>`workers`</b>: Number of workers.
* <b>`max_queue_size`</b>: queue size
    (when full, workers could block on `put()`)

<h3 id="stop"><code>stop</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/utils/data_utils.py#L654-L668">View source</a>

``` python
stop(timeout=None)
```

Stops running threads and wait for them to exit, if necessary.

Should be called by the same thread which called `start()`.

#### Arguments:


* <b>`timeout`</b>: maximum time to wait on `thread.join()`
