There is an Apache-style access log file in the working directory.

Analyze the traffic in the log and create a JSON summary report.

Save the report at:

/app/report.json

The report must contain these fields:

- total_requests: the total number of requests in the log
- unique_ips: the number of unique client IP addresses
- top_path: the most frequently requested URL path

The output must be valid JSON and contain the correct summary values from the access log.