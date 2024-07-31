# API version
API_VERSION_ONE = "/api/v1"

# Pagination defaults
PAGINATION_START_DEFAULT = 0
PAGINATION_LIMIT_DEFAULT = 5

# Rating bounds
RATING_LOWER_BOUND = 0
RATING_UPPER_BOUND = 5

# Response messages
INVALID_START_DATA_TYPE_MESSAGE = "Start must be an integer."
INVALID_LIMIT_DATA_TYPE_MESSAGE = "Limit must be an integer."
INVALID_RATING_DATA_TYPE_MESSAGE = "Rating must be an integer between 0 and 5."
INVALID_RATING_RANGE_MESSAGE = "Rating must be between 0 and 5."
SONG_TITLE_NOT_FOUND_MESSAGE = "Song with the following title not found: "
SONG_ID_NOT_FOUND_MESSAGE = "Song with the following ID not found: "

# Response mimetypes
JSON_MIMETYPE = "application/json"

# Testing
NOT_INTEGER = 'a'
DEGREE_OF_ERROR = 0.000001
NUMBER_OF_SONGS = 100
NUMBER_OF_ATTRIBUTES = 20
