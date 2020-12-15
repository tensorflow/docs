description: A transformation that moves dataset processing to the tf.data service.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.data.experimental.service.distribute" />
<meta itemprop="path" content="Stable" />
</div>

# tf.data.experimental.service.distribute

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/data/experimental/ops/data_service_ops.py#L301-L483">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A transformation that moves dataset processing to the tf.data service.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.data.experimental.service.distribute`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.data.experimental.service.distribute(
    processing_mode, service, job_name=None, max_outstanding_requests=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

When you iterate over a dataset containing the `distribute` transformation,
the tf.data service creates a "job" which produces data for the dataset
iteration.

The tf.data service uses a cluster of workers to prepare data for training
your model.
The `processing_mode` argument to <a href="../../../../tf/data/experimental/service/distribute.md"><code>tf.data.experimental.service.distribute</code></a>
describes how to leverage multiple workers to process the input dataset.
Currently, there are two processing modes to choose from: "distributed_epoch"
and "parallel_epochs".

"distributed_epoch" means that the dataset will be split across all tf.data
service workers.
The dispatcher produces "splits" for the dataset and sends them to workers for
further processing. For example, if a dataset begins with a list of filenames,
the dispatcher will iterate through the filenames and send the filenames to
tf.data workers, which will perform the rest of the dataset transformations on
those files. "distributed_epoch" is useful when your model needs to see each
element of the dataset exactly once, or if it needs to see the data in a
generally-sequential order. "distributed_epoch" only works for datasets with
splittable sources, such as <a href="../../../../tf/data/Dataset.md#from_tensor_slices"><code>Dataset.from_tensor_slices</code></a>,
<a href="../../../../tf/data/Dataset.md#list_files"><code>Dataset.list_files</code></a>, or <a href="../../../../tf/data/Dataset.md#range"><code>Dataset.range</code></a>.

"parallel_epochs" means that the entire input dataset will be processed
independently by each of the tf.data service workers.
For this reason, it is important to shuffle data (e.g. filenames)
non-deterministically, so that each worker will process the elements of the
dataset in a different order. "parallel_epochs" can be used to distribute
datasets that aren't splittable.

With two workers, "parallel_epochs" will produce every element of the dataset
twice:

```
>>> dispatcher = tf.data.experimental.service.DispatchServer()
>>> dispatcher_address = dispatcher.target.split("://")[1]
>>> # Start two workers
>>> workers = [
...     tf.data.experimental.service.WorkerServer(
...         tf.data.experimental.service.WorkerConfig(
...             dispatcher_address=dispatcher_address)) for _ in range(2)
... ]
>>> dataset = tf.data.Dataset.range(10)
>>> dataset = dataset.apply(tf.data.experimental.service.distribute(
...     processing_mode="parallel_epochs", service=dispatcher.target))
>>> print(sorted(list(dataset.as_numpy_iterator())))
[0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]
```

"distributed_epoch", on the other hand, will still produce each element once:

```
>>> dispatcher = tf.data.experimental.service.DispatchServer()
>>> dispatcher_address = dispatcher.target.split("://")[1]
>>> workers = [
...     tf.data.experimental.service.WorkerServer(
...         tf.data.experimental.service.WorkerConfig(
...             dispatcher_address=dispatcher_address)) for _ in range(2)
... ]
>>> dataset = tf.data.Dataset.range(10)
>>> dataset = dataset.apply(tf.data.experimental.service.distribute(
...     processing_mode="distributed_epoch", service=dispatcher.target))
>>> print(sorted(list(dataset.as_numpy_iterator())))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

When using `apply(tf.data.experimental.service.distribute(...))`, the dataset
before the `apply` transformation executes within the tf.data service, while
the operations after `apply` happen within the local process.

```
>>> dispatcher = tf.data.experimental.service.DispatchServer()
>>> dispatcher_address = dispatcher.target.split("://")[1]
>>> workers = [
...     tf.data.experimental.service.WorkerServer(
...         tf.data.experimental.service.WorkerConfig(
...             dispatcher_address=dispatcher_address)) for _ in range(2)
... ]
>>> dataset = tf.data.Dataset.range(5)
>>> dataset = dataset.map(lambda x: x*x)
>>> dataset = dataset.apply(
...    tf.data.experimental.service.distribute("parallel_epochs",
...                                            dispatcher.target))
>>> dataset = dataset.map(lambda x: x+1)
>>> print(sorted(list(dataset.as_numpy_iterator())))
[1, 1, 2, 2, 5, 5, 10, 10, 17, 17]
```

In the above example, the dataset operations (before applying the `distribute`
function on the elements) will be executed on the tf.data workers,
and the elements are provided over RPC. The remaining transformations
(after the call to `distribute`) will be executed locally. The dispatcher
and the workers will bind to usused free ports (which are chosen at random),
in order to communicate with each other. However, to bind them to specific
ports, the `port` parameter can be passed.

The `job_name` argument allows jobs to be shared across multiple
datasets. Instead of each dataset creating its own job, all
datasets with the same `job_name` will consume from the same job. A new job
will be created for each iteration of the dataset (with each repetition of
<a href="../../../../tf/data/Dataset.md#repeat"><code>Dataset.repeat</code></a> counting as a new iteration). Suppose the `DispatchServer`
is serving on `localhost:5000` and two training workers (in either a single
client or multi-client setup) iterate over the below dataset, and there is a
single tf.data worker:

```
range5_dataset = tf.data.Dataset.range(5)
dataset = range5_dataset.apply(tf.data.experimental.service.distribute(
    "parallel_epochs", "grpc://localhost:5000", job_name="my_job_name"))
for iteration in range(3):
  print(list(dataset))
```

The elements of each job will be split between the two processes, with
elements being consumed by the processes on a first-come first-served basis.
One possible result is that process 1 prints

```
[0, 2, 4]
[0, 1, 3]
[1]
```

and process 2 prints

```
[1, 3]
[2, 4]
[0, 2, 3, 4]
```

Job names must not be re-used across different training jobs within the
lifetime of the tf.data service. In general, the tf.data service is expected
to live for the duration of a single training job.
To use the tf.data service with multiple training jobs, make sure to use
different job names to avoid conflicts. For example, suppose a training job
calls `distribute` with `job_name="job"` and reads until end of input. If
another independent job connects to the same tf.data service and tries to read
from `job_name="job"`, it will immediately receive end of input, without
getting any data.

**Keras and Distribution Strategies**

The dataset produced by the `distribute` transformation can be passed to
Keras' <a href="../../../../tf/keras/Model.md#fit"><code>Model.fit</code></a> or Distribution Strategy's
<a href="../../../../tf/distribute/Strategy.md#experimental_distribute_dataset"><code>tf.distribute.Strategy.experimental_distribute_dataset</code></a> like any other
<a href="../../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a>. We recommend setting a `job_name` on the call to
`distribute` so that if there are multiple workers, they read data from the
same job. Note that the autosharding normally performed by
`experimental_distribute_dataset` will be disabled when setting a `job_name`,
since sharing the job already results in splitting data across the workers.
When using a shared job, data will be dynamically balanced across workers, so
that they reach end of input about the same time. This results in better
worker utilization than with autosharding, where each worker processes an
independent set of files, and some workers may run out of data earlier than
others.

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

<tr>
<td>
`Dataset`
</td>
<td>
A `Dataset` of the elements produced by the data service.
</td>
</tr>
</table>

