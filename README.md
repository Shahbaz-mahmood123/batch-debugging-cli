<h3 align="center">Batch Debugging CLI</h3>

<p align="center">
    The Batch Debugging CLI is designed to streamline the debugging process for AWS Batch, GCP, Azure, and Kubernetes compute environments. Leveraging the capabilities of [batch-debugging](https://github.com/Shahbaz-mahmood123/batch-debugging).
    <br />
    <a href="https://github.com/Shahbaz-mahmood123/batch-debugging"><strong>Explore the documentation »</strong></a>
    <br />
    <br />
</p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <!-- <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul> -->
    </li>
    <li>
      <a href="#installation">Installation</a>
      <ul>
        <li><a href="#getting-started">Getting Started</a></li>
        <!-- <li><a href="#prerequisites">Prerequisites</a></li> -->
      </ul>
    </li>
    <!-- <li><a href="#usage">Usage</a></li> -->
    <!-- <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li> -->
    <li><a href="#contact">Contact</a></li>
    <!-- <li><a href="#acknowledgments">Acknowledgments</a></li> -->
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

The Batch Debugging CLI is a command-line tool designed to assist in debugging batch compute environments across AWS, GCP, Azure, and Kubernetes. It currently relies on [batch-debugging](https://github.com/Shahbaz-mahmood123/batch-debugging) for its underlying logic, so refer to its documentation for detailed information on the debugging process.

Please note that the CLI assumes AWS Batch compute environments were built using the Seqera platform. However, a more generic debugging tool will be implemented in the future.


### Installation

To use this library, just install the package via pip. 

```sh
pip install batch-debugging-cli
```


<!-- GETTING STARTED -->
## Getting Started

Before using the CLI, ensure you have an account in your compute provider, a valid compute enviornment and credentials to access the account(AWS, GCP, Azure)

Currently, the CLI supports a few commands, and it expects the environment name to match the corresponding AWS environment. When supplying a compute environment ID, provide the full name of the environment (e.g., TowerForge-1rVcJ5K5wnvky3zohO4EaN-head).

## AWS 
For AWS please declare the region where your batch enviornmets are located. For example:

```sh 
export AWS_REGION=us-east-1
```
Additionally the below IAM permissions are required.

## GCP

To use the GCP commands please use the set the below enviornment variables:
```sh
export GCP_PROJECT_ID=test-environment
export GCP_REGION=us-central1
```

For Seqera platform, please declare the below two enviornment variables prior to attempting to run any of the seqera cli commands:
```sh 
export PLATFORM_TOKEN=
export PLATFORM_URL=
```

 ## Contact

Shahbaz Mahmood -  shahbazmahmooood@gmail.com