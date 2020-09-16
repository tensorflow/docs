description: Base class used to parse and convert arguments.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.flags.ArgumentParser" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="flag_type"/>
<meta itemprop="property" content="parse"/>
<meta itemprop="property" content="syntactic_help"/>
</div>

# tf.compat.v1.flags.ArgumentParser

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Base class used to parse and convert arguments.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.app.flags.ArgumentParser`</p>
</p>
</section>

<!-- Placeholder for "Used in" -->

The parse() method checks to make sure that the string argument is a
legal value and convert it to a native type.  If the value cannot be
converted, it should throw a 'ValueError' exception with a human
readable explanation of why the value is illegal.

Subclasses should also define a syntactic_help string which may be
presented to the user to describe the form of the legal values.

Argument parser classes must be stateless, since instances are cached
and shared between flags. Initializer arguments are allowed, but all
member variables must be derived from initializer arguments only.

## Methods

<h3 id="flag_type"><code>flag_type</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>flag_type()
</code></pre>

Returns a string representing the type of the flag.


<h3 id="parse"><code>parse</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>parse(
    argument
)
</code></pre>

Parses the string argument and returns the native value.

By default it returns its argument unmodified.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`argument`
</td>
<td>
string argument passed in the commandline.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
Raised when it fails to parse the argument.
</td>
</tr><tr>
<td>
`TypeError`
</td>
<td>
Raised when the argument has the wrong type.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The parsed value in native type.
</td>
</tr>

</table>





## Class Variables

* `syntactic_help = ''` <a id="syntactic_help"></a>
