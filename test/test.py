from alpha import starter 
from alpha.utils import logger
from alpha.utils.tools import ts_to_datetime_str
import time
from alpha.tasks import LoopRunTask,SingleTask
import pdb
def d():
    pdb.set_trace()

async def cur_ts(**kwargs):
    logger.info(ts_to_datetime_str())


if __name__ == '__main__':
    LoopRunTask.register(cur_ts,1)
    starter.start()