<h3 align="center">batch_debugging_cli</h3>

  <p align="center">
    This is a CLI for https://github.com/Shahbaz-mahmood123/batch-debugging, it allows easier debugging of AWS Batch compute enviornments.
    <br />
    <a href="https://github.com/Shahbaz-mahmood123/batch-debugging"><strong>Explore the docs »</strong></a>
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

A CLI that assists in debugging batch compute enviornments in AWS, GCP and Azure and Kubernetes, it currently uses https://github.com/Shahbaz-mahmood123/batch-debugging for the logic so please check there for more details around how the debugging is done. Currently only supports AWS Batch but this will be extended to include other cloud enviornment. 

Additionally currently assumes your compute enviornments in AWS batch were built using Seqera platform but a more standard debugging tool will eventually be implemented.
<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Installation

To use this library, just install the package via pip. 

```sh
pip install batch-debugging-cli
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To use this CLI, you will need to first export two enviornment variables.

```sh 
export PLATFORM_TOKEN=
export PLATFORM_URL=
```

You will also need aws credentials stored locally so the CLI can fetch the various resources from AWS. 

Currently only two commands are support and the CLI expects the enviornment name to match what is currently in AWS. 
For example `TowerForge-1rVcJ5K5wnvky3zohO4EaN-head`.
<!-- ### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```
 -->

 ## Contact

Shahbaz Mahmood -  shahbazmahmooood@gmail.com

<p align="right">(<a href="#readme-top">back to top</a>)</p>