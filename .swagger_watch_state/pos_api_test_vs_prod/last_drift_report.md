# TEST vs PROD drift detected: POS API

- Time: 2026-10-28T17:29:00Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `4cea260bb3d486d6a9de7128aceb4cebef723ae86c5fb6930fa7775244fb7e05`
- PROD hash: `88f988f876f6b8940eb951a57afd6df43c06e8cbad7ea3d720ff53b9fddc7e5d`

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
