description: Parser of an integer value.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.flags.IntegerParser" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="convert"/>
<meta itemprop="property" content="flag_type"/>
<meta itemprop="property" content="is_outside_bounds"/>
<meta itemprop="property" content="parse"/>
<meta itemprop="property" content="number_article"/>
<meta itemprop="property" content="number_name"/>
<meta itemprop="property" content="syntactic_help"/>
</div>

# tf.compat.v1.flags.IntegerParser

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Parser of an integer value.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.app.flags.IntegerParser`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.flags.IntegerParser(
    lower_bound=None, upper_bound=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Parsed value may be bounded to a given upper and lower bound.

## Methods

<h3 id="convert"><code>convert</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>convert(
    argument
)
</code></pre>

Returns the int value of argument.


<h3 id="flag_type"><code>flag_type</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>flag_type()
</code></pre>

See base class.


<h3 id="is_outside_bounds"><code>is_outside_bounds</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>is_outside_bounds(
    val
)
</code></pre>

Returns whether the value is outside the bounds or not.


<h3 id="parse"><code>parse</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>parse(
    argument
)
</code></pre>

See base class.




## Class Variables

* `number_article = 'an'` <a id="number_article"></a>
* `number_name = 'integer'` <a id="number_name"></a>
* `syntactic_help = 'an integer'` <a id="syntactic_help"></a>
