page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.summary.create_db_writer


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/summary_ops_v2.py#L441-L490">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Creates a summary database writer in the current context.

``` python
tf.contrib.summary.create_db_writer(
    db_uri,
    experiment_name=None,
    run_name=None,
    user_name=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

This can be used to write tensors from the execution graph directly
to a database. Only SQLite is supported right now. This function
will create the schema if it doesn't exist. Entries in the Users,
Experiments, and Runs tables will be created automatically if they
don't already exist.

#### Args:


* <b>`db_uri`</b>: For example "file:/tmp/foo.sqlite".
* <b>`experiment_name`</b>: Defaults to YYYY-MM-DD in local time if None.
  Empty string means the Run will not be associated with an
  Experiment. Can't contain ASCII control characters or <>. Case
  sensitive.
* <b>`run_name`</b>: Defaults to HH:MM:SS in local time if None. Empty string
  means a Tag will not be associated with any Run. Can't contain
  ASCII control characters or <>. Case sensitive.
* <b>`user_name`</b>: Defaults to system username if None. Empty means the
  Experiment will not be associated with a User. Must be valid as
  both a DNS label and Linux username.
* <b>`name`</b>: Shared name for this SummaryWriter resource stored to default
  <a href="../../../tf/Graph"><code>tf.Graph</code></a>.


#### Returns:

A `tf.summary.SummaryWriter` instance.
