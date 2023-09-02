# Machine Learning Ground

Portifolio to annotate classes and projects in Data Science, Machine Learning and Python in general.

`[PT-BR]`Portifólio para anotações das aulas e projetos em Data Science, Machine Learning e Python no geral.

## General information
- Since I'm using a `venv`, I use the following function to open files from the current directory:
    ```python
    from os import path

    def dir(file_name):
        return path.join(path.dirname(__file__), file_name)
    ```
- Requirements are in `requirements.txt` and can be installed with `pip install -r requirements.txt`.
- To get only the used dependencies, I used `pipreqs --ignore .venv` from the `pipreqs` package, you can install it with `pip install pipreqs` if you want to use it.
- In projects where an `.env` was used, the variables are in `env.example` and should be copied to a `.env` file.
