page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.sparse.add


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/sparse_ops.py#L434-L515">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Adds two tensors, at least one of each is a `SparseTensor`.

### Aliases:

* `tf.compat.v2.sparse.add`


``` python
tf.sparse.add(
    a,
    b,
    threshold=0
)
```



<!-- Placeholder for "Used in" -->

If one `SparseTensor` and one `Tensor` are passed in, returns a `Tensor`.  If
both arguments are `SparseTensor`s, this returns a `SparseTensor`.  The order
of arguments does not matter.  Use vanilla <a href="../../tf/math/add"><code>tf.add()</code></a> for adding two dense
`Tensor`s.

The shapes of the two operands must match: broadcasting is not supported.

The indices of any input `SparseTensor` are assumed ordered in standard
lexicographic order.  If this is not the case, before this step run
`SparseReorder` to restore index ordering.

If both arguments are sparse, we perform "clipping" as follows.  By default,
if two values sum to zero at some index, the output `SparseTensor` would still
include that particular location in its index, storing a zero in the
corresponding value slot.  To override this, callers can specify `threshold`,
indicating that if the sum has a magnitude strictly smaller than `threshold`,
its corresponding value and index would then not be included.  In particular,
`threshold == 0.0` (default) means everything is kept and actual thresholding
happens only for a positive value.

For example, suppose the logical sum of two sparse operands is (densified):

    [       2]
    [.1     0]
    [ 6   -.2]

Then,

* `threshold == 0` (the default): all 5 index/value pairs will be
    returned.
* `threshold == 0.11`: only .1 and 0 will vanish, and the remaining three
    index/value pairs will be returned.
* `threshold == 0.21`: .1, 0, and -.2 will vanish.

#### Args:


* <b>`a`</b>: The first operand; `SparseTensor` or `Tensor`.
* <b>`b`</b>: The second operand; `SparseTensor` or `Tensor`. At least one operand
  must be sparse.
* <b>`threshold`</b>: A 0-D `Tensor`. The magnitude threshold that determines if an
  output value/index pair takes space. Its dtype should match that of the
  values if they are real; if the latter are complex64/complex128, then the
  dtype should be float32/float64, correspondingly.


#### Returns:

A `SparseTensor` or a `Tensor`, representing the sum.



#### Raises:


* <b>`TypeError`</b>: If both `a` and `b` are `Tensor`s.  Use <a href="../../tf/math/add"><code>tf.add()</code></a> instead.
