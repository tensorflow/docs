


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.gfile.Walk

### `tf.gfile.Walk`

```
tf.gfile.Walk(top, in_order=True)
```


Recursive directory tree generator for directories.

#### Args:

* <b>`top`</b>: string, a Directory name
* <b>`in_order`</b>: bool, Traverse in order if True, post order if False.

Errors that happen while listing directories are ignored.


#### Yields:

  Each yield is a 3-tuple:  the pathname of a directory, followed by lists of
  all its subdirectories and leaf files.
  (dirname, [subdirname, subdirname, ...], [filename, filename, ...])
  as strings

Defined in [`tensorflow/python/lib/io/file_io.py`](https://www.tensorflow.org/code/tensorflow/python/lib/io/file_io.py).

