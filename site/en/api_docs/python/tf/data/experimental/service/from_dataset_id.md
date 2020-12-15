description: Creates a dataset which reads data from the tf.data service.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.data.experimental.service.from_dataset_id" />
<meta itemprop="path" content="Stable" />
</div>

# tf.data.experimental.service.from_dataset_id

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/data/experimental/ops/data_service_ops.py#L550-L629">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Creates a dataset which reads data from the tf.data service.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.data.experimental.service.from_dataset_id`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.data.experimental.service.from_dataset_id(
    processing_mode, service, dataset_id, element_spec=None, job_name=None,
    max_outstanding_requests=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This is useful when the dataset is registered by one process, then used in
another process. When the same process is both registering and reading from
the dataset, it is simpler to use <a href="../../../../tf/data/experimental/service/distribute.md"><code>tf.data.experimental.service.distribute</code></a>
instead.

Before using `from_dataset_id`, the dataset must have been registered with the
tf.data service using <a href="../../../../tf/data/experimental/service/register_dataset.md"><code>tf.data.experimental.service.register_dataset</code></a>.
`register_dataset` returns a dataset id for the registered dataset. That is
the `dataset_id` which should be passed to `from_dataset_id`.

The `element_spec` argument indicates the <a href="../../../../tf/TypeSpec.md"><code>tf.TypeSpec</code></a>s for the elements
produced by the dataset. Currently `element_spec` must be explicitly
specified, and match the dataset registered under `dataset_id`. `element_spec`
defaults to `None` so that in the future we can support automatically
discovering the `element_spec` by querying the tf.data service.

<a href="../../../../tf/data/experimental/service/distribute.md"><code>tf.data.experimental.service.distribute</code></a> is a convenience method which
combines `register_dataset` and `from_dataset_id` into a dataset
transformation.
See the documentation for <a href="../../../../tf/data/experimental/service/distribute.md"><code>tf.data.experimental.service.distribute</code></a> for more
detail about how `from_dataset_id` works.

```
>>> dispatcher = tf.data.experimental.service.DispatchServer()
>>> dispatcher_address = dispatcher.target.split("://")[1]
>>> worker = tf.data.experimental.service.WorkerServer(
...     tf.data.experimental.service.WorkerConfig(
...         dispatcher_address=dispatcher_address))
>>> dataset = tf.data.Dataset.range(10)
>>> dataset_id = tf.data.experimental.service.register_dataset(
...     dispatcher.target, dataset)
>>> dataset = tf.data.experimental.service.from_dataset_id(
...     processing_mode="parallel_epochs",
...     service=dispatcher.target,
...     dataset_id=dataset_id,
...     element_spec=dataset.element_spec)
>>> print(list(dataset.as_numpy_iterator()))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`processing_mode`
</td>
<td>
A string specifying the policy for how data should be
processed by tf.data workers. Can be either "parallel_epochs" to have
each tf.data worker process a copy of the dataset, or
"distributed_epoch" to split a single iteration of the dataset across
all the workers.
</td>
</tr><tr>
<td>
`service`
</td>
<td>
A string indicating how to connect to the tf.data service. The
string should be in the format "protocol://address", e.g.
"grpc://localhost:5000".
</td>
</tr><tr>
<td>
`dataset_id`
</td>
<td>
The id of the dataset to read from. This id is returned by
`register_dataset` when the dataset is registered with the tf.data
service.
</td>
</tr><tr>
<td>
`element_spec`
</td>
<td>
A nested structure of <a href="../../../../tf/TypeSpec.md"><code>tf.TypeSpec</code></a>s representing the type of
elements produced by the dataset. Use <a href="../../../../tf/data/Dataset.md#element_spec"><code>tf.data.Dataset.element_spec</code></a> to
see the element spec for a given dataset.
</td>
</tr><tr>
<td>
`job_name`
</td>
<td>
(Optional.) The name of the job. This argument makes it possible
for multiple datasets to share the same job. The default behavior is that
the dataset creates anonymous, exclusively owned jobs.
</td>
</tr><tr>
<td>
`max_outstanding_requests`
</td>
<td>
(Optional.) A limit on how many elements may be
requested at the same time. You can use this option to control the amount
of memory used, since `distribute` won't use more than `element_size` *
`max_outstanding_requests` of memory.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A <a href="../../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> which reads from the tf.data service.
</td>
</tr>

</table>

