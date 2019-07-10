page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.eager.save_network_checkpoint

``` python
tf.contrib.eager.save_network_checkpoint(
    network,
    save_path,
    global_step=None,
    map_func=None
)
```



Defined in [`tensorflow/contrib/eager/python/network.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/eager/python/network.py).

Save variables from the Network to a checkpoint. (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Please inherit from tf.keras.Model instead of tfe.Network, and use tf.keras.Model.save_weights.

#### Args:

* <b>`network`</b>: A Network object to save.
* <b>`save_path`</b>: Either a checkpoint prefix or the name of a directory to save
    the checkpoint in (in which case the checkpoint will be named based on
    the Network name).
* <b>`global_step`</b>: The global step to use when naming the checkpoint. If None
    (default), we will first try to get the default global step. If that
    fails because no default global step exists, then the checkpoint is
    created without a global step suffix.
* <b>`map_func`</b>: A function mapping fully qualified variable names
    (e.g. 'my_network_1/dense_1/kernel') to names in the checkpoint. By
    default (if `map_func=None`), the variable prefix for the network being
    restored (`Network.scope_name + '/'`, e.g. 'my_network_1/') is stripped
    and all other variable names (shared with other Networks) are left
    unchanged.

#### Returns:

The checkpoint prefix for the saved checkpoint, which may be passed to
`Network.restore`.

#### Raises:

* <b>`ValueError`</b>: If the Network has not yet been called, or if map_func results
    in a name collision.