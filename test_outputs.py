import json


def test_report_contains_correct_summary():
    """
    Verifies success criterion 1:
    The report contains the correct request count, unique client count,
    and most popular path.
    """
    with open("/app/report.json") as f:
        report = json.load(f)

    assert report["total_requests"] == 6
    assert report["unique_ips"] == 3
    assert report["top_path"] == "/index.html"