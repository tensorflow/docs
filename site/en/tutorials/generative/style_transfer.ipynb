{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "g_nWetWWd_ns"
      },
      "source": [
        "##### Copyright 2018 The TensorFlow Authors."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cellView": "form",
        "id": "2pHVBk_seED1"
      },
      "outputs": [],
      "source": [
        "#@title Licensed under the Apache License, Version 2.0 (the \"License\");\n",
        "# you may not use this file except in compliance with the License.\n",
        "# You may obtain a copy of the License at\n",
        "#\n",
        "# https://www.apache.org/licenses/LICENSE-2.0\n",
        "#\n",
        "# Unless required by applicable law or agreed to in writing, software\n",
        "# distributed under the License is distributed on an \"AS IS\" BASIS,\n",
        "# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n",
        "# See the License for the specific language governing permissions and\n",
        "# limitations under the License."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "6msVLevwcRhm"
      },
      "source": [
        "# Neural style transfer"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Ds4o1h4WHz9U"
      },
      "source": [
        "<table class=\"tfo-notebook-buttons\" align=\"left\">\n",
        "  <td>\n",
        "    <a target=\"_blank\" href=\"https://www.tensorflow.org/tutorials/generative/style_transfer\"><img src=\"https://www.tensorflow.org/images/tf_logo_32px.png\" />View on TensorFlow.org</a>\n",
        "  </td>\n",
        "  <td>\n",
        "    <a target=\"_blank\" href=\"https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/generative/style_transfer.ipynb\"><img src=\"https://www.tensorflow.org/images/colab_logo_32px.png\" />Run in Google Colab</a>\n",
        "  </td>\n",
        "  <td>\n",
        "    <a target=\"_blank\" href=\"https://github.com/tensorflow/docs/blob/master/site/en/tutorials/generative/style_transfer.ipynb\"><img src=\"https://www.tensorflow.org/images/GitHub-Mark-32px.png\" />View on GitHub</a>\n",
        "  </td>\n",
        "  <td>\n",
        "    <a href=\"https://storage.googleapis.com/tensorflow_docs/docs/site/en/tutorials/generative/style_transfer.ipynb\"><img src=\"https://www.tensorflow.org/images/download_logo_32px.png\" />Download notebook</a>\n",
        "  </td>\n",
        "  <td>\n",
        "    <a href=\"https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2\"><img src=\"https://www.tensorflow.org/images/hub_logo_32px.png\" />See TF Hub model</a>\n",
        "  </td>\n",
        "</table>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "aDyGj8DmXCJI"
      },
      "source": [
        "This tutorial uses deep learning to compose one image in the style of another image (ever wish you could paint like Picasso or Van Gogh?). This is known as *neural style transfer* and the technique is outlined in <a href=\"https://arxiv.org/abs/1508.06576\" class=\"external\">A Neural Algorithm of Artistic Style</a> (Gatys et al.). \n",
        "\n",
        "Note: This tutorial demonstrates the original style-transfer algorithm. It optimizes the image content to a particular style. Modern approaches train a model to generate the stylized image directly (similar to [CycleGAN](./cyclegan.ipynb)). This approach is much faster (up to 1000x).\n",
        "\n",
        "For a simple application of style transfer with a pretrained model from [TensorFlow Hub](https://tfhub.dev), check out the [Fast style transfer for arbitrary styles](https://www.tensorflow.org/hub/tutorials/tf2_arbitrary_image_stylization) tutorial that uses an [arbitrary image stylization model](https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2). For an example of style transfer with [TensorFlow Lite](https://www.tensorflow.org/lite), refer to [Artistic style transfer with TensorFlow Lite](https://www.tensorflow.org/lite/examples/style_transfer/overview)."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "1b3XwN9V1nvR"
      },
      "source": [
        "Neural style transfer is an optimization technique used to take two images—a *content* image and a *style reference* image (such as an artwork by a famous painter)—and blend them together so the output image looks like the content image, but “painted” in the style of the style reference image.\n",
        "\n",
        "This is implemented by optimizing the output image to match the content statistics of the content image and the style statistics of the style reference image. These statistics are extracted from the images using a convolutional network."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "28W8ggyO1KER"
      },
      "source": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "3kb_UJY-jCEl"
      },
      "source": [
        "For example, let’s take an image of this dog and Wassily Kandinsky's Composition 7:\n",
        "\n",
        "<img src=\"https://storage.googleapis.com/download.tensorflow.org/example_images/YellowLabradorLooking_new.jpg\" width=\"500px\"/>\n",
        "\n",
        "[Yellow Labrador Looking](https://commons.wikimedia.org/wiki/File:YellowLabradorLooking_new.jpg), from Wikimedia Commons by [Elf](https://en.wikipedia.org/wiki/User:Elf). License [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)\n",
        "\n",
        "<img src=\"https://storage.googleapis.com/download.tensorflow.org/example_images/Vassily_Kandinsky%2C_1913_-_Composition_7.jpg\" width=\"500px\"/>\n",
        "\n",
        "\n",
        "Now, what would it look like if Kandinsky decided to paint the picture of this Dog exclusively with this style? Something like this?\n",
        "\n",
        "<img src=\"https://tensorflow.org/tutorials/generative/images/stylized-image.png\" style=\"width: 500px;\"/>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "U8ajP_u73s6m"
      },
      "source": [
        "## Setup\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "eqxUicSPUOP6"
      },
      "source": [
        "### Import and configure modules"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "NyftRTSMuwue"
      },
      "outputs": [],
      "source": [
        "import os\n",
        "import tensorflow as tf\n",
        "# Load compressed models from tensorflow_hub\n",
        "os.environ['TFHUB_MODEL_LOAD_FORMAT'] = 'COMPRESSED'"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "sc1OLbOWhPCO"
      },
      "outputs": [],
      "source": [
        "import IPython.display as display\n",
        "\n",
        "import matplotlib.pyplot as plt\n",
        "import matplotlib as mpl\n",
        "mpl.rcParams['figure.figsize'] = (12, 12)\n",
        "mpl.rcParams['axes.grid'] = False\n",
        "\n",
        "import numpy as np\n",
        "import PIL.Image\n",
        "import time\n",
        "import functools"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "GM6VEGrGLh62"
      },
      "outputs": [],
      "source": [
        "def tensor_to_image(tensor):\n",
        "  tensor = tensor*255\n",
        "  tensor = np.array(tensor, dtype=np.uint8)\n",
        "  if np.ndim(tensor)>3:\n",
        "    assert tensor.shape[0] == 1\n",
        "    tensor = tensor[0]\n",
        "  return PIL.Image.fromarray(tensor)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "oeXebYusyHwC"
      },
      "source": [
        "Download images and choose a style image and a content image:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "wqc0OJHwyFAk"
      },
      "outputs": [],
      "source": [
        "content_path = tf.keras.utils.get_file('YellowLabradorLooking_new.jpg', 'https://storage.googleapis.com/download.tensorflow.org/example_images/YellowLabradorLooking_new.jpg')\n",
        "style_path = tf.keras.utils.get_file('kandinsky5.jpg','https://storage.googleapis.com/download.tensorflow.org/example_images/Vassily_Kandinsky%2C_1913_-_Composition_7.jpg')"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "xE4Yt8nArTeR"
      },
      "source": [
        "## Visualize the input"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "klh6ObK2t_vH"
      },
      "source": [
        "Define a function to load an image and limit its maximum dimension to 512 pixels."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "3TLljcwv5qZs"
      },
      "outputs": [],
      "source": [
        "def load_img(path_to_img):\n",
        "  max_dim = 512\n",
        "  img = tf.io.read_file(path_to_img)\n",
        "  img = tf.image.decode_image(img, channels=3)\n",
        "  img = tf.image.convert_image_dtype(img, tf.float32)\n",
        "\n",
        "  shape = tf.cast(tf.shape(img)[:-1], tf.float32)\n",
        "  long_dim = max(shape)\n",
        "  scale = max_dim / long_dim\n",
        "\n",
        "  new_shape = tf.cast(shape * scale, tf.int32)\n",
        "\n",
        "  img = tf.image.resize(img, new_shape)\n",
        "  img = img[tf.newaxis, :]\n",
        "  return img"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "2yAlRzJZrWM3"
      },
      "source": [
        "Create a simple function to display an image:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "cBX-eNT8PAK_"
      },
      "outputs": [],
      "source": [
        "def imshow(image, title=None):\n",
        "  if len(image.shape) > 3:\n",
        "    image = tf.squeeze(image, axis=0)\n",
        "\n",
        "  plt.imshow(image)\n",
        "  if title:\n",
        "    plt.title(title)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "_UWQmeEaiKkP"
      },
      "outputs": [],
      "source": [
        "content_image = load_img(content_path)\n",
        "style_image = load_img(style_path)\n",
        "\n",
        "plt.subplot(1, 2, 1)\n",
        "imshow(content_image, 'Content Image')\n",
        "\n",
        "plt.subplot(1, 2, 2)\n",
        "imshow(style_image, 'Style Image')"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "YMzChXSlKTA2"
      },
      "source": [
        "## Fast Style Transfer using TF-Hub\n",
        "\n",
        "This tutorial demonstrates the original style-transfer algorithm, which optimizes the image content to a particular style. Before getting into the details, let's see how the [TensorFlow Hub model](https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2) does this:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "iYSLexgRKSh-"
      },
      "outputs": [],
      "source": [
        "import tensorflow_hub as hub\n",
        "hub_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')\n",
        "stylized_image = hub_model(tf.constant(content_image), tf.constant(style_image))[0]\n",
        "tensor_to_image(stylized_image)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "GEwZ7FlwrjoZ"
      },
      "source": [
        "## Define content and style representations\n",
        "\n",
        "Use the intermediate layers of the model to get the *content* and *style* representations of the image. Starting from the network's input layer, the first few layer activations represent low-level features like edges and textures. As you step through the network, the final few layers represent higher-level features—object parts like *wheels* or *eyes*. In this case, you are using the VGG19 network architecture, a pretrained image classification network. These intermediate layers are necessary to define the representation of content and style from the images. For an input image, try to match the corresponding style and content target representations at these intermediate layers.\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "LP_7zrziuiJk"
      },
      "source": [
        "Load a [VGG19](https://keras.io/api/applications/vgg/#vgg19-function) and test run it on our image to ensure it's used correctly:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "fMbzrr7BCTq0"
      },
      "outputs": [],
      "source": [
        "x = tf.keras.applications.vgg19.preprocess_input(content_image*255)\n",
        "x = tf.image.resize(x, (224, 224))\n",
        "vgg = tf.keras.applications.VGG19(include_top=True, weights='imagenet')\n",
        "prediction_probabilities = vgg(x)\n",
        "prediction_probabilities.shape"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "1_FyCm0dYnvl"
      },
      "outputs": [],
      "source": [
        "predicted_top_5 = tf.keras.applications.vgg19.decode_predictions(prediction_probabilities.numpy())[0]\n",
        "[(class_name, prob) for (number, class_name, prob) in predicted_top_5]"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ljpoYk-0f6HS"
      },
      "source": [
        "Now load a `VGG19` without the classification head, and list the layer names"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Yh_AV6220ebD"
      },
      "outputs": [],
      "source": [
        "vgg = tf.keras.applications.VGG19(include_top=False, weights='imagenet')\n",
        "\n",
        "print()\n",
        "for layer in vgg.layers:\n",
        "  print(layer.name)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Wt-tASys0eJv"
      },
      "source": [
        "Choose intermediate layers from the network to represent the style and content of the image:\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "ArfX_6iA0WAX"
      },
      "outputs": [],
      "source": [
        "content_layers = ['block5_conv2'] \n",
        "\n",
        "style_layers = ['block1_conv1',\n",
        "                'block2_conv1',\n",
        "                'block3_conv1', \n",
        "                'block4_conv1', \n",
        "                'block5_conv1']\n",
        "\n",
        "num_content_layers = len(content_layers)\n",
        "num_style_layers = len(style_layers)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "2o4nSwuN0U3X"
      },
      "source": [
        "#### Intermediate layers for style and content\n",
        "\n",
        "So why do these intermediate outputs within our pretrained image classification network allow us to define style and content representations?\n",
        "\n",
        "At a high level, in order for a network to perform image classification (which this network has been trained to do), it must understand the image. This requires taking the raw image as input pixels and building an internal representation that converts the raw image pixels into a complex understanding of the features present within the image.\n",
        "\n",
        "This is also a reason why convolutional neural networks are able to generalize well: they’re able to capture the invariances and defining features within classes (e.g. cats vs. dogs) that are agnostic to background noise and other nuisances. Thus, somewhere between where the raw image is fed into the model and the output classification label, the model serves as a complex feature extractor. By accessing intermediate layers of the model, you're able to describe the content and style of input images."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Jt3i3RRrJiOX"
      },
      "source": [
        "## Build the model \n",
        "\n",
        "The networks in `tf.keras.applications` are designed so you can easily extract the intermediate layer values using the Keras functional API.\n",
        "\n",
        "To define a model using the functional API, specify the inputs and outputs:\n",
        "\n",
        "`model = Model(inputs, outputs)`\n",
        "\n",
        "This following function builds a VGG19 model that returns a list of intermediate layer outputs:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "nfec6MuMAbPx"
      },
      "outputs": [],
      "source": [
        "def vgg_layers(layer_names):\n",
        "  \"\"\" Creates a VGG model that returns a list of intermediate output values.\"\"\"\n",
        "  # Load our model. Load pretrained VGG, trained on ImageNet data\n",
        "  vgg = tf.keras.applications.VGG19(include_top=False, weights='imagenet')\n",
        "  vgg.trainable = False\n",
        "  \n",
        "  outputs = [vgg.get_layer(name).output for name in layer_names]\n",
        "\n",
        "  model = tf.keras.Model([vgg.input], outputs)\n",
        "  return model"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "jbaIvZf5wWn_"
      },
      "source": [
        "And to create the model:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "LkyvPpBHSfVi"
      },
      "outputs": [],
      "source": [
        "style_extractor = vgg_layers(style_layers)\n",
        "style_outputs = style_extractor(style_image*255)\n",
        "\n",
        "#Look at the statistics of each layer's output\n",
        "for name, output in zip(style_layers, style_outputs):\n",
        "  print(name)\n",
        "  print(\"  shape: \", output.numpy().shape)\n",
        "  print(\"  min: \", output.numpy().min())\n",
        "  print(\"  max: \", output.numpy().max())\n",
        "  print(\"  mean: \", output.numpy().mean())\n",
        "  print()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "lGUfttK9F8d5"
      },
      "source": [
        "## Calculate style\n",
        "\n",
        "The content of an image is represented by the values of the intermediate feature maps.\n",
        "\n",
        "It turns out, the style of an image can be described by the means and correlations across the different feature maps. Calculate a Gram matrix that includes this information by taking the outer product of the feature vector with itself at each location, and averaging that outer product over all locations. This Gram matrix can be calculated for a particular layer as:\n",
        "\n",
        "$$G^l_{cd} = \\frac{\\sum_{ij} F^l_{ijc}(x)F^l_{ijd}(x)}{IJ}$$\n",
        "\n",
        "This can be implemented concisely using the `tf.linalg.einsum` function:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "HAy1iGPdoEpZ"
      },
      "outputs": [],
      "source": [
        "def gram_matrix(input_tensor):\n",
        "  result = tf.linalg.einsum('bijc,bijd->bcd', input_tensor, input_tensor)\n",
        "  input_shape = tf.shape(input_tensor)\n",
        "  num_locations = tf.cast(input_shape[1]*input_shape[2], tf.float32)\n",
        "  return result/(num_locations)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "pXIUX6czZABh"
      },
      "source": [
        "## Extract style and content\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "1HGHvwlJ1nkn"
      },
      "source": [
        "Build a model that returns the style and content tensors."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Sr6QALY-I1ja"
      },
      "outputs": [],
      "source": [
        "class StyleContentModel(tf.keras.models.Model):\n",
        "  def __init__(self, style_layers, content_layers):\n",
        "    super(StyleContentModel, self).__init__()\n",
        "    self.vgg = vgg_layers(style_layers + content_layers)\n",
        "    self.style_layers = style_layers\n",
        "    self.content_layers = content_layers\n",
        "    self.num_style_layers = len(style_layers)\n",
        "    self.vgg.trainable = False\n",
        "\n",
        "  def call(self, inputs):\n",
        "    \"Expects float input in [0,1]\"\n",
        "    inputs = inputs*255.0\n",
        "    preprocessed_input = tf.keras.applications.vgg19.preprocess_input(inputs)\n",
        "    outputs = self.vgg(preprocessed_input)\n",
        "    style_outputs, content_outputs = (outputs[:self.num_style_layers],\n",
        "                                      outputs[self.num_style_layers:])\n",
        "\n",
        "    style_outputs = [gram_matrix(style_output)\n",
        "                     for style_output in style_outputs]\n",
        "\n",
        "    content_dict = {content_name: value\n",
        "                    for content_name, value\n",
        "                    in zip(self.content_layers, content_outputs)}\n",
        "\n",
        "    style_dict = {style_name: value\n",
        "                  for style_name, value\n",
        "                  in zip(self.style_layers, style_outputs)}\n",
        "\n",
        "    return {'content': content_dict, 'style': style_dict}"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Xuj1o33t1edl"
      },
      "source": [
        "When called on an image, this model returns the gram matrix (style) of the `style_layers` and content of the `content_layers`:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "rkjO-DoNDU0A"
      },
      "outputs": [],
      "source": [
        "extractor = StyleContentModel(style_layers, content_layers)\n",
        "\n",
        "results = extractor(tf.constant(content_image))\n",
        "\n",
        "print('Styles:')\n",
        "for name, output in sorted(results['style'].items()):\n",
        "  print(\"  \", name)\n",
        "  print(\"    shape: \", output.numpy().shape)\n",
        "  print(\"    min: \", output.numpy().min())\n",
        "  print(\"    max: \", output.numpy().max())\n",
        "  print(\"    mean: \", output.numpy().mean())\n",
        "  print()\n",
        "\n",
        "print(\"Contents:\")\n",
        "for name, output in sorted(results['content'].items()):\n",
        "  print(\"  \", name)\n",
        "  print(\"    shape: \", output.numpy().shape)\n",
        "  print(\"    min: \", output.numpy().min())\n",
        "  print(\"    max: \", output.numpy().max())\n",
        "  print(\"    mean: \", output.numpy().mean())\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "y9r8Lyjb_m0u"
      },
      "source": [
        "## Run gradient descent\n",
        "\n",
        "With this style and content extractor, you can now implement the style transfer algorithm. Do this by calculating the mean square error for your image's output relative to each target, then take the weighted sum of these losses.\n",
        "\n",
        "Set your style and content target values:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "PgkNOnGUFcKa"
      },
      "outputs": [],
      "source": [
        "style_targets = extractor(style_image)['style']\n",
        "content_targets = extractor(content_image)['content']"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "CNPrpl-e_w9A"
      },
      "source": [
        "Define a `tf.Variable` to contain the image to optimize. To make this quick, initialize it with the content image (the `tf.Variable` must be the same shape as the content image):"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "J0vKxF8ZO6G8"
      },
      "outputs": [],
      "source": [
        "image = tf.Variable(content_image)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "M6L8ojmn_6rH"
      },
      "source": [
        "Since this is a float image, define a function to keep the pixel values between 0 and 1:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "kdgpTJwL_vE2"
      },
      "outputs": [],
      "source": [
        "def clip_0_1(image):\n",
        "  return tf.clip_by_value(image, clip_value_min=0.0, clip_value_max=1.0)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "MBU5RFpcAo7W"
      },
      "source": [
        "Create an optimizer. The paper recommends LBFGS, but Adam works okay, too:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "r4XZjqUk_5Eu"
      },
      "outputs": [],
      "source": [
        "opt = tf.keras.optimizers.Adam(learning_rate=0.02, beta_1=0.99, epsilon=1e-1)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "As-evbBiA2qT"
      },
      "source": [
        "To optimize this, use a weighted combination of the two losses to get the total loss:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Dt4pxarvA4I4"
      },
      "outputs": [],
      "source": [
        "style_weight=1e-2\n",
        "content_weight=1e4"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "0ggx2Na8oROH"
      },
      "outputs": [],
      "source": [
        "def style_content_loss(outputs):\n",
        "    style_outputs = outputs['style']\n",
        "    content_outputs = outputs['content']\n",
        "    style_loss = tf.add_n([tf.reduce_mean((style_outputs[name]-style_targets[name])**2) \n",
        "                           for name in style_outputs.keys()])\n",
        "    style_loss *= style_weight / num_style_layers\n",
        "\n",
        "    content_loss = tf.add_n([tf.reduce_mean((content_outputs[name]-content_targets[name])**2) \n",
        "                             for name in content_outputs.keys()])\n",
        "    content_loss *= content_weight / num_content_layers\n",
        "    loss = style_loss + content_loss\n",
        "    return loss"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "vbF2WnP9BI5M"
      },
      "source": [
        "Use `tf.GradientTape` to update the image."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "0t0umkajFIuh"
      },
      "outputs": [],
      "source": [
        "@tf.function()\n",
        "def train_step(image):\n",
        "  with tf.GradientTape() as tape:\n",
        "    outputs = extractor(image)\n",
        "    loss = style_content_loss(outputs)\n",
        "\n",
        "  grad = tape.gradient(loss, image)\n",
        "  opt.apply_gradients([(grad, image)])\n",
        "  image.assign(clip_0_1(image))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "5FHMJq4UBRIQ"
      },
      "source": [
        "Now run a few steps to test:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Y542mxi-O2a2"
      },
      "outputs": [],
      "source": [
        "train_step(image)\n",
        "train_step(image)\n",
        "train_step(image)\n",
        "tensor_to_image(image)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "mNzE-mTbBVgY"
      },
      "source": [
        "Since it's working, perform a longer optimization:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "rQW1tXYoLbUS"
      },
      "outputs": [],
      "source": [
        "import time\n",
        "start = time.time()\n",
        "\n",
        "epochs = 10\n",
        "steps_per_epoch = 100\n",
        "\n",
        "step = 0\n",
        "for n in range(epochs):\n",
        "  for m in range(steps_per_epoch):\n",
        "    step += 1\n",
        "    train_step(image)\n",
        "    print(\".\", end='', flush=True)\n",
        "  display.clear_output(wait=True)\n",
        "  display.display(tensor_to_image(image))\n",
        "  print(\"Train step: {}\".format(step))\n",
        "  \n",
        "end = time.time()\n",
        "print(\"Total time: {:.1f}\".format(end-start))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "GWVB3anJMY2v"
      },
      "source": [
        "## Total variation loss\n",
        "\n",
        "One downside to this basic implementation is that it produces a lot of high frequency artifacts. Decrease these using an explicit regularization term on the high frequency components of the image. In style transfer, this is often called the *total variation loss*:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "7szUUybCQMB3"
      },
      "outputs": [],
      "source": [
        "def high_pass_x_y(image):\n",
        "  x_var = image[:, :, 1:, :] - image[:, :, :-1, :]\n",
        "  y_var = image[:, 1:, :, :] - image[:, :-1, :, :]\n",
        "\n",
        "  return x_var, y_var"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Atc2oL29PXu_"
      },
      "outputs": [],
      "source": [
        "x_deltas, y_deltas = high_pass_x_y(content_image)\n",
        "\n",
        "plt.figure(figsize=(14, 10))\n",
        "plt.subplot(2, 2, 1)\n",
        "imshow(clip_0_1(2*y_deltas+0.5), \"Horizontal Deltas: Original\")\n",
        "\n",
        "plt.subplot(2, 2, 2)\n",
        "imshow(clip_0_1(2*x_deltas+0.5), \"Vertical Deltas: Original\")\n",
        "\n",
        "x_deltas, y_deltas = high_pass_x_y(image)\n",
        "\n",
        "plt.subplot(2, 2, 3)\n",
        "imshow(clip_0_1(2*y_deltas+0.5), \"Horizontal Deltas: Styled\")\n",
        "\n",
        "plt.subplot(2, 2, 4)\n",
        "imshow(clip_0_1(2*x_deltas+0.5), \"Vertical Deltas: Styled\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "lqHElVgBkgkz"
      },
      "source": [
        "This shows how the high frequency components have increased.\n",
        "\n",
        "Also, this high frequency component is basically an edge-detector. You can get similar output from the Sobel edge detector, for example:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "HyvqCiywiUfL"
      },
      "outputs": [],
      "source": [
        "plt.figure(figsize=(14, 10))\n",
        "\n",
        "sobel = tf.image.sobel_edges(content_image)\n",
        "plt.subplot(1, 2, 1)\n",
        "imshow(clip_0_1(sobel[..., 0]/4+0.5), \"Horizontal Sobel-edges\")\n",
        "plt.subplot(1, 2, 2)\n",
        "imshow(clip_0_1(sobel[..., 1]/4+0.5), \"Vertical Sobel-edges\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "vv5bKlSDnPP7"
      },
      "source": [
        "The regularization loss associated with this is the sum of the squares of the values:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "mP-92lXMIYPn"
      },
      "outputs": [],
      "source": [
        "def total_variation_loss(image):\n",
        "  x_deltas, y_deltas = high_pass_x_y(image)\n",
        "  return tf.reduce_sum(tf.abs(x_deltas)) + tf.reduce_sum(tf.abs(y_deltas))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "s4OYBUX2KQ25"
      },
      "outputs": [],
      "source": [
        "total_variation_loss(image).numpy()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "pu2hJ8zOKMc1"
      },
      "source": [
        "That demonstrated what it does. But there's no need to implement it yourself, TensorFlow includes a standard implementation:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "YQjWW04NKLfJ"
      },
      "outputs": [],
      "source": [
        "tf.image.total_variation(image).numpy()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "nTessd-DCdcC"
      },
      "source": [
        "## Re-run the optimization\n",
        "\n",
        "Choose a weight for the `total_variation_loss`:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "tGeRLD4GoAd4"
      },
      "outputs": [],
      "source": [
        "total_variation_weight=30"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "kG1-T4kJsoAv"
      },
      "source": [
        "Now include it in the `train_step` function:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "BzmfcyyYUyWq"
      },
      "outputs": [],
      "source": [
        "@tf.function()\n",
        "def train_step(image):\n",
        "  with tf.GradientTape() as tape:\n",
        "    outputs = extractor(image)\n",
        "    loss = style_content_loss(outputs)\n",
        "    loss += total_variation_weight*tf.image.total_variation(image)\n",
        "\n",
        "  grad = tape.gradient(loss, image)\n",
        "  opt.apply_gradients([(grad, image)])\n",
        "  image.assign(clip_0_1(image))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "lcLWBQChsutQ"
      },
      "source": [
        "Reinitialize the image-variable and the optimizer:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "a-dPRr8BqexB"
      },
      "outputs": [],
      "source": [
        "opt = tf.keras.optimizers.Adam(learning_rate=0.02, beta_1=0.99, epsilon=1e-1)\n",
        "image = tf.Variable(content_image)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "BEflRstmtGBu"
      },
      "source": [
        "And run the optimization:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "q3Cc3bLtoOWy"
      },
      "outputs": [],
      "source": [
        "import time\n",
        "start = time.time()\n",
        "\n",
        "epochs = 10\n",
        "steps_per_epoch = 100\n",
        "\n",
        "step = 0\n",
        "for n in range(epochs):\n",
        "  for m in range(steps_per_epoch):\n",
        "    step += 1\n",
        "    train_step(image)\n",
        "    print(\".\", end='', flush=True)\n",
        "  display.clear_output(wait=True)\n",
        "  display.display(tensor_to_image(image))\n",
        "  print(\"Train step: {}\".format(step))\n",
        "\n",
        "end = time.time()\n",
        "print(\"Total time: {:.1f}\".format(end-start))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "KKox7K46tKxy"
      },
      "source": [
        "Finally, save the result:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "SSH6OpyyQn7w"
      },
      "outputs": [],
      "source": [
        "file_name = 'stylized-image.png'\n",
        "tensor_to_image(image).save(file_name)\n",
        "\n",
        "try:\n",
        "  from google.colab import files\n",
        "  files.download(file_name)\n",
        "except (ImportError, AttributeError):\n",
        "  pass"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "tNlwRXagxQZk"
      },
      "source": [
        "## Learn more\n",
        "\n",
        "This tutorial demonstrates the original style-transfer algorithm. For a simple application of style transfer check out this [tutorial](https://www.tensorflow.org/hub/tutorials/tf2_arbitrary_image_stylization) to learn more about how to use the arbitrary image style transfer model from [TensorFlow Hub](https://tfhub.dev)."
      ]
    }
  ],
  "metadata": {
    "accelerator": "GPU",
    "colab": {
      "collapsed_sections": [],
      "name": "style_transfer.ipynb",
            "toc_visible": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
