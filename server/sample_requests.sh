curl -X POST "http://localhost:5002/identify" -H "Content-type: application/json" -d '{"email":"sample@mail.com"}'
curl -X POST "http://localhost:5002/identify" -H "Content-type: application/json" -d '{"phoneNumber":"123456"}'
curl -X POST "http://localhost:5002/identify" -H "Content-type: application/json" -d '{"email":"sample@mail.com", "phoneNumber":"123456"}'
