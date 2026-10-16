# DEV vs TEST drift detected: POS API

- Time: 2026-10-16T10:11:45Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `6e55714055a41bff6688b1bce2d1e60272713759f8e6f8270b51a42ac012b1c3`
- TEST hash: `2c53f1657ebf033342e93edfd7b99f790876adf4d11456be89c0e8f933f4a0cf`

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
