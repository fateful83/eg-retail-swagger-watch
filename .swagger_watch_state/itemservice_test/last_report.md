# Swagger/OpenAPI change detected: ItemService [TEST]

- Time: 2026-10-29T17:38:19Z
- Fetch completed at: 2026-10-29T17:38:18Z
- Fetch duration ms: 2099
- Swagger URL: https://itemservice.egretail-test.cloud/swagger/v1/swagger.json
- Previous hash: `b3f87ef2513da9b6ba5ef176b8096dc8a5ef2f662ca4b153ceedce43c31153d0`
- Current hash: `8376fb7312c08810d261e77335819ddccaf311a869c5a85a6b1bd3b36f7a5823`

## Summary
- Status: breaking
- Added operations: 0
- Removed operations: 16
- Changed operations: 0
- Breaking removed operations: 16
- Breaking changed operations: 0
- Non-breaking changed operations: 0

## Added
- None

## Removed
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

## Changed
- None

## Breaking classification
- Removed operations: 16
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

- Breaking changed operations: 0
- None

- Non-breaking changed operations: 0
- None
