description: Declares that all flags key to a module are key to the current module.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.flags.adopt_module_key_flags" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.flags.adopt_module_key_flags

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Declares that all flags key to a module are key to the current module.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.app.flags.adopt_module_key_flags`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.flags.adopt_module_key_flags(
    module, flag_values=_flagvalues.FLAGS
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`module`
</td>
<td>
module, the module object from which all key flags will be declared
as key flags to the current module.
</td>
</tr><tr>
<td>
`flag_values`
</td>
<td>
FlagValues, the FlagValues instance in which the flags will be
declared as key flags. This should almost never need to be overridden.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`Error`
</td>
<td>
Raised when given an argument that is a module name (a string),
instead of a module object.
</td>
</tr>
</table>

