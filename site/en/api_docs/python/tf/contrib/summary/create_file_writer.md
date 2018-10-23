

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



Defined in [`tensorflow/contrib/summary/summary_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/contrib/summary/summary_ops.py).

Creates a summary file writer in the current context.

#### Args:

* <b>`logdir`</b>: a string, or None. If a string, creates a summary file writer
   which writes to the directory named by the string. If None, returns
   a mock object which acts like a summary writer but does nothing,
   useful to use as a context manager.
* <b>`max_queue`</b>: the largest number of summaries to keep in a queue; will
   flush once the queue gets bigger than this.
* <b>`flush_millis`</b>: the largest interval between flushes.
* <b>`filename_suffix`</b>: optional suffix for the event file name.
* <b>`name`</b>: Shared name for this SummaryWriter resource stored to default
    Graph.


#### Returns:

Either a summary writer or an empty object which can be used as a
summary writer.