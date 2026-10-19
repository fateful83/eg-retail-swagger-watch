# DEV vs TEST drift detected: POS API

- Time: 2026-10-19T17:49:10Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `c8d7587c70c81e6d0d968be538b34f8592480faf09b2fee7f49e6fb836949f92`
- TEST hash: `e7404dc66a4f3600fd953d84dc30478b15df57a018c85b768b497c9d22329257`

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
