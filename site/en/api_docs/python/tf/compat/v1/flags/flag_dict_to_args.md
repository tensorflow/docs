description: Convert a dict of values into process call parameters.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.flags.flag_dict_to_args" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.flags.flag_dict_to_args

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Convert a dict of values into process call parameters.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.app.flags.flag_dict_to_args`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.flags.flag_dict_to_args(
    flag_map
)
</code></pre>



<!-- Placeholder for "Used in" -->

This method is used to convert a dictionary into a sequence of parameters
for a binary that parses arguments using this module.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`flag_map`
</td>
<td>
dict, a mapping where the keys are flag names (strings).
values are treated according to their type:
* If value is None, then only the name is emitted.
* If value is True, then only the name is emitted.
* If value is False, then only the name prepended with 'no' is emitted.
* If value is a string then --name=value is emitted.
* If value is a collection, this will emit --name=value1,value2,value3.
* Everything else is converted to string an passed as such.
</td>
</tr>
</table>



#### Yields:

sequence of string suitable for a subprocess execution.
