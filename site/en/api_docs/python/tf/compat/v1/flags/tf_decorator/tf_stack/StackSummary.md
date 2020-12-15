<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.flags.tf_decorator.tf_stack.StackSummary" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__bool__"/>
<meta itemprop="property" content="__contains__"/>
<meta itemprop="property" content="__eq__"/>
<meta itemprop="property" content="__getitem__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__iter__"/>
<meta itemprop="property" content="__len__"/>
<meta itemprop="property" content="__ne__"/>
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="append"/>
<meta itemprop="property" content="count"/>
<meta itemprop="property" content="extend"/>
<meta itemprop="property" content="insert"/>
<meta itemprop="property" content="pop"/>
<meta itemprop="property" content="remove"/>
</div>

# tf.compat.v1.flags.tf_decorator.tf_stack.StackSummary

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/_tf_stack.so">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>





<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.app.flags.tf_decorator.tf_stack.StackSummary`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.flags.tf_decorator.tf_stack.StackSummary()
</code></pre>



<!-- Placeholder for "Used in" -->


## Methods

<h3 id="append"><code>append</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>append()
</code></pre>

append(self: tensorflow.python._tf_stack.StackSummary, x: tensorflow.python._tf_stack.FrameSummary) -> None

Add an item to the end of the list

<h3 id="count"><code>count</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>count()
</code></pre>

count(self: tensorflow.python._tf_stack.StackSummary, x: tensorflow.python._tf_stack.FrameSummary) -> int

Return the number of times ``x`` appears in the list

<h3 id="extend"><code>extend</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>extend()
</code></pre>

extend(*args, **kwargs)
Overloaded function.

1. extend(self: tensorflow.python._tf_stack.StackSummary, L: tensorflow.python._tf_stack.StackSummary) -> None

Extend the list by appending all the items in the given list

2. extend(self: tensorflow.python._tf_stack.StackSummary, L: iterable) -> None

Extend the list by appending all the items in the given list

<h3 id="insert"><code>insert</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>insert()
</code></pre>

insert(self: tensorflow.python._tf_stack.StackSummary, i: int, x: tensorflow.python._tf_stack.FrameSummary) -> None

Insert an item at a given position.

<h3 id="pop"><code>pop</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>pop()
</code></pre>

pop(*args, **kwargs)
Overloaded function.

1. pop(self: tensorflow.python._tf_stack.StackSummary) -> tensorflow.python._tf_stack.FrameSummary

Remove and return the last item

2. pop(self: tensorflow.python._tf_stack.StackSummary, i: int) -> tensorflow.python._tf_stack.FrameSummary

Remove and return the item at index ``i``

<h3 id="remove"><code>remove</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>remove()
</code></pre>

remove(self: tensorflow.python._tf_stack.StackSummary, x: tensorflow.python._tf_stack.FrameSummary) -> None

Remove the first item from the list whose value is x. It is an error if there is no such item.

<h3 id="__bool__"><code>__bool__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__bool__()
</code></pre>

__bool__(self: tensorflow.python._tf_stack.StackSummary) -> bool

Check whether the list is nonempty

<h3 id="__contains__"><code>__contains__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__contains__()
</code></pre>

__contains__(self: tensorflow.python._tf_stack.StackSummary, x: tensorflow.python._tf_stack.FrameSummary) -> bool

Return true the container contains ``x``

<h3 id="__eq__"><code>__eq__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__eq__()
</code></pre>

__eq__(self: tensorflow.python._tf_stack.StackSummary, arg0: tensorflow.python._tf_stack.StackSummary) -> bool


<h3 id="__getitem__"><code>__getitem__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__getitem__()
</code></pre>

__getitem__(*args, **kwargs)
Overloaded function.

1. __getitem__(self: tensorflow.python._tf_stack.StackSummary, s: slice) -> tensorflow.python._tf_stack.StackSummary

Retrieve list elements using a slice object

2. __getitem__(self: tensorflow.python._tf_stack.StackSummary, arg0: int) -> tensorflow.python._tf_stack.FrameSummary

3. __getitem__(self: tensorflow.python._tf_stack.StackSummary, arg0: int) -> tensorflow.python._tf_stack.FrameSummary

<h3 id="__iter__"><code>__iter__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__iter__()
</code></pre>

__iter__(self: tensorflow.python._tf_stack.StackSummary) -> iterator


<h3 id="__len__"><code>__len__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__len__()
</code></pre>

__len__(self: tensorflow.python._tf_stack.StackSummary) -> int


<h3 id="__ne__"><code>__ne__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__ne__()
</code></pre>

__ne__(self: tensorflow.python._tf_stack.StackSummary, arg0: tensorflow.python._tf_stack.StackSummary) -> bool




