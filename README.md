# secret-service-scripts

<div align="center">

[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/johanwiden/secret-service-scripts/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/johanwiden/secret-service-scripts/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/johanwiden/secret-service-scripts/releases)
[![License](https://img.shields.io/github/license/johanwiden/secret-service-scripts)](https://github.com/johanwiden/secret-service-scripts/blob/master/LICENSE)

List password entries, search for username, get username and password using [Secret Service API](https://specifications.freedesktop.org/secret-service).

The default collection (service) in Secret Service is used, this is normally the login collection.
On at least Ubuntu this collection is by default open when a user is logged in. So there is no
need to enter a master password to unlock the collection.

</div>

## Installation

Install the scripts by copying them from the repo. Currently there is no pip package for these scripts.

### Dependencies
Depends on python package [SecretStorage](https://pypi.org/project/SecretStorage)

## How to use
The commands can be run from the command line.

secret-service-list-all: List the entries in the default Secret Service collection.

secret-service-list-keys: List the keys in the entries in the default Secret Service collection.

secret-service-show-password: Return password for password entry with name given by first argument, in the default Secret Service collection.

secret-service-show-username: Return field 'username' for password entry with name given by first argument, in the default Secret Service collection.

## 📈 Releases

You can see the list of available releases on the [GitHub Releases](https://github.com/johanwiden/i3-sway-switch-window/releases) page.

We follow [Semantic Versions](https://semver.org/) specification.

We use [`Release Drafter`](https://github.com/marketplace/actions/release-drafter). As pull requests are merged, a draft release is kept up-to-date listing the changes, ready to publish when you’re ready. With the categories option, you can categorize pull requests in release notes using labels.

### List of labels and corresponding titles

|               **Label**               |  **Title in Releases**  |
| :-----------------------------------: | :---------------------: |
|       `enhancement`, `feature`        |       🚀 Features       |
| `bug`, `refactoring`, `bugfix`, `fix` | 🔧 Fixes & Refactoring  |
|       `build`, `ci`, `testing`        | 📦 Build System & CI/CD |
|              `breaking`               |   💥 Breaking Changes   |
|            `documentation`            |    📝 Documentation     |
|            `dependencies`             | ⬆️ Dependencies updates |

You can update it in [`release-drafter.yml`](https://github.com/johanwiden/secret-service-scripts/blob/master/.github/release-drafter.yml).

GitHub creates the `bug`, `enhancement`, and `documentation` labels for you. Dependabot creates the `dependencies` label. Create the remaining labels on the Issues tab of your GitHub repository, when you need them.

## 🛡 License

[![License](https://img.shields.io/github/license/johanwiden/secret-service-scripts)](https://github.com/johanwiden/secret-service-scripts/blob/master/LICENSE)

This project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/johanwiden/secret-service-scripts/blob/master/LICENSE) for more details.

## 📃 Citation

```bibtex
@misc{secret-service-scripts,
  author = {Johan Widén},
  title = {List password entries, search for username, get username and password using Secret Service API},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/johanwiden/secret-service-scripts}}
}
```
