description: Sets the AutoGraph verbosity level.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.autograph.set_verbosity" />
<meta itemprop="path" content="Stable" />
</div>

# tf.autograph.set_verbosity

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/autograph/utils/ag_logging.py#L40-L88">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Sets the AutoGraph verbosity level.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.autograph.set_verbosity`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.autograph.set_verbosity(
    level, alsologtostdout=(False)
)
</code></pre>



<!-- Placeholder for "Used in" -->

_Debug logging in AutoGraph_

More verbose logging is useful to enable when filing bug reports or doing
more in-depth debugging.

There are two means to control the logging verbosity:

 * The `set_verbosity` function

 * The `AUTOGRAPH_VERBOSITY` environment variable

`set_verbosity` takes precedence over the environment variable.

#### For example:



```python
import os
import tensorflow as tf

os.environ['AUTOGRAPH_VERBOSITY'] = 5
# Verbosity is now 5

tf.autograph.set_verbosity(0)
# Verbosity is now 0

os.environ['AUTOGRAPH_VERBOSITY'] = 1
# No effect, because set_verbosity was already called.
```

Logs entries are output to [absl](https://abseil.io)'s 
[default output](https://abseil.io/docs/python/guides/logging),
with `INFO` level.
Logs can be mirrored to stdout by using the `alsologtostdout` argument.
Mirroring is enabled by default when Python runs in interactive mode.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`level`
</td>
<td>
int, the verbosity level; larger values specify increased verbosity;
0 means no logging. When reporting bugs, it is recommended to set this
value to a larger number, like 10.
</td>
</tr><tr>
<td>
`alsologtostdout`
</td>
<td>
bool, whether to also output log messages to `sys.stdout`.
</td>
</tr>
</table>

