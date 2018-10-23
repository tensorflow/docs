


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.gfile.Rename

### `tf.gfile.Rename`

```
tf.gfile.Rename(oldname, newname, overwrite=False)
```


Rename or move a file / directory.

#### Args:

* <b>`oldname`</b>: string, pathname for a file
* <b>`newname`</b>: string, pathname to which the file needs to be moved
* <b>`overwrite`</b>: boolean, if false its an error for newpath to be occupied by an
      existing file.


#### Raises:

  errors.OpError: If the operation fails.

Defined in [`tensorflow/python/lib/io/file_io.py`](https://www.tensorflow.org/code/tensorflow/python/lib/io/file_io.py).

