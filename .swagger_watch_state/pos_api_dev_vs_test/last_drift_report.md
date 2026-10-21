# DEV vs TEST drift detected: POS API

- Time: 2026-10-21T10:39:48Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `72f5fcc248403e196ce3699f61f8d53d0eea073f82593d44451001e1fc803c4b`
- TEST hash: `3f033f829ae2b4ad73772ea32bb0d0c123a0d3e2ad3a948f54fa96fa5cdede04`

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
