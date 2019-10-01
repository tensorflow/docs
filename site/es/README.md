# Documentacion de TensorFlow

## Traducciones de la Comunidad

Nuestra comunidad de Tensorflow ha traducido estos documentos. Como las traducciones de la comunidad
son basados en el "mejor esfuerzo", no hay ninguna garantia que esta sea un reflejo preciso y actual 
de la [Documentacion Oficial en Ingles](https://www.tensorflow.org/?hl=en).
Si tienen sugerencias sobre como mejorar esta traduccion, por favor envian un "Pull request"
al siguiente repositorio [tensorflow/docs](https://github.com/tensorflow/docs).
Para ofrecerse como voluntario o hacer revision de las traducciones de la Comunidad
por favor contacten al siguiente grupo [docs@tensorflow.org list](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs).

Note: Por favor enfoquen sus esfuerzos de traduccion en
[TensorFlow 2](https://www.tensorflow.org) que se encuentra en el siguiente
directorio. [site/en/](https://github.com/tensorflow/docs/tree/master/site/en/)
Documentos de la comunidad en la version TF 1.x ya no sera mantneida por ninguna
comunidad mientras se prepara para el lanzamiento de la version 2.0.

Por favor revisar [El Anuncio](https://groups.google.com/a/tensorflow.org/d/msg/docs/vO0gQnEXcSM/YK_ybv7tBQAJ).
Igualmente, p por favor no traduzcan la seccion de `install/`, cualquier archivo `*.yaml`, o archivo `index.md`.
Revisar [El Anuncio](https://groups.google.com/a/tensorflow.org/forum/#!msg/docs-zh-cn/mhLp-egzNyE/EhGSeIBqAQAJ).

Note: el siguiente directorio
[site/ko/swift](https://github.com/tensorflow/docs/tree/master/site/ko/swift)
es el "Home" para las traducciones
[Swift para Tensorflow](https://www.tensorflow.org/swift)(S4TF).
Los archivos originales estan en el directorio
[docs/site](https://github.com/tensorflow/swift/tree/master/docs/site) del repositorio 
tensorflow/swif. Los "notebooks" S4TF deben tener los resultados guardados.

## Community translations

Our TensorFlow community has translated these documents. Because community
translations are *best-effort*, there is no guarantee that this is an accurate
and up-to-date reflection of the
[official English documentation](https://www.tensorflow.org/?hl=en).
If you have suggestions to improve this translation, please send a pull request 
to the [tensorflow/docs](https://github.com/tensorflow/docs) GitHub repository. 
To volunteer to write or review community translations, contact the
[docs@tensorflow.org list](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs).

Note: Please focus translation efforts on
[TensorFlow 2](https://www.tensorflow.org) in the
[site/en/r2](https://github.com/tensorflow/docs/tree/master/site/en/r2)
directory. TF 1.x community docs will no longer be updated as we prepare for the
2.0 release. See
[the announcement](https://groups.google.com/a/tensorflow.org/d/msg/docs/vO0gQnEXcSM/YK_ybv7tBQAJ).
Also, please do not translate the `install/` section, any `*.yaml` files, or `index.md` files.
See [the announcement](https://groups.google.com/a/tensorflow.org/forum/#!msg/docs-zh-cn/mhLp-egzNyE/EhGSeIBqAQAJ).

Note: The
[site/es/swift](https://github.com/tensorflow/docs/tree/master/site/es/swift)
directory is the home for
[Swift for TensorFlow](https://www.tensorflow.org/swift)(S4TF) translations.
Original files are in the
[docs/site](https://github.com/tensorflow/swift/tree/master/docs/site) directory
of the tensorflow/swift repository. S4TF notebooks must have the outputs saved.

## Para nuevos contribuidores

Muchas gracias por unirse a el esfuerzo de traduccion!
Por favor lean los documentos existentes en
[Es documentos](https://github.com/tensorflow/docs/tree/master/site/es)
Antes de comenzar su traduccion.
Por favor no utilicen coloquismos como Guey, Parcero, Ueon, Che o palabras Soeces.
No agregar acentos, dieresis o tildes ya que pueden afectar la ejecucion de los codigos.
Sigan el estilo de los documentos lo mas posible.

Una vez la traduccion este completa por favor notifiquen a los contribuidores
[Contribuidores en Espanol de Documentacion en TensorFlow ](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs)
para coordinar la traduccion.

Copien un archivo en el folder `es` desde el folder `en`, asegurensen que el directorio de folders sea el adecuado.
`site/es/r1` es para TensorFlow 1.x.
`site/es/` es para TensorFlow 2.x.

Deben traducir los comentarios y los "Markdowns" no deben correr las celdas.
La estructura de Archivos y folders no debe ser cambiado esto dificulta la revision en GitHub.
Usen un editor de texto para editar "Jupyter Notebooks".
Prueben el "Notebook" en su repositorio con Colab luego de que terminen la traduccion para comprobar.
Pueden pedir revision si no hay ningun error.

Si tienen alguna pregunta sobre traducciones, por favor envien un mensaje a
[Contribuidores en Espanol de Documentacion en TensorFlow ](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs)

Gracias!

## For new contributors

Thanks for joining the translation effort.
Please read the existing
[ES documents](https://github.com/tensorflow/docs/tree/master/site/es)
before starting your translation.
Do not use country Coloquialisms.
Follow the style of existing documents, as possible as you can.

After your translation is complete, notify the
[Spanish TensorFlow Documentation Contributors](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs)
mailing list to coordinate a review.

Copy a file in `en` folder to same location under `ko` folder if anybody doesn't work on the file,
and get it start.
`site/es/r1` are for TensorFlow 1.x.
`site/es/` are for TensorFlow 2.x.

You should translate markdown and comments. You should not run code cells.
Whole file structure can be changed even if you modify only a chunk in the notebook.
It is hard to review such a file in GitHub.
You should use a text editor when you edit a few words of existing notebook.
You should test the notebook in your repository with Colab after you finish the translation.
You can request for review if there is no error.

If you have any question about translation, feel free to contact
[Spanish TensorFlow Documentation Contributors](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs)
mailing list.

Thanks!

## Guia de Traduccion en Espanol/Spanish translation guide

Algunas palabras Tecnicas en ingles no tienen una traduccion natural al Espanol por favor *NO*
traduzcan las siguientes palabras.

*   mini-batch
*   batch
*   label
*   class
*   helper
*   hyperparameter
*   optimizer
*   one-hot encoding
*   epoch
*   callback
*   sequence
*   dictionary (in python)
*   embedding
*   padding
*   unit
*   node
*   neuron
*   target
*   checkpoint
*   compile
*   dropout
*   penalty
*   eager execution 
*   eagerly
