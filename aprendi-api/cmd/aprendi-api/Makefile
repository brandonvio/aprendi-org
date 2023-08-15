.PHONY: all build test run
# build: 0629

# export sh1 = $$(git rev-parse HEAD)
# export sh2 = $$(echo $(sh1) | cut -c 1-7)

	
test: 
	go test ./...

build: test
	GOOS=linux GOARCH=amd64 CGO_ENABLED=0 go build -o aprendi-api-exe .

run: build
	go run .

push: build
	mkdir ./build
	cp ./aprendi-api-exe ./build/aprendi-api-exe
	cd build && zip -r aprendi-api.zip .
	cd build && aws s3 cp aprendi-api.zip s3://aprendi-builds/aprendi-api/${GITHUB_SHA}/aprendi-api.zip

generate-jwt-keys:
	ssh-keygen -t rsa -b 4096 -m PEM -f jwtRS256.key
