page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.image.bipartite_match

Find bipartite matching based on a given distance matrix.

``` python
tf.contrib.image.bipartite_match(
    distance_mat,
    num_valid_rows,
    top_k=-1,
    name='bipartite_match'
)
```



Defined in [`contrib/image/python/ops/image_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/image/python/ops/image_ops.py).

<!-- Placeholder for "Used in" -->

A greedy bi-partite matching algorithm is used to obtain the matching with
the (greedy) minimum distance.

#### Args:


* <b>`distance_mat`</b>: A 2-D float tensor of shape `[num_rows, num_columns]`. It is a
  pair-wise distance matrix between the entities represented by each row and
  each column. It is an asymmetric matrix. The smaller the distance is, the
  more similar the pairs are. The bipartite matching is to minimize the
  distances.
* <b>`num_valid_rows`</b>: A scalar or a 1-D tensor with one element describing the
  number of valid rows of distance_mat to consider for the bipartite
  matching. If set to be negative, then all rows from `distance_mat` are
  used.
* <b>`top_k`</b>: A scalar that specifies the number of top-k matches to retrieve.
  If set to be negative, then is set according to the maximum number of
  matches from `distance_mat`.
* <b>`name`</b>: The name of the op.


#### Returns:


* <b>`row_to_col_match_indices`</b>: A vector of length num_rows, which is the number
  of rows of the input `distance_matrix`. If `row_to_col_match_indices[i]`
  is not -1, row i is matched to column `row_to_col_match_indices[i]`.
* <b>`col_to_row_match_indices`</b>: A vector of length num_columns, which is the
  number of columns of the input distance matrix.
  If `col_to_row_match_indices[j]` is not -1, column j is matched to row
  `col_to_row_match_indices[j]`.