
# Model compatibility for TF1/TF2

## TF Hub model formats

TF Hub offers reusable model pieces that can be loaded back, built upon, and
possibly be retrained in a TensorFlow program. These come in two different
formats:

*   The custom [TF1 Hub format](https://www.tensorflow.org/hub/tf1_hub_module) .
    Its main intended use is in TF1 (or TF1 compatibility mode in TF2) via its
    [hub.Module API](https://www.tensorflow.org/hub/api_docs/python/hub/Module).
    Full compatibility details [below](#compatibility_of_hubmodule).
*   The native [TF2 SavedModel](https://www.tensorflow.org/hub/tf2_saved_model)
    format. Its main intended use is in TF2 via the
    [hub.load](https://www.tensorflow.org/hub/api_docs/python/hub/load) and
    [hub.KerasLayer](https://www.tensorflow.org/hub/api_docs/python/hub/KerasLayer)
    APIs. Full compatibility details [below](#compatibility_of_tf2_savedmodel).

The model format can be found on the model page on
[tfhub.dev](https://tfhub.dev). Model **loading/inference**, **fine-tuning** or
**creation** might not be supported in TF1/2 based on the model formats.

## Compatibility of the TF1 Hub format {:#compatibility_of_hubmodule}

<table style="width: 100%;">
  <tr style="text-align: center">
    <col style="width: 20%" />
    <col style="width: 40%" />
    <col style="width: 40%" />
    <td style="text-align: center; background-color: #D0D0D0">Operation</td>
    <td style="text-align: center; background-color: #D0D0D0">TF1/ TF1 compat mode in TF2 <a href="#compatfootnote">[1]</a></td>
    <td style="text-align: center; background-color: #D0D0D0">TF2</td>
  </tr>
  <tr>
    <td>Loading / Inference</td>
    <td>
      Fully supported (<a href="https://www.tensorflow.org/hub/tf1_hub_module#using_a_module">complete TF1 Hub format loading guide</a>)
      <pre style="font-size: 12px;" lang="python">m = hub.Module(handle)
outputs = m(inputs)</pre>
    </td>
    <td> It's recommended to use either hub.load
    <pre style="font-size: 12px;" lang="python">m = hub.load(handle)
outputs = m.signatures["sig"](inputs)</pre>
      or hub.KerasLayer
      <pre style="font-size: 12px;" lang="python">m = hub.KerasLayer(handle, signature="sig")
outputs = m(inputs)</pre>
    </td>
  </tr>
  <tr>
    <td>Fine-tuning</td>
    <td>
      Fully supported (<a href="https://www.tensorflow.org/hub/tf1_hub_module#for_consumers">complete TF1 Hub format fine-tuning guide</a>)
    <pre style="font-size: 12px;" lang="python">m = hub.Module(handle,
               trainable=True,
               tags=["train"]*is_training)
outputs = m(inputs)</pre>
      <div style="font-style: italic; font-size: 14px">
      Note: modules that don't need a separate train graph don't have a train
        tag.
      </div>
    </td>
    <td style="text-align: center">
      Not supported
    </td>
  </tr>
  <tr>
    <td>Creation</td>
    <td> Fully supported (see <a href="https://www.tensorflow.org/hub/tf1_hub_module#general_approach">complete TF1 Hub format creation guide</a>) <br> <div style="font-style: italic; font-size: 14px">
      Note: The TF1 Hub format is geared towards TF1 and is only partially supported in TF2. Consider creating a TF2 SavedModel.
      </div></td>
    <td style="text-align: center">Not supported</td>
  </tr>
</table>

## Compatibility of TF2 SavedModel {:#compatibility_of_tf2_savedmodel}

Not supported before TF1.15.
<table style="width: 100%;">
  <tr style="text-align: center">
    <col style="width: 20%" />
    <col style="width: 40%" />
    <col style="width: 40%" />
    <td style="text-align: center; background-color: #D0D0D0">Operation</td>
    <td style="text-align: center; background-color: #D0D0D0">TF1.15/ TF1 compat mode in TF2 <a href="#compatfootnote">[1]</a></td>
    <td style="text-align: center; background-color: #D0D0D0">TF2</td>
  </tr>
  <tr>
    <td>Loading / Inference</td>
    <td>
      Use either hub.load
    <pre style="font-size: 12px;" lang="python">m = hub.load(handle)
outputs = m(inputs)</pre>
      or hub.KerasLayer
      <pre style="font-size: 12px;" lang="python">m = hub.KerasLayer(handle)
outputs = m(inputs)</pre>
    </td>
    <td> Fully supported (<a href="https://www.tensorflow.org/hub/tf2_saved_model#using_savedmodels_from_tf_hub">complete TF2 SavedModel loading guide</a>). Use either hub.load
    <pre style="font-size: 12px;" lang="python">m = hub.load(handle)
outputs = m(inputs)</pre>
      or hub.KerasLayer
      <pre style="font-size: 12px;" lang="python">m = hub.KerasLayer(handle)
outputs = m(inputs)</pre>
    </td>
  </tr>
  <tr>
    <td>Fine-tuning</td>
    <td>
      Supported for a hub.KerasLayer used in  tf.keras.Model when trained with
      Model.fit() or trained in an Estimator whose model_fn wraps the Model per the <a href="https://www.tensorflow.org/guide/migrate#using_a_custom_model_fn">custom model_fn guide</a>.
      <br/><div style="font-style: italic; font-size: 14px;">
        Note: hub.KerasLayer <span style="font-weight: bold;">does not</span>
        fill in graph collections like the old tf.compat.v1.layers or hub.Module
        APIs did.
      </div>
    </td>
    <td>
      Fully supported (<a href="https://www.tensorflow.org/hub/tf2_saved_model#for_savedmodel_consumers">complete TF2 SavedModel fine-tuning guide</a>).
      Use either hub.load:
      <pre style="font-size: 12px;" lang="python">m = hub.load(handle)
outputs = m(inputs, training=is_training)</pre>
      or hub.KerasLayer:
      <pre style="font-size: 12px;" lang="python">m =  hub.KerasLayer(handle, trainable=True)
outputs = m(inputs)</pre>
    </td>
  </tr>
  <tr>
    <td>Creation</td>
    <td>
     The TF2 API <a href="https://www.tensorflow.org/api_docs/python/tf/saved_model/save">
      tf.saved_model.save()</a> can be called from within compat mode.
   </td>
   <td>Fully supported (see <a href="https://www.tensorflow.org/hub/tf2_saved_model#creating_savedmodels_for_tf_hub">complete TF2 SavedModel creation guide</a>) </td>
  </tr>
</table>

<p id="compatfootnote">[1] "TF1 compat mode in TF2" refers to the combined
  effect of importing TF2 with
  <code style="font-size: 12px;" lang="python">import tensorflow.compat.v1 as tf</code>
  and running
  <code style="font-size: 12px;" lang="python">tf.disable_v2_behavior()</code>
 as described in the
  <a href="https://www.tensorflow.org/guide/migrate">TensorFlow Migration guide
  </a>.</p>
