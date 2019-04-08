from core4.queue.job import CoreJob
from core4.queue.helper.functool import enqueue, execute

import random
import time

class SwarmJob(CoreJob):
    author = "mra"

    def execute(self, count=20, prob_launch=0.5, max_launch=3,
                min_sleep=3, max_sleep=10, **kwargs):
        sleep = random.randint(min_sleep, max_sleep)
        self.logger.info("sleeping [%d] seconds", sleep)
        time.sleep(sleep)
        if count > 0:
            n = random.randint(0, count)
            for i in range(n):
                if random.random() <= prob_launch:
                    enqueue(self.__class__, count=count - 2,
                            prob_launch=prob_launch, max_launch=max_launch,
                            id="%s.%d" %(self._id, i))


if __name__ == '__main__':
    execute(SwarmJob, count=3, min_sleep=0, max_sleep=3)
