def test_beachbot_import():
    from beachbot.config import config, logger

    logger.info("BEACHBOT_HOME: " + str(config.BEACHBOT_HOME))
