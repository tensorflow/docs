page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.gfile.Glob

Returns a list of files that match the given pattern(s).

### Aliases:

* `tf.compat.v1.gfile.Glob`
* `tf.gfile.Glob`

``` python
tf.gfile.Glob(filename)
```



Defined in [`python/lib/io/file_io.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/lib/io/file_io.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`filename`</b>: string or iterable of strings. The glob pattern(s).


#### Returns:

A list of strings containing filenames that match the given pattern(s).



#### Raises:


* <b>`errors.OpError`</b>: If there are filesystem / directory listing errors.