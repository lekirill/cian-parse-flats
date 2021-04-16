import os

DB = {
    'dsn': os.getenv('DB_URL') or 'postgresql://test:test@127.0.0.1:5432/test',
    'max_size': os.getenv('DB_POOL_MAXSIZE') or 5,
    'min_size': os.getenv('DB_POOL_MINSIZE') or 1,
}
