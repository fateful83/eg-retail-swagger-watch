# DEV vs TEST drift detected: POS API

- Time: 2026-10-23T15:58:01Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `12f89931eb085c8ec4d6056974c7d8ad140c1843e5b8fec1fdd398be5fb1a5e6`
- TEST hash: `f319dc480786e8e73937b1eb5cd84978c5e0e2bb74261f2868a3e4c95dad7138`

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
