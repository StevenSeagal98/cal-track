from .home import home_content
from .info import info_content
from .preferences import preferences_content
from .current_day import current_day_content

windows = {
    'main': home_content,
    'preferences': preferences_content,
    'info': info_content,
    'current_day': current_day_content
}