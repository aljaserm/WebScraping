from libSource import log
from libSource import TheNewsWeb
from libSource import helper

if __name__ == '__main__':
    # Define log file location
    log.set_custom_log_info('html/error.log')

    # SSL or HTTPS ISSUE
    helper.verify_https_issue()

    # create scraping object
    webScrap = TheNewsWeb.News(TheNewsWeb.url_aj, log)

    # checking if we should redownload from url or not
    if helper.check_cache(TheNewsWeb.raw_html, TheNewsWeb.CACHE):
        webScrap.retrieve_webpage()
        webScrap.write_webpage_as_html()

    webScrap.read_webpage_from_html()
    webScrap.convert_data_to_bs4()
    #webScrap.print_beautiful_soup()
    webScrap.parse_soup_to_simple_html()
