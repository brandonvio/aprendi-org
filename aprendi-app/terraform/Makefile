.PHONY: all build test run plan deploy

deploy:
	terraform init
	terraform validate
	terraform plan
	terraform apply -auto-approve

plan:
	terraform validate
	terraform plan