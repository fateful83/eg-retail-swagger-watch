# DEV vs TEST drift detected: POS API

- Time: 2026-10-22T10:43:11Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `3651b9296eff3fd7deb418800c04aba86c07303c00389fafc06d2bec2fcf6d9c`
- TEST hash: `2087f5560355c88b10db44b00f89ea1b032f579a7b20a4ad2ae92382d3e9779f`

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
