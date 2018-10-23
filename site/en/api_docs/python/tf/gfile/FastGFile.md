

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.gfile.FastGFile

### `class tf.gfile.FastGFile`



Defined in [`tensorflow/python/platform/gfile.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/python/platform/gfile.py).

File I/O wrappers without thread locking.

## Properties

<h3 id="mode"><code>mode</code></h3>

Returns the mode in which the file was opened.

<h3 id="name"><code>name</code></h3>

Returns the file name.



## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    name,
    mode='r'
)
```



<h3 id="__enter__"><code>__enter__</code></h3>

``` python
__enter__()
```

Make usable with "with" statement.

<h3 id="__exit__"><code>__exit__</code></h3>

``` python
__exit__(
    unused_type,
    unused_value,
    unused_traceback
)
```

Make usable with "with" statement.

<h3 id="__iter__"><code>__iter__</code></h3>

``` python
__iter__()
```



<h3 id="__next__"><code>__next__</code></h3>

``` python
__next__()
```



<h3 id="close"><code>close</code></h3>

``` python
close()
```

Closes FileIO. Should be called for the WritableFile to be flushed.

<h3 id="flush"><code>flush</code></h3>

``` python
flush()
```

Flushes the Writable file.

This only ensures that the data has made its way out of the process without
any guarantees on whether it's written to disk. This means that the
data would survive an application crash but not necessarily an OS crash.

<h3 id="next"><code>next</code></h3>

``` python
next()
```



<h3 id="read"><code>read</code></h3>

``` python
read(n=-1)
```

Returns the contents of a file as a string.

Starts reading from current position in file.

#### Args:

* <b>`n`</b>: Read 'n' bytes if n != -1. If n = -1, reads to end of file.


#### Returns:

  'n' bytes of the file (or whole file) in bytes mode or 'n' bytes of the
  string if in string (regular) mode.

<h3 id="readline"><code>readline</code></h3>

``` python
readline()
```

Reads the next line from the file. Leaves the '\n' at the end.

<h3 id="readlines"><code>readlines</code></h3>

``` python
readlines()
```

Returns all lines from the file in a list.

<h3 id="seek"><code>seek</code></h3>

``` python
seek(position)
```

Seeks to the position in the file.

<h3 id="size"><code>size</code></h3>

``` python
size()
```

Returns the size of the file.

<h3 id="tell"><code>tell</code></h3>

``` python
tell()
```

Returns the current position in the file.

<h3 id="write"><code>write</code></h3>

``` python
write(file_content)
```

Writes file_content to the file. Appends to the end of the file.



