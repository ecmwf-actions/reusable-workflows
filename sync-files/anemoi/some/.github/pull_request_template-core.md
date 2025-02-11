{% extends "sync-files/anemoi/all/.github/pull_request_template.md" %}

{% block testing %}
-   [ ] I have tested the changes on a single GPU
-   [ ] I have tested the changes on multiple GPUs / multi-node setups
-   [ ] I have run the Benchmark Profiler against the old version of the code
-   [ ] If the new feature introduces modifications at the config level, I have made sure to update Pydantic Schemas and default configs accordingly

{% endblock %}

{% block documentation %}
{% endblock %}

{% block dependencies %}
-   [ ] I have not introduced new dependencies in the inference portion of the pipeline
{% endblock %}
