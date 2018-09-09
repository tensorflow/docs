# Post Training weight quantization and faster inference in TensorFlow

## Overview

[TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/) now supports
converting weights to 8 bit precision as part of model conversion from
tensorflow graphdefs to TFLite's flat buffer format. Weight quantization
achieves a 4x reduction in the model size. In addition, TFLite supports on the
fly quantization and dequantization of activations to allow for:

1.  Using quantized kernels for faster implementation when available.

2.  Mixing of floating-point kernels with quantized kernels for different parts
    of the graph.

Note that the activations are always stored in floating point. For ops that
support quantized kernels, the activations are quantized to 8 bits of precision
dynamically prior to processing and are de-quantized to float precision after
processing. Depending on the model being converted, this can give a speedup over
pure floating point computation.

In contrast to
[quantization aware training](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/quantize)
, the weights are quantized post training and the activations are quantized dynamically 
at inference in this method.
Therefore, the model weights are not retrained to compensate for quantization
induced errors. It is important to check the accuracy of the quantized model to
ensure that the degradation is acceptable.

In this tutorial, we train an MNIST model from scratch, check its accuracy in
tensorflow and then convert the saved model into a Tensorflow Lite flatbuffer
with weight quantization. We finally check the
accuracy of the converted model and compare it to the original saved model. We
run the training script mnist.py from
[Tensorflow official mnist tutorial](https://github.com/tensorflow/models/tree/master/official/mnist).

### Building an MNIST model

```
python mnist.py --logtostderr --export_dir /tmp/mnist_saved_model
```

Running this code produces a model with evaluation accuracy of 0.9928. An
example of the output is

```
I0812 00:05:39.419336 110613 estimator.py:1766] Saving dict for global step 24000: accuracy = 0.9928, global_step = 24000, loss = 0.0244758
I0812 00:05:39.423463 110613 estimator.py:1812] Saving 'checkpoint_path' summary for global step 24000: /tmp/mnist_model/model.ckpt-24000
Evaluation results: {'global_step': 24000, 'accuracy': 0.9928, 'loss':0.024475832}
I0812 00:05:40.740344 110613 builder_impl.py:475] SavedModel written to: /tmp/mnist_saved_model/temp-1534057539/saved_model.pb
```

The saved model available in /tmp/mnist_saved_model/<timestamp> is converted into
a TFLite model with and without quantized weights, by setting the attribute
post_training_quantize to True and False respectively.

```

saved_model_dir = '/tmp/mnist_saved_model/<time-stamp>/'
converter = tf.contrib.lite.TocoConverter.from_saved_model(saved_model_dir)
converter.post_training_quantize = False
tflite_model = converter.convert()
open("/tmp/mnist_tflite_model/mnist_model.tflite", "wb").write(tflite_model)
converter.post_training_quantize = True
tflite_model = converter.convert()
open("/tmp/mnist_saved_model/mnist_model_quantized.tflite","wb").write(tflite_model)

```

We check the file sizes of the floating point and quantized models and see that
the quantized model is 4x smaller.

```

/tmp/mnist_saved_model/mnist_model.tflite 13101280
/tmp/mnist_saved_model/mnist_model_quantized.tflite 3283704

```

We can run the float TensorFlow Lite model using the python TensorFlow Lite
Interpreter as shown in the file mnist_tflite.py. The interpreter first loads
the mnist tflite model and then evaluates the model one image at a time. Note we
run the TensorFlow data pipeline for minist to get the input to provide to the model.

```
from tensorflow.contrib.lite.tutorials import dataset
def test_image_generator():
  # Generates an iterator over images
  with tf.Session() as sess:
    input_data = dataset.test(
        flags.data_dir).make_one_shot_iterator().get_next()
    try:
      while True:
        yield sess.run(input_data)
    except tf.errors.OutOfRangeError:
      pass


def run_eval(interpreter, input_image):
  """Performs evaluation for input image over specified model.
  """
  # Get input and output tensors.
  input_details = interpreter.get_input_details()
  output_details = interpreter.get_output_details()

  # Test model on the input images.
  input_image = np.reshape(input_image, input_details[0]['shape'])
  interpreter.set_tensor(input_details[0]['index'], input_image)

  interpreter.invoke()
  output_data = interpreter.get_tensor(output_details[0]['index'])
  output = np.squeeze(output_data)
  return output


def main(_):
  interpreter = tf.contrib.lite.Interpreter(model_path=flags.model_file)
  interpreter.allocate_tensors()
  num_correct, total = 0, 0
  for input_data in test_image_generator():
    output = run_eval(interpreter, input_data[0])
    total += 1
    if output == input_data[1]:
      num_correct += 1
    if total % 500 == 0:
      print('Accuracy after %i images: %f' %
            (total, float(num_correct) / float(total)))

```

Invoking this code, we can run evaluation on the TFLite buffer:

```

python mnist_tflite --data_dir='/tmp/mnist_data' --model_file='/tmp/mnist_saved_model/mnist_model.tflite'
Accuracy after 500 images: 0.992000
Accuracy after 1000 images: 0.990000
Accuracy after 1500 images: 0.985333
Accuracy after 2000 images: 0.987000
Accuracy after 2500 images: 0.986400
Accuracy after 3000 images: 0.986667
Accuracy after 3500 images: 0.988286
Accuracy after 4000 images: 0.988250
Accuracy after 4500 images: 0.988889
Accuracy after 5000 images: 0.989400
Accuracy after 5500 images: 0.990182
Accuracy after 6000 images: 0.990333
Accuracy after 6500 images: 0.991077
Accuracy after 7000 images: 0.990857
Accuracy after 7500 images: 0.991467
Accuracy after 8000 images: 0.992000
Accuracy after 8500 images: 0.992471
Accuracy after 9000 images: 0.992778
Accuracy after 9500 images: 0.992947
Accuracy after 10000 images: 0.992800

```

We can repeat the evaluation on the weight quantized model to obtain:

```

python mnist_tflite --data_dir='/tmp/mnist_data' --model_file='/tmp/mnist_saved_model/mnist_model_quantized.tflite'
Accuracy after 500 images: 0.992000
Accuracy after 1000 images: 0.990000
Accuracy after 1500 images: 0.985333
Accuracy after 2000 images: 0.987000
Accuracy after 2500 images: 0.986400
Accuracy after 3000 images: 0.986667
Accuracy after 3500 images: 0.988286
Accuracy after 4000 images: 0.988250
Accuracy after 4500 images: 0.988889
Accuracy after 5000 images: 0.989400
Accuracy after 5500 images: 0.990182
Accuracy after 6000 images: 0.990333
Accuracy after 6500 images: 0.991077
Accuracy after 7000 images: 0.990857
Accuracy after 7500 images: 0.991467
Accuracy after 8000 images: 0.992000
Accuracy after 8500 images: 0.992471
Accuracy after 9000 images: 0.992778
Accuracy after 9500 images: 0.992947
Accuracy after 10000 images: 0.992800
```

In this example, we have compressed model with no difference in the accuracy.

### Optimizing an existing model
We now consider another example. Resnets with pre-activation layers (Resnet-v2) are widely used for vision applications.
  Pre-trained frozen graph for resnet-v2-101 is available at the
  [Tensorflow Lite model repository](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/contrib/lite/g3doc/models.md).

We can convert the frozen graph to a TFLite flatbuffer with quantization by:
  
```
import tensorflow as tf

graph_def_file = "/path/to/Downloads/resnet_v2_101/resnet_v2_101_299_frozen.pb"
input_arrays = ["input"]
output_arrays = ["resnet_v2_101/predictions/Reshape_1"]

converter = tf.contrib.lite.TocoConverter.from_frozen_graph(
  graph_def_file, input_arrays, output_arrays)
converter.post_training_quantize = True
tflite_model = converter.convert()
open("resnet_v2_101_quantized.tflite", "wb").write(tflite_model)
```
The model size reduces from 241 MB to 60.8 MB.
The accuracy of this model on imagenet can be evaluated using the scripts provided for [TFLite accuracy measurement](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/lite/tools/accuracy/ilsvrc).
The optimized model top-1 accuracy is 76.8, compared to the floating point model top-1 accuracy of 77.0.
