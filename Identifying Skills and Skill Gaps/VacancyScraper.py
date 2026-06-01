import scrapy
from scrapy.crawler import CrawlerProcess
from datetime import datetime

custom_settings = {
    'CONCURRENT_REQUESTS': 2,
    'DOWNLOADER_MIDDLEWARES': 
        {
        'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
        'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
        },
    'FEED_FORMAT': 'csv',
    'FEED_URI': '/Users/markrichardson-griffiths/Documents/Masters/Capstone/Data' + datetime.now().strftime('%Y_%m_%d__%H_%M_%S') + 'civilservice.csv'
    }

class civilservice(scrapy.Spider):
    name = 'civilservice'
    PROXY = ''

    def start_requests(self):
        url = 'https://www.civilservicejobs.service.gov.uk/csr/index.cgi'
        yield scrapy.Request(url=url, 
            callback=self.parse,
            meta={
                    'PROXY' : self.PROXY
            })

    def parse(self, response):
        #Get Session ID (SID)
        sid = response.css("input[name='SID']::attr('value')").get()
        #Construct new URL with the SID
        url = f"https://www.civilservicejobs.service.gov.uk/csr/esearch.cgi?SID={sid}"

        #Create a new request
        yield scrapy.Request(url=url, 
                            callback=self.get_all_results,
                            meta={
                                 'PROXY' : self.PROXY
                            })

    def get_all_results(self,response):
        #Extract session identifiers
        sid = response.css("input[name='SID']::attr('value')").get()
        reqsig = response.css("input[name='reqsig']::attr('value')").get()
        url = f"https://www.civilservicejobs.service.gov.uk/csr/esearch.cgi?SID={sid}"

        #Set data for the search form on the website
        formdata = {
            "what":"",
            "where":"",
            "id_postcodeselectorid":"#where",
            "distance":"600",
            "units":"miles",
            "overseas":"1",
            "oselect-filter-textbox":["","","","",""],
            "salaryminimum":"NULL",
            "salarymaximum":"NULL",
            "nghr_grade":["166601","166602","211621","211622","211623","211624"],
            "update_button":"Update+results",
            "SID":sid,
            "csource":"csfsearch",
            "easting":"",
            "northing":"",
            "region":"",
            "id_chosen_placeholder_text_multiple":"resultpage",
            "whatoption":"words",
            "reqsig":reqsig
        }

        #Post the search form request
        yield scrapy.FormRequest(url=url,formdata=formdata,callback=self.get_filtered_results,
            meta={
                'PROXY' : self.PROXY
            })
    #2.Manage the data from posting the search form request     
    def get_filtered_results(self,response):
        #Get job links
        all_job_links = response.css(".search-results-job-box-title a::attr('href')").getall()

        #Iterate over job links
        for link in all_job_links:
            yield scrapy.Request(url=link,callback=self.get_individual_details,
                meta={
                    'PROXY' : self.PROXY
                })
            
        #If pagination, create a new yield request 
        if(response.css("a[title='Go to next search results page']").get()):
            yield scrapy.Request(url=response.css("a[title='Go to next search results page']::attr('href')").get(),callback=self.get_filtered_results, 
                meta={
                    'PROXY' : self.PROXY
                })
            
    #Process the response for an indiviudal job vacancy
    def get_individual_details(self,response):
        ref_no = response.xpath("//div[@class='vac_display_field']/h3[contains(text(),'Reference number')]/ancestor::div[1]/div//text()").get()
        title = response.css("#id_common_page_title_h1::text").get()
        department = response.css(".csr-page-subtitle::text").get()
        grade = ", ".join(response.xpath("//div[@class='vac_display_field']/h3[contains(text(),'Job grade')]/ancestor::div[1]/div//text()").getall())
        salary = response.xpath("//div[@class='vac_display_field']/h3[contains(text(),'Salary')]/ancestor::div[1]/div//text()").get()
        type_of_role = ", ".join(response.xpath("//div[@class='vac_display_field']/h3[contains(text(),'Type of role')]/ancestor::div[1]/div//text()").getall())

        #Source 'About the Job' information
        about_the_job = []
        main_panel = response.xpath("//div[@class='vac_display_panel_main_inner']//div") # Select all div elements inside the main job display panel
        for index,div in enumerate(main_panel):
            if div.xpath("./@id").get() == "section_link_about": #if div is 'about the job'
                for needed_div in main_panel[index:]:
                    if needed_div.xpath("./@id").get() != None and needed_div.xpath("./@id").get() != "section_link_about":
                        break
                    about_the_job.extend(needed_div.xpath(".//text()").getall()) #Extract the text
                break

        #Construct a dictionary with the job vacancy details
        yield {
            "url":response.url,
            "ref_no":ref_no.strip() if ref_no else "",
            "title":title.strip() if title else "",
            "department":department.strip() if department else "",
            "grade":grade.strip() if grade else "",
            "salary":salary.strip() if salary else "",
            "type_of_role":type_of_role.strip() if type_of_role else "",
            "about_the_job":"\n".join([job.strip() for job in about_the_job])
        }


process = CrawlerProcess(custom_settings)

process.crawl(civilservice)
process.start()
