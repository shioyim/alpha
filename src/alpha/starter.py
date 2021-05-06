"""
Asynchronous driven quantitative trading framework.
"""
import signal
import asyncio
from alpha.utils import logger
from alpha.config import config
from alpha.heartbeat import heartbeat
from alpha.const.platform import VERSION,CONFIG_FILE


class Starter:
    """ Asynchronous driven quantitative trading framework.
    """

    def __init__(self):
        self.loop = None

    def initialize(self, config_module=None):
        """ Initialize.
        Args:
            config_module: config file path, normally it"s a json file.
        """
        self._get_event_loop()
        self._load_settings(config_module)
        self._init_logger()
        self._get_version()
        self._beat_heart()

    def start(self):
        """Start the event loop."""
        def keyboard_interrupt(s, f):
            print("KeyboardInterrupt (ID: {}) has been caught. Cleaning up...".format(s))
            self.loop.stop()
        signal.signal(signal.SIGINT, keyboard_interrupt)

        logger.info("Start in \"{}\" io loop...".format(config.project), caller=self)
        self.loop.run_forever()

    def stop(self):
        """Stop the event loop."""
        logger.info("Stop \"{}\" io loop.".format(config.project), caller=self)
        self.loop.stop()

    def _get_version(self):
        """ get software version
        """
        logger.info("Version:", VERSION, caller=self)

    def _get_event_loop(self):
        """ Get a main io loop. """
        if not self.loop:
            self.loop = asyncio.get_event_loop()
            #self.loop.set_debug(True)
        return self.loop

    def _load_settings(self, config_module):
        """ Load config settings.
        Args:
            config_module: config file path, normally it"s a json file.
        """
        config.loads(config_module)

    def _init_logger(self):
        """Initialize logger."""
        console = config.log.get("console", True)
        level = config.log.get("level", "DEBUG")
        path = config.log.get("path", "/tmp/logs/Alpha")
        name = config.log.get("name", "alpha.log")
        clear = config.log.get("clear", False)
        backup_count = config.log.get("backup_count", 0)
        if console:
            logger.initLogger(level)
        else:
            logger.initLogger(level, path, name, clear, backup_count)

    def _beat_heart(self):
        """Start server heartbeat."""
        self.loop.call_later(0.5, heartbeat.ticker)



starter = Starter()
starter.initialize(config_module=CONFIG_FILE)
