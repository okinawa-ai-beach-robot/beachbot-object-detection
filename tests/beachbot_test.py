def test_beachbot_import(caplog):
    # Import your module and logger
    from beachbot.config import config, logger

    # Access the config variable
    beachbot_home = config.BEACHBOT_HOME

    # Log the message
    logger.info("BEACHBOT_HOME: " + str(beachbot_home))

    # Check if the correct log message was recorded
    assert "BEACHBOT_HOME: " + str(beachbot_home) in caplog.text
