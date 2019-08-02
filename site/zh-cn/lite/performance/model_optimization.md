# 模型优化

Tensorflow Lite 和 [Tensorflow Model Optimization Toolkit](https://www.tensorflow.org/model_optimization) (Tensorflow模型优化工具包)提供了最小优化推理复杂性的工具。

对于移动和物联网 (IoT) 等边缘设备,推理效率尤其重要。这些设备在处理，内存，能耗和模型存储方面有许多限制。
此外，模型优化解锁了定点硬件 (fixed-point hardware) 和下一代硬件加速器的处理能力。

## 模型量化

深度神经网络的量化使用了一些技术，这些技术可以降低权重的精确表示，并且可选的降低存储和计算的激活值。量化的好处有:

* 对现有 CPU 平台的支持。
* 激活值得的量化降低了用于读取和存储中间激活值的存储器访问成本。
* 许多 CPU 和硬件加速器实现提供 SIMD 指令功能，这对量化特别有益。

TensorFlow Lite 对量化提供了多种级别的对量化支持。

* Tensorflow Lite [post-training quantization](post_training_quantization.md) 量化使权重和激活值的 Post training 更简单。
* [Quantization-aware training](https://github.com/tensorflow/tensorflow/tree/r1.13/tensorflow/contrib/quantize){:.external} 可以以最小精度下降来训练网络；这仅适用于卷积神经网络的一个子集。

### 延时和准确性结果

以下是一些模型经过 post-training quantization 和 quantization-aware training 后的延迟和准确性结果。所有延迟数都是在使用单个大内核的 Pixel 2 设备上测量的。随着工具包的改进，这些数字也会随之提高:

<figure>
  <table>
    <tr>
      <th>模型</th>
      <th>Top-1 精确性(初始) </th> 
      <th>Top-1 精确性(Post Training量化) </th>
      <th>Top-1 精确性 (Quantization Aware Training) </th>
      <th>延迟 (初始) (ms) </th> 
      <th>延迟 (Post Training量化) (ms) </th>
      <th>延迟 (Quantization Aware) (ms) </th>
      <th> 大小 (初始) (MB)</th>
      <th> 大小 (优化后) (MB)</th>
    </tr> <tr><td>Mobilenet-v1-1-224</td><td>0.709</td><td>0.657</td><td>0.70</td>
      <td>124</td><td>112</td><td>64</td><td>16.9</td><td>4.3</td></tr>
    <tr><td>Mobilenet-v2-1-224</td><td>0.719</td><td>0.637</td><td>0.709</td>
      <td>89</td><td>98</td><td>54</td><td>14</td><td>3.6</td></tr>
   <tr><td>Inception_v3</td><td>0.78</td><td>0.772</td><td>0.775</td>
      <td>1130</td><td>845</td><td>543</td><td>95.7</td><td>23.9</td></tr>
   <tr><td>Resnet_v2_101</td><td>0.770</td><td>0.768</td><td>N/A</td>
      <td>3973</td><td>2868</td><td>N/A</td><td>178.3</td><td>44.9</td></tr>
 </table>
  <figcaption>
    <b>Table 1</b> 模型量化对选择CNN模型的好处
  </figcaption>
</figure>

## 工具选择

首先，检查 [hosted models](../guide/hosted_models.md) 中的模型是否适合您的应用程序。如果没有，我们建议用户从 [post-training quantization tool](post_training_quantization.md) 开始，因为它广泛适用的，且无需训练数据。

对于精度和延迟目标没有达到，或者需要硬件加速器支持情况， [quantization-aware training](https://github.com/tensorflow/tensorflow/tree/r1.13/tensorflow/contrib/quantize) {:.external} 是更好的选择。参见 Tensorflow 模型优化工具包[Tensorflow Model Optimization Toolkit](https://www.tensorflow.org/model_optimization) 中的的其他优化技术。

注意: Quantization-aware training 支持卷积神经网络体系结构的子集。
