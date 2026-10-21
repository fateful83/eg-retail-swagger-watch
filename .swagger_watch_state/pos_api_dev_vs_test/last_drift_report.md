# DEV vs TEST drift detected: POS API

- Time: 2026-10-21T02:07:19Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `bc85dc2200c65e205e018b4ce1fa033c98ba93c19fcab725c4315af3233121cb`
- TEST hash: `56533985155716c8bcab7d1a2cc3f1e087ab2422aaf6439b988bb57daa179f2b`

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
