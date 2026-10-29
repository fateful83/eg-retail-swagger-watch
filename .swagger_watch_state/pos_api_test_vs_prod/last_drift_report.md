# TEST vs PROD drift detected: POS API

- Time: 2026-10-29T22:04:19Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `aa69fcd972b68a5939c328f8a49e3b5b23b28540129de65e5bbf9d490f634b17`
- PROD hash: `0364bef32fbe512d940d8ef9868b4d17664ae467ccd0d5eae81ea90676d5d815`

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
