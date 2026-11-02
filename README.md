# Zone Check

Decide whether a service point is covered by a dispatch polygon, accounting for internal exclusions and distinguishing boundary addresses for manual review.

## Run locally

Use Python 3.12. The project uses the standard library. From the repository root:

```sh
python cli.py example.json
python -m unittest -v
```

The included example is synthetic. Pass a different UTF-8 JSON file to inspect your own input. The command prints JSON to stdout. Invalid input returns status 2 and an explanation on stderr. See [CONTRACT.md](CONTRACT.md) for input fields and interpretation.

## Operational limits

Planar integer coordinates only. The algorithm uses exact integer orientation tests and half-open ray crossings. Survey projection, validation of polygon topology and geographic antimeridian handling are upstream responsibilities.

## Resumen en español

Clasifica ubicaciones dentro, fuera o en el límite de zonas con exclusiones interiores usando coordenadas enteras.
