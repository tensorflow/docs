

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.gfile.Copy

``` python
Copy(
    oldpath,
    newpath,
    overwrite=False
)
```



Defined in [`tensorflow/python/lib/io/file_io.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/python/lib/io/file_io.py).

Copies data from oldpath to newpath.

#### Args:

* <b>`oldpath`</b>: string, name of the file who's contents need to be copied
* <b>`newpath`</b>: string, name of the file to which to copy to
* <b>`overwrite`</b>: boolean, if false its an error for newpath to be occupied by an
      existing file.


#### Raises:

  errors.OpError: If the operation fails.