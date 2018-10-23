

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.gfile.MkDir

``` python
MkDir(dirname)
```



Defined in [`tensorflow/python/lib/io/file_io.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/python/lib/io/file_io.py).

Creates a directory with the name 'dirname'.

#### Args:

* <b>`dirname`</b>: string, name of the directory to be created

Notes:
  The parent directories need to exist. Use recursive_create_dir instead if
  there is the possibility that the parent dirs don't exist.


#### Raises:

* <b>`errors.OpError`</b>: If the operation fails.