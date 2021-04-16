import asyncio
from typing import Dict, List, Optional

import asyncpg


class DBClient:

    def __init__(self, settings: dict, *,
                 loop: Optional[asyncio.AbstractEventLoop] = None,
                 pool_settings: Optional[Dict] = None):
        self._settings = settings
        self._loop = loop
        self._pool_settings = pool_settings
        self._lock = asyncio.Lock(loop=loop)

        self.db_pool = None

    async def setup(self):
        async with self._lock:
            self.db_pool = await asyncpg.create_pool(loop=self._loop, **self._settings)

    async def close(self):
        async with self._lock:
            try:
                await self.db_pool.close()
            except asyncpg.PostgresError as e:
                pass

    async def select(self, query: str, values: List) -> List[asyncpg.Record]:
        values = values or ()
        return await self._select(query=query, values=values)

    async def first(self, query: str, values: List) -> Optional[asyncpg.Record]:
        values = values or ()
        return await self._first(query=query, values=values)

    async def insert(self, query: str, values: List):
        return await self._execute(query=query, values=values)

    async def insertmany(self, query: str, values: List):
        return await self._executemany(query=query, values=values)

    async def update(self, query: str, values: List):
        return await self._execute(query=query, values=values)

    async def delete(self, query: str, values: List):
        return await self._execute(query=query, values=values)

    async def _execute(self, query: str, values: List):
        async with self.db_pool.acquire() as conn:
            async with conn.transaction():
                return await conn.fetchrow(query, *values)

    async def _executemany(self, query: str, values: List):
        async with self.db_pool.acquire() as conn:
            async with conn.transaction():
                await conn.executemany(query, values)
                return len(values)

    async def _select(self, query: str, values: List):
        async with self.db_pool.acquire() as conn:
            return await conn.fetch(query, *values)

    async def _first(self, query: str, values: List):
        async with self.db_pool.acquire() as conn:
            return await conn.fetchrow(query, *values)
