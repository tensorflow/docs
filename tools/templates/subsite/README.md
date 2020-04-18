# Subsite projects

Subsite projects are sections of the
[tensorflow.org](https://www.tensorflow.org) website that *do not* live in the
[tensorflow/docs](https://github.com/tensorflow/docs) repo. Instead, the project
docs live with the code in the project repo. Some example subsites:

* [TensorFlow Probability](https://www.tensorflow.org/probability/)
  [[tensorflow/probability](https://github.com/tensorflow/probability)]
* [TensorFlow Serving](https://www.tensorflow.org/serving/)
  [[tensorflow/serving](https://github.com/tensorflow/serving)]

Documentation changes are submitted to the project repo and *not* the
tensorflow/docs repo. Guides can be Markdown files or Colab/Jupyter notebooks.

## Set up the base template for the subsite project

1. Copy the `tools/templates/subsite/g3doc` directory from the docs repo to the
   project repo:

   ```
   $ cp -r tensorflow/docs/tools/templates/subsite/g3doc tensorflow/myproject/
   ```

	In GitHub, you may rename the project's `/g3doc` directory to `/docs`.

2. In the project's `g3doc/` directory, replace `PROJECT_NAME` in each template
   file with the *short name* of the project. This is used for the project URL,
   for example, `https://www.tensorflow.org/myproject`:

   ```
   $ find tensorflow/myproject/g3doc/ -type f | xargs sed -i 's/PROJECT_NAME/myproject/g'
   ```

## Update the configuration files

1. The `_book.yaml` file configures the lower tabs and left navigation for
   files. Each page must have an entry in `_book.yaml` to be navigable on
   [tensorflow.org](https://www.tensorflow.org).
2. The TensorFlow docs team must set up a project file.

Changes to `.yaml` files must be approved by the TensorFlow docs team.



## Set up the API generator for reference docs

To build reference docs for the project, write a `build_docs.py` script using the
[api_generator](https://github.com/tensorflow/docs/tree/master/tools/tensorflow_docs/api_generator)
API. The best way to do this is to look at examples from other subsite projects.

If the project does not have an API reference, remove this navigation section
from the `_book.yaml` file.

## Create a link to your project docs

To make it easier for contributors to find your doc set, add a project entry to
[tensorflow/docs/site/en](https://github.com/tensorflow/docs/blob/master/g3doc/en/)
and include a `README.md` file with a link. For example,
[site/en/probability/](https://github.com/tensorflow/docs/blob/master/g3doc/en/probability/).
