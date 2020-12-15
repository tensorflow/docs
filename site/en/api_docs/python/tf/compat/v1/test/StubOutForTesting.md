description: Support class for stubbing methods out for unit testing.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.test.StubOutForTesting" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="CleanUp"/>
<meta itemprop="property" content="Set"/>
<meta itemprop="property" content="SmartSet"/>
<meta itemprop="property" content="SmartUnsetAll"/>
<meta itemprop="property" content="UnsetAll"/>
<meta itemprop="property" content="__enter__"/>
<meta itemprop="property" content="__exit__"/>
<meta itemprop="property" content="__init__"/>
</div>

# tf.compat.v1.test.StubOutForTesting

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/platform/googletest.py#L116-L273">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Support class for stubbing methods out for unit testing.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.test.StubOutForTesting()
</code></pre>



<!-- Placeholder for "Used in" -->


#### Sample Usage:



You want os.path.exists() to always return true during testing.

   stubs = StubOutForTesting()
   stubs.Set(os.path, 'exists', lambda x: 1)
     ...
   stubs.CleanUp()

The above changes os.path.exists into a lambda that returns 1.  Once
the ... part of the code finishes, the CleanUp() looks up the old
value of os.path.exists and restores it.

## Methods

<h3 id="CleanUp"><code>CleanUp</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/platform/googletest.py#L152-L155">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>CleanUp()
</code></pre>

Undoes all SmartSet() & Set() calls, restoring original definitions.


<h3 id="Set"><code>Set</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/platform/googletest.py#L234-L258">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>Set(
    parent, child_name, new_child
)
</code></pre>

In parent, replace child_name's old definition with new_child.

The parent could be a module when the child is a function at
module scope.  Or the parent could be a class when a class' method
is being replaced.  The named child is set to new_child, while the
prior definition is saved away for later, when UnsetAll() is
called.

This method supports the case where child_name is a staticmethod or a
classmethod of parent.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`parent`
</td>
<td>
The context in which the attribute child_name is to be changed.
</td>
</tr><tr>
<td>
`child_name`
</td>
<td>
The name of the attribute to change.
</td>
</tr><tr>
<td>
`new_child`
</td>
<td>
The new value of the attribute.
</td>
</tr>
</table>



<h3 id="SmartSet"><code>SmartSet</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/platform/googletest.py#L157-L218">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>SmartSet(
    obj, attr_name, new_attr
)
</code></pre>

Replace obj.attr_name with new_attr.

This method is smart and works at the module, class, and instance level
while preserving proper inheritance. It will not stub out C types however
unless that has been explicitly allowed by the type.

This method supports the case where attr_name is a staticmethod or a
classmethod of obj.

#### Notes:

- If obj is an instance, then it is its class that will actually be
  stubbed. Note that the method Set() does not do that: if obj is
  an instance, it (and not its class) will be stubbed.
- The stubbing is using the builtin getattr and setattr. So, the __get__
  and __set__ will be called when stubbing (
  probably be to manipulate obj.__dict__ instead of getattr() and
  setattr()).



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`obj`
</td>
<td>
The object whose attributes we want to modify.
</td>
</tr><tr>
<td>
`attr_name`
</td>
<td>
The name of the attribute to modify.
</td>
</tr><tr>
<td>
`new_attr`
</td>
<td>
The new value for the attribute.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`AttributeError`
</td>
<td>
If the attribute cannot be found.
</td>
</tr>
</table>



<h3 id="SmartUnsetAll"><code>SmartUnsetAll</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/platform/googletest.py#L220-L232">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>SmartUnsetAll()
</code></pre>

Reverses SmartSet() calls, restoring things to original definitions.

This method is automatically called when the StubOutForTesting()
object is deleted; there is no need to call it explicitly.

It is okay to call SmartUnsetAll() repeatedly, as later calls have
no effect if no SmartSet() calls have been made.

<h3 id="UnsetAll"><code>UnsetAll</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/platform/googletest.py#L260-L273">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>UnsetAll()
</code></pre>

Reverses Set() calls, restoring things to their original definitions.

This method is automatically called when the StubOutForTesting()
object is deleted; there is no need to call it explicitly.

It is okay to call UnsetAll() repeatedly, as later calls have no
effect if no Set() calls have been made.

<h3 id="__enter__"><code>__enter__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/platform/googletest.py#L146-L147">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__enter__()
</code></pre>




<h3 id="__exit__"><code>__exit__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/platform/googletest.py#L149-L150">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__exit__(
    unused_exc_type, unused_exc_value, unused_tb
)
</code></pre>






