# DEV vs TEST drift detected: POS API

- Time: 2026-10-17T01:41:58Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `0fe936253d99d06f5bce059cc8fcaaa18dd0c9ce2db469a0604a609949635d85`
- TEST hash: `3eed4521b3d99349af6ffe5b66158afa74736e8cb1b0d2ab8c736aee0179bdd5`

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
