{% extends "sync-files/anemoi/all/.github/pull_request_template.md" %}

{% block testing %}
-   [ ] I have tested the changes on a single GPU
-   [ ] I have tested the changes on multiple GPUs / multi-node setups
-   [ ] I have run the [Benchmark Profiler](https://anemoi.readthedocs.io/projects/training/en/latest/user-guide/benchmarking.html) against the old version of the code

{% endblock %}

{% block documentation %}
{% endblock %}

{% block dependencies %}
-   [ ] I have not introduced new dependencies in the inference portion of the pipeline
{% endblock %}
