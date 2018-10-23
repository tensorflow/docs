

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.gfile.Exists

``` python
tf.gfile.Exists(filename)
```



Defined in [`tensorflow/python/lib/io/file_io.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/python/lib/io/file_io.py).

Determines whether a path exists or not.

#### Args:

* <b>`filename`</b>: string, a path


#### Returns:

True if the path exists, whether its a file or a directory.
False if the path does not exist and there are no filesystem errors.


#### Raises:

* <b>`errors.OpError`</b>: Propagates any errors reported by the FileSystem API.