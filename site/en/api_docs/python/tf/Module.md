description: Base neural network module class.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.Module" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="with_name_scope"/>
</div>

# tf.Module

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/module/module.py#L35-L302">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Base neural network module class.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.Module`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.Module(
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

A module is a named container for <a href="../tf/Variable.md"><code>tf.Variable</code></a>s, other <a href="../tf/Module.md"><code>tf.Module</code></a>s and
functions which apply to user input. For example a dense layer in a neural
network might be implemented as a <a href="../tf/Module.md"><code>tf.Module</code></a>:

```
>>> class Dense(tf.Module):
...   def __init__(self, input_dim, output_size, name=None):
...     super(Dense, self).__init__(name=name)
...     self.w = tf.Variable(
...       tf.random.normal([input_dim, output_size]), name='w')
...     self.b = tf.Variable(tf.zeros([output_size]), name='b')
...   def __call__(self, x):
...     y = tf.matmul(x, self.w) + self.b
...     return tf.nn.relu(y)
```

You can use the Dense layer as you would expect:

```
>>> d = Dense(input_dim=3, output_size=2)
>>> d(tf.ones([1, 3]))
<tf.Tensor: shape=(1, 2), dtype=float32, numpy=..., dtype=float32)>
```


By subclassing <a href="../tf/Module.md"><code>tf.Module</code></a> instead of `object` any <a href="../tf/Variable.md"><code>tf.Variable</code></a> or
<a href="../tf/Module.md"><code>tf.Module</code></a> instances assigned to object properties can be collected using
the `variables`, `trainable_variables` or `submodules` property:

```
>>> d.variables
    (<tf.Variable 'b:0' shape=(2,) dtype=float32, numpy=...,
    dtype=float32)>,
    <tf.Variable 'w:0' shape=(3, 2) dtype=float32, numpy=..., dtype=float32)>)
```


Subclasses of <a href="../tf/Module.md"><code>tf.Module</code></a> can also take advantage of the `_flatten` method
which can be used to implement tracking of any other types.

All <a href="../tf/Module.md"><code>tf.Module</code></a> classes have an associated <a href="../tf/name_scope.md"><code>tf.name_scope</code></a> which can be used
to group operations in TensorBoard and create hierarchies for variable names
which can help with debugging. We suggest using the name scope when creating
nested submodules/parameters or for forward methods whose graph you might want
to inspect in TensorBoard. You can enter the name scope explicitly using
`with self.name_scope:` or you can annotate methods (apart from `__init__`)
with `@tf.Module.with_name_scope`.

```
>>> class MLP(tf.Module):
...   def __init__(self, input_size, sizes, name=None):
...     super(MLP, self).__init__(name=name)
...     self.layers = []
...     with self.name_scope:
...       for size in sizes:
...         self.layers.append(Dense(input_dim=input_size, output_size=size))
...         input_size = size
...   @tf.Module.with_name_scope
...   def __call__(self, x):
...     for layer in self.layers:
...       x = layer(x)
...     return x
```

```
>>> module = MLP(input_size=5, sizes=[5, 5])
>>> module.variables
(<tf.Variable 'mlp/b:0' shape=(5,) dtype=float32, numpy=..., dtype=float32)>,
<tf.Variable 'mlp/w:0' shape=(5, 5) dtype=float32, numpy=...,
   dtype=float32)>,
<tf.Variable 'mlp/b:0' shape=(5,) dtype=float32, numpy=..., dtype=float32)>,
<tf.Variable 'mlp/w:0' shape=(5, 5) dtype=float32, numpy=...,
   dtype=float32)>)
```



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`name`
</td>
<td>
Returns the name of this module as passed or determined in the ctor.

NOTE: This is not the same as the `self.name_scope.name` which includes
parent module names.
</td>
</tr><tr>
<td>
`name_scope`
</td>
<td>
Returns a <a href="../tf/name_scope.md"><code>tf.name_scope</code></a> instance for this class.
</td>
</tr><tr>
<td>
`submodules`
</td>
<td>
Sequence of all sub-modules.

Submodules are modules which are properties of this module, or found as
properties of modules which are properties of this module (and so on).

```
>>> a = tf.Module()
>>> b = tf.Module()
>>> c = tf.Module()
>>> a.b = b
>>> b.c = c
>>> list(a.submodules) == [b, c]
True
>>> list(b.submodules) == [c]
True
>>> list(c.submodules) == []
True
```
</td>
</tr><tr>
<td>
`trainable_variables`
</td>
<td>
Sequence of trainable variables owned by this module and its submodules.

Note: this method uses reflection to find variables on the current instance
and submodules. For performance reasons you may wish to cache the result
of calling this method if you don't expect the return value to change.
</td>
</tr><tr>
<td>
`variables`
</td>
<td>
Sequence of variables owned by this module and its submodules.

Note: this method uses reflection to find variables on the current instance
and submodules. For performance reasons you may wish to cache the result
of calling this method if you don't expect the return value to change.
</td>
</tr>
</table>



## Methods

<h3 id="with_name_scope"><code>with_name_scope</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/module/module.py#L271-L302">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>with_name_scope(
    method
)
</code></pre>

Decorator to automatically enter the module name scope.

```
>>> class MyModule(tf.Module):
...   @tf.Module.with_name_scope
...   def __call__(self, x):
...     if not hasattr(self, 'w'):
...       self.w = tf.Variable(tf.random.normal([x.shape[1], 3]))
...     return tf.matmul(x, self.w)
```

Using the above module would produce <a href="../tf/Variable.md"><code>tf.Variable</code></a>s and <a href="../tf/Tensor.md"><code>tf.Tensor</code></a>s whose
names included the module name:

```
>>> mod = MyModule()
>>> mod(tf.ones([1, 2]))
<tf.Tensor: shape=(1, 3), dtype=float32, numpy=..., dtype=float32)>
>>> mod.w
<tf.Variable 'my_module/Variable:0' shape=(2, 3) dtype=float32,
numpy=..., dtype=float32)>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`method`
</td>
<td>
The method to wrap.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The original method wrapped such that it enters the module's name scope.
</td>
</tr>

</table>





