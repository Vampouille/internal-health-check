import logging
from c2cwsgiutils import services


update_service = services.create("update", "/update")


@update_service.get()
def update(request):
    logging.getLogger(__name__+".update").info("Test")
    return {'test': True}
