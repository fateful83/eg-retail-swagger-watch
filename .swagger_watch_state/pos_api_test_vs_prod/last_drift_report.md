# TEST vs PROD drift detected: POS API

- Time: 2026-10-31T16:22:03Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `ad9a1029f868ef30cf024dfd48050d00f127e4c720db932f3d0f358505f61e06`
- PROD hash: `23fe15e3b78b733ac9a923d6e254dc8a6f553b0397d30722e8f13c34d103b2fa`

## Summary
- Only in TEST: 3
- Only in PROD: 0
- Present in both but different: 0

## Only in TEST
- GET /api/UserService/PingHealth
- POST /api/UserService/Authenticate
- POST /api/UserService/CheckUserExists

## Only in PROD
- None

## Different in TEST and PROD
- None
