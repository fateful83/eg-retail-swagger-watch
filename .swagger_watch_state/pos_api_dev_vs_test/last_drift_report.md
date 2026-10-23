# DEV vs TEST drift detected: POS API

- Time: 2026-10-23T20:41:54Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `fec32f27d05801f6c0708cf29f4b5afbfe914bdd92ed0784ed0a0752963e70c1`
- TEST hash: `e12ae70a6fb9ef81515cdb7c5496a4c6e5b6f39058338ab1a7c88a11b88deb64`

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
