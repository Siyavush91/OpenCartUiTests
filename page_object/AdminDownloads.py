from locators import Catalog, Alert
from .BasePage import BasePage


class AdminDownloads(BasePage):

    def open_downloads_page(self):
        self._click(Catalog.navigation.catalog_outs)
        self._click(Catalog.catalog_download.downloads)

    def add_download(self):
        self._click(Catalog.catalog_download.add_new_button)
