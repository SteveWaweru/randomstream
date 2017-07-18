from channels.generic.websockets import WebsocketDemultiplexer
from channels.routing import route_class

from stream.bindings import RandomNumberBinding


class APIDemultiplexer(WebsocketDemultiplexer):

    consumers = {
      'number': RandomNumberBinding.consumer
    }

channel_routing = [
    route_class(APIDemultiplexer)
]