# DEV vs TEST drift detected: POS API

- Time: 2026-10-19T21:46:52Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `1afd5c17eca5d7db3ad0117ddfa6e76163e7c32f0ebaae7eef84c63acf2686a4`
- TEST hash: `5b194aa69f5eb32cad70d27d90692226a23b16e720c94120563e4c1b32720741`

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
