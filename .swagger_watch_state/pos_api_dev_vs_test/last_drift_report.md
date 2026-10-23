# DEV vs TEST drift detected: POS API

- Time: 2026-10-23T10:35:34Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `b9aec73d90434b8aeb48c7811aa562d970c84dca92aeec17dd16244fa69f05e2`
- TEST hash: `e1369302c57a53eaee0b18e4c152bc8a6de82408790767b37184ca3c05de8687`

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
