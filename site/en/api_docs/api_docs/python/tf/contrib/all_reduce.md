

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.contrib.all_reduce



Defined in [`tensorflow/contrib/all_reduce/__init__.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/all_reduce/__init__.py).

All-reduce implementations.

## Functions

[`build_nccl_all_reduce(...)`](../../tf/contrib/all_reduce/build_nccl_all_reduce): Build a subgraph that does one full all-reduce, using NCCL.

[`build_nccl_then_recursive_hd(...)`](../../tf/contrib/all_reduce/build_nccl_then_recursive_hd): Construct hybrid of NCCL within workers, Recursive-HD across workers.

[`build_nccl_then_ring(...)`](../../tf/contrib/all_reduce/build_nccl_then_ring): Construct hybrid of NCCL within workers, Ring across workers.

[`build_nccl_then_shuffle(...)`](../../tf/contrib/all_reduce/build_nccl_then_shuffle): Construct hybrid of NCCL within workers, Shuffle across workers.

[`build_recursive_hd_all_reduce(...)`](../../tf/contrib/all_reduce/build_recursive_hd_all_reduce): Construct a subgraph for recursive halving-doubling all-reduce.

[`build_ring_all_reduce(...)`](../../tf/contrib/all_reduce/build_ring_all_reduce): Construct a subgraph performing a ring-style all-reduce of input_tensors.

[`build_shuffle_all_reduce(...)`](../../tf/contrib/all_reduce/build_shuffle_all_reduce): Construct a subgraph for shuffle all-reduce.

[`build_shuffle_then_ring(...)`](../../tf/contrib/all_reduce/build_shuffle_then_ring): Construct hybrid of Shuffle within workers, Ring across workers.

[`build_shuffle_then_shuffle(...)`](../../tf/contrib/all_reduce/build_shuffle_then_shuffle): Construct hybrid of Shuffle within workers, Shuffle across workers.

