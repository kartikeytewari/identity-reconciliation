test_mail:
	curl -X POST "http://localhost:5002/identify" -H "Content-type: application/json" -d '{"email":"sample@mail.com"}'

test_phone:
	curl -X POST "http://localhost:5002/identify" -H "Content-type: application/json" -d '{"phoneNumber":"123456"}'

test_all:
	curl -X POST "http://localhost:5002/identify" -H "Content-type: application/json" -d '{"email":"sample@mail.com", "phoneNumber":"123456"}'
