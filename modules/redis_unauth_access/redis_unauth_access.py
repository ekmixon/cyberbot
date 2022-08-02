import redis


def run(seed):
    try:
        ip, port = seed.split(':')
    except ValueError as ex:
        ip, port = seed, 6379

    r = redis.Redis(ip, port, socket_connect_timeout=5)
    info = r.info()
    return info


def callback(result):
    seed = result['seed']
    if data := result['data']:
        exception = result['exception']

        version = data.get('redis_version', '') if data else None
        os = data.get('os', '') if data else None

        print(
            f'seed: "{seed}", version: "{version}", os: "{os}", exception: "{exception}"'
        )


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print(f'Usage: python {sys.argv[0]} <seed>')
        sys.exit()

    callback(dict(seed=sys.argv[1].strip(),
                  data=run(sys.argv[1].strip()),
                  exception=None))
