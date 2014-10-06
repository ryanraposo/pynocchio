# -*- coding: UTF-8 -*-
__author__ = 'michell'

from loader import *
import zipfile


class ZipLoader(Loader):

    def _load_core(self, page_data, page_title, file_name):

        zf = zipfile.ZipFile(file_name, 'r')

        name_list = zf.namelist()
        name_list.sort()

        for info in name_list:

            data = zf.read(info)

            page_data.append(data)
            page_title.append(info)

        zf.close()

    @staticmethod
    def is_zip_file(file_name):
        return zipfile.is_zipfile(file_name)






