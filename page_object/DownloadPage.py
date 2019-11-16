from locators import Downloads
from .BasePage import BasePage
import time

class DownloadPage(BasePage):

    def input_down_name(self, name):
        self._input(Downloads.download_name_field, name)

    def input_filename(self, model):
        self._input(Downloads.filename_field, model)

    def input_meta(self, meta_tag):
        self._input(Downloads.mask_field, meta_tag)



    # def upload_file(self, file, name):
    #     """Загрузка файла в раздел загрузок"""
    #     script = """
    #             document.getElementById("button-upload").click();
    #             var f = document.createElement("form");
    #             f.id = "form-upload";
    #             f.style.display = "block";
    #             f.enctype = "multipart/form-data";
    #             inp = document.createElement("input");
    #             inp.type = "file";
    #             inp.name = "file";
    #             f.appendChild(inp);
    #             body = document.getElementsByTagName("body")[0];
    #             body.insertBefore(f, body.firstChild);
    #             """
    #     self._upload_file(script, file)
    #     time.sleep(2)
    #     self.alert().accept()
    #     return self


    # def input

    def click_savebutton(self):
        self._click(Downloads.save_button)


    def verify_element(self):
        self._wait_for_visible(Downloads.filename_field)
