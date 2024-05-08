# aws

1. docker pull nvcr.io/nvidia/nightly/cuda-quantum:latest
2. Run docker images to get the image id which in this case is 069231c4037e
3. Turn image into container: docker run -it --net=host --user root --gpus all -d --name cudaq34_zohim 069231c4037e
4. Run python file with this container 
