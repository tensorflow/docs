page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.summary.record_summaries_every_n_global_steps

``` python
tf.contrib.summary.record_summaries_every_n_global_steps(
    n,
    global_step=None
)
```



Defined in [`tensorflow/python/ops/summary_ops_v2.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/summary_ops_v2.py).

Sets the should_record_summaries Tensor to true if global_step % n == 0.