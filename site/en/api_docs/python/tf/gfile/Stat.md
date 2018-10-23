

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.gfile.Stat

### `tf.gfile.Stat`

``` python
Stat(filename)
```



Defined in [`tensorflow/python/lib/io/file_io.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/python/lib/io/file_io.py).

Returns file statistics for a given path.

#### Args:

* <b>`filename`</b>: string, path to a file


#### Returns:

  FileStatistics struct that contains information about the path


#### Raises:

  errors.OpError: If the operation fails.