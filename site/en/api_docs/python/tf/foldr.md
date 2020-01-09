page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.foldr


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/functional_ops.py#L162-L277">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



foldr on the list of tensors unpacked from `elems` on dimension 0.

### Aliases:

* `tf.compat.v1.foldr`
* `tf.compat.v2.foldr`


``` python
tf.foldr(
    fn,
    elems,
    initializer=None,
    parallel_iterations=10,
    back_prop=True,
    swap_memory=False,
    name=None
)
```



<!-- Placeholder for "Used in" -->

This foldr operator repeatedly applies the callable `fn` to a sequence
of elements from last to first. The elements are made of the tensors
unpacked from `elems`. The callable fn takes two tensors as arguments.
The first argument is the accumulated value computed from the preceding
invocation of fn, and the second is the value at the current position of
`elems`. If `initializer` is None, `elems` must contain at least one element,
and its first element is used as the initializer.

Suppose that `elems` is unpacked into `values`, a list of tensors. The shape
of the result tensor is `fn(initializer, values[0]).shape`.

This method also allows multi-arity `elems` and output of `fn`.  If `elems`
is a (possibly nested) list or tuple of tensors, then each of these tensors
must have a matching first (unpack) dimension.  The signature of `fn` may
match the structure of `elems`.  That is, if `elems` is
`(t1, [t2, t3, [t4, t5]])`, then an appropriate signature for `fn` is:
`fn = lambda (t1, [t2, t3, [t4, t5]]):`.

#### Args:


* <b>`fn`</b>: The callable to be performed.
* <b>`elems`</b>: A tensor or (possibly nested) sequence of tensors, each of which will
  be unpacked along their first dimension.  The nested sequence of the
  resulting slices will be the first argument to `fn`.
* <b>`initializer`</b>: (optional) A tensor or (possibly nested) sequence of tensors,
  as the initial value for the accumulator.
* <b>`parallel_iterations`</b>: (optional) The number of iterations allowed to run in
  parallel.
* <b>`back_prop`</b>: (optional) True enables support for back propagation.
* <b>`swap_memory`</b>: (optional) True enables GPU-CPU memory swapping.
* <b>`name`</b>: (optional) Name prefix for the returned tensors.


#### Returns:

A tensor or (possibly nested) sequence of tensors, resulting from applying
`fn` consecutively to the list of tensors unpacked from `elems`, from last
to first.



#### Raises:


* <b>`TypeError`</b>: if `fn` is not callable.


#### Example:

```python
elems = [1, 2, 3, 4, 5, 6]
sum = foldr(lambda a, x: a + x, elems)
# sum == 21
```
