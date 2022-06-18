import unittest
from main import ImageExtractor


class TestImageExtractor(unittest.TestCase):

    def test_successful_image_extraction_empty_file(self):
        src_file_path = "urls_empty.txt"
        save_file_path = "images/"
        self.__img_extractor_obj = ImageExtractor(src_file_path, save_file_path)
        status = self.__img_extractor_obj.process_urls()

        self.assertEqual(status, "File Empty")

    def test_successful_image_extraction_general(self):
        src_file_path = "urls.txt"
        save_file_path = "images/"
        self.__img_extractor_obj = ImageExtractor(src_file_path, save_file_path)
        status = self.__img_extractor_obj.process_urls()

        self.assertEqual(status, "Check logs")

    def test_successful_image_extraction_each_url_page_unreachable(self):
        src_file_path = "urls.txt"
        save_file_path = "images/"
        url = "http://somewebsrv.com/img/992147.jpg"
        self.__img_extractor_obj = ImageExtractor(src_file_path, save_file_path)
        status = self.__img_extractor_obj._ImageExtractor__extract_image_from_each_url(url)

        self.assertEqual(status, "Cannot reach page")

    def test_successful_image_extraction_each_url_content_not_image(self):
        src_file_path = "urls.txt"
        save_file_path = "images/"
        url = "http://eu.httpbin.org"
        self.__img_extractor_obj = ImageExtractor(src_file_path, save_file_path)
        status = self.__img_extractor_obj._ImageExtractor__extract_image_from_each_url(url)

        self.assertEqual(status, "Content in http://eu.httpbin.org not an image")

    def test_successful_image_extraction_each_url_success(self):
        src_file_path = "urls.txt"
        save_file_path = "images/"
        url = "http://s9.postimage.org/n92phj9tr/image2.jpg"
        self.__img_extractor_obj = ImageExtractor(src_file_path, save_file_path)
        status = self.__img_extractor_obj._ImageExtractor__extract_image_from_each_url(url)

        self.assertEqual(status, "Success")
