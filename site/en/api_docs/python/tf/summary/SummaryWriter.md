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
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/summary_ops_v2.py#L202-L226">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Interface representing a stateful summary writer object.

<!-- Placeholder for "Used in" -->


## Methods

<h3 id="as_default"><code>as_default</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/summary_ops_v2.py#L210-L214">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@abc.abstractmethod</code>
<code>@tf_contextlib.contextmanager</code>
<code>as_default()
</code></pre>

Returns a context manager that enables summary writing.


<h3 id="close"><code>close</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/summary_ops_v2.py#L224-L226">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>close()
</code></pre>

Flushes and closes the summary writer.


<h3 id="flush"><code>flush</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/summary_ops_v2.py#L220-L222">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>flush()
</code></pre>

Flushes any buffered data.


<h3 id="init"><code>init</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/summary_ops_v2.py#L216-L218">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>init()
</code></pre>

Initializes the summary writer.


<h3 id="set_as_default"><code>set_as_default</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/summary_ops_v2.py#L205-L208">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@abc.abstractmethod</code>
<code>set_as_default()
</code></pre>

Enables this summary writer for the current thread.




