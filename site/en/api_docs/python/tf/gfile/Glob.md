

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.gfile.Glob

### `tf.gfile.Glob`

``` python
Glob(filename)
```



Defined in [`tensorflow/python/lib/io/file_io.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/python/lib/io/file_io.py).

Returns a list of files that match the given pattern.

#### Args:

* <b>`filename`</b>: string, the pattern


#### Returns:

  Returns a list of strings containing filenames that match the given pattern.


#### Raises:

  errors.OpError: If there are filesystem / directory listing errors.