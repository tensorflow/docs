
# Quantization-aware training

Quantization-aware model training ensures that the forward pass matches precision
for both training and inference. There are two aspects to this:

* Operator fusion at inference time are accurately modeled at training time.
* Quantization effects at inference are modeled at training time.

For efficient inference, TensorFlow combines batch normalization with the preceding
convolutional and fully-connected layers prior to quantization by
[folding batch norm layers](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/contrib/quantize/python/fold_batch_norms.py). 

The quantization error is modeled using [fake quantization](../api_guides/python/array_ops.md#Fake_quantization)
nodes to simulate the effect of quantization in the forward and backward passes. The
forward-pass models quantization, while the backward-pass models quantization as a
straight-through `Estimator`. Both the forward- and backward-pass simulate the quantization
of weights and activations.

Additionally, the minimum and maximum values for activations are determined
during training. This allows a model trained with quantization in the loop to be
converted to a fixed point inference model with little effort, eliminating the
need for a separate calibration step.

Since it's difficult to add these fake quantization operations to all the
required locations in the model, there's a function available that rewrites the
training graph. To create a fake quantized training graph:

```
# Build forward pass of model.
loss = tf.losses.get_total_loss()

# Call the training rewrite which rewrites the graph in-place with
# FakeQuantization nodes and folds batchnorm for training. It is
# often needed to fine tune a floating point model for quantization
# with this training tool. When training from scratch, quant_delay
# can be used to activate quantization after training to converge
# with the float graph, effectively fine-tuning the model.
tf.contrib.quantize.create_training_graph(quant_delay=2000000)

# Call backward pass optimizer as usual.
optimizer = tf.train.GradientDescentOptimizer(learning_rate)
optimizer.minimize(loss)
```

The rewritten *eval graph* is non-trivially different from the *training graph*
since the quantization ops affect the batch normalization step. Because of this,
we've added a separate rewrite for the *eval graph*:

```
# Build eval model
logits = tf.nn.softmax_cross_entropy_with_logits_v2(...)

# Call the eval rewrite which rewrites the graph in-place with
# FakeQuantization nodes and fold batchnorm for eval.
tf.contrib.quantize.create_eval_graph()

# Save the checkpoint and eval graph proto to disk for freezing
# and providing to TFLite.
with open(eval_graph_file, ‘w’) as f:
  f.write(str(g.as_graph_def()))
saver = tf.train.Saver()
saver.save(sess, checkpoint_name)
```

Methods to rewrite the training and eval graphs are an active area of research
and experimentation. Although rewrites and quantized training might not work or
improve performance for all models, we are working to generalize these techniques.


## Generating fully-quantized models

The previously demonstrated after-rewrite eval graph only *simulates*
quantization. To generate real fixed-point computations from a trained
quantization model, convert it to a fixed-point kernel. TensorFlow Lite supports
this conversion from the graph resulting from `create_eval_graph`.

First, create a frozen graph that will be the input for the TensorFlow Lite
toolchain:

```
bazel build tensorflow/python/tools:freeze_graph && \
  bazel-bin/tensorflow/python/tools/freeze_graph \
  --input_graph=eval_graph_def.pb \
  --input_checkpoint=checkpoint \
  --output_graph=frozen_eval_graph.pb --output_node_names=outputs
```

Provide this to the TensorFlow Lite Optimizing Converter (TOCO) to get a
fully-quantized TensorFlow Lite model:

```
bazel build tensorflow/contrib/lite/toco:toco && \
  ./bazel-bin/third_party/tensorflow/contrib/lite/toco/toco \
  --input_file=frozen_eval_graph.pb \
  --output_file=tflite_model.tflite \
  --input_format=TENSORFLOW_GRAPHDEF --output_format=TFLITE \
  --inference_type=QUANTIZED_UINT8 \
  --input_shape="1,224, 224,3" \
  --input_array=input \
  --output_array=outputs \
  --std_value=127.5 --mean_value=127.5
```

See the documentation for `tf.contrib.quantize` and [TensorFlow Lite](../mobile/tflite/).


## Quantized accuracy results

The following are results of trainiing some popular CNN models (Mobilenet-v1,
Mobilenet-v2, and Inception-v3) using this tool:

<figure>
  <table>
    <tr>
      <th>Model</th>
      <th>Top-1 Accuracy:<br>Floating point</th>
      <th>Top-1 Accuracy:<br>Fixed point: 8 bit weights and activations</th>
    </tr>
    <tr><td>Mobilenet-v1-128-0.25</td><td>0.415</td><td>0.399</td></tr>
    <tr><td>Mobilenet-v1-128-0.5</td><td>0.563</td><td>0.549</td></tr>
    <tr><td>Mobilenet-v1-128-0.75</td><td>0.621</td><td>0.598</td></tr>
    <tr><td>Mobilenet-v1-128-1</td><td>0.652</td><td>0.64</td></tr>
    <tr><td>Mobilenet-v1-160-0.25</td><td>0.455</td><td>0.435</td></tr>
    <tr><td>Mobilenet-v1-160-0.5</td><td>0.591</td><td>0.577</td></tr>
    <tr><td>Mobilenet-v1-160-0.75</td><td>0.653</td><td>0.639</td></tr>
    <tr><td>Mobilenet-v1-160-1</td><td>0.68</td><td>0.673</td></tr>
    <tr><td>Mobilenet-v1-192-0.25</td><td>0.477</td><td>0.458</td></tr>
    <tr><td>Mobilenet-v1-192-0.5</td><td>0.617</td><td>0.604</td></tr>
    <tr><td>Mobilenet-v1-192-0.75</td><td>0.672</td><td>0.662</td></tr>
    <tr><td>Mobilenet-v1-192-1</td><td>0.7</td><td>0.69</td></tr>
    <tr><td>Mobilenet-v1-224-0.25</td><td>0.498</td><td>0.482</td></tr>
    <tr><td>Mobilenet-v1-224-0.5</td><td>0.633</td><td>0.622</td></tr>
    <tr><td>Mobilenet-v1-224-0.75</td><td>0.684</td><td>0.679</td></tr>
    <tr><td>Mobilenet-v1-224-1</td><td>0.709</td><td>0.697</td></tr>
    <tr><td>Mobilenet-v2-224-1</td><td>0.718</td><td>0.708</td></tr>
   <tr><td>Inception_v3</td><td>0.78</td><td>0.775</td></tr>
  </table>
  <figcaption>
    <b>Table 1</b>: Top-1 accuracy of floating point and fully quantized CNNs on Imagenet Validation dataset.
  </figcaption>
</figure>

Our pre-trained models are available in the
<a href="https://github.com/tensorflow/tensorflow/blob/master/tensorflow/contrib/lite/g3doc/models.md#image-classification-quantized-models">TensorFlow Lite model repository</a>. The code used to generate
these models <a href="https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1_train.py"> is available</a>.


## Representation for quantized tensors

TensorFlow approaches the conversion of floating-point arrays of numbers into
8-bit representations as a compression problem. Since the weights and activation
tensors in trained neural network models tend to have values that are distributed
across comparatively small ranges (for example, -15 to +15 for weights or -500 to
1000 for image model activations). And since neural nets tend to be robust
handling noise, the error introduced by quantizing to a small set of values
maintains the precision of the overall results within an acceptable threshold. A
chosen representation must perform fast calculations, especially the large matrix
multiplications that comprise the bulk of the computations while running a model.

This is represented with two floats that store the overall minimum and maximum
values corresponding to the lowest and highest quantized value. Each entry in the
quantized array represents a float value in that range, distributed linearly
between the minimum and maximum. For example, with a minimum of -10.0 and maximum
of 30.0f, and an 8-bit array, the quantized values represent the following:

<figure>
  <table>
    <tr><th>Quantized</th><th>Float</th></tr>
    <tr><td>0</td><td>-10.0</td></tr>
    <tr><td>128</td><td>10.0</td></tr>
    <tr><td>255</td><td>30.0</td></tr>
  </table>
  <figcaption>
    <b>Table 2</b>: Example quantized value range
  </figcaption>
</figure>

The advantages of this representation format are:

* It efficiently represents an arbitrary magnitude of ranges.
* The values don't have to be symmetrical.
* The format represents both signed and unsigned values.
* The linear spread makes multiplications straightforward.

Alternative techniques use lower bit depths by non-linearly distributing the
float values across the representation, but currently are more expensive in terms
of computation time.
