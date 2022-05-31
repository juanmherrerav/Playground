# Creacion de ambientes en Python

1. Crear ambiente virtual Python

    ```bash
    python3 -m venv mi_ambiente
    ```

1. Activar ambiente

    ```bash
    mi_ambiente/Scripts/activate
    ```

    Opcionalmente

    ```bash
    mi_ambiente/bin/activate
    ```

1. Para listar los paquetes instalados

    ```bash
    pip3 list
    ```

1. Para fijar los paquetes instalados en el archivo requirements.txt

    ```bash
    pip3 freeze > requirements.txt
    ```

1. Actualizar pip

    ```bash
    pip3 install --upgrade pip
    ```

    Opcionalmente

    ```bash
    python3 -m pip install --upgrade pip
    ```

1. Instalar Dependencias desde requirements.txt

    ```bash
    pip3 install -r requirements.txt
    ```

1. Desactivar ambiente

    ```bash
    mi_ambiente/Scripts/deactivate
    ```

    Opcionalmente

    ```bash
    mi_ambiente/bin/deactivate
    ```
