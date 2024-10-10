from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from .provider import *
from .service_area import *