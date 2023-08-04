curl -X POST "http://localhost:5002/identify" \
-H "Content-type: application/json" \
-d '{"email":"series_1@sample_mail.com", "phoneNumber":"1"}'

curl -X POST "http://localhost:5002/identify" \
-H "Content-type: application/json" \
-d '{"email":"series_2@sample_mail.com", "phoneNumber":"100"}'
