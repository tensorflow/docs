# Model optimization
As more machine learning models are deployed to mobile devices,
inference efficiency has become a critical issue. Where the computational demand
for *training* grows with the amount of models trained on different
architectures, the computational demand for *inference* grows in proportion to
the amount of users. We introduce the <b> Tensorflow Model Optimization Toolkit </b> to minimize complexity of inference: model size, latency and power consumption.

## Benefits
Optimizing models is useful in a variety of situations:
<ul> 
  <li>Deploying models on edge devices (e.g. mobile, IOT) with restrictions on processing, memory and/or power-consumption. </li>
<li> Reduce payload size for over-the-air model updates. </li>
<li> Enable execution on hardware restricted-to or optimized-for fixed-point operations. </li>
<li> Optimize models for special purpose hardware accelerators.</li>
<li> Reducing latency and power consumption for inference on cloud </li>
</ul>

## Optimization Methods

Model optimization encompasses multiple techniques falling under the following broad categories:
<ul> 
  <li> Reduced parameter count (e.g pruning, structured pruning) </li>
  <li> Reduced representational precision (e.g. quantization). </li>
  <li> Alteration of the original topology into a more efficient one, with reduced parameters and/or faster to execute (e.g. tensor decomposition methods,distillation).</li>
</ul>


### Model Quantization
Quantizing deep neural networks refers to techniques that allow for reduced precision representations
of weights and optionally activations for both storage and computation.
Quantization provides several benefits:

<ul> 
  <li> Support on existing CPU platforms. </li>
<li> Quantizing activations reduces memory access costs for reading and storing intermediate activations </li>
<li> Many CPU and hardware accelerator implementations provide SIMD instruction capabilities, which are especially beneficial for
  quantization </li>
</ul>

 [TensorFlow Lite](/mobile/tflite/) provides several levels
of support for quantization. 

#### Post Training Quantization
Post Training quantization is a broadly applicable technique that reduces model size by a factor of 4, while also providing
upto 2x lower latency and very little degradation in model accuracy.
Post training quantization quantizes weights to 8 bits of precision from floating point.
This technique is very simple to use and can be invoked by enabling an option in tflite_convert:

```
tflite_convert \
  --output_file=/tmp/foo.tflite \
  --graph_def_file=/tmp/some_quantized_graph.pb \
  --post_training_quantize
```
Our [tutorial](../../tutorials/model_optimization/post_training_quantization.md) walks you through an end
  to end example.
  
##### How does it work?
At inference, we convert the weights from 8-bits of precision to floating point and
compute using floating point kernels. The conversion is done only once and is cached for
reducing latency.

To further improve latency, we introduce hybrid operators. Hybrid operators dynamically
quantize activations to 8 bits and perform computations with 8-bit weights and activations, 
thereby providing latencies close to fully fixed point inference. However, the outputs are still stored at
floating point, so the speedup with hybrid ops is lesser than full fixed point computation. Hybrid ops are
available for the most compute intensive operators in a network:

*  FULLY_CONNECTED
*  CONV_2D
*  SVDF
*  EMBEDDING_LOOKUP
*  RNN
*  BIDIRECTIONAL_SEQUENCE_RNN
*  UNIDIRECTIONAL_SEQUENCE_LSTM
*  UNIDIRECTIONAL_SEQUENCE_RNN

Note that since weights are quantized post training, there could be an accuracy loss, particularly for smaller networks.
We provide pre-trained fully quantized models for specific networks at the Tensorflow lite [model repository](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/contrib/lite/g3doc/models.md#image-classification-quantized-models).
It is important to check the accuracy of the quantized model to verify that
any degradation in accuracy is within acceptable limits. We provide a [tool](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/contrib/lite/tools/accuracy/README.md)
for evaluating TensorFlow Lite model accuracy.

#### Quantization Aware Training

For advanced users, we also provide the option of quantization aware training for a subset of convolutional
neural network architectures. This technique allows for:
1. Higher accuracy by modeling quantization during training
2. Fully fixed point models, quantizing weights and activations, suitable for hardware accelerators.
addition,

Quantization aware training requires accurate modeling of quantization effects during training and access
to training data.  Tensorflow enables quantization aware training by providing tools for automatic insertion of fake quantization
 operations in a graph. Please see [quantization aware training](quantization_training.md) for details.


#### Results
We evaluated the latency and accuracy of post training quantization and quantization aware training on a few models
and our results are below. Note that all latency numbers are measured on a Pixel 2 device on a single big core.
We are constantly improving our toolkit, so please check here for our latest numbers.

<figure>
  <table>
    <tr>
      <th>Model</th>
      <th>Top-1 Accuracy (Original) </th>
      <th>Top-1 Accuracy (Post Training Quantized) </th>
      <th>Top-1 Accuracy (Quantization Aware Training) </th>
      <th>Latency (Original) (ms) </th>
      <th>Latency (Post Training Quantized) (ms) </th>
      <th>Latency (Quantization Aware Training) (ms) </th>
      <th> Size (Original) (MB)</th>
      <th> Size (Optimized) (MB)</th>
    </tr>
    <tr><td>Mobilenet-v1-1-224</td><td>0.709</td><td>0.657</td><td>0.70</td>
      <td>180</td><td>145</td><td>80.2</td><td>16.9</td><td>4.3</td></tr>
    <tr><td>Mobilenet-v2-1-224</td><td>0.719</td><td>0.637</td><td>0.709</td>
      <td>117</td><td>121</td><td>80.3</td><td>14</td><td>3.6</td></tr>
   <tr><td>Inception_v3</td><td>0.78</td><td>0.772</td><td>0.775</td>
      <td>1585</td><td>1187</td><td>637</td><td>95.7</td><td>23.9</td></tr>
   <tr><td>Resnet_v2_101</td><td>0.770</td><td>0.768</td><td>N/A</td>
      <td>3973</td><td>2868</td><td>N/A</td><td>178.3</td><td>44.9</td></tr>
 </table>
  <figcaption>
    <b>Table 1</b> Benefits of model quantization for select CNN models
  </figcaption>
</figure>

#### Choice of quantization tool
 As a starting point, check if the models in the Tensorflow Lite model repository can work for your application. If not, we recommend that our users
 start with the post training quantization tool as this is broadly applicable and does not require training data. For cases where the accuracy and 
 latency targets are not met or hardware accelerator support is important, quantization aware training is a better option. 
 Note that quantization aware training supports only a subset of convolutional neural network architectures.

