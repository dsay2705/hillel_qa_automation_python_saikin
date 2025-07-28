import pytest
import logging
import os
from .homework_10 import log_event

LOG_FILE = "login_system.log"

class TestEventsLogger:
    @pytest.mark.parametrize(
        "status, expected_level",
        [
            ("success", "INFO"),
            ("expired", "WARNING"),
            ("failed", "ERROR"),
        ],
    )
    def test_log_event_levels(self, caplog, status, expected_level):
        with caplog.at_level("INFO"):
            log_event("User", status)
        assert any(record.levelname == expected_level for record in caplog.records)
        assert any("Login event - Username: User, Status: {}".format(status) in record.message for record in caplog.records)

    def test_log_event_other_status(self, caplog):
        with caplog.at_level("INFO"):
            log_event("User", "other")
        assert any(record.levelname == "ERROR" for record in caplog.records)
        assert any("Login event - Username: User, Status: other" in record.message for record in caplog.records)


    def test_log_event_empty_status(self, caplog):
        with caplog.at_level("INFO"):
            log_event("User", "")
        assert any(record.levelname == "ERROR" for record in caplog.records)
        assert any("Login event - Username: User, Status: " in record.message for record in caplog.records)

    def test_log_event_none_status(self, caplog):
        with caplog.at_level("INFO"):
            log_event("User", None)
        assert any(record.levelname == "ERROR" for record in caplog.records)
        assert any("Login event - Username: User, Status: None" in record.message for record in caplog.records)

    @pytest.mark.parametrize(
        "username",
        ["", "user!@#", "тест", " "]
    )
    def test_log_event_usernames(self, caplog, username):
        with caplog.at_level("INFO"):
            log_event(username, "success")
        assert any("Login event - Username: {}, Status: success".format(username) in record.message for record in caplog.records)
        assert any(record.levelname == "INFO" for record in caplog.records)

    @pytest.mark.parametrize(
        "username, status, expected_text",
        [
            ("User", "success", "Login event - Username: User, Status: success"),
            ("User", "expired", "Login event - Username: User, Status: expired"),
            ("User", "failed", "Login event - Username: User, Status: failed"),
            ("User", "other", "Login event - Username: User, Status: other"),
            ("", "success", "Login event - Username: , Status: success"),
            ("тест", "", "Login event - Username: тест, Status: "),
            ("User", None, "Login event - Username: User, Status: None"),
        ]
    )
    def test_log_event_from_file(self, username, status, expected_text):
        logging.shutdown()
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        if os.path.exists(LOG_FILE):
            os.remove(LOG_FILE)
        log_event(username, status)
        assert os.path.exists(LOG_FILE)
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            content = f.read()
        assert expected_text in content