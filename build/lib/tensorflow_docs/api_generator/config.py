# Copyright 2015 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""The `ParserConfig` contains the information extracted by walking the API."""

class ParserConfig(object):
  """Stores all indexes required to parse the docs."""

  def __init__(
      self,
      *,
      reference_resolver,
      duplicates,
      duplicate_of,
      tree,
      index,
      reverse_index,
      path_tree,
      api_tree,
      base_dir,
      code_url_prefix,
      self_link_base
  ):
    """Object with the common config for docs_for_object() calls.

    Args:
      reference_resolver: An instance of ReferenceResolver.
      duplicates: A `dict` mapping fully qualified names to a set of all aliases
        of this name. This is used to automatically generate a list of all
        aliases for each name.
      duplicate_of: A map from duplicate names to preferred names of API
        symbols.
      tree: A `dict` mapping a fully qualified name to the names of all its
        members. Used to populate the members section of a class or module page.
      index: A `dict` mapping full names to objects.
      reverse_index: A `dict` mapping object ids to full names.
      path_tree: A PathTree datastructure to manage all the API paths.
      api_tree: A PathTree datastructure to manage all the API objects.
      base_dir: A base path that is stripped from file locations written to the
        docs.
      code_url_prefix: A Url to pre-pend to the links to file locations.
      self_link_base: A Url to pre-pend to self-links to the generated docs
        pages.
    """
    self.reference_resolver = reference_resolver
    self.duplicates = duplicates
    self.duplicate_of = duplicate_of
    self.tree = tree
    self.reverse_index = reverse_index
    self.index = index
    self.path_tree = path_tree
    self.api_tree = api_tree
    self.base_dir = base_dir
    self.code_url_prefix = code_url_prefix
    self.self_link_base = self_link_base

  def py_name_to_object(self, full_name):
    """Return the Python object for a Python symbol name."""
    return self.index[full_name]
