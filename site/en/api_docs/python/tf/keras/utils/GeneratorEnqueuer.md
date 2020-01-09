page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.utils.GeneratorEnqueuer


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/utils/GeneratorEnqueuer">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/utils/data_utils.py#L836-L922">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `GeneratorEnqueuer`

Builds a queue out of a data generator.

Inherits From: [`SequenceEnqueuer`](../../../tf/keras/utils/SequenceEnqueuer)

### Aliases:

* Class <a href="/api_docs/python/tf/keras/utils/GeneratorEnqueuer"><code>tf.compat.v1.keras.utils.GeneratorEnqueuer</code></a>
* Class <a href="/api_docs/python/tf/keras/utils/GeneratorEnqueuer"><code>tf.compat.v2.keras.utils.GeneratorEnqueuer</code></a>


<!-- Placeholder for "Used in" -->

The provided generator can be finite in which case the class will throw
a `StopIteration` exception.

Used in `fit_generator`, `evaluate_generator`, `predict_generator`.

#### Arguments:


* <b>`generator`</b>: a generator function which yields data
* <b>`use_multiprocessing`</b>: use multiprocessing if True, otherwise threading
* <b>`wait_time`</b>: time to sleep in-between calls to `put()`
* <b>`random_seed`</b>: Initial seed for workers,
    will be incremented by one for each worker.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/utils/data_utils.py#L852-L856">View source</a>

``` python
__init__(
    sequence,
    use_multiprocessing=False,
    random_seed=None
)
```

Initialize self.  See help(type(self)) for accurate signature.




## Methods

<h3 id="get"><code>get</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/utils/data_utils.py#L886-L922">View source</a>

``` python
get()
```

Creates a generator to extract data from the queue.

Skip the data if it is `None`.

#### Yields:

The next element in the queue, i.e. a tuple
`(inputs, targets)` or
`(inputs, targets, sample_weights)`.


<h3 id="is_running"><code>is_running</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/utils/data_utils.py#L626-L627">View source</a>

``` python
is_running()
```




<h3 id="start"><code>start</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/utils/data_utils.py#L629-L647">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/utils/data_utils.py#L654-L668">View source</a>

``` python
stop(timeout=None)
```

Stops running threads and wait for them to exit, if necessary.

Should be called by the same thread which called `start()`.

#### Arguments:


* <b>`timeout`</b>: maximum time to wait on `thread.join()`
