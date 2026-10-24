# DEV vs TEST drift detected: POS API

- Time: 2026-10-24T14:56:25Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `8069ddb31217a357c8cef55134bb7e76bf704ed6c9d6b1b7c7a59d162c1af845`
- TEST hash: `b3c053b7a616cda680d722ebf0dbf96bfd340f2102551cc524679fa172cf69c7`

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
