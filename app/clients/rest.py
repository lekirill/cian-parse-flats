import aiohttp
import json


class RestClient:

    def __init__(self, app, loop, limit=100, timeout=60):
        self.app = app
        connector = aiohttp.TCPConnector(loop=loop, limit=limit)
        self.connection_pool = aiohttp.ClientSession(loop=loop, json_serialize=json.dumps, connector=connector,
                                                     timeout=aiohttp.ClientTimeout(total=timeout))

    async def close(self):
        if self.connection_pool and not self.connection_pool.closed:
            await self.connection_pool.close()

    async def request(self, method, url, **kwargs):
        async with self.connection_pool.request(method, url=url, **kwargs) as response:
            try:
                return await response.json(), response.status, response.content_type
            except aiohttp.client.ContentTypeError:
                return await response.text(), response.status, response.content_type
