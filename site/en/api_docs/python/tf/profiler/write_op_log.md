

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.profiler.write_op_log

``` python
write_op_log(
    graph,
    log_dir,
    op_log=None,
    run_meta=None,
    add_trace=True
)
```



Defined in [`tensorflow/python/profiler/tfprof_logger.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/python/profiler/tfprof_logger.py).

Log provided 'op_log', and add additional model information below.

  The API also assigns ops in tf.trainable_variables() an op type called
  '_trainable_variables'.
  The API also logs 'flops' statistics for ops with op.RegisterStatistics()
  defined. flops calculation depends on Tensor shapes defined in 'graph',
  which might not be complete. 'run_meta', if provided, completes the shape
  information with best effort.

#### Args:

* <b>`graph`</b>: tf.Graph.
* <b>`log_dir`</b>: directory to write the log file.
* <b>`op_log`</b>: (Optional) OpLogProto proto to be written. If not provided, an new
      one is created.
* <b>`run_meta`</b>: (Optional) RunMetadata proto that helps flops computation using
      run time shape information.
* <b>`add_trace`</b>: Whether to add python code trace information.
      Used to support "code" view.