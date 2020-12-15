description: Parser of an Enum class member.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.flags.EnumClassParser" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="flag_type"/>
<meta itemprop="property" content="parse"/>
<meta itemprop="property" content="syntactic_help"/>
</div>

# tf.compat.v1.flags.EnumClassParser

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Parser of an Enum class member.

Inherits From: [`ArgumentParser`](../../../../tf/compat/v1/flags/ArgumentParser.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.app.flags.EnumClassParser`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.flags.EnumClassParser(
    enum_class, case_sensitive=(True)
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`enum_class`
</td>
<td>
class, the Enum class with all possible flag values.
</td>
</tr><tr>
<td>
`case_sensitive`
</td>
<td>
bool, whether or not the enum is to be case-sensitive. If
False, all member names must be unique when case is ignored.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
When enum_class is not a subclass of Enum.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
When enum_class is empty.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`member_names`
</td>
<td>
The accepted enum names, in lowercase if not case sensitive.
</td>
</tr>
</table>



## Methods

<h3 id="flag_type"><code>flag_type</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>flag_type()
</code></pre>

See base class.


<h3 id="parse"><code>parse</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>parse(
    argument
)
</code></pre>

Determines validity of argument and returns the correct element of enum.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`argument`
</td>
<td>
str or Enum class member, the supplied flag value.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The first matching Enum class member in Enum class.
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
Raised when argument didn't match anything in enum.
</td>
</tr>
</table>





## Class Variables

* `syntactic_help = ''` <a id="syntactic_help"></a>
