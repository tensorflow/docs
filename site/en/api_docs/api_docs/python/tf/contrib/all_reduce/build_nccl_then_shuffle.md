

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.all_reduce.build_nccl_then_shuffle

``` python
tf.contrib.all_reduce.build_nccl_then_shuffle(
    input_tensors,
    gather_devices,
    nccl_red_op,
    shuffle_red_op,
    un_op=None
)
```



Defined in [`tensorflow/contrib/all_reduce/python/all_reduce.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/all_reduce/python/all_reduce.py).

Construct hybrid of NCCL within workers, Shuffle across workers.