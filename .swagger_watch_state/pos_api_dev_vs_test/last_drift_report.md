# DEV vs TEST drift detected: POS API

- Time: 2026-10-16T01:46:40Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `1779a6aec06d4a2e145a5bf16965b6980b43cf52bc91fd6c7ce196dc0617f4e9`
- TEST hash: `1e46a78ff84e1affe8b8184d95970d82ae2f596318a131d791ebdde829a8990f`

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
