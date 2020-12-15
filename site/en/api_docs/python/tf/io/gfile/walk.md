description: Recursive directory tree generator for directories.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.io.gfile.walk" />
<meta itemprop="path" content="Stable" />
</div>

# tf.io.gfile.walk

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/lib/io/file_io.py#L722-L777">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Recursive directory tree generator for directories.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.io.gfile.walk`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.io.gfile.walk(
    top, topdown=(True), onerror=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`top`
</td>
<td>
string, a Directory name
</td>
</tr><tr>
<td>
`topdown`
</td>
<td>
bool, Traverse pre order if True, post order if False.
</td>
</tr><tr>
<td>
`onerror`
</td>
<td>
optional handler for errors. Should be a function, it will be
called with the error as argument. Rethrowing the error aborts the walk.
Errors that happen while listing directories are ignored.
</td>
</tr>
</table>



#### Yields:

Each yield is a 3-tuple:  the pathname of a directory, followed by lists of
all its subdirectories and leaf files. That is, each yield looks like:
`(dirname, [subdirname, subdirname, ...], [filename, filename, ...])`.
Each item is a string.
