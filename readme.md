[//]: # (What happened when you hit local request i.e : http://127.0.0.1:8000/)
[Android App/Web Browser]
         ↓ HTTP Request
    [Django URLs]  ←── Routes requests to right function
         ↓
    [Django Views] ←── Your business logic
         ↓
    [Django Models] ←── Database structure
         ↓
    [PostgreSQL/SQLite] ←── Actual data storage


When someone hits /api/projects/:
1. Request arrives → "GET /api/projects/"
2. Django checks urls.py → Finds ProjectViewSet
3. ViewSet queries database → Project.objects.all()
4. Serializer converts → Python objects to JSON
5. Response sent back → [{"title": "My App", ...}]

[//]: # (What happens when you hit adityacheke.com underthehood)
[adityacheke.com]
      ↓
[Route 53] → DNS Management
      ↓
[EC2 Instance] → Your Django Server
      ↓
[RDS PostgreSQL] → Production Database
      ↓
[S3 Bucket] → Static files and uploads

