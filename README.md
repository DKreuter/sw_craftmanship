# sw_craftmanship
## Workshop Overview

In this workshop, we will cover various aspects of software craftsmanship, including setting up your local environment, social coding practices, and writing your first code example.

## Setting Up Your Local Environment

To get started, follow these steps to set up your local environment using conda:

1. Create a new conda environment:
    ```sh
    conda create -p .\.env
    ```

2. Install Python and pip:
    ```sh
    conda install pip python=3.10
    ```

3. Install necessary packages:
    ```sh
    pip install jupyter requests pandas
    ```

4. Verify your conda installation:
    ```sh
    conda info -e
    ```

5. Refer to the conda cheatsheet for more commands and tips:
    [Conda Cheatsheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)

## Social Coding

- Create a new private repository on GitHub and connect it to your project.
- Use pyscaffold to set up your project structure:
    ```sh
    pip install -U pyscaffold
    putup my_project_name
    ```
- Connect your project with your GitHub repository:
    ```sh
    git clone https://github.com/user/repo.git
    ```
- Install additional tools and configure your project:
    ```sh
    pip install tox
    pip install -e .[testing]
    ```

- Add commit hooks for code quality:
    [Pre-commit Hooks](https://pre-commit.com/)

- Collaborate with your team by adding issues, creating branches, and making pull requests.

## Writing Your First Code Example

- Form a team with two other users and create a common project.
- Define a branch strategy and add different issues for new features, functions, and plots.
- Practice social coding by reviewing each other's code and pair programming.

## Test Driven Development

- Work with GPS data containing NaN values and write tests using pytest and coverage.
- Define new tests and let GitHub Copilot assist in writing the corresponding functions.
- Set up a GitHub action to enforce 100% test coverage and display the coverage report on GitHub Pages.

## Documentation

- Write a comprehensive README.md file.
- Use docstrings for documenting your code.
- Generate documentation with Sphinx and host it on GitHub Pages.
- Utilize the GitHub Wiki for additional project documentation.
