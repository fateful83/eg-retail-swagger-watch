# DEV vs TEST drift detected: POS API

- Time: 2026-10-18T01:37:49Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `0dc505b6dd5b395a34627be3807fe666d285436ca310bca4729b30a57edf4892`
- TEST hash: `76fd855f16c21e25c4d9bafd3527669859f9887895d299a99201289dabe133ec`

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
