from __future__ import absolute_import, division, print_function
# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
# Helper libraries
import numpy as np
import matplotlib.pyplot as plt
import os

print(tf.__version__)
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()
train_labels = train_labels[:1000]
test_labels = test_labels[:1000]
train_images = train_images[:1000].reshape(-1, 28 * 28) / 255.0
test_images = test_images[:1000].reshape(-1, 28 * 28) / 255.0

# Returns a short sequential model
def create_model():
    model = tf.keras.models.Sequential([
        keras.layers.Dense(512, activation=tf.keras.activations.relu, input_shape=(784,)),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(10, activation=tf.keras.activations.softmax)
    ])
    model.compile(optimizer=tf.keras.optimizers.Adam(),
                  loss=tf.keras.losses.sparse_categorical_crossentropy,
                  metrics=['accuracy'])

    return model

# Save checkpoints during training
model = create_model()
model.summary()
checkpoint_path = "training_2/cp-{epoch:04d}.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)
cp_callback = tf.keras.callbacks.ModelCheckpoint(
    checkpoint_path, verbose=1, save_weights_only=True,
    period=5)
model = create_model()
model.save_weights(checkpoint_path.format(epoch=0))
model.fit(train_images, train_labels,
          epochs = 50, callbacks = [cp_callback],
          validation_data = (test_images,test_labels),
          verbose=0)
latest = tf.train.latest_checkpoint(checkpoint_dir)
model = create_model()
model.load_weights(latest)
loss, acc = model.evaluate(test_images, test_labels)
print("Restored model, accuracy: {:5.2f}%".format(100*acc))

# Manually save weights
model.save_weights('./checkpoints/my_checkpoint')
model = create_model()
model.load_weights('./checkpoints/my_checkpoint')
loss,acc = model.evaluate(test_images, test_labels)
print("Restored model, accuracy: {:5.2f}%".format(100*acc))

# Save the entire model [As an HDF5 file]
model = create_model()
model.fit(train_images, train_labels, epochs=5)
model.save('my_model.h5')
new_model = keras.models.load_model('my_model.h5')
new_model.summary()
loss, acc = new_model.evaluate(test_images, test_labels)
print("Restored model, accuracy: {:5.2f}%".format(100*acc))

# Save the entire model [As a saved_model]
# tf.contrib has been deprecated in TensorFlow 2.0. 
# [RFC: Sunset tf.contrib](https://github.com/tensorflow/community/pull/18)

# Extras:
# Checkpoints without versioning
  # checkpoint_path = "training_1/cp.ckpt"
  # checkpoint_dir = os.path.dirname(checkpoint_path)
  # cp_callback = tf.keras.callbacks.ModelCheckpoint(checkpoint_path, 
  #                                                  save_weights_only=True,
  #                                                  verbose=1)
  # model = create_model()
  # model.fit(train_images, train_labels,  epochs = 10, 
  #           validation_data = (test_images,test_labels),
  #           callbacks = [cp_callback])
  # model = create_model()
  # loss, acc = model.evaluate(test_images, test_labels)
  # print("Untrained model, accuracy: {:5.2f}%".format(100*acc))
  # model.load_weights(checkpoint_path)
  # loss,acc = model.evaluate(test_images, test_labels)
  # print("Restored model, accuracy: {:5.2f}%".format(100*acc))