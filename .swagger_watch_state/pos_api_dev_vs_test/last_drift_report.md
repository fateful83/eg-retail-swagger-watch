# DEV vs TEST drift detected: POS API

- Time: 2026-10-20T10:29:08Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `e715b63518c90a8d2c4ca3ecb2cb05c59e44b7b1880f5d42a29bd89f38cfed7c`
- TEST hash: `76d432e0a19ba00a724bb97c2a0682d1df0b2a8154a3d48b1f671a4f3e11efdc`

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
