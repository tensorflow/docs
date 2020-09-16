description: A class representing a type of model export.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.estimator.Exporter" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="export"/>
</div>

# tf.estimator.Exporter

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/exporter.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A class representing a type of model export.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.estimator.Exporter`</p>
</p>
</section>

<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`name`
</td>
<td>
Directory name.

A directory name under the export base directory where exports of
this type are written.  Should not be `None` nor empty.
</td>
</tr>
</table>



## Methods

<h3 id="export"><code>export</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/exporter.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@abc.abstractmethod</code>
<code>export(
    estimator, export_path, checkpoint_path, eval_result, is_the_final_export
)
</code></pre>

Exports the given `Estimator` to a specific format.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`estimator`
</td>
<td>
the `Estimator` to export.
</td>
</tr><tr>
<td>
`export_path`
</td>
<td>
A string containing a directory where to write the export.
</td>
</tr><tr>
<td>
`checkpoint_path`
</td>
<td>
The checkpoint path to export.
</td>
</tr><tr>
<td>
`eval_result`
</td>
<td>
The output of <a href="../../tf/compat/v1/estimator/Estimator.md#evaluate"><code>Estimator.evaluate</code></a> on this checkpoint.
</td>
</tr><tr>
<td>
`is_the_final_export`
</td>
<td>
This boolean is True when this is an export in the
end of training.  It is False for the intermediate exports during the
training. When passing `Exporter` to <a href="../../tf/estimator/train_and_evaluate.md"><code>tf.estimator.train_and_evaluate</code></a>
`is_the_final_export` is always False if <a href="../../tf/estimator/TrainSpec.md#max_steps"><code>TrainSpec.max_steps</code></a> is
`None`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The string path to the exported directory or `None` if export is skipped.
</td>
</tr>

</table>





