description: Returns a list of files that match the given pattern(s).

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.io.gfile.glob" />
<meta itemprop="path" content="Stable" />
</div>

# tf.io.gfile.glob

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/lib/io/file_io.py#L355-L421">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns a list of files that match the given pattern(s).

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.io.gfile.glob`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.io.gfile.glob(
    pattern
)
</code></pre>



<!-- Placeholder for "Used in" -->

The patterns are defined as strings. Supported patterns are defined
here. Note that the pattern can be a Python iteratable of string patterns.

The format definition of the pattern is:

**pattern**: `{ term }`

**term**:
  * `'*'`: matches any sequence of non-'/' characters
  * `'?'`: matches a single non-'/' character
  * `'[' [ '^' ] { match-list } ']'`: matches any single
    character (not) on the list
  * `c`: matches character `c`  where `c != '*', '?', '\\', '['`
  * `'\\' c`: matches character `c`

**character range**:
  * `c`: matches character `c` while `c != '\\', '-', ']'`
  * `'\\' c`: matches character `c`
  * `lo '-' hi`: matches character `c` for `lo <= c <= hi`

#### Examples:



```
>>> tf.io.gfile.glob("*.py")
... # For example, ['__init__.py']
```

```
>>> tf.io.gfile.glob("__init__.??")
... # As above
```

```
>>> files = {"*.py"}
>>> the_iterator = iter(files)
>>> tf.io.gfile.glob(the_iterator)
... # As above
```

See the C++ function `GetMatchingPaths` in
[`core/platform/file_system.h`]
(../../../core/platform/file_system.h)
for implementation details.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`pattern`
</td>
<td>
string or iterable of strings. The glob pattern(s).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A list of strings containing filenames that match the given pattern(s).
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`errors.OpError`
</td>
<td>
If there are filesystem / directory listing errors.
</td>
</tr><tr>
<td>
`errors.NotFoundError`
</td>
<td>
If pattern to be matched is an invalid directory.
</td>
</tr>
</table>

