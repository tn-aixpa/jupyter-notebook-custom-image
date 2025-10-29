# Jupyter Notebook Custom Image

[![license](https://img.shields.io/badge/license-Apache%202.0-blue)](https://github.com/scc-digitalhub/digitalhub-core/LICENSE) ![GitHub Release](https://img.shields.io/github/v/release/scc-digitalhub/jupyter-notebook-custom-image)
![Status](https://img.shields.io/badge/status-stable-gold)

Jupyter Notebook custom image used in Digitalhub Platform.

## Configuration

Dockerfile parameters can be set to customize the image. Parameters refers to PYPI package versions of [SDK](https://github.com/scc-digitalhub/digitalhub-sdk) and related runtimes. The following parameters are available:

- `ver_sdk`: Version of the SDK to use.
- `ver_python`: Version of the python runtime to use.
- `ver_container`: Version of the container runtime to use.
- `ver_modelserve`: Version of the model serving runtime to use.
- `ver_dbt`: Version of the dbt runtime to use.
- `ver_kfp`: Version of the kfp runtime to use.

## Development

See CONTRIBUTING for contribution instructions.

### Build container images

To build the container image, you need to have Docker installed. Use the following command to build the image:

```bash
docker build -t jupyter-notebook-custom:3.[VERSION] -f Dockerfile-3-[VERSION] .
```

### Launch container

To run the container, use the following command:

```bash
docker run -p 8888:8888 jupyter-notebook-custom:3.[VERSION]
```

Once started, the container will output a URL with a token that you can use to access the Jupyter notebook interface in your browser.

## Security Policy

The current release is the supported version. Security fixes are released together with all other fixes in each new release.

If you discover a security vulnerability in this project, please do not open a public issue.

Instead, report it privately by emailing us at digitalhub@fbk.eu. Include as much detail as possible to help us understand and address the issue quickly and responsibly.

## Contributing

To report a bug or request a feature, please first check the existing issues to avoid duplicates. If none exist, open a new issue with a clear title and a detailed description, including any steps to reproduce if it's a bug.

To contribute code, start by forking the repository. Clone your fork locally and create a new branch for your changes. Make sure your commits follow the [Conventional Commits v1.0](https://www.conventionalcommits.org/en/v1.0.0/) specification to keep history readable and consistent.

Once your changes are ready, push your branch to your fork and open a pull request against the main branch. Be sure to include a summary of what you changed and why. If your pull request addresses an issue, mention it in the description (e.g., “Closes #123”).

Please note that new contributors may be asked to sign a Contributor License Agreement (CLA) before their pull requests can be merged. This helps us ensure compliance with open source licensing standards.

We appreciate contributions and help in improving the project!

## Authors

This project is developed and maintained by **DSLab – Fondazione Bruno Kessler**, with contributions from the open source community. A complete list of contributors is available in the project’s commit history and pull requests.

For questions or inquiries, please contact: [digitalhub@fbk.eu](mailto:digitalhub@fbk.eu)

## Copyright and license

Copyright © 2025 DSLab – Fondazione Bruno Kessler and individual contributors.

This project is licensed under the Apache License, Version 2.0.
You may not use this file except in compliance with the License. Ownership of contributions remains with the original authors and is governed by the terms of the Apache 2.0 License, including the requirement to grant a license to the project.
