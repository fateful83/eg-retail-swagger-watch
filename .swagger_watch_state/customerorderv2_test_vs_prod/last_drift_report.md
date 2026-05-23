# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-05-23T12:50:58Z
- Severity: non_breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `852b7c864b98b8e2977e0b7801958a82db5984910bc5ac3a491a5ab8a371f4e0`
- PROD hash: `32817373462a70f1a8e36a21b87a49b8185588848147882521dce2b3ea2d6f8a`

## Summary
- Only in TEST: 1
- Only in PROD: 0
- Present in both but different: 0

## Only in TEST
- GET /api/gateway/ServiceOrders/{storeNumber}

## Only in PROD
- None

## Different in TEST and PROD
- None
