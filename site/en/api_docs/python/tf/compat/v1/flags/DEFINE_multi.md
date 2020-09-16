description: Registers a generic MultiFlag that parses its args with a given parser.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.flags.DEFINE_multi" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.flags.DEFINE_multi

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Registers a generic MultiFlag that parses its args with a given parser.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.app.flags.DEFINE_multi`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.flags.DEFINE_multi(
    parser, serializer, name, default, help, flag_values=_flagvalues.FLAGS,
    module_name=None, **args
)
</code></pre>



<!-- Placeholder for "Used in" -->

Auxiliary function.  Normal users should NOT use it directly.

Developers who need to create their own 'Parser' classes for options
which can appear multiple times can call this module function to
register their flags.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`parser`
</td>
<td>
ArgumentParser, used to parse the flag arguments.
</td>
</tr><tr>
<td>
`serializer`
</td>
<td>
ArgumentSerializer, the flag serializer instance.
</td>
</tr><tr>
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
Union[Iterable[T], Text, None], the default value of the flag.
If the value is text, it will be parsed as if it was provided from
the command line. If the value is a non-string iterable, it will be
iterated over to create a shallow copy of the values. If it is None,
it is left as-is.
</td>
</tr><tr>
<td>
`help`
</td>
<td>
str, the help message.
</td>
</tr><tr>
<td>
`flag_values`
</td>
<td>
FlagValues, the FlagValues instance with which the flag will
be registered. This should almost never need to be overridden.
</td>
</tr><tr>
<td>
`module_name`
</td>
<td>
A string, the name of the Python module declaring this flag.
If not provided, it will be computed using the stack trace of this call.
</td>
</tr><tr>
<td>
`**args`
</td>
<td>
Dictionary with extra keyword args that are passed to the
Flag __init__.
</td>
</tr>
</table>

