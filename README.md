# Practical Labs — Docker

Serves the whole labs hub (`index.html` + all 16 `challenge_XX_*` folders) as
a static site behind nginx on port 80. No backend is needed — each lab runs
its Python in the browser via [Pyodide](https://pyodide.org).

Answer keys (`task.txt`) stay out of the image entirely — see `.dockerignore`.

## Quick Start

```bash
docker compose up -d --build
```

Open **http://127.0.0.1** for the labs hub, or jump straight to a lab, e.g.
**http://127.0.0.1/challenge_01_off_by_one/challenge.html**.

## Teardown

```bash
docker compose down
```

## Files

| Path | Purpose |
|------|---------|
| `Dockerfile` | `nginx:alpine` serving this whole directory as static content |
| `docker-compose.yml` | Runs the site on `127.0.0.1:80` |
| `nginx.conf` | Static file server config |
| `.dockerignore` | Keeps `task.txt` answer keys (and this Docker tooling itself) out of the served image |
