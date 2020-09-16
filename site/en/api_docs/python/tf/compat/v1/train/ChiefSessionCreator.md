description: Creates a tf.compat.v1.Session for a chief.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.train.ChiefSessionCreator" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="create_session"/>
</div>

# tf.compat.v1.train.ChiefSessionCreator

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/monitored_session.py#L619-L669">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Creates a tf.compat.v1.Session for a chief.

Inherits From: [`SessionCreator`](../../../../tf/compat/v1/train/SessionCreator.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.train.ChiefSessionCreator(
    scaffold=None, master='', config=None, checkpoint_dir=None,
    checkpoint_filename_with_path=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`scaffold`
</td>
<td>
A `Scaffold` used for gathering or building supportive ops. If
not specified a default one is created. It's used to finalize the graph.
</td>
</tr><tr>
<td>
`master`
</td>
<td>
`String` representation of the TensorFlow master to use.
</td>
</tr><tr>
<td>
`config`
</td>
<td>
`ConfigProto` proto used to configure the session.
</td>
</tr><tr>
<td>
`checkpoint_dir`
</td>
<td>
A string.  Optional path to a directory where to restore
variables.
</td>
</tr><tr>
<td>
`checkpoint_filename_with_path`
</td>
<td>
Full file name path to the checkpoint file.
</td>
</tr>
</table>



## Methods

<h3 id="create_session"><code>create_session</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/monitored_session.py#L659-L669">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>create_session()
</code></pre>






