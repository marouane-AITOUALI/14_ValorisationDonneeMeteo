from time import time

from django.http import HttpResponse


def metrics_view(_request):
    body = "\n".join(
        [
            "# HELP meteo_app_up Django app health status.",
            "# TYPE meteo_app_up gauge",
            "meteo_app_up 1",
            "# HELP meteo_metrics_timestamp_seconds Metrics generation timestamp.",
            "# TYPE meteo_metrics_timestamp_seconds gauge",
            f"meteo_metrics_timestamp_seconds {time()}",
            "",
        ]
    )
    return HttpResponse(body, content_type="text/plain; version=0.0.4")
