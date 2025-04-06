# URL Shortener - Week 1 Completion

## Test Results
```bash
$ curl -X POST -H "Content-Type: application/json" -d '{"url":"https://example.com"}' http://localhost:5000/shorten
{"short_url":"http://localhost:5000/EQHbzF"}

$ curl -v http://localhost:5000/EQHbzF
< HTTP/1.0 302 FOUND
< Location: https://example.com
