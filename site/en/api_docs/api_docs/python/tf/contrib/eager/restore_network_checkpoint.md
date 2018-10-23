

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.eager.restore_network_checkpoint

``` python
tf.contrib.eager.restore_network_checkpoint(
    network,
    save_path,
    map_func=None
)
```



Defined in [`tensorflow/contrib/eager/python/network.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/eager/python/network.py).

Restore the Network from a checkpoint. (deprecated)

THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Please inherit from tf.keras.Model instead of tfe.Network, and use tf.keras.Model.load_weights.

If variables have already been created (typically when some or all of the
`Network` is built), they are assigned values from the checkpoint immediately,
overwriting any existing values (in graph mode the default session is used for
the assignments).

If there are checkpoint entries which do not correspond to any existing
variables in the `Network`, these values are saved for deferred restoration;
their initial values will be the checkpointed values once they are
created. Requests for multiple deferred restorations behave the same way as
immediate restorations, in that later requests will take priority over earlier
requests relevant to the same variable.

If this `Network` shares `Layer`s with another network, those `Layer`s will
also have their variables restored from the checkpoint.

#### Args:

* <b>`network`</b>: A Network object to restore.
* <b>`save_path`</b>: The return value of `tfe.save_network_checkpoint`, or a directory
    to search for a checkpoint.
* <b>`map_func`</b>: A function mapping fully qualified variable names
    (e.g. 'my_network_1/dense_1/kernel') to names in the checkpoint. By
    default (if `map_func=None`), the variable prefix for the network being
    restored (`Network.scope_name + '/'`, e.g. 'my_network_1/') is stripped
    and all other variable names (shared with other Networks) are left
    unchanged. Note that this is the _same_ map_func as
    `tfe.save_network_checkpoint`, not an inverse mapping.