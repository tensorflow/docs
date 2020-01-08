

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.tpu.cross_replica_sum

``` python
tf.contrib.tpu.cross_replica_sum(
    input,
    group_assignment=[],
    name=None
)
```



Defined in generated file: `tensorflow/contrib/tpu/ops/gen_tpu_ops.py`.

An Op to sum inputs across replicated TPU instances. Each

instance supplies its own input. If group_assignment is empty, the output of
each is the sum of all the inputs, otherwise the output of each is the sum of
the inputs belonging to the same group.

For example, suppose there are 4 TPU instances: `[A, B, C, D]`. Passing
group_assignment=`[0,1,0,1]` sets `A, C` as group 0, and `B, D` as group 1.
Thus we get the outputs: `[A+C, B+D, A+C, B+D]`.

#### Args:

* <b>`input`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `float32`.
    The local input to the sum.
* <b>`group_assignment`</b>: An optional list of `ints`. Defaults to `[]`.
    The list of group ids. `group_assignment[i]` represents the
    group id of replica i.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `input`.
The sum of all the distributed inputs.