description: Registers a flag whose value can be a list of enum members.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.flags.DEFINE_multi_enum_class" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.flags.DEFINE_multi_enum_class

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Registers a flag whose value can be a list of enum members.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.app.flags.DEFINE_multi_enum_class`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.flags.DEFINE_multi_enum_class(
    name, default, enum_class, help, flag_values=_flagvalues.FLAGS,
    module_name=None, case_sensitive=(False), **args
)
</code></pre>



<!-- Placeholder for "Used in" -->

Use the flag on the command line multiple times to place multiple
enum values into the list.

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
Union[Iterable[Enum], Iterable[Text], Enum, Text, None], the
default value of the flag; see `DEFINE_multi`; only differences are
documented here. If the value is a single Enum, it is treated as a
single-item list of that Enum value. If it is an iterable, text values
within the iterable will be converted to the equivalent Enum objects.
</td>
</tr><tr>
<td>
`enum_class`
</td>
<td>
class, the Enum class with all the possible values for the flag.
help: str, the help message.
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
A string, the name of the Python module declaring this flag. If
not provided, it will be computed using the stack trace of this call.
</td>
</tr><tr>
<td>
`case_sensitive`
</td>
<td>
bool, whether to map strings to members of the enum_class
without considering case.
</td>
</tr><tr>
<td>
`**args`
</td>
<td>
Dictionary with extra keyword args that are passed to the Flag
__init__.
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

