description: Base class to enqueue inputs.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.utils.SequenceEnqueuer" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="get"/>
<meta itemprop="property" content="is_running"/>
<meta itemprop="property" content="start"/>
<meta itemprop="property" content="stop"/>
</div>

# tf.keras.utils.SequenceEnqueuer

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/utils/data_utils.py#L683-L808">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Base class to enqueue inputs.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.utils.SequenceEnqueuer`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.utils.SequenceEnqueuer(
    sequence, use_multiprocessing=(False)
)
</code></pre>



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
    enqueuer.stop()
```

The `enqueuer.get()` should be an infinite stream of datas.

## Methods

<h3 id="get"><code>get</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/utils/data_utils.py#L799-L808">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get()
</code></pre>

Creates a generator to extract data from the queue.

Skip the data if it is `None`.
# Returns
    Generator yielding tuples `(inputs, targets)`
        or `(inputs, targets, sample_weights)`.

<h3 id="is_running"><code>is_running</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/utils/data_utils.py#L734-L735">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>is_running()
</code></pre>




<h3 id="start"><code>start</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/utils/data_utils.py#L737-L755">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>start(
    workers=1, max_queue_size=10
)
</code></pre>

Starts the handler's workers.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`workers`
</td>
<td>
Number of workers.
</td>
</tr><tr>
<td>
`max_queue_size`
</td>
<td>
queue size
(when full, workers could block on `put()`)
</td>
</tr>
</table>



<h3 id="stop"><code>stop</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/utils/data_utils.py#L762-L776">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>stop(
    timeout=None
)
</code></pre>

Stops running threads and wait for them to exit, if necessary.

Should be called by the same thread which called `start()`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`timeout`
</td>
<td>
maximum time to wait on `thread.join()`
</td>
</tr>
</table>





