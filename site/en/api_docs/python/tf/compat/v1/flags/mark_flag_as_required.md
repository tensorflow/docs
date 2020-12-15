description: Ensures that flag is not None during program execution.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.flags.mark_flag_as_required" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.flags.mark_flag_as_required

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Ensures that flag is not None during program execution.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.app.flags.mark_flag_as_required`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.flags.mark_flag_as_required(
    flag_name, flag_values=_flagvalues.FLAGS
)
</code></pre>



<!-- Placeholder for "Used in" -->

Registers a flag validator, which will follow usual validator rules.
Important note: validator will pass for any non-None value, such as False,
0 (zero), '' (empty string) and so on.

If your module might be imported by others, and you only wish to make the flag
required when the module is directly executed, call this method like this:

  if __name__ == '__main__':
    flags.mark_flag_as_required('your_flag_name')
    app.run()

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`flag_name`
</td>
<td>
str, name of the flag
</td>
</tr><tr>
<td>
`flag_values`
</td>
<td>
flags.FlagValues, optional FlagValues instance where the flag
is defined.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`AttributeError`
</td>
<td>
Raised when flag_name is not registered as a valid flag
name.
</td>
</tr>
</table>

