


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.gfile.ListDirectory

### `tf.gfile.ListDirectory`

```
tf.gfile.ListDirectory(dirname)
```


Returns a list of entries contained within a directory.

The list is in arbitrary order. It does not contain the special entries "."
and "..".

#### Args:

* <b>`dirname`</b>: string, path to a directory


#### Returns:

  [filename1, filename2, ... filenameN] as strings


#### Raises:

  errors.NotFoundError if directory doesn't exist

Defined in [`tensorflow/python/lib/io/file_io.py`](https://www.tensorflow.org/code/tensorflow/python/lib/io/file_io.py).

