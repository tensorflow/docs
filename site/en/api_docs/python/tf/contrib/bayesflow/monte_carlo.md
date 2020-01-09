page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.contrib.bayesflow.monte_carlo


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/bayesflow/python/ops/monte_carlo.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Monte Carlo integration and helpers.

<!-- Placeholder for "Used in" -->

Use [tfp.monte_carlo](/probability/api_docs/python/tfp/monte_carlo) instead.

## Functions

[`expectation(...)`](../../../tf/contrib/bayesflow/monte_carlo/expectation): Computes the Monte-Carlo approximation of \\(E_p[f(X)]\\). (deprecated)

[`expectation_importance_sampler(...)`](../../../tf/contrib/bayesflow/monte_carlo/expectation_importance_sampler): Monte Carlo estimate of \\(E_p[f(Z)] = E_q[f(Z) p(Z) / q(Z)]\\).

[`expectation_importance_sampler_logspace(...)`](../../../tf/contrib/bayesflow/monte_carlo/expectation_importance_sampler_logspace): Importance sampling with a positive function, in log-space.
