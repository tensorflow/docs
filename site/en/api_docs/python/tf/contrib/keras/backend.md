

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# Module: tf.contrib.keras.backend

### Module `tf.contrib.keras.backend`



Defined in [`tensorflow/contrib/keras/api/keras/backend/__init__.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/keras/api/keras/backend/__init__.py).

Keras backend API.

## Functions

[`abs(...)`](../../../tf/contrib/keras/backend/abs): Element-wise absolute value.

[`all(...)`](../../../tf/contrib/keras/backend/all): Bitwise reduction (logical AND).

[`any(...)`](../../../tf/contrib/keras/backend/any): Bitwise reduction (logical OR).

[`arange(...)`](../../../tf/contrib/keras/backend/arange): Creates a 1D tensor containing a sequence of integers.

[`argmax(...)`](../../../tf/contrib/keras/backend/argmax): Returns the index of the maximum value along an axis.

[`argmin(...)`](../../../tf/contrib/keras/backend/argmin): Returns the index of the minimum value along an axis.

[`backend(...)`](../../../tf/contrib/keras/backend/backend): Publicly accessible method for determining the current backend.

[`batch_dot(...)`](../../../tf/contrib/keras/backend/batch_dot): Batchwise dot product.

[`batch_flatten(...)`](../../../tf/contrib/keras/backend/batch_flatten): Turn a nD tensor into a 2D tensor with same 0th dimension.

[`batch_get_value(...)`](../../../tf/contrib/keras/backend/batch_get_value): Returns the value of more than one tensor variable.

[`batch_normalization(...)`](../../../tf/contrib/keras/backend/batch_normalization): Applies batch normalization on x given mean, var, beta and gamma.

[`batch_set_value(...)`](../../../tf/contrib/keras/backend/batch_set_value): Sets the values of many tensor variables at once.

[`bias_add(...)`](../../../tf/contrib/keras/backend/bias_add): Adds a bias vector to a tensor.

[`binary_crossentropy(...)`](../../../tf/contrib/keras/backend/binary_crossentropy): Binary crossentropy between an output tensor and a target tensor.

[`cast(...)`](../../../tf/contrib/keras/backend/cast): Casts a tensor to a different dtype and returns it.

[`cast_to_floatx(...)`](../../../tf/contrib/keras/backend/cast_to_floatx): Cast a Numpy array to the default Keras float type.

[`categorical_crossentropy(...)`](../../../tf/contrib/keras/backend/categorical_crossentropy): Categorical crossentropy between an output tensor and a target tensor.

[`clear_session(...)`](../../../tf/contrib/keras/backend/clear_session): Destroys the current TF graph and creates a new one.

[`clip(...)`](../../../tf/contrib/keras/backend/clip): Element-wise value clipping.

[`concatenate(...)`](../../../tf/contrib/keras/backend/concatenate): Concatenates a list of tensors alongside the specified axis.

[`constant(...)`](../../../tf/contrib/keras/backend/constant)

[`conv1d(...)`](../../../tf/contrib/keras/backend/conv1d): 1D convolution.

[`conv2d(...)`](../../../tf/contrib/keras/backend/conv2d): 2D convolution.

[`conv2d_transpose(...)`](../../../tf/contrib/keras/backend/conv2d_transpose): 2D deconvolution (i.e.

[`conv3d(...)`](../../../tf/contrib/keras/backend/conv3d): 3D convolution.

[`cos(...)`](../../../tf/contrib/keras/backend/cos): Computes cos of x element-wise.

[`count_params(...)`](../../../tf/contrib/keras/backend/count_params): Returns the number of scalars in a Keras variable.

[`ctc_batch_cost(...)`](../../../tf/contrib/keras/backend/ctc_batch_cost): Runs CTC loss algorithm on each batch element.

[`ctc_decode(...)`](../../../tf/contrib/keras/backend/ctc_decode): Decodes the output of a softmax.

[`ctc_label_dense_to_sparse(...)`](../../../tf/contrib/keras/backend/ctc_label_dense_to_sparse): Converts CTC labels from dense to sparse.

[`dot(...)`](../../../tf/contrib/keras/backend/dot): Multiplies 2 tensors (and/or variables) and returns a *tensor*.

[`dropout(...)`](../../../tf/contrib/keras/backend/dropout): Sets entries in `x` to zero at random, while scaling the entire tensor.

[`dtype(...)`](../../../tf/contrib/keras/backend/dtype): Returns the dtype of a Keras tensor or variable, as a string.

[`elu(...)`](../../../tf/contrib/keras/backend/elu): Exponential linear unit.

[`epsilon(...)`](../../../tf/contrib/keras/backend/epsilon): Returns the value of the fuzz factor used in numeric expressions.

[`equal(...)`](../../../tf/contrib/keras/backend/equal): Element-wise equality between two tensors.

[`eval(...)`](../../../tf/contrib/keras/backend/eval): Evaluates the value of a variable.

[`exp(...)`](../../../tf/contrib/keras/backend/exp): Element-wise exponential.

[`expand_dims(...)`](../../../tf/contrib/keras/backend/expand_dims): Adds a 1-sized dimension at index "dim".

[`eye(...)`](../../../tf/contrib/keras/backend/eye): Instantiate an identity matrix and returns it.

[`flatten(...)`](../../../tf/contrib/keras/backend/flatten): Flatten a tensor.

[`floatx(...)`](../../../tf/contrib/keras/backend/floatx): Returns the default float type, as a string.

[`foldl(...)`](../../../tf/contrib/keras/backend/foldl): Reduce elems using fn to combine them from left to right.

[`foldr(...)`](../../../tf/contrib/keras/backend/foldr): Reduce elems using fn to combine them from right to left.

[`function(...)`](../../../tf/contrib/keras/backend/function): Instantiates a Keras function.

[`gather(...)`](../../../tf/contrib/keras/backend/gather): Retrieves the elements of indices `indices` in the tensor `reference`.

[`get_session(...)`](../../../tf/contrib/keras/backend/get_session): Returns the TF session to be used by the backend.

[`get_uid(...)`](../../../tf/contrib/keras/backend/get_uid)

[`get_value(...)`](../../../tf/contrib/keras/backend/get_value): Returns the value of a variable.

[`gradients(...)`](../../../tf/contrib/keras/backend/gradients): Returns the gradients of `variables` w.r.t. `loss`.

[`greater(...)`](../../../tf/contrib/keras/backend/greater): Element-wise truth value of (x > y).

[`greater_equal(...)`](../../../tf/contrib/keras/backend/greater_equal): Element-wise truth value of (x >= y).

[`hard_sigmoid(...)`](../../../tf/contrib/keras/backend/hard_sigmoid): Segment-wise linear approximation of sigmoid.

[`image_data_format(...)`](../../../tf/contrib/keras/backend/image_data_format): Returns the default image data format convention.

[`in_test_phase(...)`](../../../tf/contrib/keras/backend/in_test_phase): Selects `x` in test phase, and `alt` otherwise.

[`in_top_k(...)`](../../../tf/contrib/keras/backend/in_top_k): Returns whether the `targets` are in the top `k` `predictions`.

[`in_train_phase(...)`](../../../tf/contrib/keras/backend/in_train_phase): Selects `x` in train phase, and `alt` otherwise.

[`int_shape(...)`](../../../tf/contrib/keras/backend/int_shape): Returns the shape tensor or variable as a tuple of int or None entries.

[`is_sparse(...)`](../../../tf/contrib/keras/backend/is_sparse): Returns whether a tensor is a sparse tensor.

[`l2_normalize(...)`](../../../tf/contrib/keras/backend/l2_normalize): Normalizes a tensor wrt the L2 norm alongside the specified axis.

[`learning_phase(...)`](../../../tf/contrib/keras/backend/learning_phase): Returns the learning phase flag.

[`less(...)`](../../../tf/contrib/keras/backend/less): Element-wise truth value of (x < y).

[`less_equal(...)`](../../../tf/contrib/keras/backend/less_equal): Element-wise truth value of (x <= y).

[`log(...)`](../../../tf/contrib/keras/backend/log): Element-wise log.

[`manual_variable_initialization(...)`](../../../tf/contrib/keras/backend/manual_variable_initialization): Sets the manual variable initialization flag.

[`map_fn(...)`](../../../tf/contrib/keras/backend/map_fn): Map the function fn over the elements elems and return the outputs.

[`max(...)`](../../../tf/contrib/keras/backend/max): Maximum value in a tensor.

[`maximum(...)`](../../../tf/contrib/keras/backend/maximum): Element-wise maximum of two tensors.

[`mean(...)`](../../../tf/contrib/keras/backend/mean): Mean of a tensor, alongside the specified axis.

[`min(...)`](../../../tf/contrib/keras/backend/min): Minimum value in a tensor.

[`minimum(...)`](../../../tf/contrib/keras/backend/minimum): Element-wise minimum of two tensors.

[`moving_average_update(...)`](../../../tf/contrib/keras/backend/moving_average_update)

[`name_scope(...)`](../../../tf/name_scope): Returns a context manager for use when defining a Python op.

[`ndim(...)`](../../../tf/contrib/keras/backend/ndim): Returns the number of axes in a tensor, as an integer.

[`normalize_batch_in_training(...)`](../../../tf/contrib/keras/backend/normalize_batch_in_training): Computes mean and std for batch then apply batch_normalization on batch.

[`not_equal(...)`](../../../tf/contrib/keras/backend/not_equal): Element-wise inequality between two tensors.

[`one_hot(...)`](../../../tf/contrib/keras/backend/one_hot): Computes the one-hot representation of an integer tensor.

[`ones(...)`](../../../tf/contrib/keras/backend/ones): Instantiates an all-ones tensor variable and returns it.

[`ones_like(...)`](../../../tf/contrib/keras/backend/ones_like): Instantiates an all-ones variable of the same shape as another tensor.

[`permute_dimensions(...)`](../../../tf/contrib/keras/backend/permute_dimensions): Permutes axes in a tensor.

[`placeholder(...)`](../../../tf/contrib/keras/backend/placeholder): Instantiates a placeholder tensor and returns it.

[`pool2d(...)`](../../../tf/contrib/keras/backend/pool2d): 2D Pooling.

[`pool3d(...)`](../../../tf/contrib/keras/backend/pool3d): 3D Pooling.

[`pow(...)`](../../../tf/contrib/keras/backend/pow): Element-wise exponentiation.

[`print_tensor(...)`](../../../tf/contrib/keras/backend/print_tensor): Prints `message` and the tensor value when evaluated.

[`prod(...)`](../../../tf/contrib/keras/backend/prod): Multiplies the values in a tensor, alongside the specified axis.

[`random_binomial(...)`](../../../tf/contrib/keras/backend/random_binomial): Returns a tensor with random binomial distribution of values.

[`random_normal(...)`](../../../tf/contrib/keras/backend/random_normal): Returns a tensor with normal distribution of values.

[`random_normal_variable(...)`](../../../tf/contrib/keras/backend/random_normal_variable): Instantiates a variable with values drawn from a normal distribution.

[`random_uniform(...)`](../../../tf/contrib/keras/backend/random_uniform): Returns a tensor with uniform distribution of values.

[`random_uniform_variable(...)`](../../../tf/contrib/keras/backend/random_uniform_variable): Instantiates a variable with values drawn from a uniform distribution.

[`relu(...)`](../../../tf/contrib/keras/backend/relu): Rectified linear unit.

[`repeat(...)`](../../../tf/contrib/keras/backend/repeat): Repeats a 2D tensor.

[`repeat_elements(...)`](../../../tf/contrib/keras/backend/repeat_elements): Repeats the elements of a tensor along an axis, like `np.repeat`.

[`reset_uids(...)`](../../../tf/contrib/keras/backend/reset_uids)

[`reshape(...)`](../../../tf/contrib/keras/backend/reshape): Reshapes a tensor to the specified shape.

[`resize_images(...)`](../../../tf/contrib/keras/backend/resize_images): Resizes the images contained in a 4D tensor.

[`resize_volumes(...)`](../../../tf/contrib/keras/backend/resize_volumes): Resizes the volume contained in a 5D tensor.

[`reverse(...)`](../../../tf/contrib/keras/backend/reverse): Reverse a tensor along the specified axes.

[`rnn(...)`](../../../tf/contrib/keras/backend/rnn): Iterates over the time dimension of a tensor.

[`round(...)`](../../../tf/contrib/keras/backend/round): Element-wise rounding to the closest integer.

[`separable_conv2d(...)`](../../../tf/contrib/keras/backend/separable_conv2d): 2D convolution with separable filters.

[`set_epsilon(...)`](../../../tf/contrib/keras/backend/set_epsilon): Sets the value of the fuzz factor used in numeric expressions.

[`set_floatx(...)`](../../../tf/contrib/keras/backend/set_floatx): Sets the default float type.

[`set_image_data_format(...)`](../../../tf/contrib/keras/backend/set_image_data_format): Sets the value of the image data format convention.

[`set_learning_phase(...)`](../../../tf/contrib/keras/backend/set_learning_phase): Sets the learning phase to a fixed value.

[`set_session(...)`](../../../tf/contrib/keras/backend/set_session): Sets the global TensorFlow session.

[`set_value(...)`](../../../tf/contrib/keras/backend/set_value): Sets the value of a variable, from a Numpy array.

[`shape(...)`](../../../tf/contrib/keras/backend/shape): Returns the symbolic shape of a tensor or variable.

[`sigmoid(...)`](../../../tf/contrib/keras/backend/sigmoid): Element-wise sigmoid.

[`sign(...)`](../../../tf/contrib/keras/backend/sign): Element-wise sign.

[`sin(...)`](../../../tf/contrib/keras/backend/sin): Computes sin of x element-wise.

[`softmax(...)`](../../../tf/contrib/keras/backend/softmax): Softmax of a tensor.

[`softplus(...)`](../../../tf/contrib/keras/backend/softplus): Softplus of a tensor.

[`softsign(...)`](../../../tf/contrib/keras/backend/softsign): Softsign of a tensor.

[`sparse_categorical_crossentropy(...)`](../../../tf/contrib/keras/backend/sparse_categorical_crossentropy): Categorical crossentropy with integer targets.

[`spatial_2d_padding(...)`](../../../tf/contrib/keras/backend/spatial_2d_padding): Pads the 2nd and 3rd dimensions of a 4D tensor.

[`spatial_3d_padding(...)`](../../../tf/contrib/keras/backend/spatial_3d_padding): Pads 5D tensor with zeros along the depth, height, width dimensions.

[`sqrt(...)`](../../../tf/contrib/keras/backend/sqrt): Element-wise square root.

[`square(...)`](../../../tf/contrib/keras/backend/square): Element-wise square.

[`squeeze(...)`](../../../tf/contrib/keras/backend/squeeze): Removes a 1-dimension from the tensor at index "axis".

[`stack(...)`](../../../tf/contrib/keras/backend/stack): Stacks a list of rank `R` tensors into a rank `R+1` tensor.

[`std(...)`](../../../tf/contrib/keras/backend/std): Standard deviation of a tensor, alongside the specified axis.

[`stop_gradient(...)`](../../../tf/contrib/keras/backend/stop_gradient): Returns `variables` but with zero gradient w.r.t. every other variable.

[`sum(...)`](../../../tf/contrib/keras/backend/sum): Sum of the values in a tensor, alongside the specified axis.

[`switch(...)`](../../../tf/contrib/keras/backend/switch): Switches between two operations depending on a scalar value.

[`tanh(...)`](../../../tf/contrib/keras/backend/tanh): Element-wise tanh.

[`temporal_padding(...)`](../../../tf/contrib/keras/backend/temporal_padding): Pads the middle dimension of a 3D tensor.

[`to_dense(...)`](../../../tf/contrib/keras/backend/to_dense): Converts a sparse tensor into a dense tensor and returns it.

[`transpose(...)`](../../../tf/contrib/keras/backend/transpose): Transposes a tensor and returns it.

[`truncated_normal(...)`](../../../tf/contrib/keras/backend/truncated_normal): Returns a tensor with truncated random normal distribution of values.

[`update(...)`](../../../tf/contrib/keras/backend/update)

[`update_add(...)`](../../../tf/contrib/keras/backend/update_add)

[`update_sub(...)`](../../../tf/contrib/keras/backend/update_sub)

[`var(...)`](../../../tf/contrib/keras/backend/var): Variance of a tensor, alongside the specified axis.

[`variable(...)`](../../../tf/contrib/keras/backend/variable): Instantiates a variable and returns it.

[`zeros(...)`](../../../tf/contrib/keras/backend/zeros): Instantiates an all-zeros variable and returns it.

[`zeros_like(...)`](../../../tf/contrib/keras/backend/zeros_like): Instantiates an all-zeros variable of the same shape as another tensor.

