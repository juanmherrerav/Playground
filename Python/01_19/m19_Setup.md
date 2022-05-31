# Como hacer un paquete propio en Python

1. Para crear el paquete propio, se debe crear primero el archivo setup.py

  ```python
  """ Setup Package """
  from setuptools import setup
  
  setup(
      name='my_package',
      version='0.1',
      description='Ejemplo de paquete propio',
      author='Juan Herrera',
      author_email= 'juanm.herrerav@gmail.com',
      url= 'https://www.linkedin.com/in/juan-herrera-v/',
      packages=['paquete']
  )
  
  ```

1. Luego se instala el archivo usando
  
    ```bash
    python setup.py sdist   
    ```
  
1. Para instalar el paquete recien creado ubicar el archio .tar.gz en la carpeta de instalacion de python
  
  ```bash
  pip install dist/my_package-0.1.tar.gz
  ```
  
1. Finalmente en el codigo destino se importa sin tener el codigo en el repositorio sin necesidad de tener el paquete codificado en el mismo directorio

  ```python
  from my_package.funcion 
  ```
