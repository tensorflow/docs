

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.gfile.MakeDirs

### `tf.gfile.MakeDirs`

``` python
MakeDirs(dirname)
```



Defined in [`tensorflow/python/lib/io/file_io.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/python/lib/io/file_io.py).

Creates a directory and all parent/intermediate directories.

It succeeds if dirname already exists and is writable.

#### Args:

* <b>`dirname`</b>: string, name of the directory to be created


#### Raises:

  errors.OpError: If the operation fails.