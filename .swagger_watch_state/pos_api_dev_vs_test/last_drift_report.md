# DEV vs TEST drift detected: POS API

- Time: 2026-10-20T02:13:02Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `0bd1addd8d44df95990f4e8dafc83ece8377d8fd897855f1e54c5a06902fd1a6`
- TEST hash: `4328226f7d98f8d2fd9b5bbb07c97c8b0522c0e649fb4e01c323e807c290c845`

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
