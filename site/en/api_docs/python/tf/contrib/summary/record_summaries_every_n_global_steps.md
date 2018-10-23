

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.summary.record_summaries_every_n_global_steps

``` python
record_summaries_every_n_global_steps(
    n,
    global_step=None
)
```



Defined in [`tensorflow/contrib/summary/summary_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/contrib/summary/summary_ops.py).

Sets the should_record_summaries Tensor to true if global_step % n == 0.