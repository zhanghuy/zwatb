from django.http import HttpResponse
from django.views.generic import View

class upload(View):
    def post(self, request):
        project = request.POST.get("project")
        if project not in ["1", "2"]:
            return HttpResponse({"code": 400, "msg": "项目错误"})
        tar = request.FILES.get("file")
        if not tar:
            return HttpResponse({"code": 400, "msg": "请上传压缩包"})
        path = os.path.abspath('.')
        with open(path, 'wb') as f:
            for i in tar.chunks():
                f.write(i)
        return HttpResponse({"code": 0, "msg": "success", "data": []})