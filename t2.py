from keywords.create_online_page import CreateOnlinePage
from keywords.human_center_page import HumanCenterPage

from utils import app

driver = app.start_app()
app.setFront()

HumanCenterPage(driver).main()