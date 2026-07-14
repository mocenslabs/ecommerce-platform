# Error Catalog

## Authentication

| HTTP | Description |
|------|-------------|
|401|Unauthorized|
|403|Forbidden|

---

## Validation

| HTTP | Description |
|------|-------------|
|400|Validation Error|

---

## Resources

| HTTP | Description |
|------|-------------|
|404|Not Found|

---

## Conflict

| HTTP | Description |
|------|-------------|
|409|Conflict|

---

## Rate Limit

| HTTP | Description |
|------|-------------|
|429|Too Many Requests|

---

## Server Errors

| HTTP | Description |
|------|-------------|
|500|Internal Server Error|

---

# Standard Error Response

```json
{
    "success": false,
    "message": "...",
    "errors": {}
}
```
