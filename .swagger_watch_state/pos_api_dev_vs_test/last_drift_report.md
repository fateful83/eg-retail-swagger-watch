# DEV vs TEST drift detected: POS API

- Time: 2026-10-17T19:45:00Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `c7c6e282be167f25fe4b5547ed780be6ae9591bce5a75f4f08dc2d596e063531`
- TEST hash: `05c5c196a81ceaa4b05f6051b6c3cfb6848be8b00742245bdca36d87a93a1736`

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
