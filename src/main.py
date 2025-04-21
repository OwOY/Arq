from arq import create_pool
from arq.connections import RedisSettings
import asyncio

async def create_redis_pool():
    redis_dsn = ''
    redis_setting = RedisSettings.from_dsn(redis_dsn)
    return await create_pool(redis_setting)


async def main():
    redis = await create_redis_pool()
    job = await redis.enqueue_job(
        'Test.test',  # The name of the function to call
        word='Run test function',  # Keyword arguments to pass to the function
        job_id='my_job_id',  # Optional job ID
    )
    try:
        result = await job.result()  # Wait for the job to finish and get the result
    except:
        result = 'Task failed'
    return result

asyncio.run(main())