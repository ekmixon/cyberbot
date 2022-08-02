import time
import random


def run(seed):
    """ function to run

    Args:
        seed: The value of each line striped in seed file

    Returns:
        String, object, list, directory, etc.
    """

    name, age = seed.split(',')
    return f'Hello World! {seed}, {int(age)}'


def callback(result):
    """ callback function to call

    Args:
        result: ProcessTask instance pool_task_with_timeout() method returned

        result = {
            'seed': 'Jone',
            'data': 'Hello World! Jone',
            'exception': None
        }

        result = {
            'seed': 'Jone',
            'data': None,
            'exception': 'ValueError: invalid literal'
        }

    Returns:
        Anything want to return.
    """

    seed = result['seed']
    data = result['data']
    exception = result['exception']
    time.sleep(random.random()**2 / 50)
    print(f'seed: "{seed}", data: "{data}", exception: "{exception}"')
