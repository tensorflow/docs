description: Raised if there is a flag naming conflict.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.flags.DuplicateFlagError" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="from_flag"/>
</div>

# tf.compat.v1.flags.DuplicateFlagError

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Raised if there is a flag naming conflict.

Inherits From: [`Error`](../../../../tf/compat/v1/flags/Error.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.app.flags.DuplicateFlagError`</p>
</p>
</section>

<!-- Placeholder for "Used in" -->


## Methods

<h3 id="from_flag"><code>from_flag</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>from_flag(
    flagname, flag_values, other_flag_values=None
)
</code></pre>

Creates a DuplicateFlagError by providing flag name and values.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`flagname`
</td>
<td>
str, the name of the flag being redefined.
</td>
</tr><tr>
<td>
`flag_values`
</td>
<td>
FlagValues, the FlagValues instance containing the first
definition of flagname.
</td>
</tr><tr>
<td>
`other_flag_values`
</td>
<td>
FlagValues, if it is not None, it should be the
FlagValues object where the second definition of flagname occurs.
If it is None, we assume that we're being called when attempting
to create the flag a second time, and we use the module calling
this one as the source of the second definition.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
An instance of DuplicateFlagError.
</td>
</tr>

</table>





