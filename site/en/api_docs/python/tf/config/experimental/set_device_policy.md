description: Sets the current thread device policy.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.config.experimental.set_device_policy" />
<meta itemprop="path" content="Stable" />
</div>

# tf.config.experimental.set_device_policy

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/config.py#L253-L293">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Sets the current thread device policy.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.config.experimental.set_device_policy`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.config.experimental.set_device_policy(
    device_policy
)
</code></pre>



<!-- Placeholder for "Used in" -->

The device policy controls how operations requiring inputs on a specific
device (e.g., on GPU:0) handle inputs on a different device (e.g. GPU:1).

When using the default, an appropriate policy will be picked automatically.
The default policy may change over time.

This function only sets the device policy for the current thread. Any
subsequently started thread will again use the default policy.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`device_policy`
</td>
<td>
A device policy.
Valid values:
- None: Switch to a system default.
- 'warn': Copies the tensors which are not on the right device and logs
a warning.
- 'explicit': Raises an error if the placement is not as required.
- 'silent': Silently copies the tensors. Note that this may hide
performance problems as there is no notification provided when
operations are blocked on the tensor being copied between devices.
- 'silent_for_int32': silently copies `int32` tensors, raising errors on
the other ones.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If an invalid `device_policy` is passed.
</td>
</tr>
</table>

