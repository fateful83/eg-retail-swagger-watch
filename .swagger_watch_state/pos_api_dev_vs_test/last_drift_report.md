# DEV vs TEST drift detected: POS API

- Time: 2026-10-27T11:07:23Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `9c67a0cc31b27267901bb6695939dd4a3f8d8387850c50faf78666e4a1ac451d`
- TEST hash: `1251bc888046f605c638ae0edaa96af1845cf9295d2171fcff0488696276dcbf`

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
