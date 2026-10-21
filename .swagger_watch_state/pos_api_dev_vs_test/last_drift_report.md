# DEV vs TEST drift detected: POS API

- Time: 2026-10-21T16:10:42Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `fa81b199f812af1f81a965d28de7665c7d3e7c474f4ae055e7eb8a8b219a674d`
- TEST hash: `499d0ed3615cab18eddf07a00373177c4b9ba83336825954e82d4470ea2508a4`

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
