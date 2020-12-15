description: Ensures that flags are not None during program execution.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.flags.mark_flags_as_required" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.flags.mark_flags_as_required

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Ensures that flags are not None during program execution.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.app.flags.mark_flags_as_required`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.flags.mark_flags_as_required(
    flag_names, flag_values=_flagvalues.FLAGS
)
</code></pre>



<!-- Placeholder for "Used in" -->

If your module might be imported by others, and you only wish to make the flag
required when the module is directly executed, call this method like this:

  if __name__ == '__main__':
    flags.mark_flags_as_required(['flag1', 'flag2', 'flag3'])
    app.run()

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`flag_names`
</td>
<td>
Sequence[str], names of the flags.
</td>
</tr><tr>
<td>
`flag_values`
</td>
<td>
flags.FlagValues, optional FlagValues instance where the flags
are defined.
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
If any of flag name has not already been defined as a flag.
</td>
</tr>
</table>

