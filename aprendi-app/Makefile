deploy:
	npm install
	CI=true npm test
	npm run build
	aws s3 sync build/ s3://home.aprendi.org
	aws cloudfront create-invalidation --distribution-id E3VM4OIDOU9DFG --paths "/*"