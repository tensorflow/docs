description: A transformation that moves dataset processing to the tf.data service.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.data.experimental.service.distribute" />
<meta itemprop="path" content="Stable" />
</div>

# tf.data.experimental.service.distribute

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/data/experimental/ops/data_service_ops.py#L259-L385">
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

The `processing_mode` argument controls what data is produced by a tf.data
service job. Currently, the only supported mode is "parallel_epochs".

processing_mode="parallel_epochs" means that multiple tf.data workers will
iterate through the dataset in parallel, each producing all elements of the
dataset. For example, if the dataset contains {0, 1, 2}, every tf.data worker
used for execution will produce {0, 1, 2}. If there are 3 workers, the job
will produce the elements {0, 0, 0, 1, 1, 1, 2, 2, 2} (though not necessarily
in that order). To account for this, it is recommended to randomly shuffle
your dataset, so that different tf.data workers will iterate through the
dataset in different orders.

In the future, there will be additional processing modes. For example,
a "one_epoch" mode which partitions the dataset across the tf.data
workers, so that the consumers see each element of the dataset only once.

```
dataset = tf.data.Dataset.range(5)
dataset = dataset.map(lambda x: x*x)
dataset = dataset.apply(
    tf.data.experimental.service.distribute("parallel_epochs",
                                            "grpc://dataservice:5000"))
dataset = dataset.map(lambda x: x+1)

for element in dataset:
  print(element)  # prints { 1, 2, 5, 10, 17 }
```

In the above example, the first two lines (before the call to `distribute`)
will be executed on tf.data workers, and the elements provided over
RPC. The remaining transformations (after the call to `distribute`) will be
executed locally.

The `job_name` argument allows jobs to be shared across multiple
datasets. Instead of each dataset creating its own job, all
datasets with the same `job_name` will consume from the same job. A new job
will be created for each iteration of the dataset (with each repetition of
<a href="../../../../tf/data/Dataset.md#repeat"><code>Dataset.repeat</code></a> counting as a new iteration). Suppose two training workers
(in either a single client or multi-client setup) iterate over the below
dataset, and there is a single tf.data worker:

```
range5_dataset = tf.data.Dataset.range(5)
dataset = range5_dataset.apply(tf.data.experimental.service.distribute(
    "parallel_epochs", "grpc://dataservice:5000", job_name="my_job_name"))
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
processed by tf.data workers. Currently, the only supported value is
"parallel_epochs".
</td>
</tr><tr>
<td>
`service`
</td>
<td>
A string indicating how to connect to the tf.data service. The
string should be in the format <protocol>://<address>, e.g.
grpc://localhost:5000.
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

