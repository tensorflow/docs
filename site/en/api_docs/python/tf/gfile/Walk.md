page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.gfile.Walk


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/lib/io/file_io.py#L648-L663">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Recursive directory tree generator for directories.

### Aliases:

* <a href="/api_docs/python/tf/gfile/Walk"><code>tf.compat.v1.gfile.Walk</code></a>


``` python
tf.gfile.Walk(
    top,
    in_order=True
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`top`</b>: string, a Directory name
* <b>`in_order`</b>: bool, Traverse in order if True, post order if False.  Errors that
  happen while listing directories are ignored.


#### Yields:

Each yield is a 3-tuple:  the pathname of a directory, followed by lists of
all its subdirectories and leaf files.
(dirname, [subdirname, subdirname, ...], [filename, filename, ...])
as strings
