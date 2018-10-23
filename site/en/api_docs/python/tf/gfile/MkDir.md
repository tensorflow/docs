


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.gfile.MkDir

### `tf.gfile.MkDir`

```
tf.gfile.MkDir(dirname)
```


Creates a directory with the name 'dirname'.

#### Args:

* <b>`dirname`</b>: string, name of the directory to be created

Notes:
  The parent directories need to exist. Use recursive_create_dir instead if
  there is the possibility that the parent dirs don't exist.


#### Raises:

  errors.OpError: If the operation fails.

Defined in [`tensorflow/python/lib/io/file_io.py`](https://www.tensorflow.org/code/tensorflow/python/lib/io/file_io.py).

