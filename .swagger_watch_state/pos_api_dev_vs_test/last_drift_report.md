# DEV vs TEST drift detected: POS API

- Time: 2026-10-20T20:56:37Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `39c04742fb5068420c6fa6bfb74b0f05a334b08960d37cf2dc7013972a9f0f27`
- TEST hash: `607da82d86f3c2bb394d878116bf5bec2c7bd634f05c6f468bdda4a536aa19d8`

## Summary
- Only in DEV: 3
- Only in TEST: 0
- Present in both but different: 0

## Only in DEV
- GET /api/UserService/PingHealth
- POST /api/UserService/Authenticate
- POST /api/UserService/CheckUserExists

## Only in TEST
- None

## Different in DEV and TEST
- None
