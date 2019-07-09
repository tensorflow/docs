page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.summary.create_file_writer

``` python
tf.contrib.summary.create_file_writer(
    logdir,
    max_queue=None,
    flush_millis=None,
    filename_suffix=None,
    name=None
)
```



Defined in [`tensorflow/python/ops/summary_ops_v2.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/ops/summary_ops_v2.py).

Creates a summary file writer in the current context under the given name.

#### Args:

* <b>`logdir`</b>: a string, or None. If a string, creates a summary file writer
   which writes to the directory named by the string. If None, returns
   a mock object which acts like a summary writer but does nothing,
   useful to use as a context manager.
* <b>`max_queue`</b>: the largest number of summaries to keep in a queue; will
   flush once the queue gets bigger than this. Defaults to 10.
* <b>`flush_millis`</b>: the largest interval between flushes. Defaults to 120,000.
* <b>`filename_suffix`</b>: optional suffix for the event file name. Defaults to `.v2`.
* <b>`name`</b>: Shared name for this SummaryWriter resource stored to default
    Graph. Defaults to the provided logdir prefixed with `logdir:`. Note: if a
    summary writer resource with this shared name already exists, the returned
    SummaryWriter wraps that resource and the other arguments have no effect.


#### Returns:

Either a summary writer or an empty object which can be used as a
summary writer.