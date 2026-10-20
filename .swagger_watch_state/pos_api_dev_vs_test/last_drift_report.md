# DEV vs TEST drift detected: POS API

- Time: 2026-10-20T15:52:46Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `9f65afaed41188812a717d61d2ee149aaeeb71ebdaf635825d2e1c7c7da1ddfe`
- TEST hash: `1b4c65a09c5b1cccea98382fbfcff9b7d3c81d9748eda202970ad17115817aa2`

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
