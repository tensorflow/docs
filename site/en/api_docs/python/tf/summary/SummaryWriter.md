description: Interface representing a stateful summary writer object.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.summary.SummaryWriter" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="as_default"/>
<meta itemprop="property" content="close"/>
<meta itemprop="property" content="flush"/>
<meta itemprop="property" content="init"/>
<meta itemprop="property" content="set_as_default"/>
</div>

# tf.summary.SummaryWriter

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/summary_ops_v2.py#L202-L269">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Interface representing a stateful summary writer object.

<!-- Placeholder for "Used in" -->


## Methods

<h3 id="as_default"><code>as_default</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/summary_ops_v2.py#L226-L257">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@abc.abstractmethod</code>
<code>@tf_contextlib.contextmanager</code>
<code>as_default(
    step=None
)
</code></pre>

Returns a context manager that enables summary writing.

For convenience, if `step` is not None, this function also sets a default
value for the `step` parameter used in summary-writing functions elsewhere
in the API so that it need not be explicitly passed in every such
invocation. The value can be a constant or a variable.

Note: when setting `step` in a @tf.function, the step value will be
captured at the time the function is traced, so changes to the step outside
the function will not be reflected inside the function unless using
a <a href="../../tf/Variable.md"><code>tf.Variable</code></a> step.

For example, `step` can be used as:

```python
with writer_a.as_default(step=10):
  tf.summary.scalar(tag, value)   # Logged to writer_a with step 10
  with writer_b.as_default(step=20):
    tf.summary.scalar(tag, value) # Logged to writer_b with step 20
  tf.summary.scalar(tag, value)   # Logged to writer_a with step 10
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`step`
</td>
<td>
An `int64`-castable default step value, or `None`. When not `None`,
the current step is captured, replaced by a given one, and the original
one is restored when the context manager exits. When `None`, the current
step is not modified (and not restored when the context manager exits).
</td>
</tr>
</table>



<h3 id="close"><code>close</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/summary_ops_v2.py#L267-L269">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>close()
</code></pre>

Flushes and closes the summary writer.


<h3 id="flush"><code>flush</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/summary_ops_v2.py#L263-L265">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>flush()
</code></pre>

Flushes any buffered data.


<h3 id="init"><code>init</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/summary_ops_v2.py#L259-L261">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>init()
</code></pre>

Initializes the summary writer.


<h3 id="set_as_default"><code>set_as_default</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/summary_ops_v2.py#L205-L224">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@abc.abstractmethod</code>
<code>set_as_default(
    step=None
)
</code></pre>

Enables this summary writer for the current thread.

For convenience, if `step` is not None, this function also sets a default
value for the `step` parameter used in summary-writing functions elsewhere
in the API so that it need not be explicitly passed in every such
invocation. The value can be a constant or a variable.

Note: when setting `step` in a @tf.function, the step value will be
captured at the time the function is traced, so changes to the step outside
the function will not be reflected inside the function unless using
a <a href="../../tf/Variable.md"><code>tf.Variable</code></a> step.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`step`
</td>
<td>
An `int64`-castable default step value, or `None`. When not `None`,
the current step is modified to the given value. When `None`, the
current step is not modified.
</td>
</tr>
</table>





