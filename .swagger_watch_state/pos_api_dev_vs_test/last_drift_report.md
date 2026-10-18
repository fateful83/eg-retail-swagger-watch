# DEV vs TEST drift detected: POS API

- Time: 2026-10-18T19:44:03Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `28c70873297c9d04a8fd78ccae75090b6df361450912836b3b578b687c181869`
- TEST hash: `ad8dae0e0610c34dbacfb49fe12b0f4c0e966e41dcc76759a417a4a74e147f89`

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
