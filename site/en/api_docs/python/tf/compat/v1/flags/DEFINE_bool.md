description: Registers a boolean flag.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.flags.DEFINE_bool" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.flags.DEFINE_bool

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Registers a boolean flag.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.app.flags.DEFINE_bool`, `tf.compat.v1.app.flags.DEFINE_boolean`, `tf.compat.v1.flags.DEFINE_boolean`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.flags.DEFINE_bool(
    name, default, help, flag_values=_flagvalues.FLAGS, module_name=None, **args
)
</code></pre>



<!-- Placeholder for "Used in" -->

Such a boolean flag does not take an argument.  If a user wants to
specify a false value explicitly, the long option beginning with 'no'
must be used: i.e. --noflag

This flag will have a value of None, True or False.  None is possible
if default=None and the user does not specify the flag on the command
line.

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
bool|str|None, the default value of the flag.
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
FlagValues, the FlagValues instance with which the flag will be
registered. This should almost never need to be overridden.
</td>
</tr><tr>
<td>
`module_name`
</td>
<td>
str, the name of the Python module declaring this flag. If not
provided, it will be computed using the stack trace of this call.
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



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
a handle to defined flag.
</td>
</tr>

</table>

