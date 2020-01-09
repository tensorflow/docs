page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.compat.v1.sparse


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>



Sparse Tensor Representation.

<!-- Placeholder for "Used in" -->

See also <a href="../../../tf/sparse/SparseTensor"><code>tf.SparseTensor</code></a>.

## Classes

[`class SparseConditionalAccumulator`](../../../tf/compat/v1/SparseConditionalAccumulator): A conditional accumulator for aggregating sparse gradients.

[`class SparseTensor`](../../../tf/sparse/SparseTensor): Represents a sparse tensor.

## Functions

[`add(...)`](../../../tf/compat/v1/sparse_add): Adds two tensors, at least one of each is a `SparseTensor`. (deprecated arguments)

[`concat(...)`](../../../tf/compat/v1/sparse_concat): Concatenates a list of `SparseTensor` along the specified dimension. (deprecated arguments)

[`cross(...)`](../../../tf/sparse/cross): Generates sparse cross from a list of sparse and dense tensors.

[`cross_hashed(...)`](../../../tf/sparse/cross_hashed): Generates hashed sparse cross from a list of sparse and dense tensors.

[`expand_dims(...)`](../../../tf/sparse/expand_dims): Inserts a dimension of 1 into a tensor's shape.

[`eye(...)`](../../../tf/sparse/eye): Creates a two-dimensional sparse tensor with ones along the diagonal.

[`fill_empty_rows(...)`](../../../tf/sparse/fill_empty_rows): Fills empty rows in the input 2-D `SparseTensor` with a default value.

[`from_dense(...)`](../../../tf/sparse/from_dense): Converts a dense tensor into a sparse tensor.

[`mask(...)`](../../../tf/sparse/mask): Masks elements of `IndexedSlices`.

[`matmul(...)`](../../../tf/sparse/sparse_dense_matmul): Multiply SparseTensor (of rank 2) "A" by dense matrix "B".

[`maximum(...)`](../../../tf/sparse/maximum): Returns the element-wise max of two SparseTensors.

[`merge(...)`](../../../tf/compat/v1/sparse_merge): Combines a batch of feature ids and values into a single `SparseTensor`. (deprecated)

[`minimum(...)`](../../../tf/sparse/minimum): Returns the element-wise min of two SparseTensors.

[`placeholder(...)`](../../../tf/compat/v1/sparse_placeholder): Inserts a placeholder for a sparse tensor that will be always fed.

[`reduce_max(...)`](../../../tf/compat/v1/sparse_reduce_max): Computes the max of elements across dimensions of a SparseTensor. (deprecated arguments) (deprecated arguments)

[`reduce_max_sparse(...)`](../../../tf/compat/v1/sparse_reduce_max_sparse): Computes the max of elements across dimensions of a SparseTensor. (deprecated arguments)

[`reduce_sum(...)`](../../../tf/compat/v1/sparse_reduce_sum): Computes the sum of elements across dimensions of a SparseTensor. (deprecated arguments) (deprecated arguments)

[`reduce_sum_sparse(...)`](../../../tf/compat/v1/sparse_reduce_sum_sparse): Computes the sum of elements across dimensions of a SparseTensor. (deprecated arguments)

[`reorder(...)`](../../../tf/sparse/reorder): Reorders a `SparseTensor` into the canonical, row-major ordering.

[`reset_shape(...)`](../../../tf/sparse/reset_shape): Resets the shape of a `SparseTensor` with indices and values unchanged.

[`reshape(...)`](../../../tf/sparse/reshape): Reshapes a `SparseTensor` to represent values in a new dense shape.

[`retain(...)`](../../../tf/sparse/retain): Retains specified non-empty values within a `SparseTensor`.

[`segment_mean(...)`](../../../tf/compat/v1/sparse_segment_mean): Computes the mean along sparse segments of a tensor.

[`segment_sqrt_n(...)`](../../../tf/compat/v1/sparse_segment_sqrt_n): Computes the sum along sparse segments of a tensor divided by the sqrt(N).

[`segment_sum(...)`](../../../tf/compat/v1/sparse_segment_sum): Computes the sum along sparse segments of a tensor.

[`slice(...)`](../../../tf/sparse/slice): Slice a `SparseTensor` based on the `start` and `size.

[`softmax(...)`](../../../tf/sparse/softmax): Applies softmax to a batched N-D `SparseTensor`.

[`sparse_dense_matmul(...)`](../../../tf/sparse/sparse_dense_matmul): Multiply SparseTensor (of rank 2) "A" by dense matrix "B".

[`split(...)`](../../../tf/compat/v1/sparse_split): Split a `SparseTensor` into `num_split` tensors along `axis`. (deprecated arguments)

[`to_dense(...)`](../../../tf/sparse/to_dense): Converts a `SparseTensor` into a dense tensor.

[`to_indicator(...)`](../../../tf/sparse/to_indicator): Converts a `SparseTensor` of ids into a dense bool indicator tensor.

[`transpose(...)`](../../../tf/sparse/transpose): Transposes a `SparseTensor`
