from core4.api.v1.request.main import CoreRequestHandler
from core4.queue.helper.functool import enqueue
from c4t.job import SwarmJob
from core4.api.v1.application import CoreApiContainer
from core4.api.v1.request.static import CoreStaticFileHandler


class SwarmApi(CoreRequestHandler):

    author = "mra"
    title = "SwarmJob handler"

    def post(self):
        job_id = enqueue(SwarmJob)
        self.reply(job_id._id)

    def get(self):
        return self.post()


class SwarmContainer(CoreApiContainer):

    rules = [
        ("/swarm", SwarmApi)
    ]


class VueContainer(CoreApiContainer):

    root = "vue"
    rules = [
        ("/example", CoreStaticFileHandler, {
            "path": "/webapps/example/dist"
        })
    ]


if __name__ == '__main__':
    from core4.api.v1.tool.functool import serve
    serve(SwarmContainer)