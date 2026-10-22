# DEV vs TEST drift detected: POS API

- Time: 2026-10-22T02:01:16Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `8fce9104168a6bebd412dd13a1fb7b863e3edf9e6ec0ce6fc49f985631efbc99`
- TEST hash: `705c3dcdf7fa588c0fd29b7965ab7b87633eff5da99495fdb95f79172a606b2b`

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
