


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.gfile.GFile

### `class tf.gfile.GFile`
### `class tf.gfile.Open`

File I/O wrappers without thread locking.

## Properties

<h3 id="mode"><code>mode</code></h3>

Returns the mode in which the file was opened.

<h3 id="name"><code>name</code></h3>

Returns the file name.



## Methods

<h3 id="__init__"><code>__init__(name, mode='r')</code></h3>



<h3 id="close"><code>close()</code></h3>

Closes FileIO. Should be called for the WritableFile to be flushed.

<h3 id="flush"><code>flush()</code></h3>

Flushes the Writable file.

This only ensures that the data has made its way out of the process without
any guarantees on whether it's written to disk. This means that the
data would survive an application crash but not necessarily an OS crash.

<h3 id="next"><code>next()</code></h3>



<h3 id="read"><code>read(n=-1)</code></h3>

Returns the contents of a file as a string.

Starts reading from current position in file.

#### Args:

* <b>`n`</b>: Read 'n' bytes if n != -1. If n = -1, reads to end of file.


#### Returns:

  'n' bytes of the file (or whole file) requested as a string.

<h3 id="readline"><code>readline()</code></h3>

Reads the next line from the file. Leaves the '\n' at the end.

<h3 id="readlines"><code>readlines()</code></h3>

Returns all lines from the file in a list.

<h3 id="seek"><code>seek(position)</code></h3>

Seeks to the position in the file.

<h3 id="size"><code>size()</code></h3>

Returns the size of the file.

<h3 id="tell"><code>tell()</code></h3>

Returns the current position in the file.

<h3 id="write"><code>write(file_content)</code></h3>

Writes file_content to the file. Appends to the end of the file.





Defined in [`tensorflow/python/platform/gfile.py`](https://www.tensorflow.org/code/tensorflow/python/platform/gfile.py).

