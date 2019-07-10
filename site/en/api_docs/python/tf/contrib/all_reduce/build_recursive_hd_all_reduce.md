page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.all_reduce.build_recursive_hd_all_reduce

``` python
tf.contrib.all_reduce.build_recursive_hd_all_reduce(
    input_tensors,
    red_op,
    un_op=None
)
```



Defined in [`tensorflow/contrib/all_reduce/python/all_reduce.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/all_reduce/python/all_reduce.py).

Construct a subgraph for recursive halving-doubling all-reduce.

The recursive halving-doubling algorithm is described in
http://www.mcs.anl.gov/~thakur/papers/ijhpca-coll.pdf

The concept is to arrange the participating n devices in
a linear sequence where devices exchange data pairwise
with one other device in each round.  During the gather
phase there are lg(n) rounds where devices exchange
increasingly smaller sub-tensors with another device
at increasingly greater distances, until at the top
each device has 1/n of the fully reduced values.  During the
scatter phase each device exchanges its fully reduced
sub-tensor (which doubles in length at each round)
with one other device at increasingly smaller distances
until each device has all of the fully reduced values.

Note: this preliminary version requires that len(input_tensors) be a
  power of 2.  TODO(tucker): relax this restriction.  Also, the
  number of elements in each tensor must be divisible by 2^h where h
  is the number of hops in each phase.  This will also be relaxed in
  the future with edge-case specific logic.

#### Args:

* <b>`input_tensors`</b>: list of T <a href="../../../tf/Tensor"><code>tf.Tensor</code></a> to be elementwise reduced.
* <b>`red_op`</b>: a binary elementwise reduction Op.
* <b>`un_op`</b>: an optional unary elementwise Op to apply to reduced values.


#### Returns:

list of T <a href="../../../tf/Tensor"><code>tf.Tensor</code></a> which are the fully reduced tensors, one
at each device of input_tensors.


#### Raises:

* <b>`ValueError`</b>: num_devices not a power of 2, or tensor len not divisible
  by 2 the proper number of times.