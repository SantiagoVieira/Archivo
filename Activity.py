from typing import Dict, Any

class LogAnalyzer:
    def __init__(self, filename: str):
        self.filename = filename

    def analyze_logs(self) -> Dict[str, Any]:
        total_requests = 0
        http_method_stats = {}
        response_code_stats = {}
        total_response_size = 0
        url_stats = {}

        with open(self.filename) as f:
            for line in f:
                try:
                    log_data = line.strip().split(' ')
                    # Assuming log format is as follows:
                    # IP_ADDRESS DATE_TIME HTTP_METHOD URL HTTP_RESPONSE_CODE RESPONSE_SIZE
                    ip_address, date_time, http_method, url, http_response_code, response_size = log_data

                    total_requests += 1

                    http_method_stats[http_method] = http_method_stats.get(http_method, 0) + 1

                    response_code_stats[http_response_code] = response_code_stats.get(http_response_code, 0) + 1

                    total_response_size += int(response_size)

                    url_stats[url] = url_stats.get(url, 0) + 1

                except ValueError:
                    print(f"Skipping line: {line.strip()}. Invalid format.")

        top_url_stats = sorted(url_stats.items(), reverse=True, key=lambda x: x[1])[:10]

        avg_response_size = total_response_size / total_requests

        return {
            "total_requests": total_requests,
            "http_method_stats": http_method_stats,
            "response_code_stats": response_code_stats,
            "total_response_size": total_response_size,
            "avg_response_size": avg_response_size,
            "top_url_stats": top_url_stats
        }


log_analyzer = LogAnalyzer("trafico_web.log")
statistics_dict = log_analyzer.analyze_logs()
print(statistics_dict)
