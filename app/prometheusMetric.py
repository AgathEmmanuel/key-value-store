from typing import Tuple
import time
from prometheus_client import Counter, Histogram
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response
from starlette.routing import Match
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR
from starlette.types import ASGIApp


from prometheus_client import CONTENT_TYPE_LATEST, REGISTRY, CollectorRegistry, generate_latest





inf = float("inf")
HTTP_LATENCY_STATUS_KEYS = Histogram(
    "http_latency_status_keys",
    "Histogram of latency of each endpoint by path, status and no.of keys (in seconds)",
    ["method", "path_template","status_code","no_of_keys"],
    buckets=(1,2,3,4,inf)
)

HTTP_RESPONSE = Counter(
    "http_response",
    "Total count of responses by method, path and status codes and no.of.keys ",
    ["method", "path_template", "status_code","no_of_keys"],
)
class PrometheusMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp, filter_unhandled_paths: bool = False) -> None:
        super().__init__(app)
        self.filter_unhandled_paths = filter_unhandled_paths

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        method = request.method
        path_template, is_handled_path = self.get_path_template(request)

        if self._is_path_filtered(is_handled_path):
            return await call_next(request)

        no_of_keys = len(store)
        before_time = time.perf_counter()
        try:
            response = await call_next(request)
        except BaseException as e:
            status_code = HTTP_500_INTERNAL_SERVER_ERROR
            raise e from None
        else:
            status_code = response.status_code
            after_time = time.perf_counter()
            HTTP_LATENCY_STATUS_KEYS.labels(method=method, path_template=path_template,status_code=status_code,no_of_keys=no_of_keys).observe(
                after_time - before_time
            )
        finally:
            HTTP_RESPONSE.labels(method=method, path_template=path_template, status_code=status_code,no_of_keys=no_of_keys).inc()

        return response

    @staticmethod
    def get_path_template(request: Request) -> Tuple[str, bool]:
        for route in request.app.routes:
            match, child_scope = route.matches(request.scope)
            if match == Match.FULL:
                return route.path, True

        return request.url.path, False

    def _is_path_filtered(self, is_handled_path: bool) -> bool:
        return self.filter_unhandled_paths and not is_handled_path


