description: Adds a constraint to multiple flags.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.flags.register_multi_flags_validator" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.flags.register_multi_flags_validator

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Adds a constraint to multiple flags.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.app.flags.register_multi_flags_validator`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.flags.register_multi_flags_validator(
    flag_names, multi_flags_checker, message='Flags validation failed',
    flag_values=_flagvalues.FLAGS
)
</code></pre>



<!-- Placeholder for "Used in" -->

The constraint is validated when flags are initially parsed, and after each
change of the corresponding flag's value.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`flag_names`
</td>
<td>
[str], a list of the flag names to be checked.
</td>
</tr><tr>
<td>
`multi_flags_checker`
</td>
<td>
callable, a function to validate the flag.
input - dict, with keys() being flag_names, and value for each key
being the value of the corresponding flag (string, boolean, etc).
output - bool, True if validator constraint is satisfied.
If constraint is not satisfied, it should either return False or
raise flags.ValidationError.
</td>
</tr><tr>
<td>
`message`
</td>
<td>
str, error text to be shown to the user if checker returns False.
If checker raises flags.ValidationError, message from the raised
error will be shown.
</td>
</tr><tr>
<td>
`flag_values`
</td>
<td>
flags.FlagValues, optional FlagValues instance to validate
against.
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
Raised when a flag is not registered as a valid flag name.
</td>
</tr>
</table>

