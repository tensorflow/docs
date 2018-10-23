

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.kfac.loss_functions.insert_slice_in_zeros

``` python
tf.contrib.kfac.loss_functions.insert_slice_in_zeros(
    slice_to_insert,
    dim,
    dim_size,
    position
)
```



Defined in [`tensorflow/contrib/kfac/python/ops/loss_functions.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/contrib/kfac/python/ops/loss_functions.py).

Inserts slice into a larger tensor of zeros.

Forms a new tensor which is the same shape as slice_to_insert, except that
the dimension given by 'dim' is expanded to the size given by 'dim_size'.
'position' determines the position (index) at which to insert the slice within
that dimension.

Assumes slice_to_insert.shape[dim] = 1.

#### Args:

* <b>`slice_to_insert`</b>: The slice to insert.
* <b>`dim`</b>: The dimension which to expand with zeros.
* <b>`dim_size`</b>: The new size of the 'dim' dimension.
* <b>`position`</b>: The position of 'slice_to_insert' in the new tensor.


#### Returns:

The new tensor.


#### Raises:

* <b>`ValueError`</b>: If the slice's shape at the given dim is not 1.