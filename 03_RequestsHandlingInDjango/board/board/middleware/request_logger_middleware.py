import datetime


class RequestLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        date_time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M')
        url = request.META.get('HTTP_HOST') + request.path
        http_method = request.META.get('REQUEST_METHOD')
        with open('info_requests.log', 'a', encoding='utf-8') as file:
            file.write(
                f'Дата: {date_time}\tURL:{url}\tHTTP-метод: {http_method}\n')
        response = self.get_response(request)
        return response
