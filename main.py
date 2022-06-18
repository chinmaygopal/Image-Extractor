import urllib3
from urllib3 import PoolManager, Retry
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


class ImageExtractor:
    """
    Class contains procedures to extract images from URLs in specified
    text file and saves in the mentioned location
    """

    def __init__(self, src_file_path, save_file_path) -> None:
        """
        :param src_file_path: the file location of the text file containing the URLs
        :param save_file_path: the location for storing the extracted images
        """
        self.__source_file_path = src_file_path
        self.__save_file_path = save_file_path
        self.__retries = Retry(connect=5, read=2, redirect=5)
        self.__http = PoolManager(retries=self.__retries)
        self.__list_of_urls = None

    def __extract_image_from_each_url(self, each_url) -> str:
        """
        Retrieves image from the specified URL and saves it.
        :param each_url: URL to extract image from
        :return: return_status: status of the operation
        """
        return_status = "Success"

        try:
            response = self.__http.request("GET", url=each_url)

            # verify if response content is an image
            if response.headers["Content-Type"] == "image/jpeg":
                filename = each_url.split("/")[-1]
                self.__save_image(response.data, filename)
            else:
                return_status = "Content in " + each_url + " not an image"
                logging.error("Content in " + each_url + " not an image")

        except urllib3.exceptions.ConnectionError:
            return_status = "A connection error occurred. Please verify " + each_url
            logging.error("A connection error occurred. Please verify " + each_url)

        except urllib3.exceptions.ConnectTimeoutError:
            return_status = "A connection timeout occurred"
            logging.error("A connection timeout occurred")

        except urllib3.exceptions.ResponseError:
            return_status = "Error in data URL response"
            logging.error("Error in data URL response")

        except urllib3.exceptions.HTTPError:
            return_status = "Cannot reach page"
            logging.error("Cannot reach page")

        except urllib3.exceptions.RequestError:
            return_status = "an ambiguous exception that occurred while handling your request"
            logging.error("an ambiguous exception that occurred while handling your request")

        except ValueError:
            return_status = "value error"
            logging.error("value error")

        return return_status

    def __retrieve_urls(self) -> None:
        """
        Read all the URLs from the text file and perform any preprocessing if necessary
        :return: None
        """
        # read the URLs in file
        with open(self.__source_file_path, "r") as f:
            self.__list_of_urls = f.readlines()
        self.__list_of_urls = list(map(str.strip, self.__list_of_urls))
        print(self.__list_of_urls)

    def __process_each_url(self) -> str:
        """
        Iterates through each URL to extract image from
        :return: return_status: the status of the operation
        """
        # check if file is empty
        if len(self.__list_of_urls) == 0:
            return_status = "File Empty"

        else:
            return_status = "Check logs"
            for each_url in self.__list_of_urls:
                self.__extract_image_from_each_url(each_url)
        return return_status

    def __save_image(self, image_data, filename) -> None:
        """
        Saves the image contents obtained from the response to URL request into a file
        :param image_data: the contents of the response containing the image info
        :param filename: the name the file must be saved as
        :return: None
        """
        with open(self.__save_file_path + filename, 'wb') as handler:
            handler.write(image_data)

    def process_urls(self) -> str:
        """
        Interface available to user to perform the image extraction from URLs operation
        :return: return_status: the status of the operation
        """

        self.__retrieve_urls()
        return_status = self.__process_each_url()

        return return_status


if __name__ == '__main__':
    src_file_path = "URLs.txt"
    save_file_path = "images/"
    img_extractor_obj = ImageExtractor(src_file_path, save_file_path)
    status = img_extractor_obj.process_urls()
    print(status)
