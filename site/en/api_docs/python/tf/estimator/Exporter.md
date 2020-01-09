page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.estimator.Exporter


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/estimator/Exporter">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/exporter.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `Exporter`

A class representing a type of model export.



### Aliases:

* Class <a href="/api_docs/python/tf/estimator/Exporter"><code>tf.compat.v1.estimator.Exporter</code></a>
* Class <a href="/api_docs/python/tf/estimator/Exporter"><code>tf.compat.v2.estimator.Exporter</code></a>


<!-- Placeholder for "Used in" -->


## Properties

<h3 id="name"><code>name</code></h3>

Directory name.

A directory name under the export base directory where exports of
this type are written.  Should not be `None` nor empty.



## Methods

<h3 id="export"><code>export</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/exporter.py">View source</a>

``` python
export(
    estimator,
    export_path,
    checkpoint_path,
    eval_result,
    is_the_final_export
)
```

Exports the given `Estimator` to a specific format.


#### Args:


* <b>`estimator`</b>: the `Estimator` to export.
* <b>`export_path`</b>: A string containing a directory where to write the export.
* <b>`checkpoint_path`</b>: The checkpoint path to export.
* <b>`eval_result`</b>: The output of <a href="../../tf/estimator/Estimator#evaluate"><code>Estimator.evaluate</code></a> on this checkpoint.
* <b>`is_the_final_export`</b>: This boolean is True when this is an export in the
  end of training.  It is False for the intermediate exports during
  the training.
  When passing `Exporter` to <a href="../../tf/estimator/train_and_evaluate"><code>tf.estimator.train_and_evaluate</code></a>
  `is_the_final_export` is always False if <a href="../../tf/estimator/TrainSpec#max_steps"><code>TrainSpec.max_steps</code></a> is
  `None`.


#### Returns:

The string path to the exported directory or `None` if export is skipped.
