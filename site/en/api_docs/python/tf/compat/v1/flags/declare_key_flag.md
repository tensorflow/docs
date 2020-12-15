description: Declares one flag as key to the current module.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.flags.declare_key_flag" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.flags.declare_key_flag

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Declares one flag as key to the current module.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.app.flags.declare_key_flag`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.flags.declare_key_flag(
    flag_name, flag_values=_flagvalues.FLAGS
)
</code></pre>



<!-- Placeholder for "Used in" -->

Key flags are flags that are deemed really important for a module.
They are important when listing help messages; e.g., if the
--helpshort command-line flag is used, then only the key flags of the
main module are listed (instead of all flags, as in the case of
--helpfull).

#### Sample usage:


flags.declare_key_flag('flag_1')



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`flag_name`
</td>
<td>
str, the name of an already declared flag. (Redeclaring flags as
key, including flags implicitly key because they were declared in this
module, is a no-op.)
</td>
</tr><tr>
<td>
`flag_values`
</td>
<td>
FlagValues, the FlagValues instance in which the flag will be
declared as a key flag. This should almost never need to be overridden.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
Raised if flag_name not defined as a Python flag.
</td>
</tr>
</table>

