build-image:
	docker build --no-cache -t doc_check .

run-check:
	docker run \
  -it \
  --rm \
  -v $(PWD)/..:/usr/local/documents \
  doc_check \
  /bin/ash text-lint/lint.sh

clear-output:
	rm -rf ../md
