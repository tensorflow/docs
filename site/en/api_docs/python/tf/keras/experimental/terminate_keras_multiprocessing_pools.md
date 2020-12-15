description: Destroy Keras' multiprocessing pools to prevent deadlocks. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.experimental.terminate_keras_multiprocessing_pools" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.experimental.terminate_keras_multiprocessing_pools

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/utils/data_utils.py#L556-L662">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Destroy Keras' multiprocessing pools to prevent deadlocks. (deprecated)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.experimental.terminate_keras_multiprocessing_pools`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.experimental.terminate_keras_multiprocessing_pools(
    grace_period=0.1, use_sigkill=(False)
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2020-06-07.
Instructions for updating:
Please manage pools using the standard Python lib.

In general multiprocessing.Pool can interact quite badly with other, seemingly
unrelated, parts of a codebase due to Pool's reliance on fork. This method
cleans up all pools which are known to belong to Keras (and thus can be safely
terminated).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`grace_period`
</td>
<td>
Time (in seconds) to wait for process cleanup to propagate.
</td>
</tr><tr>
<td>
`use_sigkill`
</td>
<td>
Boolean of whether or not to perform a cleanup pass using
SIGKILL.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A list of human readable strings describing all issues encountered. It is up
to the caller to decide whether to treat this as an error condition.
</td>
</tr>

</table>

