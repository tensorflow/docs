# Неофициальный перевод

Вся информация в этом разделе переведена с помощью русскоговорящего Tensorflow
сообщества на общественных началах. Поскольку этот перевод не является
официальным, мы не гарантируем что он на 100% аккуратен и соответствует
[официальной документации на английском языке](https://www.tensorflow.org/?hl=en).
Если у вас есть предложение как исправить этот перевод, мы будем очень рады
увидеть pull request в [tensorflow/docs](https://github.com/tensorflow/docs)
репозиторий GitHub. Если вы хотите помочь сделать документацию по Tensorflow
лучше (сделать сам перевод или проверить перевод подготовленный кем-то другим),
напишите нам на
[docs-ru@tensorflow.org list](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-ru).

# Community translations

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

# Как добавить свой перевод?

1. Ознакомьтесь с [уже имеющейся документацией на русском языке](https://github.com/tensorflow/docs/tree/master/site/ru)
2. Внесите правки в уже готовый перевод или [выберите еще не переведенный в папке site/en/](https://github.com/tensorflow/docs/tree/master/site/en)
3. Переводите на русский язык блоки основные текста документации, а также поясняющие комментарии в коде

Обратите внимание: документы, которые начинаются с символа нижнего подчеркивания (например, `_style_transfer.ipynb`) все еще находятся в процессе работы и пока не импортируются на [tensorflow.org](https://www.tensorflow.org/)

Смотрите хороший пример переведенного нами [урока по TensorFlow Keras API здесь](https://github.com/tensorflow/docs/blob/master/site/ru/tutorials/keras/basic_classification.ipynb).

# Советы

1. Не стесняйтесь добавлять не полностью переведенные документации: таким образом другие участники смогут увидеть ваш Pull Request и помочь если требуется
2. Вы также можете [создать черновик (Draft)](https://help.github.com/en/articles/about-pull-requests#draft-pull-requests) для будущего Pull Request. Таким образом вы сможете добавлять изменения, не уведомляя владельца репозитария: это удобно для работы над крупными текстами
3. Используйте комментарии TODO или IMPROVE в тексте и коде в тех местах, где можно объяснить код или операцию более понятным языком, но вы пока не знаете как (это позволит другим переводчикам помочь вам с толкованием)
4. Проверьте основные моменты [Google Developer Documentation Style Guide](https://developers.google.com/style/highlights): это поможет вам с переводом и проверкой технической документации и уроков

# Russian translation guide

Some technical words in English do not have a natural translation. Do *not*
translate the following words:

*   (mini-) batch
*   estimator
*   eager execution
*   dense
*   dropout
