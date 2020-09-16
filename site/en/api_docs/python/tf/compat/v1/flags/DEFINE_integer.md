description: Registers a flag whose value must be an integer.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.flags.DEFINE_integer" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.flags.DEFINE_integer

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Registers a flag whose value must be an integer.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.app.flags.DEFINE_integer`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.flags.DEFINE_integer(
    name, default, help, lower_bound=None, upper_bound=None,
    flag_values=_flagvalues.FLAGS, **args
)
</code></pre>



<!-- Placeholder for "Used in" -->

If lower_bound, or upper_bound are set, then this flag must be
within the given range.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`name`
</td>
<td>
str, the flag name.
</td>
</tr><tr>
<td>
`default`
</td>
<td>
int|str|None, the default value of the flag.
</td>
</tr><tr>
<td>
`help`
</td>
<td>
str, the help message.
</td>
</tr><tr>
<td>
`lower_bound`
</td>
<td>
int, min value of the flag.
</td>
</tr><tr>
<td>
`upper_bound`
</td>
<td>
int, max value of the flag.
</td>
</tr><tr>
<td>
`flag_values`
</td>
<td>
FlagValues, the FlagValues instance with which the flag will
be registered. This should almost never need to be overridden.
</td>
</tr><tr>
<td>
`**args`
</td>
<td>
dict, the extra keyword args that are passed to DEFINE.
</td>
</tr>
</table>

