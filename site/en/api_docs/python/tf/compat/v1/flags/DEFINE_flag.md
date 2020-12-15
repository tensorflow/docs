description: Registers a 'Flag' object with a 'FlagValues' object.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.flags.DEFINE_flag" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.flags.DEFINE_flag

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Registers a 'Flag' object with a 'FlagValues' object.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.app.flags.DEFINE_flag`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.flags.DEFINE_flag(
    flag, flag_values=_flagvalues.FLAGS, module_name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

By default, the global FLAGS 'FlagValue' object is used.

Typical users will use one of the more specialized DEFINE_xxx
functions, such as DEFINE_string or DEFINE_integer.  But developers
who need to create Flag objects themselves should use this function
to register their flags.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`flag`
</td>
<td>
Flag, a flag that is key to the module.
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

