page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.keras.backend





Keras backend API.

## Classes

[`class name_scope`](../../tf/name_scope): A context manager for use when defining a Python op.

## Functions

[`abs(...)`](../../tf/keras/backend/abs): Element-wise absolute value.

[`all(...)`](../../tf/keras/backend/all): Bitwise reduction (logical AND).

[`any(...)`](../../tf/keras/backend/any): Bitwise reduction (logical OR).

[`arange(...)`](../../tf/keras/backend/arange): Creates a 1D tensor containing a sequence of integers.

[`argmax(...)`](../../tf/keras/backend/argmax): Returns the index of the maximum value along an axis.

[`argmin(...)`](../../tf/keras/backend/argmin): Returns the index of the minimum value along an axis.

[`backend(...)`](../../tf/keras/backend/backend): Publicly accessible method for determining the current backend.

[`batch_dot(...)`](../../tf/keras/backend/batch_dot): Batchwise dot product.

[`batch_flatten(...)`](../../tf/keras/backend/batch_flatten): Turn a nD tensor into a 2D tensor with same 0th dimension.

[`batch_get_value(...)`](../../tf/keras/backend/batch_get_value): Returns the value of more than one tensor variable.

[`batch_normalization(...)`](../../tf/keras/backend/batch_normalization): Applies batch normalization on x given mean, var, beta and gamma.

[`batch_set_value(...)`](../../tf/keras/backend/batch_set_value): Sets the values of many tensor variables at once.

[`bias_add(...)`](../../tf/keras/backend/bias_add): Adds a bias vector to a tensor.

[`binary_crossentropy(...)`](../../tf/keras/backend/binary_crossentropy): Binary crossentropy between an output tensor and a target tensor.

[`cast(...)`](../../tf/keras/backend/cast): Casts a tensor to a different dtype and returns it.

[`cast_to_floatx(...)`](../../tf/keras/backend/cast_to_floatx): Cast a Numpy array to the default Keras float type.

[`categorical_crossentropy(...)`](../../tf/keras/backend/categorical_crossentropy): Categorical crossentropy between an output tensor and a target tensor.

[`clear_session(...)`](../../tf/keras/backend/clear_session): Destroys the current TF graph and creates a new one.

[`clip(...)`](../../tf/keras/backend/clip): Element-wise value clipping.

[`concatenate(...)`](../../tf/keras/backend/concatenate): Concatenates a list of tensors alongside the specified axis.

[`constant(...)`](../../tf/keras/backend/constant): Creates a constant tensor.

[`conv1d(...)`](../../tf/keras/backend/conv1d): 1D convolution.

[`conv2d(...)`](../../tf/keras/backend/conv2d): 2D convolution.

