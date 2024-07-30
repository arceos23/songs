
import pytest
from http import HTTPStatus
from app import create_app
import constants

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_get_request(client):
    response = client.get(f"{constants.API_VERSION_ONE}/songs")

    assert len(response.json) == constants.PAGINATION_LIMIT_DEFAULT
    assert response.status_code == HTTPStatus.OK
    assert response.is_json

    assert len(response.json[0]) == constants.NUMBER_OF_ATTRIBUTES
    assert response.json[0]["id"] == "5vYA1mW9g2Coh1HUFUSmlb"
    assert response.json[0]["title"] == "3AM"
    assert response.json[0]["danceability"] == 0.521
    assert response.json[0]["energy"] == 0.673
    assert response.json[0]["key"] == 8
    assert response.json[0]["loudness"] == -8.685
    assert response.json[0]["mode"] == 1
    assert response.json[0]["acousticness"] == 0.00573
    assert response.json[0]["instrumentalness"] == 0.0
    assert response.json[0]["liveness"] == 0.12
    assert response.json[0]["valence"] == 0.543
    assert response.json[0]["tempo"] == 108.031
    assert response.json[0]["duration_ms"] == 225947
    assert response.json[0]["time_signature"] == 4
    assert response.json[0]["num_bars"] == 100
    assert response.json[0]["num_sections"] == 8
    assert response.json[0]["num_segments"] == 830
    assert response.json[0]["class"] == 1
    assert response.json[0]["rating"] == None


def test_get_request_with_start_query_parameter(client):
    response = client.get(f"{constants.API_VERSION_ONE}/songs", query_string={"start": constants.PAGINATION_START_DEFAULT})

    assert len(response.json) == constants.PAGINATION_LIMIT_DEFAULT
    assert response.status_code == HTTPStatus.OK
    assert response.is_json

    assert len(response.json[0]) == constants.NUMBER_OF_ATTRIBUTES
    assert response.json[0]["id"] == "5vYA1mW9g2Coh1HUFUSmlb"
    assert response.json[0]["title"] == "3AM"
    assert response.json[0]["danceability"] == 0.521
    assert response.json[0]["energy"] == 0.673
    assert response.json[0]["key"] == 8
    assert response.json[0]["loudness"] == -8.685
    assert response.json[0]["mode"] == 1
    assert response.json[0]["acousticness"] == 0.00573
    assert response.json[0]["instrumentalness"] == 0.0
    assert response.json[0]["liveness"] == 0.12
    assert response.json[0]["valence"] == 0.543
    assert response.json[0]["tempo"] == 108.031
    assert response.json[0]["duration_ms"] == 225947
    assert response.json[0]["time_signature"] == 4
    assert response.json[0]["num_bars"] == 100
    assert response.json[0]["num_sections"] == 8
    assert response.json[0]["num_segments"] == 830
    assert response.json[0]["class"] == 1
    assert response.json[0]["rating"] == None


def test_get_request_with_limit_query_parameter(client):
    response = client.get(f"{constants.API_VERSION_ONE}/songs", query_string={"limit": 1})

    assert len(response.json) == 1
    assert response.status_code == HTTPStatus.OK
    assert response.is_json

    assert len(response.json[0]) == constants.NUMBER_OF_ATTRIBUTES
    assert response.json[0]["id"] == "5vYA1mW9g2Coh1HUFUSmlb"
    assert response.json[0]["title"] == "3AM"
    assert response.json[0]["danceability"] == 0.521
    assert response.json[0]["energy"] == 0.673
    assert response.json[0]["key"] == 8
    assert response.json[0]["loudness"] == -8.685
    assert response.json[0]["mode"] == 1
    assert response.json[0]["acousticness"] == 0.00573
    assert response.json[0]["instrumentalness"] == 0.0
    assert response.json[0]["liveness"] == 0.12
    assert response.json[0]["valence"] == 0.543
    assert response.json[0]["tempo"] == 108.031
    assert response.json[0]["duration_ms"] == 225947
    assert response.json[0]["time_signature"] == 4
    assert response.json[0]["num_bars"] == 100
    assert response.json[0]["num_sections"] == 8
    assert response.json[0]["num_segments"] == 830
    assert response.json[0]["class"] == 1
    assert response.json[0]["rating"] == None


def test_get_request_with_start_and_limit_query_parameters(client):
    response = client.get(f"{constants.API_VERSION_ONE}/songs", query_string={"start": constants.PAGINATION_START_DEFAULT, "limit": 1})

    assert len(response.json) == 1
    assert response.status_code == HTTPStatus.OK
    assert response.is_json

    assert len(response.json[0]) == constants.NUMBER_OF_ATTRIBUTES
    assert response.json[0]["id"] == "5vYA1mW9g2Coh1HUFUSmlb"
    assert response.json[0]["title"] == "3AM"
    assert response.json[0]["danceability"] == 0.521
    assert response.json[0]["energy"] == 0.673
    assert response.json[0]["key"] == 8
    assert response.json[0]["loudness"] == -8.685
    assert response.json[0]["mode"] == 1
    assert response.json[0]["acousticness"] == 0.00573
    assert response.json[0]["instrumentalness"] == 0.0
    assert response.json[0]["liveness"] == 0.12
    assert response.json[0]["valence"] == 0.543
    assert response.json[0]["tempo"] == 108.031
    assert response.json[0]["duration_ms"] == 225947
    assert response.json[0]["time_signature"] == 4
    assert response.json[0]["num_bars"] == 100
    assert response.json[0]["num_sections"] == 8
    assert response.json[0]["num_segments"] == 830
    assert response.json[0]["class"] == 1
    assert response.json[0]["rating"] == None


