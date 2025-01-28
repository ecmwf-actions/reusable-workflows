{% extends "sync-files/anemoi/.github/PULL_REQUEST_TEMPLATE/pull_request_template.md" %}

{% block testing %}
-   [ ] I have tested the changes on a single GPU
-   [ ] I have tested the changes on multiple GPUs / multi-node setups
-   [ ] I have run the Benchmark Profiler against the old version of the code
{% endblock %}

{% block dependencies %}
-   [ ] I have not introduced new dependencies in the inference portion of the pipeline
{% endblock %}
