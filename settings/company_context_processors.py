from .models import Company


def getInfo(request):
    info = Company.objects.last()
    return {'info': info}