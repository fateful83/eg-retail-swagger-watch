# TEST vs PROD drift detected: ItemService

- Time: 2026-10-30T11:43:42Z
- Severity: breaking
- TEST Swagger URL: https://itemservice.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://itemservice.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `8376fb7312c08810d261e77335819ddccaf311a869c5a85a6b1bd3b36f7a5823`
- PROD hash: `0bb630280b00ffc6d939deec5346845a52123dc3e66229acb1bb8a055599ae8b`

## Summary
- Only in TEST: 0
- Only in PROD: 16
- Present in both but different: 0

## Only in TEST
- None

## Only in PROD
- DELETE /api/DeliveryDateList/DeliveryDates/{id}
- GET /api/DeliveryDateList/{id}
- GET /api/MarketingCodes
- GET /api/MarketingCodes/{id}
- GET /api/PlanningCodes
- GET /api/PlanningCodes/{id}
- POST /api/DeliveryDateList/{listId}/DeliveryDates
- POST /api/MarketingCodes
- POST /api/MarketingCodes/{id}/ToggleIsActive
- POST /api/MarketingCodes/{id}/ToggleIsDefault
- POST /api/PlanningCodes
- POST /api/PlanningCodes/{id}/ToggleIsActive
- POST /api/PlanningCodes/{id}/ToggleIsDefault
- PUT /api/DeliveryDateList/DeliveryDates/{id}
- PUT /api/MarketingCodes/{id}
- PUT /api/PlanningCodes/{id}

## Different in TEST and PROD
- None
