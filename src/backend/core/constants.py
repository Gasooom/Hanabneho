"""
Application-wide constants.

Only values that are part of the application design
and do not change between environments belong here.
"""

API_PREFIX = "/api/v1"

DEFAULT_PAGE_SIZE = 20
MAX_PAGE_SIZE = 100

SUPPORTED_IMAGE_TYPES = (
    "image/jpeg",
    "image/png",
)

SUPPORTED_AUDIO_TYPES = (
    "audio/mpeg",
    "audio/wav",
)