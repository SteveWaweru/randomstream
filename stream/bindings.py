from channels_api.bindings import ResourceBinding
from models import RandomNumber
from serializer import RandomSerializer


class RandomNumberBinding(ResourceBinding):
    model = RandomNumber
    stream = "number"
    serializer_class = RandomSerializer
    queryset = RandomNumber.objects.all()

