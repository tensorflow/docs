description: Base class for generating string representations of a flag value.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.flags.CsvListSerializer" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="serialize"/>
</div>

# tf.compat.v1.flags.CsvListSerializer

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Base class for generating string representations of a flag value.

Inherits From: [`ArgumentSerializer`](../../../../tf/compat/v1/flags/ArgumentSerializer.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.app.flags.CsvListSerializer`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.flags.CsvListSerializer(
    list_sep
)
</code></pre>



<!-- Placeholder for "Used in" -->


## Methods

<h3 id="serialize"><code>serialize</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>serialize(
    value
)
</code></pre>

Serializes a list as a CSV string or unicode.