[`conv2d_transpose(...)`](../../tf/keras/backend/conv2d_transpose): 2D deconvolution (i.e.

[`conv3d(...)`](../../tf/keras/backend/conv3d): 3D convolution.

[`cos(...)`](../../tf/keras/backend/cos): Computes cos of x element-wise.

[`count_params(...)`](../../tf/keras/backend/count_params): Returns the static number of elements in a variable or tensor.

[`ctc_batch_cost(...)`](../../tf/keras/backend/ctc_batch_cost): Runs CTC loss algorithm on each batch element.

[`ctc_decode(...)`](../../tf/keras/backend/ctc_decode): Decodes the output of a softmax.

[`ctc_label_dense_to_sparse(...)`](../../tf/keras/backend/ctc_label_dense_to_sparse): Converts CTC labels from dense to sparse.

[`dot(...)`](../../tf/keras/backend/dot): Multiplies 2 tensors (and/or variables) and returns a *tensor*.

[`dropout(...)`](../../tf/keras/backend/dropout): Sets entries in `x` to zero at random, while scaling the entire tensor.

[`dtype(...)`](../../tf/keras/backend/dtype): Returns the dtype of a Keras tensor or variable, as a string.

[`elu(...)`](../../tf/keras/backend/elu): Exponential linear unit.

[`epsilon(...)`](../../tf/keras/backend/epsilon): Returns the value of the fuzz factor used in numeric expressions.

[`equal(...)`](../../tf/keras/backend/equal): Element-wise equality between two tensors.

[`eval(...)`](../../tf/keras/backend/eval): Evaluates the value of a variable.

[`exp(...)`](../../tf/keras/backend/exp): Element-wise exponential.

[`expand_dims(...)`](../../tf/keras/backend/expand_dims): Adds a 1-sized dimension at index "axis".

[`eye(...)`](../../tf/keras/backend/eye): Instantiate an identity matrix and returns it.

[`flatten(...)`](../../tf/keras/backend/flatten): Flatten a tensor.

[`floatx(...)`](../../tf/keras/backend/floatx): Returns the default float type, as a string.

[`foldl(...)`](../../tf/keras/backend/foldl): Reduce elems using fn to combine them from left to right.

[`foldr(...)`](../../tf/keras/backend/foldr): Reduce elems using fn to combine them from right to left.

[`function(...)`](../../tf/keras/backend/function): Instantiates a Keras function.

[`gather(...)`](../../tf/keras/backend/gather): Retrieves the elements of indices `indices` in the tensor `reference`.

[`get_session(...)`](../../tf/keras/backend/get_session): Returns the TF session to be used by the backend.

[`get_uid(...)`](../../tf/keras/backend/get_uid): Associates a string prefix with an integer counter in a TensorFlow graph.

[`get_value(...)`](../../tf/keras/backend/get_value): Returns the value of a variable.

[`gradients(...)`](../../tf/keras/backend/gradients): Returns the gradients of `loss` w.r.t. `variables`.

[`greater(...)`](../../tf/keras/backend/greater): Element-wise truth value of (x > y).

[`greater_equal(...)`](../../tf/keras/backend/greater_equal): Element-wise truth value of (x >= y).

[`hard_sigmoid(...)`](../../tf/keras/backend/hard_sigmoid): Segment-wise linear approximation of sigmoid.

[`image_data_format(...)`](../../tf/keras/backend/image_data_format): Returns the default image data format convention.

[`in_test_phase(...)`](../../tf/keras/backend/in_test_phase): Selects `x` in test phase, and `alt` otherwise.

[`in_top_k(...)`](../../tf/keras/backend/in_top_k): Returns whether the `targets` are in the top `k` `predictions`.

[`in_train_phase(...)`](../../tf/keras/backend/in_train_phase): Selects `x` in train phase, and `alt` otherwise.

[`int_shape(...)`](../../tf/keras/backend/int_shape): Returns the shape of tensor or variable as a tuple of int or None entries.

[`is_sparse(...)`](../../tf/keras/backend/is_sparse): Returns whether a tensor is a sparse tensor.

[`l2_normalize(...)`](../../tf/keras/backend/l2_normalize): Normalizes a tensor wrt the L2 norm alongside the specified axis.

[`learning_phase(...)`](../../tf/keras/backend/learning_phase): Returns the learning phase flag.

[`less(...)`](../../tf/keras/backend/less): Element-wise truth value of (x < y).

[`less_equal(...)`](../../tf/keras/backend/less_equal): Element-wise truth value of (x <= y).

[`log(...)`](../../tf/keras/backend/log): Element-wise log.

[`manual_variable_initialization(...)`](../../tf/keras/backend/manual_variable_initialization): Sets the manual variable initialization flag.

[`map_fn(...)`](../../tf/keras/backend/map_fn): Map the function fn over the elements elems and return the outputs.

[`max(...)`](../../tf/keras/backend/max): Maximum value in a tensor.

[`maximum(...)`](../../tf/keras/backend/maximum): Element-wise maximum of two tensors.

[`mean(...)`](../../tf/keras/backend/mean): Mean of a tensor, alongside the specified axis.

[`min(...)`](../../tf/keras/backend/min): Minimum value in a tensor.

[`minimum(...)`](../../tf/keras/backend/minimum): Element-wise minimum of two tensors.

[`moving_average_update(...)`](../../tf/keras/backend/moving_average_update): Compute the moving average of a variable.

[`ndim(...)`](../../tf/keras/backend/ndim): Returns the number of axes in a tensor, as an integer.

[`normalize_batch_in_training(...)`](../../tf/keras/backend/normalize_batch_in_training): Computes mean and std for batch then apply batch_normalization on batch.

[`not_equal(...)`](../../tf/keras/backend/not_equal): Element-wise inequality between two tensors.

[`one_hot(...)`](../../tf/keras/backend/one_hot): Computes the one-hot representation of an integer tensor.

[`ones(...)`](../../tf/keras/backend/ones): Instantiates an all-ones variable and returns it.

[`ones_like(...)`](../../tf/keras/backend/ones_like): Instantiates an all-ones variable of the same shape as another tensor.

[`permute_dimensions(...)`](../../tf/keras/backend/permute_dimensions): Permutes axes in a tensor.

[`placeholder(...)`](../../tf/keras/backend/placeholder): Instantiates a placeholder tensor and returns it.

[`pool2d(...)`](../../tf/keras/backend/pool2d): 2D Pooling.

[`pool3d(...)`](../../tf/keras/backend/pool3d): 3D Pooling.

[`pow(...)`](../../tf/keras/backend/pow): Element-wise exponentiation.

[`print_tensor(...)`](../../tf/keras/backend/print_tensor): Prints `message` and the tensor value when evaluated.

[`prod(...)`](../../tf/keras/backend/prod): Multiplies the values in a tensor, alongside the specified axis.

[`random_binomial(...)`](../../tf/keras/backend/random_binomial): Returns a tensor with random binomial distribution of values.

[`random_normal(...)`](../../tf/keras/backend/random_normal): Returns a tensor with normal distribution of values.

[`random_normal_variable(...)`](../../tf/keras/backend/random_normal_variable): Instantiates a variable with values drawn from a normal distribution.

[`random_uniform(...)`](../../tf/keras/backend/random_uniform): Returns a tensor with uniform distribution of values.

[`random_uniform_variable(...)`](../../tf/keras/backend/random_uniform_variable): Instantiates a variable with values drawn from a uniform distribution.

[`relu(...)`](../../tf/keras/backend/relu): Rectified linear unit.

[`repeat(...)`](../../tf/keras/backend/repeat): Repeats a 2D tensor.

[`repeat_elements(...)`](../../tf/keras/backend/repeat_elements): Repeats the elements of a tensor along an axis, like `np.repeat`.

[`reset_uids(...)`](../../tf/keras/backend/reset_uids): Resets graph identifiers.

[`reshape(...)`](../../tf/keras/backend/reshape): Reshapes a tensor to the specified shape.

[`resize_images(...)`](../../tf/keras/backend/resize_images): Resizes the images contained in a 4D tensor.

[`resize_volumes(...)`](../../tf/keras/backend/resize_volumes): Resizes the volume contained in a 5D tensor.

[`reverse(...)`](../../tf/keras/backend/reverse): Reverse a tensor along the specified axes.

[`rnn(...)`](../../tf/keras/backend/rnn): Iterates over the time dimension of a tensor.

[`round(...)`](../../tf/keras/backend/round): Element-wise rounding to the closest integer.

[`separable_conv2d(...)`](../../tf/keras/backend/separable_conv2d): 2D convolution with separable filters.

[`set_epsilon(...)`](../../tf/keras/backend/set_epsilon): Sets the value of the fuzz factor used in numeric expressions.

[`set_floatx(...)`](../../tf/keras/backend/set_floatx): Sets the default float type.

[`set_image_data_format(...)`](../../tf/keras/backend/set_image_data_format): Sets the value of the image data format convention.

[`set_learning_phase(...)`](../../tf/keras/backend/set_learning_phase): Sets the learning phase to a fixed value.

[`set_session(...)`](../../tf/keras/backend/set_session): Sets the global TensorFlow session.

[`set_value(...)`](../../tf/keras/backend/set_value): Sets the value of a variable, from a Numpy array.

[`shape(...)`](../../tf/keras/backend/shape): Returns the symbolic shape of a tensor or variable.

[`sigmoid(...)`](../../tf/keras/backend/sigmoid): Element-wise sigmoid.

[`sign(...)`](../../tf/keras/backend/sign): Element-wise sign.

[`sin(...)`](../../tf/keras/backend/sin): Computes sin of x element-wise.

[`softmax(...)`](../../tf/keras/backend/softmax): Softmax of a tensor.

[`softplus(...)`](../../tf/keras/backend/softplus): Softplus of a tensor.

[`softsign(...)`](../../tf/keras/backend/softsign): Softsign of a tensor.

[`sparse_categorical_crossentropy(...)`](../../tf/keras/backend/sparse_categorical_crossentropy): Categorical crossentropy with integer targets.

[`spatial_2d_padding(...)`](../../tf/keras/backend/spatial_2d_padding): Pads the 2nd and 3rd dimensions of a 4D tensor.

[`spatial_3d_padding(...)`](../../tf/keras/backend/spatial_3d_padding): Pads 5D tensor with zeros along the depth, height, width dimensions.

[`sqrt(...)`](../../tf/keras/backend/sqrt): Element-wise square root.

[`square(...)`](../../tf/keras/backend/square): Element-wise square.

[`squeeze(...)`](../../tf/keras/backend/squeeze): Removes a 1-dimension from the tensor at index "axis".

[`stack(...)`](../../tf/keras/backend/stack): Stacks a list of rank `R` tensors into a rank `R+1` tensor.

[`std(...)`](../../tf/keras/backend/std): Standard deviation of a tensor, alongside the specified axis.

[`stop_gradient(...)`](../../tf/keras/backend/stop_gradient): Returns `variables` but with zero gradient w.r.t. every other variable.

[`sum(...)`](../../tf/keras/backend/sum): Sum of the values in a tensor, alongside the specified axis.

[`switch(...)`](../../tf/keras/backend/switch): Switches between two operations depending on a scalar value.

[`tanh(...)`](../../tf/keras/backend/tanh): Element-wise tanh.

[`temporal_padding(...)`](../../tf/keras/backend/temporal_padding): Pads the middle dimension of a 3D tensor.

[`tile(...)`](../../tf/keras/backend/tile): Creates a tensor by tiling `x` by `n`.

[`to_dense(...)`](../../tf/keras/backend/to_dense): Converts a sparse tensor into a dense tensor and returns it.

[`transpose(...)`](../../tf/keras/backend/transpose): Transposes a tensor and returns it.

[`truncated_normal(...)`](../../tf/keras/backend/truncated_normal): Returns a tensor with truncated random normal distribution of values.

[`update(...)`](../../tf/keras/backend/update)

[`update_add(...)`](../../tf/keras/backend/update_add): Update the value of `x` by adding `increment`.

[`update_sub(...)`](../../tf/keras/backend/update_sub): Update the value of `x` by subtracting `decrement`.

[`var(...)`](../../tf/keras/backend/var): Variance of a tensor, alongside the specified axis.

[`variable(...)`](../../tf/keras/backend/variable): Instantiates a variable and returns it.

[`zeros(...)`](../../tf/keras/backend/zeros): Instantiates an all-zeros variable and returns it.

[`zeros_like(...)`](../../tf/keras/backend/zeros_like): Instantiates an all-zeros variable of the same shape as another tensor.

