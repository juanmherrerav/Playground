""" Exceptions handling and error generation"""
import os


def process():
    try:
        result = 1/0
    except Exception as e:
        result = 0
        print("Error: ", e)
    finally:
        print(result)
        print("Finally try of division")
        print("********************************************************")

    try:
        file_name = "file.txt"
        os.remove(file_name)
    except FileNotFoundError as e:
        print(f"The file: '{file_name}' does not exist, the error is '{e}'")
    finally:
        print("Finally")

def my_function(input:str)-> int:
    """[summary]

    Args:
        input (str): [description]

    Returns:
        int: [description]
    """
    try:
        return int(input)
    except ValueError as e:
        print(f"The input '{input}' is not a number, the error is '{e}'")
    finally:
        print("Finally")

process()
