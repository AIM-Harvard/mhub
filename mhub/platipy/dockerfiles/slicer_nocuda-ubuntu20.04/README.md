# Slicer no-cuda Ubuntu 20.04 LTS

# Build the Image

## Intel or AMD (Linux, Windows, old Macbooks)

```
docker build  --platform=linux/amd64 --tag aimi/platipy .
```

## Apple Silicon (M1 Macbooks)

M1 Macbooks need the `--platform` flag specified (otherwise some of the instructions, 
such as pulling some packages, might fail). The platform flag can be specified at 
runtime as well, but it's not mandatory.

```
docker build  --platform=linux/amd64 --tag aimi/platipy .    
```

# Run the Container

## All the Platforms

```
# docker run -it --volume $ABS_PATH_TO_INPUT_FOLDER:/app/data/input_data --volume 
$ABS_PATH_TO_OUTPUT_FOLDER/sample_output:/app/data/output_data aimi/platipy

```
