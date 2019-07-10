page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.foldl

``` python
tf.foldl(
    fn,
    elems,
    initializer=None,
    parallel_iterations=10,
    back_prop=True,
    swap_memory=False,
    name=None
)
```



Defined in [`tensorflow/python/ops/functional_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/functional_ops.py).

foldl on the list of tensors unpacked from `elems` on dimension 0.

This foldl operator repeatedly applies the callable `fn` to a sequence
of elements from first to last. The elements are made of the tensors
unpacked from `elems` on dimension 0. The callable fn takes two tensors as
arguments. The first argument is the accumulated value computed from the
preceding invocation of fn. If `initializer` is None, `elems` must contain
at least one element, and its first element is used as the initializer.

Suppose that `elems` is unpacked into `values`, a list of tensors. The shape
of the result tensor is fn(initializer, values[0]).shape`.

This method also allows multi-arity `elems` and output of `fn`.  If `elems`
is a (possibly nested) list or tuple of tensors, then each of these tensors
must have a matching first (unpack) dimension.  The signature of `fn` may
match the structure of `elems`.  That is, if `elems` is
`(t1, [t2, t3, [t4, t5]])`, then an appropriate signature for `fn` is:
`fn = lambda (t1, [t2, t3, [t4, t5]]):`.

#### Args:

* <b>`fn`</b>: The callable to be performed.
* <b>`elems`</b>: A tensor or (possibly nested) sequence of tensors, each of which
    will be unpacked along their first dimension.  The nested sequence
    of the resulting slices will be the first argument to `fn`.
* <b>`initializer`</b>: (optional) A tensor or (possibly nested) sequence of tensors,
    as the initial value for the accumulator.
* <b>`parallel_iterations`</b>: (optional) The number of iterations allowed to run
    in parallel.
* <b>`back_prop`</b>: (optional) True enables support for back propagation.
* <b>`swap_memory`</b>: (optional) True enables GPU-CPU memory swapping.
* <b>`name`</b>: (optional) Name prefix for the returned tensors.


#### Returns:

A tensor or (possibly nested) sequence of tensors, resulting from applying
`fn` consecutively to the list of tensors unpacked from `elems`, from first
to last.


#### Raises:

* <b>`TypeError`</b>: if `fn` is not callable.

Example:
>     elems = tf.constant([1, 2, 3, 4, 5, 6])
>     sum = foldl(lambda a, x: a + x, elems)
>     # sum == 21
