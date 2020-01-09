page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.utils.OrderedEnqueuer


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/utils/OrderedEnqueuer">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/utils/data_utils.py#L704-L789">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `OrderedEnqueuer`

Builds a Enqueuer from a Sequence.

Inherits From: [`SequenceEnqueuer`](../../../tf/keras/utils/SequenceEnqueuer)

### Aliases:

* Class <a href="/api_docs/python/tf/keras/utils/OrderedEnqueuer"><code>tf.compat.v1.keras.utils.OrderedEnqueuer</code></a>
* Class <a href="/api_docs/python/tf/keras/utils/OrderedEnqueuer"><code>tf.compat.v2.keras.utils.OrderedEnqueuer</code></a>


<!-- Placeholder for "Used in" -->

Used in `fit_generator`, `evaluate_generator`, `predict_generator`.

#### Arguments:


* <b>`sequence`</b>: A `tf.keras.utils.data_utils.Sequence` object.
* <b>`use_multiprocessing`</b>: use multiprocessing if True, otherwise threading
* <b>`shuffle`</b>: whether to shuffle the data at the beginning of each epoch

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/utils/data_utils.py#L715-L717">View source</a>

``` python
__init__(
    sequence,
    use_multiprocessing=False,
    shuffle=False
)
```

Initialize self.  See help(type(self)) for accurate signature.




## Methods

<h3 id="get"><code>get</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/utils/data_utils.py#L771-L789">View source</a>

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
