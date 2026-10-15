# DEV vs TEST drift detected: POS API

- Time: 2026-10-15T15:49:28Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `6d1e970221737fbb0458bfd97baef09854c6c780a4a89c8b647ca4a2457caedd`
- TEST hash: `eb84f4141e7532f37f7b76e2876c823954768d5d510232d7e87033c28cc50de3`

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
