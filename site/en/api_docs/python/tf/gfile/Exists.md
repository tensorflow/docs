

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.gfile.Exists

### `tf.gfile.Exists`

``` python
Exists(filename)
```



Defined in [`tensorflow/python/lib/io/file_io.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/python/lib/io/file_io.py).

Determines whether a path exists or not.

#### Args:

* <b>`filename`</b>: string, a path


#### Returns:

  True if the path exists, whether its a file or a directory.
  False if the path does not exist and there are no filesystem errors.


#### Raises:

  errors.OpError: Propagates any errors reported by the FileSystem API.