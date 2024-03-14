from models import *
from utils import *

create_user()
create_admin()
format_string()
log_in_file()

print(list(filter(lambda str: not ("__" in str), dir())))
