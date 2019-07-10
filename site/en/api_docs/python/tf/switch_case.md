page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.switch_case

Create a switch/case operation, i.e. an integer-indexed conditional.

### Aliases:

* `tf.compat.v1.switch_case`
* `tf.compat.v2.switch_case`
* `tf.switch_case`

``` python
tf.switch_case(
    branch_index,
    branch_fns,
    default=None,
    name='switch_case'
)
```



Defined in [`python/ops/control_flow_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/control_flow_ops.py).

<!-- Placeholder for "Used in" -->

See also <a href="../tf/case"><code>tf.case</code></a>.

This op can be substantially more efficient than <a href="../tf/case"><code>tf.case</code></a> when exactly one
branch will be selected. <a href="../tf/switch_case"><code>tf.switch_case</code></a> is more like a C++ switch/case
statement than <a href="../tf/case"><code>tf.case</code></a>, which is more like an if/elif/elif/else chain.

The `branch_fns` parameter is either a dict from `int` to callables, or list
of (`int, callable) pairs, or simply a list of callables (in which case the
index is implicitly the key). The `branch_index` `Tensor` is used to select an
element in `branch_fns` with matching `int` key, falling back to `default`
if none match, or `max(keys)` if no `default` is provided. The keys must form
a contiguous set from `0` to `len(branch_fns) - 1`.

<a href="../tf/switch_case"><code>tf.switch_case</code></a> supports nested structures as implemented in <a href="../tf/nest"><code>tf.nest</code></a>. All
callables must return the same (possibly nested) value structure of lists,
tuples, and/or named tuples.

**Example:**

#### Pseudocode:



```
switch (branch_index) {  // c-style switch
  case 0: return 17;
  case 1: return 31;
  default: return -1;
}
```
or

```python
branches = {0: lambda: 17, 1: lambda: 31}
branches.get(branch_index, lambda: -1)()
```

#### Expressions:



```python
def f1(): return tf.constant(17)
def f2(): return tf.constant(31)
def f3(): return tf.constant(-1)
r = tf.switch_case(branch_index, branch_fns={0: f1, 1: f2}, default=f3)
# Equivalent: tf.switch_case(branch_index, branch_fns={0: f1, 1: f2, 2: f3})
```

#### Args:


* <b>`branch_index`</b>: An int Tensor specifying which of `branch_fns` should be
  executed.
* <b>`branch_fns`</b>: A `dict` mapping `int`s to callables, or a `list` of
  (`int, callable) pairs, or simply a list of callables (in which case the
  index serves as the key). Each callable must return a matching structure
  of tensors.
* <b>`default`</b>: Optional callable that returns a structure of tensors.
* <b>`name`</b>: A name for this operation (optional).


#### Returns:

The tensors returned by the callable identified by `branch_index`, or those
returned by `default` if no key matches and `default` was provided, or those
returned by the max-keyed `branch_fn` if no `default` is provided.



#### Raises:


* <b>`TypeError`</b>: If `branch_fns` is not a list/dictionary.
* <b>`TypeError`</b>: If `branch_fns` is a list but does not contain 2-tuples or
           callables.
* <b>`TypeError`</b>: If `fns[i]` is not callable for any i, or `default` is not
           callable.