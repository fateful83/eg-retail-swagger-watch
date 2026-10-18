# DEV vs TEST drift detected: POS API

- Time: 2026-10-18T14:56:37Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `ab42564269414bb158a2df8c4d24faf4b773bd514db2d63ebf91913bccf1b4cf`
- TEST hash: `cf95c2b441c2097cf0e10f1319e4dc0d565590e8dea6423a2afe13d5e424f7de`

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
