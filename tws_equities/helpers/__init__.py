from tws_equities.helpers.logger_setup import get_logger
from tws_equities.helpers.contract_maker import create_stock
from tws_equities.helpers.utils import clear_directory
from tws_equities.helpers.utils import get_date_range
from tws_equities.helpers.utils import delete_file
from tws_equities.helpers.utils import make_dirs
from tws_equities.helpers.utils import save_data_as_json
from tws_equities.helpers.utils import load_json_data
from tws_equities.helpers.utils import create_batches


BAR_CONFIG = {
                'title': '=> Status∶',
                'calibrate': 5,
                'force_tty': True,
                'spinner': 'dots_reverse',
                'bar': 'smooth'
             }
