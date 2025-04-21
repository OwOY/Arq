from arq.connections import RedisSettings


redis_dsn = ''
redis_setting = RedisSettings.from_dsn(redis_dsn)

class Test:
    @staticmethod
    async def test(ctx, word):
        print(f'worker start : {word}')
        

class WorkerSettings:
    functions = [
        Test.test,
    ]
    redis_settings = redis_setting
    