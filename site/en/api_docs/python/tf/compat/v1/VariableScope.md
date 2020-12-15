description: Variable scope object to carry defaults to provide to get_variable.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.VariableScope" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="get_collection"/>
<meta itemprop="property" content="get_variable"/>
<meta itemprop="property" content="global_variables"/>
<meta itemprop="property" content="local_variables"/>
<meta itemprop="property" content="reuse_variables"/>
<meta itemprop="property" content="set_caching_device"/>
<meta itemprop="property" content="set_custom_getter"/>
<meta itemprop="property" content="set_dtype"/>
<meta itemprop="property" content="set_initializer"/>
<meta itemprop="property" content="set_partitioner"/>
<meta itemprop="property" content="set_regularizer"/>
<meta itemprop="property" content="set_use_resource"/>
<meta itemprop="property" content="trainable_variables"/>
</div>

# tf.compat.v1.VariableScope

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/variable_scope.py#L1083-L1389">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Variable scope object to carry defaults to provide to `get_variable`.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.VariableScope(
    reuse, name='', initializer=None, regularizer=None, caching_device=None,
    partitioner=None, custom_getter=None, name_scope='', dtype=tf.dtypes.float32,
    use_resource=None, constraint=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Many of the arguments we need for `get_variable` in a variable store are most
easily handled with a context. This object is used for the defaults.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`name`
</td>
<td>
name of the current scope, used as prefix in get_variable.
</td>
</tr><tr>
<td>
`initializer`
</td>
<td>
default initializer passed to get_variable.
</td>
</tr><tr>
<td>
`regularizer`
</td>
<td>
default regularizer passed to get_variable.
</td>
</tr><tr>
<td>
`reuse`
</td>
<td>
Boolean, None, or tf.compat.v1.AUTO_REUSE, setting the reuse in
get_variable. When eager execution is enabled this argument is always
forced to be False.
</td>
</tr><tr>
<td>
`caching_device`
</td>
<td>
string, callable, or None: the caching device passed to
get_variable.
</td>
</tr><tr>
<td>
`partitioner`
</td>
<td>
callable or `None`: the partitioner passed to `get_variable`.
</td>
</tr><tr>
<td>
`custom_getter`
</td>
<td>
default custom getter passed to get_variable.
</td>
</tr><tr>
<td>
`name_scope`
</td>
<td>
The name passed to <a href="../../../tf/name_scope.md"><code>tf.name_scope</code></a>.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
default type passed to get_variable (defaults to DT_FLOAT).
</td>
</tr><tr>
<td>
`use_resource`
</td>
<td>
if False, create a normal Variable; if True create an
experimental ResourceVariable with well-defined semantics. Defaults to
False (will later change to True). When eager execution is enabled this
argument is always forced to be True.
</td>
</tr><tr>
<td>
`constraint`
</td>
<td>
An optional projection function to be applied to the variable
after being updated by an `Optimizer` (e.g. used to implement norm
constraints or value constraints for layer weights). The function must
take as input the unprojected Tensor representing the value of the
variable and return the Tensor for the projected value (which must have
the same shape). Constraints are not safe to use when doing asynchronous
distributed training.
</td>
</tr><tr>
<td>
`original_name_scope`
</td>
<td>

</td>
</tr>
</table>



## Methods

<h3 id="get_collection"><code>get_collection</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/variable_scope.py#L1228-L1231">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_collection(
    name
)
</code></pre>

Get this scope's variables.


<h3 id="get_variable"><code>get_variable</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/variable_scope.py#L1245-L1315">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_variable(
    var_store, name, shape=None, dtype=None, initializer=None, regularizer=None,
    reuse=None, trainable=None, collections=None, caching_device=None,
    partitioner=None, validate_shape=(True), use_resource=None, custom_getter=None,
    constraint=None, synchronization=tf.VariableSynchronization.AUTO,
    aggregation=tf.compat.v1.VariableAggregation.NONE
)
</code></pre>

Gets an existing variable with this name or create a new one.


<h3 id="global_variables"><code>global_variables</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/variable_scope.py#L1237-L1239">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>global_variables()
</code></pre>

Get this scope's global variables.


<h3 id="local_variables"><code>local_variables</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/variable_scope.py#L1241-L1243">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>local_variables()
</code></pre>

Get this scope's local variables.


<h3 id="reuse_variables"><code>reuse_variables</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/variable_scope.py#L1190-L1192">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>reuse_variables()
</code></pre>

Reuse variables in this scope.


<h3 id="set_caching_device"><code>set_caching_device</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/variable_scope.py#L1213-L1218">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>set_caching_device(
    caching_device
)
</code></pre>

Set caching_device for this scope.


<h3 id="set_custom_getter"><code>set_custom_getter</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/variable_scope.py#L1224-L1226">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>set_custom_getter(
    custom_getter
)
</code></pre>

Set custom getter for this scope.


<h3 id="set_dtype"><code>set_dtype</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/variable_scope.py#L1198-L1200">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>set_dtype(
    dtype
)
</code></pre>

Set data type for this scope.


<h3 id="set_initializer"><code>set_initializer</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/variable_scope.py#L1194-L1196">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>set_initializer(
    initializer
)
</code></pre>

Set initializer for this scope.


<h3 id="set_partitioner"><code>set_partitioner</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/variable_scope.py#L1220-L1222">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>set_partitioner(
    partitioner
)
</code></pre>

Set partitioner for this scope.


<h3 id="set_regularizer"><code>set_regularizer</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/variable_scope.py#L1209-L1211">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>set_regularizer(
    regularizer
)
</code></pre>

Set regularizer for this scope.


<h3 id="set_use_resource"><code>set_use_resource</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/variable_scope.py#L1202-L1207">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>set_use_resource(
    use_resource
)
</code></pre>

Sets whether to use ResourceVariables for this scope.


<h3 id="trainable_variables"><code>trainable_variables</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/variable_scope.py#L1233-L1235">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>trainable_variables()
</code></pre>

Get this scope's trainable variables.




