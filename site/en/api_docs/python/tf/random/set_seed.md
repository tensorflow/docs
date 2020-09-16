description: Sets the global random seed.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.random.set_seed" />
<meta itemprop="path" content="Stable" />
</div>

# tf.random.set_seed

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/framework/random_seed.py#L198-L346">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Sets the global random seed.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.random.set_seed(
    seed
)
</code></pre>



<!-- Placeholder for "Used in" -->

Operations that rely on a random seed actually derive it from two seeds:
the global and operation-level seeds. This sets the global seed.

Its interactions with operation-level seeds is as follows:

  1. If neither the global seed nor the operation seed is set: A randomly
    picked seed is used for this op.
  2. If the graph-level seed is set, but the operation seed is not:
    The system deterministically picks an operation seed in conjunction with
    the graph-level seed so that it gets a unique random sequence. Within the
    same version of tensorflow and user code, this sequence is deterministic.
    However across different versions, this sequence might change. If the
    code depends on particular seeds to work, specify both graph-level
    and operation-level seeds explicitly.
  3. If the operation seed is set, but the global seed is not set:
    A default global seed and the specified operation seed are used to
    determine the random sequence.
  4. If both the global and the operation seed are set:
    Both seeds are used in conjunction to determine the random sequence.

To illustrate the user-visible effects, consider these examples:

If neither the global seed nor the operation seed is set, we get different
results for every call to the random op and every re-run of the program:

```python
print(tf.random.uniform([1]))  # generates 'A1'
print(tf.random.uniform([1]))  # generates 'A2'
```

(now close the program and run it again)

```python
print(tf.random.uniform([1]))  # generates 'A3'
print(tf.random.uniform([1]))  # generates 'A4'
```

If the global seed is set but the operation seed is not set, we get different
results for every call to the random op, but the same sequence for every
re-run of the program:

```python
tf.random.set_seed(1234)
print(tf.random.uniform([1]))  # generates 'A1'
print(tf.random.uniform([1]))  # generates 'A2'
```

(now close the program and run it again)

```python
tf.random.set_seed(1234)
print(tf.random.uniform([1]))  # generates 'A1'
print(tf.random.uniform([1]))  # generates 'A2'
```

The reason we get 'A2' instead 'A1' on the second call of <a href="../../tf/random/uniform.md"><code>tf.random.uniform</code></a>
above is because the second call uses a different operation seed.

Note that <a href="../../tf/function.md"><code>tf.function</code></a> acts like a re-run of a program in this case. When
the global seed is set but operation seeds are not set, the sequence of random
numbers are the same for each <a href="../../tf/function.md"><code>tf.function</code></a>. For example:

```python
tf.random.set_seed(1234)

@tf.function
def f():
  a = tf.random.uniform([1])
  b = tf.random.uniform([1])
  return a, b

@tf.function
def g():
  a = tf.random.uniform([1])
  b = tf.random.uniform([1])
  return a, b

print(f())  # prints '(A1, A2)'
print(g())  # prints '(A1, A2)'
```

If the operation seed is set, we get different results for every call to the
random op, but the same sequence for every re-run of the program:

```python
print(tf.random.uniform([1], seed=1))  # generates 'A1'
print(tf.random.uniform([1], seed=1))  # generates 'A2'
```

(now close the program and run it again)

```python
print(tf.random.uniform([1], seed=1))  # generates 'A1'
print(tf.random.uniform([1], seed=1))  # generates 'A2'
```

The reason we get 'A2' instead 'A1' on the second call of <a href="../../tf/random/uniform.md"><code>tf.random.uniform</code></a>
above is because the same <a href="../../tf/random/uniform.md"><code>tf.random.uniform</code></a> kernel (i.e. internal
representation) is used by TensorFlow for all calls of it with the same
arguments, and the kernel maintains an internal counter which is incremented
every time it is executed, generating different results.

Calling <a href="../../tf/random/set_seed.md"><code>tf.random.set_seed</code></a> will reset any such counters:

```python
tf.random.set_seed(1234)
print(tf.random.uniform([1], seed=1))  # generates 'A1'
print(tf.random.uniform([1], seed=1))  # generates 'A2'
tf.random.set_seed(1234)
print(tf.random.uniform([1], seed=1))  # generates 'A1'
print(tf.random.uniform([1], seed=1))  # generates 'A2'
```

When multiple identical random ops are wrapped in a <a href="../../tf/function.md"><code>tf.function</code></a>, their
behaviors change because the ops no long share the same counter. For example:

```python
@tf.function
def foo():
  a = tf.random.uniform([1], seed=1)
  b = tf.random.uniform([1], seed=1)
  return a, b
print(foo())  # prints '(A1, A1)'
print(foo())  # prints '(A2, A2)'

@tf.function
def bar():
  a = tf.random.uniform([1])
  b = tf.random.uniform([1])
  return a, b
print(bar())  # prints '(A1, A2)'
print(bar())  # prints '(A3, A4)'
```

The second call of `foo` returns '(A2, A2)' instead of '(A1, A1)' because
<a href="../../tf/random/uniform.md"><code>tf.random.uniform</code></a> maintains an internal counter. If you want `foo` to return
'(A1, A1)' every time, use the stateless random ops such as
<a href="../../tf/random/stateless_uniform.md"><code>tf.random.stateless_uniform</code></a>. Also see <a href="../../tf/random/Generator.md"><code>tf.random.experimental.Generator</code></a> for
a new set of stateful random ops that use external variables to manage their
states.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`seed`
</td>
<td>
integer.
</td>
</tr>
</table>

