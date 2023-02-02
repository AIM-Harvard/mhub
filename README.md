# Medical Imaging Model Hub (MHub)

Making machine learning models for medical imaging available through a standardized I/O framework.

MHub is still being developed, so bear with us if some functionalities are still not implemented or to be improved. MHub is developed by researchers for researchers, and thus we welcome and appreciate any feedback that can help improve the platform (so feel free to [open an Issue on GitHub](https://github.com/AIM-Harvard/mhub/issues/new) with your suggestions).

To learn more about our vision, you can check the presentation we gave at the [38th NA-MIC Project Week](https://projectweek.na-mic.org/PW38_2023_GranCanaria/) at [this link](https://docs.google.com/presentation/d/1UoI74RaTDinsKoTQEA46bAs62bgOmeikKwiFi0GGq0A/edit?usp=sharing).

If you want to give a quick try to MHub or to our 3D Slicer plug-in, you can do so in **less than five minutes** by reading our guide to the [MHub CLI quickstart](#running-mhub-containers-from-cli) and to the [MHub 3D Slicer plugin quick setup](#integration-with-3d-slicer). 


# Table of Contents
- [About MHub](#about-mhub-)
- [Installation](#installation)
  - [Windows](#install-docker-on-windows)
  - [Linux](#install-docker-on-linux)
- [Usage](#usage)
  - [Command-line Interface (CLI)](#running-mhub-containers-from-cli)
  - [3D Slicer](#integration-with-3d-slicer)
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

## Install Docker on Linux 

To install docker on Linux, you can follow Docker's official documentation at:

https://docs.docker.com/desktop/install/linux-install/

There are also plenty of unofficial guided tutorials on the internet depending on OS you are running. Most likely, installing Docker from scratch will take a basic understanding of the terminal, a few instructions and a few minutes.

Alternatively, the user can also install Docker Desktop following the OS-specific guide found at the webpage linked above. 

For instance, for systems running Ubuntu:

https://docs.docker.com/desktop/install/ubuntu/

> Docker Desktop includes the Docker daemon (dockerd), the Docker client (docker), Docker Compose, Docker Content Trust, Kubernetes, and Credential Helper.

## Install Docker on Windows

To install docker on Windows, please follow Docker's official documentation at:

https://docs.docker.com/desktop/install/windows-install/

Please, note that:

> While Docker Desktop on Windows can be run without having Administrator privileges, it does require them during installation. On installation the user gets a UAC prompt which allows a privileged helper service to be installed. After that, Docker Desktop can be run by users without administrator privileges, provided they are members of the docker-users group. The user who performs the installation is automatically added to this group, but other users must be added manually. This allows the administrator to control who has access to Docker Desktop.

# Usage

## Running MHub Containers from CLI

### Pulling Containers from Dockerhub

All the MHub images are multi-platform whenever possible, and [made available through Dockerhub](https://hub.docker.com/repositories/mhubai). Since pulling images from Dockerhub is considerably faster than building images on your system, we advise you do so if you don't have platform-related issues.

Assuming you want to try the `totalsegmentator` container with CUDA (v12.0) support (`mhubai/totalsegmentator:cuda12.0`), and the DICOM Series you want to process is stored at `$ABS_PATH_TO_DICOM_SERIES_FOLDER` (absolute path!), you want to store the output of the model at `$ABS_PATH_TO_OUTPUT_FOLDER` (absolute path!), and you want to use whatever GPU is available on your system (`--gpu all`), you can run:

```
docker run \
--volume $ABS_PATH_TO_DICOM_SERIES_FOLDER:/app/data/input_data \
--volume $ABS_PATH_TO_OUTPUT_FOLDER:/app/data/output_data
--gpus all \
mhubai/totalsegmentator:cuda12.0
```

Here follows an example how to populate the variables above. In this case, the entire pipeline (DICOM to DICOM SEG) - including the pull of the CUDA-accelrated docker container - took less than three minutes to run (on a Desktop PC equipped with a TITAN RTX, an AMD Ryzen 7 3800X, and 64GB of RAM):

```
time docker run \
  --volume /home/dennis/Desktop/sample_data/input_dcm:/app/data/input_data \
  --volume /home/dennis/Desktop/sample_data/output_data/totalsegmentator:/app/data/output_data \
  --gpus all mhubai/totalsegmentator:cuda12.0

> Unable to find image 'mhubai/totalsegmentator:nocuda' locally
> nocuda: Pulling from mhubai/totalsegmentator
> 846c0b181fff: Pull complete 
c9c6540f8dd7: Pull complete 
...
> cf5d6d5df729: Pull complete 
> Digest: sha256:4ce05edbc1b79ce805e7d718a3888f944439b5ed317cff497ceff9b72317532e
> Status: Downloaded newer image for mhubai/totalsegmentator:nocuda
> 100%|██████████| 139/139 [00:00<00:00, 823.41it/s]Files sorted

> If you use this tool please cite: https://doi.org/10.48550/arXiv.2208.05868

> Using 'fast' option: resampling to lower resolution (3mm)
> Resampling...
>   Resampled in 1.79s
> Predicting...
>   Predicted in 3.89s
> Resampling...
> Saving segmentations...
> 100%|██████████| 104/104 [00:05<00:00, 20.72it/s]
>   Saved in 6.07s

> --------------------------
> Start UnsortedInstanceImporter
> Done in 2.69413e-05 seconds.

> --------------------------
> Start DataSorter
> sorting schema: /app/data/sorted/%SeriesInstanceUID/dicom/%SOPInstanceUID.dcm
> ['dicomsort', '-k', '-u', '/app/data/input_data', '/app/data/sorted/%SeriesInstanceUID/dicom/%SOPInstanceUID.dcm']
> Done in 0.394417 seconds.

> --------------------------
> Start NiftiConverter

> Running 'plastimatch convert' with the specified arguments:
>   --input /app/data/sorted/1.2.826.0.1.3680043.8.498.99748665631895691356693177610672446391/dicom
>   --output-img /app/data/sorted/1.2.826.0.1.3680043.8.498.99748665631895691356693177610672446391/image.nii.gz
> ... Done.
> Done in 10.9903 seconds.

> --------------------------
> Start TotalSegmentatorRunner
> Running TotalSegmentator in fast mode ('--fast', 3mm): 
> >> run ts:  ['TotalSegmentator', '-i', '/app/data/sorted/1.2.826.0.1.3680043.8.498.99748665631895691356693177610672446391/image.nii.gz', '-o', > '/app/tmp/b5f0e986-4370-4560-a6fe-63e1f4a0ccc5', '--fast']
> Done in 15.8204 seconds.

> --------------------------
> Start DsegConverter
...
> Done in 18.1758 seconds.

> --------------------------
> Start DataOrganizer
> organizing instance <I:/app/data/sorted/1.2.826.0.1.3680043.8.498.99748665631895691356693177610672446391>
> created directory /app/data/output_data/1.2.826.0.1.3680043.8.498.99748665631895691356693177610672446391
> Done in 0.0676122 seconds.

> real	2m58,528s
> user	0m0,110s
> sys	0m0,053s
```

Since the `mhubai/totalsegmentator:cuda12.0` container will now be stored in your system, new runs will likely take around 30 seconds.

### Building Containers Locally

If for some specific reason (e.g., platform compatibility) you would like to build the MHub containers locally, you can do so in a couple of very simple steps.

First, `cd` in the directory storing the dockerfile of the container you're interested to. The MHub containers are provided both without CUDA support (`nocuda`) and with CUDA support (`cudaXX.X`, .e.g, `cuda12.0`) whenever possible:

```
cd git/mhub/mhub/totalsegmentator/dockerfiles/nocuda
```

Once you find yourself in the correct directory, you can build the container by simply running:

```
docker build . --no-cache --tag $CONTAINER_NAME
```

If you want to [specify the platform to build for](https://docs.docker.com/build/building/multi-platform/), you're free to do so using the `--platform` argument.

You will now be able to run the container as explained in the "Pulling Containers from Dockerhub" section above.

## Integration with 3D Slicer

You can find instructions regarding how to install our 3D Slicer plug-in in less than five minutes at the following repository:

https://github.com/AIM-Harvard/SlicerMHubRunner


# Contributing to MHub

We want to make MHub crowdsourced through contributions by the scientific research community.

We are in the process of developing tools to allow researchers and developers to contribute to MHub with the models they developed.

# Known Issues

## Docker Support of Machines with AppleSilicon (e.g., M1 Processors)

The users building Docker containers on Apple Silicon devices still face some issues, as documented in many blogposts all over the web.

For instance, some packages might not have an available candidate for installation if you try to build a Linux-based Docker image on an M1 macbook:

```
# build the mhubai base image without CUDA support
cd git/mhub/mhub/dockerfiles/nocuda

[+] Building 3.9s (7/18)                                                                                
 => [internal] load build definition from Dockerfile                                               0.0s
 => => transferring dockerfile: 37B                                                                0.0s
 => [internal] load .dockerignore                                                                  0.0s
 => => transferring context: 2B                                                                    0.0s
 => [internal] load metadata for docker.io/library/ubuntu:20.04                                    0.7s
 => CACHED [ 1/15] FROM docker.io/library/ubuntu:20.04@sha256:0e0402cd13f68137edb0266e1d2c682f217  0.0s
 => [ 2/15] RUN rm -f /etc/apt/sources.list.d/*.list                                               0.2s
 => [ 3/15] RUN ln -snf /usr/share/zoneinfo/Europe/Amsterdam /etc/localtime && echo Europe/Amster  0.1s
 => ERROR [ 4/15] RUN apt update && apt install -y --no-install-recommends   wget   unzip   sudo   2.8s

...

#7 2.274 Reading package lists...
#7 2.680 Building dependency tree...
#7 2.767 Reading state information...
#7 2.777 Package plastimatch is not available, but is referred to by another package.
#7 2.777 This may mean that the package is missing, has been obsoleted, or
#7 2.777 is only available from another source
#7 2.777 
#7 2.785 E: Package 'plastimatch' has no installation candidate
```

If you want to know more, there are some [very relevant posts about this exact issue](https://groups.google.com/g/plastimatch/c/IGpuVP5ZLm8?pli=1).

The only way this problem can be solved is by running the `docker build` command specifying the platform, with the `--platform` flag. In our case, passing the argument `--platform linux/amd64` will result in a successful build, with the caveat that all the libraries installed in the Docker container will of course not be optimized for the Apple Silicon processor. This practically means that running computationally intensive tasks (e.g., the `mhubai/totalsegmentator:nocuda` image) will take approximately 10 times longer than what it would take if AppleSilicon-optimized libraries were parsed.
