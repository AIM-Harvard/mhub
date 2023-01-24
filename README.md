# Medical Imaging Model Hub (MHub)

Making machine learning models for medical imaging available through a standardized I/O framework.


MHub is still being developed, so bear with us if some functionalities are still not implemented or to be improved. MHub is developed by researchers for researchers, and thus we welcome and appreciate any feedback that can help improve the platform (so feel free to [open an Issue on GitHub](https://github.com/AIM-Harvard/mhub/issues/new) with your suggestions).

# Table of Contents
- [About MHub](#about-mhub-)
- [Installation](#installation)
  -[Windows](#install-on-windows)
  -[Linux](#install-on-linux)
- [Usage](#usage)
  - [Command-line Interface (CLI)](#running-mhub-containers-from-cli)
  - [3D Slicer](#integration-with-3dslicer)
- [Contributing to MHub](#contributing-to-mhub)
- [Known Issues](#known-issues)

# About MHub 🤖🏥🐳

MHub is a repository of self-contained deep learning models pretrained for a wide variety of applications in the medical imaging domain. MHub highlights recent trends in deep learning applications and promotes reproducible science, empowering AI researchers to share fully reproducible and portable model implementations.

**MHub models are:**

- **Peer-reviewed.** All the models in MHub are accompanied by peer-reviewed studies published in scientific journals. Integrating MHub models in your analysis pipelines means integrating AI models which results are backed by published studies.

- **Framework-agnostic.** As MHub is built using Docker, by nature it is framework agnostic and supports all numerical computing backends. Packaging a model in MHub means providing the community with a tool that will work out of the box as intended by the developers.

- **Documented and tested.** Together with the models, we provide instructions on how to run the containers on your system and example use-cases of our models running on the cloud on publicly available data from [The Imaging Data Commons](https://portal.imaging.datacommons.cancer.gov/).

# Installation

MHub is based on Docker, which is a platform and technology that allows developers to package their applications and all their dependencies into portable containers, making it easy to deploy and run on any machine that supports Docker.

Therefore, as long as the node has Docker installed, MHub models can run anywhere - on a laptop, on a research workstation in a hospital, on a research server or in the cloud.

## Install on Linux 

To install docker on Linux, you can follow Docker's official documentation at:

https://docs.docker.com/desktop/install/linux-install/

There are also plenty of unofficial guided tutorials on the internet depending on OS you are running. Most likely, installing Docker from scratch will take a basic understanding of the terminal, a few instructions and a few minutes.

Alternatively, the user can also install Docker Desktop following the OS-specific guide found at the webpage linked above. 

For instance, for systems running Ubuntu:

https://docs.docker.com/desktop/install/ubuntu/

> Docker Desktop includes the Docker daemon (dockerd), the Docker client (docker), Docker Compose, Docker Content Trust, Kubernetes, and Credential Helper.


## Install on Windows

To install docker on Windows, please follow Docker's official documentation at:

https://docs.docker.com/desktop/install/windows-install/

Please, note that:

> While Docker Desktop on Windows can be run without having Administrator privileges, it does require them during installation. On installation the user gets a UAC prompt which allows a privileged helper service to be installed. After that, Docker Desktop can be run by users without administrator privileges, provided they are members of the docker-users group. The user who performs the installation is automatically added to this group, but other users must be added manually. This allows the administrator to control who has access to Docker Desktop.

# Usage

## Running MHub Containers from CLI

<Some examples of how to build and pull MHub containers and run them>

## Integration with 3D Slicer

Link and short explanation of the 3D Slicer plug-in:

https://github.com/AIM-Harvard/SlicerMHubRunner

# Contributing to MHub

We want to make MHub crowdsourced through contributions by the scientific research community.

We are in the process of developing tools to allow researchers and developers to contribute to MHub with the models they developed.

# Known Issues

## Docker Support of Machines with AppleSilicon (e.g., M1 Processors)

<Document the M1 issue here>
