page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.all_reduce.build_shuffle_then_ring

``` python
tf.contrib.all_reduce.build_shuffle_then_ring(
    input_tensors,
    gather_devices,
    subdiv,
    red_n_op,
    red_op,
    un_op=None
)
```



Defined in [`tensorflow/contrib/all_reduce/python/all_reduce.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/all_reduce/python/all_reduce.py).

Construct hybrid of Shuffle within workers, Ring across workers.