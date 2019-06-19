page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.eager.Saver

## Class `Saver`





Defined in [`tensorflow/contrib/eager/python/saver.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/eager/python/saver.py).

A tf.train.Saver adapter for use when eager execution is enabled.
  

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(var_list)
```

A  tf.train.Saver adapter for use when eager execution is enabled.

  The API, and on-disk format, mimic tf.train.Saver except that no
  Session is needed.

#### Args:

* <b>`var_list`</b>: The list of variables that will be saved and restored. Either a
    list of `tfe.Variable` objects, or a dictionary mapping names to
    `tfe.Variable` objects.


#### Raises:

* <b>`RuntimeError`</b>: if invoked when eager execution has not been enabled.

<h3 id="restore"><code>restore</code></h3>

``` python
restore(file_prefix)
```

Restores previously saved variables.

#### Args:

* <b>`file_prefix`</b>: Path prefix where parameters were previously saved.
    Typically obtained from a previous `save()` call, or from
    <a href="../../../tf/train/latest_checkpoint"><code>tf.train.latest_checkpoint</code></a>.

<h3 id="save"><code>save</code></h3>

``` python
save(
    file_prefix,
    global_step=None
)
```

Saves variables.

#### Args:

* <b>`file_prefix`</b>: Path prefix of files created for the checkpoint.
* <b>`global_step`</b>: If provided the global step number is appended to file_prefix
    to create the checkpoint filename. The optional argument can be a
    Tensor, a Variable, or an integer.


#### Returns:

A string: prefix of filenames created for the checkpoint. This may be
 an extension of file_prefix that is suitable to pass as an argument
 to a subsequent call to `restore()`.



