
[![CI](https://github.com/Adeemy/huggingface-ghcr/actions/workflows/main.yml/badge.svg)](https://github.com/Adeemy/huggingface-ghcr/actions/workflows/main.yml)

# 🤗 Hugging Face model packaging using GitHub Container Registry

A web application uses FastAPI with GPT-2 model sourced from Hugging Face and exposes a single endpoint that you can interact with it.

# Instructions to access the app in local docker container
1. Install docker in local machine if not already installed. For debian version, follow instruction in this [link](https://docs.docker.com/engine/install/debian/#install-using-the-repository)
2. Build container (using root if needed): sudo docker build -t hugginface:local . 
3. Run the app inside the container: docker run -i -p 8000:8000 huggingface:local

