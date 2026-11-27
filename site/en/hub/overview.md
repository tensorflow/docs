
# TensorFlow Hub

TensorFlow Hub is an open repository and library for reusable machine learning.
[Kaggle Models](https://www.kaggle.com/models) provides many pre-trained models:
text embeddings, image classification models, TF.js/TFLite models and much more.
The repository is open to
[community contributors](https://www.kaggle.com/models?owner-type=user).

The [`tensorflow_hub`](https://github.com/tensorflow/hub) library lets you
download and reuse them in your TensorFlow program with a minimum amount of
code.

```python
import tensorflow_hub as hub

model = hub.KerasLayer("https://www.kaggle.com/models/google/nnlm/TensorFlow2/en-dim128/2")
embeddings = model(["The rain in Spain.", "falls",
                    "mainly", "In the plain!"])

print(embeddings.shape)  #(4,128)
```

## Next Steps

-   [Find models on kaggle.com](https://www.kaggle.com/models)
-   [Publish models on kaggle.com](publish.md)
-   TensorFlow Hub library
    -   [Install TensorFlow Hub](installation.md)
    -   [Library overview](lib_overview.md)
-   [Follow tutorials](tutorials)
