page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.all_reduce.build_nccl_then_recursive_hd

``` python
tf.contrib.all_reduce.build_nccl_then_recursive_hd(
    input_tensors,
    red_op,
    un_op=None
)
```



Defined in [`tensorflow/contrib/all_reduce/python/all_reduce.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/contrib/all_reduce/python/all_reduce.py).

Construct hybrid of NCCL within workers, Recursive-HD across workers.