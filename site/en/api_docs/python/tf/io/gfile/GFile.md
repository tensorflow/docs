page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.gfile.GFile


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/platform/gfile.py#L41-L52">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `GFile`

File I/O wrappers without thread locking.



### Aliases:

* Class `tf.compat.v1.gfile.GFile`
* Class `tf.compat.v1.gfile.Open`
* Class `tf.compat.v1.io.gfile.GFile`
* Class `tf.compat.v2.io.gfile.GFile`


<!-- Placeholder for "Used in" -->

Note, that this  is somewhat like builtin Python  file I/O, but
there are  semantic differences to  make it more  efficient for
some backing filesystems.  For example, a write  mode file will
not  be opened  until the  first  write call  (to minimize  RPC
invocations in network filesystems).

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/platform/gfile.py#L51-L52">View source</a>

``` python
__init__(
    name,
    mode='r'
)
```

Initialize self.  See help(type(self)) for accurate signature.




## Properties

<h3 id="mode"><code>mode</code></h3>

Returns the mode in which the file was opened.


<h3 id="name"><code>name</code></h3>

Returns the file name.




## Methods

<h3 id="__enter__"><code>__enter__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/lib/io/file_io.py#L202-L204">View source</a>

``` python
__enter__()
```

Make usable with "with" statement.


<h3 id="__exit__"><code>__exit__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/lib/io/file_io.py#L206-L208">View source</a>

``` python
__exit__(
    unused_type,
    unused_value,
    unused_traceback
)
```

Make usable with "with" statement.


<h3 id="__iter__"><code>__iter__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/lib/io/file_io.py#L210-L211">View source</a>

``` python
__iter__()
```




<h3 id="close"><code>close</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/lib/io/file_io.py#L234-L241">View source</a>

``` python
close()
```

Closes FileIO. Should be called for the WritableFile to be flushed.


<h3 id="flush"><code>flush</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/lib/io/file_io.py#L222-L232">View source</a>

``` python
flush()
```

Flushes the Writable file.

This only ensures that the data has made its way out of the process without
any guarantees on whether it's written to disk. This means that the
data would survive an application crash but not necessarily an OS crash.

<h3 id="next"><code>next</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/lib/io/file_io.py#L213-L217">View source</a>

``` python
next()
```




<h3 id="read"><code>read</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/lib/io/file_io.py#L110-L128">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/lib/io/file_io.py#L176-L179">View source</a>

``` python
readline()
```

Reads the next line from the file. Leaves the '\n' at the end.


<h3 id="readlines"><code>readlines</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/lib/io/file_io.py#L181-L190">View source</a>

``` python
readlines()
```

Returns all lines from the file in a list.


<h3 id="seek"><code>seek</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/lib/io/file_io.py#L130-L174">View source</a>

``` python
seek(
    offset=None,
    whence=0,
    position=None
)
```

Seeks to the offset in the file. (deprecated arguments)

Warning: SOME ARGUMENTS ARE DEPRECATED: `(position)`. They will be removed in a future version.
Instructions for updating:
position is deprecated in favor of the offset argument.

#### Args:


* <b>`offset`</b>: The byte count relative to the whence argument.
* <b>`whence`</b>: Valid values for whence are:
  0: start of the file (default)
  1: relative to the current position of the file
  2: relative to the end of file. offset is usually negative.

<h3 id="seekable"><code>seekable</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/lib/io/file_io.py#L243-L245">View source</a>

``` python
seekable()
```

Returns True as FileIO supports random access ops of seek()/tell()


<h3 id="size"><code>size</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/lib/io/file_io.py#L100-L102">View source</a>

``` python
size()
```

Returns the size of the file.


<h3 id="tell"><code>tell</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/lib/io/file_io.py#L192-L200">View source</a>

``` python
tell()
```

Returns the current position in the file.


<h3 id="write"><code>write</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/lib/io/file_io.py#L104-L108">View source</a>

``` python
write(file_content)
```

Writes file_content to the file. Appends to the end of the file.
