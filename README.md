# reusable-workflows

[![Build Status](https://img.shields.io/github/workflow/status/ecmwf-actions/reusable-workflows/test)](https://github.com/ecmwf-actions/reusable-workflows/actions/workflows/test.yml)
[![Licence](https://img.shields.io/github/license/ecmwf-actions/reusable-workflows)](https://github.com/ecmwf-actions/reusable-workflows/blob/main/LICENSE)

A collection of [reusable GitHub workflows] for ECMWF repositories.

> **NOTE:**  
> Reusable workflows are currently in beta and subject to change. It is strongly advised NOT to use these workflows in production yet, as they can stop working at any time.

## Workflows

* [ci.yml](#ciyml): Continuous Integration workflow for ecbuild/CMake-based projects
* [ci-python.yml](#ci-pythonyml): Continuous Integration and Continuous Deployment workflow for Python-based projects
* [ci-node.yml](#ci-nodeyml): Continuous Integration workflow for NodeJS-based projects
* [docs.yml](#docsyml): Workflow for testing Sphinx-based documentation

[Samples]

## Supported Operating Systems

* Linux
* macOS

## ci.yml

### Usage

```yaml
jobs:

  # Calls a reusable CI workflow to build & test current repository.
  #   It will pull in all needed dependencies and produce a code coverage report on success.
  #   In case the job fails, a message will be posted to a Microsoft Teams channel.
  ci:
    name: ci
    uses: ecmwf-actions/reusable-workflows/.github/workflows/ci.yml@main
    with:
      codecov_upload: true
      notify_teams: true
      build_package_inputs: |
        dependencies: |
          ecmwf/ecbuild
          ecmwf/eckit
        dependency_branch: develop
    secrets:
      incoming_webhook: ${{ secrets.MS_TEAMS_INCOMING_WEBHOOK }}
```

### Inputs

#### `skip_matrix_jobs`

A list of matrix jobs to skip. Job names should be the full form of `<compiler>@<platform>`.  
**Default:** `''`  
**Type:** `string`

#### `deps_cache_key`

Dependency cache key to restore from. Note that the key should be platform agnostic, as the `<compiler>@<platform>` suffix will be automatically appended. Upon extraction, a file called `.env` from the cache root directory will be loaded into the build environment, if it exists.  
**Default:** `''`  
**Type:** `string`

#### `deps_cache_path`

Optional dependency cache path to restore to, falls back to `${{ runner.temp }}/deps`. Will be considered only if [deps_cache_key](#deps_cache_key) is supplied.  
**Default:** `''`  
**Type:** `string`

#### `codecov_upload`

Whether to generate and upload code coverage to [codecov service] for main branches.  
**Default:** `false`  
**Type:** `boolean`

#### `notify_teams`

Whether to notify about workflow status via Microsoft Teams. Note that you must supply [incoming_webhook](#incoming_webhook) secret if you switch on this feature.  
**Default:** `false`  
**Type:** `boolean`

#### `repository`

The source repository name, in case it differs from the current one. Repository names should follow the standard Github `owner/name` format.  
**Default:** `${{ github.repository }}`  
**Type:** `string`

#### `ref`

The source repository reference, in case it differs from the current one.  
**Default:** `${{ github.ref }}`  
**Type:** `string`

#### `build_package_inputs`

Optional [inputs for the build-package] action, provided as a YAML object value.  
**Default:** `''`  
**Type:** `string`

### Secrets

#### `incoming_webhook`

Public URL of the Microsoft Teams incoming webhook. To get the value, make sure that channel in Teams has the appropriate connector set up. It will only be used if [notify_teams](#notify_teams) input is switched on.  
**Example:** `https://webhook.office.com/webhookb2/...`

## ci-python.yml

### Usage

```yaml
jobs:

  # Calls a reusable CI workflow to qa, test & deploy the current repository.
  #   It will pull in all needed dependencies and produce a code coverage report on success.
  #   If all checks were successful and a new release tag pushed, the package will be published on PyPI.
  #   In case the job fails, a message will be posted to a Microsoft Teams channel.
  ci:
    name: ci
    uses: ecmwf-actions/reusable-workflows/.github/workflows/ci-python.yml@main
    with:
      codecov_upload: true
      notify_teams: true
      build_package_inputs: |
        dependencies: |
          ecmwf/ecbuild
          ecmwf/eckit
          ecmwf/odc
        dependency_branch: develop
        self_build: false
    secrets:
      pypi_username: ${{ secrets.PYPI_USERNAME }}
      pypi_password: ${{ secrets.PYPI_PASSWORD }}
      incoming_webhook: ${{ secrets.MS_TEAMS_INCOMING_WEBHOOK }}
```

### Inputs

#### `skip_matrix_jobs`

A list of matrix jobs to skip. Job names should be the full form of `<compiler>@<platform>`.  
**Default:** `''`  
**Type:** `string`

#### `codecov_upload`

Whether to generate and upload code coverage to [codecov service] for main branches.  
**Default:** `false`  
**Type:** `boolean`

#### `notify_teams`

Whether to notify about workflow status via Microsoft Teams. Note that you must supply [incoming_webhook](#incoming_webhook-1) secret if you switch on this feature.  
**Default:** `false`  
**Type:** `boolean`

#### `python_version`

The version of Python binary to use.  
**Default:** `'3.9'`  
**Type:** `ring`

#### `repository`

The source repository name. Repository names should follow the standard Github `owner/name` format.  
**Default:** `${{ github.repository }}`  
**Type:** `string`

#### `ref`

The source repository reference.  
**Default:** `${{ github.ref }}`  
**Type:** `string`

#### `build_package_inputs`

Optional [inputs for the build-package] action, provided as a YAML object value.  
**Default:** `''`  
**Type:** `string`

### Secrets

#### `pypi_username`

Username of the PyPI account. The account must have sufficient permissions to deploy the current project.  
**Example:** `MyUsername`

#### `pypi_password`

Password of the PyPI account.  
**Example:** `MyPassword`

#### `incoming_webhook`

Public URL of the Microsoft Teams incoming webhook. To get the value, make sure that channel in Teams has the appropriate connector set up. It will only be used if [notify_teams](#notify_teams-1) input is switched on.  
**Example:** `https://webhook.office.com/webhookb2/...`

## ci-node.yml

### Usage

```yaml
jobs:

  # Calls a reusable CI NodeJS workflow to qa & test & deploy the current repository.
  #   It will install dependencies and produce a code coverage report on success.
  #   In case the job fails, a message will be posted to a Microsoft Teams channel.
  ci:
    name: ci
    uses: ecmwf-actions/reusable-workflows/.github/workflows/ci-node.yml@main
    with:
      codecov_upload: true
      notify_teams: true
    secrets:
      incoming_webhook: ${{ secrets.MS_TEAMS_INCOMING_WEBHOOK }}
```

### Inputs

#### `skip_matrix_jobs`

A list of matrix jobs to skip. Job names should be the form of `<platform>`.  
**Default:** `''`  
**Type:** `string`

#### `codecov_upload`

Whether to generate and upload code coverage to [codecov service] for main branches.  
**Default:** `false`  
**Type:** `boolean`

#### `notify_teams`

Whether to notify about workflow status via Microsoft Teams. Note that you must supply [incoming_webhook](#incoming_webhook-2) secret if you switch on this feature.  
**Default:** `false`  
**Type:** `boolean`

#### `node_version`

The version of NodeJS interpreter to use.
**Default:** `'12'`  
**Type:** `boolean`

#### `repository`

The source repository name. Repository names should follow the standard Github `owner/name` format.  
**Default:** `${{ github.repository }}`  
**Type:** `string`

#### `ref`

The source repository reference.  
**Default:** `${{ github.ref }}`  
**Type:** `string`

### Secrets

#### `incoming_webhook`

Public URL of the Microsoft Teams incoming webhook. To get the value, make sure that channel in Teams has the appropriate connector set up. It will only be used if [notify_teams](#notify_teams-2) input is switched on.  
**Example:** `https://webhook.office.com/webhookb2/...`

## docs.yml

### Usage

```yaml
jobs:

  # Calls a reusable CI workflow to build & check the documentation in the current repository.
  #   It will install required system dependencies and test Read the Docs build process.
  docs:
    name: docs
    uses: ecmwf-actions/reusable-workflows/.github/workflows/docs.yml@main
    with:
      system_dependencies: doxygen pandoc
```

### Inputs

#### `requirements_path`

Path of the `requirements.txt` file which includes all dependencies needed for building of the documentation, relative to the repository root.  
**Default:** `docs/requirements.txt`  
**Type:** `string`

#### `docs_path`

Path of the documentation directory, relative to the repository root.  
**Default:** `docs`  
**Type:** `string`

#### `system_dependencies`

Optional list of system dependencies to install via `apt` command, separated by spaces. Note that each dependency must be available via standard Ubuntu 20.04 package repositories.  
**Default:** `''`  
**Type:** `string`

#### `python_version`

The version of Python binary to use.  
**Default:** `'3.9'`  
**Type:** `ring`

#### `repository`

The source repository name, in case it differs from the current one. Repository names should follow the standard Github `owner/name` format.  
**Default:** `${{ github.repository }}`  
**Type:** `string`

#### `ref`

The source repository reference, in case it differs from the current one.  
**Default:** `${{ github.ref }}`  
**Type:** `string`

## Licence

This software is licensed under the terms of the Apache License Version 2.0 which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.

In applying this licence, ECMWF does not waive the privileges and immunities granted to it by virtue of its status as an intergovernmental organisation nor does it submit to any jurisdiction.

[reusable GitHub workflows]: https://docs.github.com/en/actions/learn-github-actions/reusing-workflows
[Samples]: https://github.com/ecmwf-actions/reusable-workflows/tree/main/samples
[codecov service]: https://codecov.io
[inputs for the build-package]: https://github.com/ecmwf-actions/build-package#inputs