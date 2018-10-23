

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.dynamic_partition

``` python
tf.dynamic_partition(
    data,
    partitions,
    num_partitions,
    name=None
)
```



Defined in `tensorflow/python/ops/gen_data_flow_ops.py`.

See the guide: [Tensor Transformations > Slicing and Joining](../../../api_guides/python/array_ops#Slicing_and_Joining)

Partitions `data` into `num_partitions` tensors using indices from `partitions`.

For each index tuple `js` of size `partitions.ndim`, the slice `data[js, ...]`
becomes part of `outputs[partitions[js]]`.  The slices with `partitions[js] = i`
are placed in `outputs[i]` in lexicographic order of `js`, and the first
dimension of `outputs[i]` is the number of entries in `partitions` equal to `i`.
In detail,

```python
    outputs[i].shape = [sum(partitions == i)] + data.shape[partitions.ndim:]

    outputs[i] = pack([data[js, ...] for js if partitions[js] == i])
```

`data.shape` must start with `partitions.shape`.

For example:

```python
    # Scalar partitions.
    partitions = 1
    num_partitions = 2
    data = [10, 20]
    outputs[0] = []  # Empty with shape [0, 2]
    outputs[1] = [[10, 20]]

    # Vector partitions.
    partitions = [0, 0, 1, 1, 0]
    num_partitions = 2
    data = [10, 20, 30, 40, 50]
    outputs[0] = [10, 20, 50]
    outputs[1] = [30, 40]
```

See `dynamic_stitch` for an example on how to merge partitions back.

<div style="width:70%; margin:auto; margin-bottom:10px; margin-top:20px;">
<img style="width:100%" src="https://www.tensorflow.org/images/DynamicPartition.png" alt>
</div>

#### Args:

* <b>`data`</b>: A `Tensor`.
* <b>`partitions`</b>: A `Tensor` of type `int32`.
    Any shape.  Indices in the range `[0, num_partitions)`.
* <b>`num_partitions`</b>: An `int` that is `>= 1`.
    The number of partitions to output.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A list of `num_partitions` `Tensor` objects with the same type as `data`.