description: Callback used to stream events to a server.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.callbacks.RemoteMonitor" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="set_model"/>
<meta itemprop="property" content="set_params"/>
</div>

# tf.keras.callbacks.RemoteMonitor

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/callbacks.py#L1795-L1854">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Callback used to stream events to a server.

Inherits From: [`Callback`](../../../tf/keras/callbacks/Callback.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.callbacks.RemoteMonitor`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.callbacks.RemoteMonitor(
    root='http://localhost:9000', path='/publish/epoch/end/', field='data',
    headers=None, send_as_json=(False)
)
</code></pre>



<!-- Placeholder for "Used in" -->

Requires the `requests` library.
Events are sent to `root + '/publish/epoch/end/'` by default. Calls are
HTTP POST, with a `data` argument which is a
JSON-encoded dictionary of event data.
If `send_as_json=True`, the content type of the request will be
`"application/json"`.
Otherwise the serialized JSON will be sent within a form.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`root`
</td>
<td>
String; root url of the target server.
</td>
</tr><tr>
<td>
`path`
</td>
<td>
String; path relative to `root` to which the events will be sent.
</td>
</tr><tr>
<td>
`field`
</td>
<td>
String; JSON field under which the data will be stored.
The field is used only if the payload is sent within a form
(i.e. send_as_json is set to False).
</td>
</tr><tr>
<td>
`headers`
</td>
<td>
Dictionary; optional custom HTTP headers.
</td>
</tr><tr>
<td>
`send_as_json`
</td>
<td>
Boolean; whether the request should be
sent as `"application/json"`.
</td>
</tr>
</table>



## Methods

<h3 id="set_model"><code>set_model</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/callbacks.py#L633-L634">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>set_model(
    model
)
</code></pre>




<h3 id="set_params"><code>set_params</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/callbacks.py#L630-L631">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>set_params(
    params
)
</code></pre>