def test_get_request_with_invalid_start_query_parameter(client):
    response = client.get(f"{constants.API_VERSION_ONE}/songs", query_string={"start": constants.NOT_INTEGER})
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.data == f"{constants.INVALID_START_DATA_TYPE_MESSAGE}".encode()


def test_get_request_with_invalid_limit_query_parameter(client):
    response = client.get(f"{constants.API_VERSION_ONE}/songs", query_string={"limit": constants.NOT_INTEGER})
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.data == f"{constants.INVALID_LIMIT_DATA_TYPE_MESSAGE}".encode()


def test_get_request_with_title_query_parameter(client):
    response = client.get(f"{constants.API_VERSION_ONE}/songs", query_string={"title": "3AM"})

    assert len(response.json) == 1
    assert response.status_code == HTTPStatus.OK
    assert response.is_json

    assert len(response.json[0]) == constants.NUMBER_OF_ATTRIBUTES
    assert response.json[0]["id"] == "5vYA1mW9g2Coh1HUFUSmlb"
    assert response.json[0]["title"] == "3AM"
    assert response.json[0]["danceability"] == 0.521
    assert response.json[0]["energy"] == 0.673
    assert response.json[0]["key"] == 8
    assert response.json[0]["loudness"] == -8.685
    assert response.json[0]["mode"] == 1
    assert response.json[0]["acousticness"] == 0.00573
    assert response.json[0]["instrumentalness"] == 0.0
    assert response.json[0]["liveness"] == 0.12
    assert response.json[0]["valence"] == 0.543
    assert response.json[0]["tempo"] == 108.031
    assert response.json[0]["duration_ms"] == 225947
    assert response.json[0]["time_signature"] == 4
    assert response.json[0]["num_bars"] == 100
    assert response.json[0]["num_sections"] == 8
    assert response.json[0]["num_segments"] == 830
    assert response.json[0]["class"] == 1
    assert response.json[0]["rating"] == None


def test_patch_request_update_rating(client):
    response = client.patch(f"{constants.API_VERSION_ONE}/songs/5vYA1mW9g2Coh1HUFUSmlb", data={"rating": 2})

    assert len(response.json) == 1
    assert response.status_code == HTTPStatus.OK
    assert response.is_json

    assert len(response.json[0]) == constants.NUMBER_OF_ATTRIBUTES
    assert response.json[0]["id"] == "5vYA1mW9g2Coh1HUFUSmlb"
    assert response.json[0]["title"] == "3AM"
    assert response.json[0]["danceability"] == 0.521
    assert response.json[0]["energy"] == 0.673
    assert response.json[0]["key"] == 8
    assert response.json[0]["loudness"] == -8.685
    assert response.json[0]["mode"] == 1
    assert response.json[0]["acousticness"] == 0.00573
    assert response.json[0]["instrumentalness"] == 0.0
    assert response.json[0]["liveness"] == 0.12
    assert response.json[0]["valence"] == 0.543
    assert response.json[0]["tempo"] == 108.031
    assert response.json[0]["duration_ms"] == 225947
    assert response.json[0]["time_signature"] == 4
    assert response.json[0]["num_bars"] == 100
    assert response.json[0]["num_sections"] == 8
    assert response.json[0]["num_segments"] == 830
    assert response.json[0]["class"] == 1
    assert response.json[0]["rating"] == 2

    response = client.get(f"{constants.API_VERSION_ONE}/songs", query_string={"title": "3AM"})

    assert len(response.json) == 1
    assert response.status_code == HTTPStatus.OK
    assert response.is_json

    assert len(response.json[0]) == constants.NUMBER_OF_ATTRIBUTES
    assert response.json[0]["id"] == "5vYA1mW9g2Coh1HUFUSmlb"
    assert response.json[0]["title"] == "3AM"
    assert response.json[0]["danceability"] == 0.521
    assert response.json[0]["energy"] == 0.673
    assert response.json[0]["key"] == 8
    assert response.json[0]["loudness"] == -8.685
    assert response.json[0]["mode"] == 1
    assert response.json[0]["acousticness"] == 0.00573
    assert response.json[0]["instrumentalness"] == 0.0
    assert response.json[0]["liveness"] == 0.12
    assert response.json[0]["valence"] == 0.543
    assert response.json[0]["tempo"] == 108.031
    assert response.json[0]["duration_ms"] == 225947
    assert response.json[0]["time_signature"] == 4
    assert response.json[0]["num_bars"] == 100
    assert response.json[0]["num_sections"] == 8
    assert response.json[0]["num_segments"] == 830
    assert response.json[0]["class"] == 1
    assert response.json[0]["rating"] == 2


def test_patch_request_update_non_integer_rating(client):
    response = client.patch(f"{constants.API_VERSION_ONE}/songs/5vYA1mW9g2Coh1HUFUSmlb", data={"rating": constants.NOT_INTEGER})
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.data == f"{constants.INVALID_RATING_DATA_TYPE_MESSAGE}".encode()


def test_patch_request_update_rating_below_minimum_rating(client):
    response = client.patch(f"{constants.API_VERSION_ONE}/songs/5vYA1mW9g2Coh1HUFUSmlb", data={"rating": constants.RATING_LOWER_BOUND - 1})
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.data == f"{constants.INVALID_RATING_RANGE_MESSAGE}".encode()


def test_patch_request_update_rating_above_maximum_rating(client):
    response = client.patch(f"{constants.API_VERSION_ONE}/songs/5vYA1mW9g2Coh1HUFUSmlb", data={"rating": constants.RATING_UPPER_BOUND + 1})
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.data == f"{constants.INVALID_RATING_RANGE_MESSAGE}".encode()
