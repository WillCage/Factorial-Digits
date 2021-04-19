# Factorial-Digits

This utility program calculates the sum of the digits for the result of the factorial of the user supplied non-negative integer. For example, if a user supplies the value of 10, a non-negative integer, the factorial of this is 10! = 10 × 9 × 8 ⋯ 3 × 2 × 1 = 3628800. The sum of all the digits for 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

The python files for the utility are supplied along with a Dockerfile to build the Docker image, which allow for the utility to be run using Docker.

## Getting Started

These instructions will get you a copy of the utility up and running on your local machine for development and testing purposes.

### Prerequisites

Before the Docker image of the utility can be built, it is required for Docker to be installed.

[Docker](https://docs.docker.com/docker-for-windows/install/) - Instructions on how to install Docker Engine for all supported Operating Systems.

### Installing

A step by step series of instructions to build and run the utility.

The first step is building the Docker image. Open a terminal and navigate to the folder containing the Dockerfile. Run the following command, as this will build the Docker image.

```
$ docker build . -t factorial-digits
```

Once the Docker image is built, the image can be run. The following command will run the image, where value is the user desired numeric value to be calculated for.

```
$  docker run --rm factorial-digits $VALUE
```

For example, running the following command will result in the output of 10539.

```
$  docker run --rm factorial-digits 1000
```

## Running the tests

The unit tests for this utility were setup using the Python unittest library. The test file can be found in the tests folder. To run the tests using Docker, the following command needs to be run. This will output the results of the test.

```
$ docker run --entrypoint "python" factorial-digits -m unittest
```

## Authors

* **Mark Pinks**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
