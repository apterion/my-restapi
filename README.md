# my-restapi
# Author: Sergei Shavlovskiy apterion@yandex.ru
#
# Init: ./db_create.py
# Run: ./run.py
#
# Example usage:
# Add contract:
# curl -s -X POST -d '{"signed_date": "2018-06-21", "text": "line1\nline2\nline3"}' http://localhost:8882/contracts
# Update contract:
# curl -s -X PUT -d '{"signed_date": "2018-06-21", "text": "line1\nline2\nline3"}' http://localhost:8882/contracts/1
# Get contracts:
# curl -s -X GET http://localhost:8882/contracts
# Get contract:
# curl -s -X GET http://localhost:8882/contracts/1
#
# OR
# Go to http://localhost:8882/ in your browser
