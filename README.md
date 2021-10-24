![GitHub license](https://img.shields.io/github/license/torresflo/Tag-Machine.svg)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
![GitHub contributors](https://img.shields.io/github/contributors/torresflo/Tag-Machine.svg)
![GitHub issues](https://img.shields.io/github/issues/torresflo/Tag-Machine.svg)

<p align="center">
  <h1 align="center">Tag Machine</h3>

  <p align="center">
    A little python application to auto tag your photos with the power of machine learning.
    <br />
    <a href="https://github.com/torresflo/Tag-Machine/issues">Report a bug or request a feature</a>
  </p>
</p>

## Table of Contents

* [Getting Started](#getting-started)
  * [Prerequisites and dependencies](#prerequisites-and-dependencies)
  * [Installation](#installation)
* [Usage](#usage)
* [Examples](#examples)
* [Contributing](#contributing)
* [License](#license)

## Getting Started

### Prerequisites and dependencies

This repository is tested on Python 3.7+ and PyTorch LTS 1.8.2.

You should install Tag Machine in a [virtual environment](https://docs.python.org/3/library/venv.html). If you're unfamiliar with Python virtual environments, check out the [user guide](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).
First, create a virtual environment with the version of Python you're going to use and activate it.

Then, you will need to install PyTorch.
Please refer to [PyTorch installation page](https://pytorch.org/get-started/locally/#start-locally) regarding the specific install command for your platform.

When PyTorch is installed, 🤗 Transformers can be installed using pip as follows:

```bash
pip install transformers
```

You can refer to the repository of [🤗 Transformers](https://github.com/huggingface/transformers) for more information.

Then you will need to install PySide6, a port of QT for Python used for the graphic interface. It can be installed using pip as follows:

```bash
pip install pyside6
```

Finally you will need to install IPTCInfo3 to allow Tag Machine to write tags in your images. It can be installed using pip as follows:

```bash
pip install iptcinfo3
```

### Installation

Follow the instructions above then clone the repo (`git clone https:://github.com/torresflo/Tag-Machine.git`). You can now run `main.py`.

## Usage

Press the button `Load files...` to load your images then press the button `Classify images` to start the classifier. Depending on your machine hardware and the number of images this can take some time.

The results are loaded in a table below so you can see which tags are detected.

![Example image](https://github.com/torresflo/Tag-Machine/blob/main/Photos/Example1.png)

## Examples

Here are some examples with results. You can find these images in the folder `Photos`. All images come from the [Wikimedia Commons](https://commons.wikimedia.org/) website.

Note that the detection uses the labels computed by the [PhotoPrism](https://github.com/photoprism/photoprism) project. It allows to regroup similar tags in more generic categories and discard non useful ones. Also, a threshold is also calculated to avoid wrong tagging.

| Image                                                                                      | Tags found                     | Probability |
| ------------------------------------------------------------------------------------------ | ------------------------------ | ----------- |
| <img src="https://github.com/torresflo/Tag-Machine/blob/main/Photos/1.jpg" height="300px"> | tower, architecture            |  97,98%     |
| <img src="https://github.com/torresflo/Tag-Machine/blob/main/Photos/2.jpg" height="300px"> | Nothing                        |  --,--%     |
| <img src="https://github.com/torresflo/Tag-Machine/blob/main/Photos/3.jpg" height="300px"> | dining                         |  87,52%     |
| <img src="https://github.com/torresflo/Tag-Machine/blob/main/Photos/4.jpg" height="300px"> | alpine, landscape, mountain    |  66,37%     |
| <img src="https://github.com/torresflo/Tag-Machine/blob/main/Photos/5.jpg" height="300px"> | Nothing                        |  --,--%     |
| <img src="https://github.com/torresflo/Tag-Machine/blob/main/Photos/6.jpg" height="300px"> | shark, water, fish, animal     |  76,77%     |
| <img src="https://github.com/torresflo/Tag-Machine/blob/main/Photos/7.jpg" height="300px"> | Nothing                        |  --,--%     |
| <img src="https://github.com/torresflo/Tag-Machine/blob/main/Photos/8.jpg" height="300px"> | castle, historic, architecture |  99,64%     |
| <img src="https://github.com/torresflo/Tag-Machine/blob/main/Photos/9.jpg" height="300px"> | castle, historic, architecture |  98,44%     |

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the GNU General Public License v3.0. See `LICENSE` for more information.