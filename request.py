class GenericView:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def get(self, request):
        return ""

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass

class DetailView(GenericView):
    def __init__(self, methods=('GET',)):
        super().__init__(methods)

    def render_request(self, request, method):
        if method.upper() in self.methods:
            f = getattr(self, method.lower())
            return f(request)
        else:
            raise TypeError('данный запрос не может быть выполнен')

    def get(self, request):
        if isinstance(request,dict):
            if 'url' in request:
                return f"url: {request['url']}"
            else:
                raise TypeError('request не содержит обязательного ключа url')
        else:
            raise TypeError('request не является словарем')


