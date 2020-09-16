description: Registers a flag whose value can be any string from enum_values.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.flags.DEFINE_enum" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.flags.DEFINE_enum

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Registers a flag whose value can be any string from enum_values.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.app.flags.DEFINE_enum`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.flags.DEFINE_enum(
    name, default, enum_values, help, flag_values=_flagvalues.FLAGS,
    module_name=None, **args
)
</code></pre>



<!-- Placeholder for "Used in" -->

Instead of a string enum, prefer `DEFINE_enum_class`, which allows
defining enums from an `enum.Enum` class.

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
str|None, the default value of the flag.
</td>
</tr><tr>
<td>
`enum_values`
</td>
<td>
[str], a non-empty list of strings with the possible values for
the flag.
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
`flag_values`
</td>
<td>
FlagValues, the FlagValues instance with which the flag will
be registered. This should almost never need to be overridden.
</td>
</tr><tr>
<td>
`module_name`
</td>
<td>
str, the name of the Python module declaring this flag.
If not provided, it will be computed using the stack trace of this call.
</td>
</tr><tr>
<td>
`**args`
</td>
<td>
dict, the extra keyword args that are passed to Flag __init__.
</td>
</tr>
</table>

