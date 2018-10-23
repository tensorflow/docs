

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.losses.metric_learning.npairs_loss_multilabel

``` python
tf.contrib.losses.metric_learning.npairs_loss_multilabel(
    sparse_labels,
    embeddings_anchor,
    embeddings_positive,
    reg_lambda=0.002,
    print_losses=False
)
```



Defined in [`tensorflow/contrib/losses/python/metric_learning/metric_loss_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/losses/python/metric_learning/metric_loss_ops.py).

Computes the npairs loss with multilabel data.

Npairs loss expects paired data where a pair is composed of samples from the
same labels and each pairs in the minibatch have different labels. The loss
has two components. The first component is the L2 regularizer on the
embedding vectors. The second component is the sum of cross entropy loss
which takes each row of the pair-wise similarity matrix as logits and
the remapped one-hot labels as labels. Here, the similarity is defined by the
dot product between two embedding vectors. S_{i,j} = f(x_i)^T f(x_j)

To deal with multilabel inputs, we use the count of label intersection
i.e. L_{i,j} = | set_of_labels_for(i) \cap set_of_labels_for(j) |
Then we normalize each rows of the count based label matrix so that each row
sums to one.

#### Args:

* <b>`sparse_labels`</b>: List of 1-D Boolean `SparseTensor` of dense_shape
                 [batch_size/2, num_classes] labels for the anchor-pos pairs.
* <b>`embeddings_anchor`</b>: 2-D `Tensor` of shape [batch_size/2, embedding_dim] for
    the embedding vectors for the anchor images. Embeddings should not be
    l2 normalized.
* <b>`embeddings_positive`</b>: 2-D `Tensor` of shape [batch_size/2, embedding_dim] for
    the embedding vectors for the positive images. Embeddings should not be
    l2 normalized.
* <b>`reg_lambda`</b>: Float. L2 regularization term on the embedding vectors.
* <b>`print_losses`</b>: Boolean. Option to print the xent and l2loss.


#### Returns:

* <b>`npairs_loss`</b>: tf.float32 scalar.

#### Raises:

* <b>`TypeError`</b>: When the specified sparse_labels is not a `SparseTensor`.