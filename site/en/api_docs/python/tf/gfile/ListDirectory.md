

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.gfile.ListDirectory

``` python
tf.gfile.ListDirectory(dirname)
```



Defined in [`tensorflow/python/lib/io/file_io.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/lib/io/file_io.py).

Returns a list of entries contained within a directory.

The list is in arbitrary order. It does not contain the special entries "."
and "..".

#### Args:

* <b>`dirname`</b>: string, path to a directory


#### Returns:

[filename1, filename2, ... filenameN] as strings


#### Raises:

errors.NotFoundError if directory doesn't exist