# DEV vs TEST drift detected: POS API

- Time: 2026-10-19T01:55:56Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `3b59f02132cc69b8c1fc65446c25c7a4442e8a00f2c6a5079189b2041b8f8e09`
- TEST hash: `2b688cd5954f2a310ee8315a0d1647eb8d44cfcf846cbbc3b7f252641d9bf883`

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
