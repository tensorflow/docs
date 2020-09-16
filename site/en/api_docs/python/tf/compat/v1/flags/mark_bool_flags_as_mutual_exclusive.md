description: Ensures that only one flag among flag_names is True.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.flags.mark_bool_flags_as_mutual_exclusive" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.flags.mark_bool_flags_as_mutual_exclusive

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Ensures that only one flag among flag_names is True.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.app.flags.mark_bool_flags_as_mutual_exclusive`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.flags.mark_bool_flags_as_mutual_exclusive(
    flag_names, required=(False), flag_values=_flagvalues.FLAGS
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`flag_names`
</td>
<td>
[str], names of the flags.
</td>
</tr><tr>
<td>
`required`
</td>
<td>
bool. If true, exactly one flag must be True. Otherwise, at most
one flag can be True, and it is valid for all flags to be False.
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

