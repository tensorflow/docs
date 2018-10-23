

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.gfile.Glob

``` python
tf.gfile.Glob(filename)
```



Defined in [`tensorflow/python/lib/io/file_io.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/lib/io/file_io.py).

Returns a list of files that match the given pattern(s).

#### Args:

* <b>`filename`</b>: string or iterable of strings. The glob pattern(s).


#### Returns:

A list of strings containing filenames that match the given pattern(s).


#### Raises:

* <b>`errors.OpError`</b>: If there are filesystem / directory listing errors.