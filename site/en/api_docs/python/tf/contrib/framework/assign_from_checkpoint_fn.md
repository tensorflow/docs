

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.framework.assign_from_checkpoint_fn

### `tf.contrib.framework.assign_from_checkpoint_fn`

``` python
assign_from_checkpoint_fn(
    model_path,
    var_list,
    ignore_missing_vars=False,
    reshape_variables=False
)
```



Defined in [`tensorflow/contrib/framework/python/ops/variables.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/framework/python/ops/variables.py).

See the guide: [Framework (contrib) > Variables](../../../../../api_guides/python/contrib.framework#Variables)

Returns a function that assigns specific variables from a checkpoint.

If ignore_missing_vars is True and no variables are found in the checkpoint
it returns None.

#### Args:

* <b>`model_path`</b>: The full path to the model checkpoint. To get latest checkpoint
      use `model_path = tf.train.latest_checkpoint(checkpoint_dir)`
* <b>`var_list`</b>: A list of `Variable` objects or a dictionary mapping names in the
      checkpoint to the corresponding variables to initialize. If empty or
      `None`, it would return `no_op(), None`.
* <b>`ignore_missing_vars`</b>: Boolean, if True it would ignore variables missing in
      the checkpoint with a warning instead of failing.
* <b>`reshape_variables`</b>: Boolean, if True it would automatically reshape variables
      which are of different shape then the ones stored in the checkpoint but
      which have the same number of elements.


#### Returns:

  A function that takes a single argument, a `tf.Session`, that applies the
  assignment operation. If no matching variables were found in the checkpoint
  then `None` is returned.


#### Raises:

* <b>`ValueError`</b>: If var_list is empty.