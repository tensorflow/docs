description: Contains the results of Session.run().

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.estimator.SessionRunValues" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="options"/>
<meta itemprop="property" content="results"/>
<meta itemprop="property" content="run_metadata"/>
</div>

# tf.estimator.SessionRunValues

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/training/session_run_hook.py#L267-L287">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Contains the results of `Session.run()`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.estimator.SessionRunValues`, `tf.compat.v1.train.SessionRunValues`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.estimator.SessionRunValues(
    results, options, run_metadata
)
</code></pre>



<!-- Placeholder for "Used in" -->

In the future we may use this object to add more information about result of
run without changing the Hook API.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`results`
</td>
<td>
The return values from `Session.run()` corresponding to the fetches
attribute returned in the RunArgs. Note that this has the same shape as
the RunArgs fetches.  For example:
fetches = global_step_tensor
=> results = nparray(int)
fetches = [train_op, summary_op, global_step_tensor]
=> results = [None, nparray(string), nparray(int)]
fetches = {'step': global_step_tensor, 'summ': summary_op}
=> results = {'step': nparray(int), 'summ': nparray(string)}
</td>
</tr><tr>
<td>
`options`
</td>
<td>
`RunOptions` from the `Session.run()` call.
</td>
</tr><tr>
<td>
`run_metadata`
</td>
<td>
`RunMetadata` from the `Session.run()` call.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`results`
</td>
<td>

</td>
</tr><tr>
<td>
`options`
</td>
<td>

</td>
</tr><tr>
<td>
`run_metadata`
</td>
<td>

</td>
</tr>
</table>



## Class Variables

* `options` <a id="options"></a>
* `results` <a id="results"></a>
* `run_metadata` <a id="run_metadata"></a>
