### Worker
```sh
celery -A tasks worker --loglevel=info
```

### Beat
```sh
celery -A tasks beat --loglevel=info
```

### Flower Dashboard
```sh
celery -A tasks --broker=redis://localhost:6379/0 flower
```